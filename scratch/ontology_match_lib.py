
import yaml
import os
import re
import json

# TODO: make the find_best_fit_type look at inheritance for general_type, and not require it at all if wanted
# TODO: update the yaml import to reference the modified version dbo uses today.
# TODO: add ancestry walking to the Ontology (currently doesnt support it, just walks the tree and builds the types).
# TODO: add a method to check if a field set is an exact match to the ontology. 

# RESOURCE DIRECTORY

RESOURCE_DIR = '../ontology/yaml/resources'

### Ontology import helper functions. 

def PrettyPrint(obj):
	""" Pretty print the input dictionary. """ 
	print(json.dumps(obj,sort_keys=True,indent=2))

def load_yaml(file_path):
	""" Load a yaml file. Handles doc separation by loading all and combining into common dict. """
	docs = yaml.load_all(open(file_path,'r',encoding='utf-8'),Loader=yaml.FullLoader)

	data = {}
	for doc in docs:
		for key in doc:
			if key not in data:
				data[key] = doc[key]
			else:
				data[key] += doc[key]
	#print('Ontology: Imported doc {}'.format(file_path))
	return data

class Subfield:
	""" Class for defining and validating a subfield. """
	
	def __init__(self, subfield_category, subfield_name, description):
		self.category = subfield_category
		self.name = subfield_name
		self.description = description
		self.validate()

	def validate(self):
		""" Perform a series of validations. """
		valid_categories = ['aggregation','component','descriptor','measurement','measurement_descriptor','point_type']

		assert self.category in valid_categories, "{} is not a valid category.".format(self.category)
		assert self.description, "{} is missing a category".format(self.name)
		assert isinstance(self.name,str), "{} name is not a string.".format(self.name)
		assert isinstance(self.category,str), "{} category is not a string.".format(self.category)
		assert isinstance(self.description,str), "{} description is not a string.".format(self.description)		 

	def get_category(self):
		""" Get the category of the subfield. """
		return self.category

	def get_description(self):
		""" Get the description of the subfield. """
		return self.description

class Field:
	""" Class for defining and validating a field. """

	def __init__(self,name,states=[]):
		self.name = name
		self.states = states
		self._validate()

	def _validate(self):
		""" Perform a series of field validations (intrinsic only; extrinsic checks in Fields class). """
		pass

class EntityType:
	""" Class to hold type definitions"""
	def __init__(self, name, description, local_fields=[], implements=[],is_abstract=False,is_canonical=False,namespace='GLOBAL'):
		self.name = name
		self.local_fields = local_fields 	# Only local fields
		self.inherited_fields = [] 			# Only inherited fields
		self.required_fields = [] 			# Only required fields
		self.optional_fields = [] 			# Only optional fields
		self.fields = [] 					# All fields for the device
		self.description = description
		self.implements = implements
		self.is_abstract = is_abstract
		self.is_canonical = is_canonical
		self.namespace = namespace

	def set_inherited_fields(self,inherited_fields):
		""" Set inherited fields for the type. """
		self.inherited_fields = inherited_fields

	def set_req_and_opt_fields(self):
		""" Set the required and optional fields for the type. """
		for field in self.fields:
			if field[1] == True:
				self.required_fields.append(field[0])
			else:
				self.optional_fields.append(field[0])

	def get_fields(self):
		""" Return the fields for the type. """
		return self.fields

	def get_required_fields(self):
		""" Return the required fields for the type. """
		return self.required_fields

	def get_optional_fields(self):
		""" Return the optional fields for the type. """
		return self.optional_fields

	def get_local_fields(self):
		""" Return the local fields for the type. """
		return self.local_fields

	def get_parents(self):
		""" Return the parents for the type. """
		return self.implements

class Subfields:
	""" Helper class to hold all subfields. """

	def __init__(self,resource_dir):
		self.mapping_key = {
			'units':resource_dir+'/units',
			'subfields':resource_dir+'/subfields',
			'fields':resource_dir+'/fields',
			'states':resource_dir+'/states'
		}
		self.subfields = self._import_subfields()


	def get_subfield(self,subfield_name):
		""" Return a specified subfield """
		subfield = self.subfields[subfield_name]
		return subfield

	def get_subfield_files(self):
		""" Return a list of fully qualified file paths for any subfield files. """

		target = 'subfields'
		files = os.listdir(self.mapping_key[target])
		files = [self.mapping_key[target] + '/' + file for file in files]
		return files

	def _import_subfields(self):
		""" Import the subfields from the relevant YAML files and instantiate them as individual objects. """

		subfield_files = self.get_subfield_files()

		subfields_set = set()
		subfields = {}
		for file in subfield_files:
			subfields_raw = load_yaml(file)
			for category in subfields_raw:
				for name in subfields_raw[category]:
					assert name not in subfields_set, 'Subfield {} used more than once.'.format(name)
					description = subfields_raw[category][name]
					subfields[name] = Subfield(category,name,description)
					subfields_set.add(name)

		return subfields

class Fields:
	""" Helper class to hold all fields. """

	def __init__(self,resource_dir):
		self.mapping_key = {
			'units':resource_dir+'/units',
			'subfields':resource_dir+'/subfields',
			'fields':resource_dir+'/fields',
			'states':resource_dir+'/states'
		}

		self.fields = self._import_fields()
		self.validate()

	def get_field(self,field_name):
		field = self.fields[field_name]
		return field

	def _get_field_files(self):
		""" Return a list of fully qualified file paths for any field files. """

		target = 'fields'
		files = os.listdir(self.mapping_key[target])
		files = [self.mapping_key[target] + '/' + file for file in files]
		return files

	def _import_fields(self):
		""" Import the fields from the relevant YAML files and instantiate them as individual objects. """

		field_files = self._get_field_files()
		fields = {}
		for file in field_files:
			data = load_yaml(file)

			# Check that the field files have the right literals.
			for field in data: 
				assert field in ['literals'], "Field file '{}'' contains invalid field '{}'".format(file,field)
			for field in data['literals']:
				if isinstance(field,str):
					fields[field] = Field(field)
				elif isinstance(field,dict):
					for key in field:
						fields[key] = Field(key,field[key])

		return fields

	def validate(self):
		""" Perform a series of validations. """
		pass

class Types:
	""" Helper class to hold all entity types. """

	def __init__(self,resource_dir):
		self.resource_dir = resource_dir
		self.types = self._import_types()
		self.namespaces = [namespace for namespace in self.types]
		for namespace in self.namespaces:
			for t in self.types[namespace]:
				self._get_type_fields(namespace,t)

	def _get_type_files(self):
		""" Return a list of fully qualified file paths for any entity files. """

		namespace_pattern = 'resources\\W(\\w+)\\Wentity_types'
		w = os.walk(self.resource_dir)
		entity_type_files = []
		for f in w: 
			# Index reference: 
			# - 0 = directory path
			# - 1 = directory names
			# - 2 = file name
			if 'entity_types' in f[0]:
				for file in f[2]:
					if '.yaml' in file:
						matches = re.search(namespace_pattern,f[0])
						if matches:
							namespace = matches.group(1)
						else:
							namespace = 'GLOBAL'
						entity_type_files.append((namespace,f[0]+'/'+file))
		return entity_type_files

	def _import_types(self):
		""" Import the entity types and store them as class objects. """

		# things to store:
		# - is-abstract

		entity_types = {}
		type_files = self._get_type_files()
		for file in type_files:
			try:
				namespace = file[0]
				if namespace not in entity_types:
					entity_types[namespace] = {}
				data = load_yaml(file[1])
				for key in data:
					if key not in entity_types[namespace]:
						# Check that the fields in the type yaml are allowed. 
						for field in data[key]:
							assert field in ['is_canonical','is_abstract','implements','id','uses','opt_uses','description'], 'Type {} has invalid key {} in file {}.'.format(key,field,file)
						name = key
						description = data[key]['description']
						opt_fields = [(field,False) for field in data[key].get('opt_uses',[])]
						req_fields = [(field,True) for field in data[key].get('uses',[])]
						local_fields = opt_fields + req_fields
						implements = data[key].get('implements',[])
						is_abstract = data[key].get('is_abstract',False)
						is_canonical = data[key].get('is_canonical',False)
						entity_types[namespace][key] = EntityType(name, description, local_fields, implements, is_abstract, is_canonical, namespace)				
					else: 
						print('Key found twice in same namespace: {} {}'.format(namespace,key))
			except Exception as e:
				print("Type file '{}'' raises exception '{}'.".format(file[1],e))
				raise

		return entity_types

	def get_type(self,namespace,type_name):
		entity_type = self.types[namespace][type_name]
		return entity_type

	def _get_type_fields(self,namespace,type_name):
		""" Walk the tree and find all inherited fields for a type. """
		target_type_name = type_name

		inherited_fields = set()
		local_fields = set(self.types[namespace][target_type_name].local_fields)

		def _get_fields(namespace,type_name):
			""" Recursively walk the inheritance tree collecting fields. """
			t = self.types[namespace][type_name]

			for i in t.implements:

				# Get the fields of a type in a different namespace.
				if len(i.split('/')) > 1:
					tmp_namespace = i.split('/')[0]
					tmp_i = i.split('/')[1]

					# In the event that a namespaced item represents the global namespace
					if tmp_namespace == '':
						tmp_namespace = 'GLOBAL'
					_get_fields(tmp_namespace,tmp_i)

				# Get the fields of a type in the global namespace
				elif i not in self.types[namespace]:
					tmp_namespace = 'GLOBAL'
					_get_fields(tmp_namespace,i)

				# Otherwise just work. 
				else:
					_get_fields(namespace,i)
			if type_name != target_type_name:
				for u in t.local_fields:
					inherited_fields.add(u)

		def _promote_fields(field_set):
			""" Takes a full set of fields for a given type and deduplicates them. As part of the deduplication,
			promote any field based on its strictest requirement setting (i.e. promote False --> True if both exist). """		
			pts = {}
			for t in field_set:
				if t[0] not in pts:
					pts[t[0]] = [t[1]]
				elif t[0] in pts:
					pts[t[0]].append(t[1])

			f = set()
			for t in pts:
				f.add((t,max(pts[t])))

			return list(f)

		_get_fields(namespace,target_type_name)
				
		self.types[namespace][target_type_name].inherited_fields = _promote_fields(inherited_fields)
		self.types[namespace][target_type_name].fields = _promote_fields(local_fields|inherited_fields)
		self.types[namespace][target_type_name].set_req_and_opt_fields()

	def get_required_fields(self,namespace,type_name):
		required_fields = self.types[namespace][type_name].get_required_fields()
		return required_fields

	def get_optional_fields(self,namespace,type_name):
		optional_fields = self.types[namespace][type_name].get_optional_fields()
		return optional_fields

	def get_all_fields(self,namespace,type_name):
		fields = self.types[namespace][type_name].get_fields()
		return fields

	def get_all_types(self,namespace):
		""" Get a list of all types in the types object. """
		type_list = [t for t in self.types[namespace]]
		return type_list

class Ontology:

	def __init__(self):
		self.subfields = Subfields(RESOURCE_DIR)
		self.fields = Fields(RESOURCE_DIR)
		self.types = Types(RESOURCE_DIR)
		self.validate()

	def refresh(self):
		""" Refresh the ontology by rebuilding it. """
		self.subfields = Subfields(RESOURCE_DIR)
		self.fields = Fields(RESOURCE_DIR)
		self.types = Types(RESOURCE_DIR)
		self.validate()

	def validate(self):
		""" Perform all-up ontology validation now that the key components are in hand. 
		Things to validate:
			Subfields:
			- unique
			- correct form (no illegal characters)

			Fields:
			- unique

			Types:
			- unique fields
			- unique parents (no dupe implements)

		"""
		
		# Check the fields file against the subfields doc.
		invalid_fields = {}
		for field in self.fields.fields:
			subfields = self.fields.fields[field].name.split('_')
			for subfield in subfields:
				
				if subfield not in self.subfields.subfields:
					if field not in invalid_fields:
						invalid_fields[field] = [subfield]
					else:
						invalid_fields[field].append(subfield)
		assert len(invalid_fields) == 0, "These fields are invalid: {}".format(str(invalid_fields))


		# Check types for duplicate fields. 
		duplicate_fields = {}
		for namespace in self.types.types:
			for t in self.types.types[namespace]:
				fields = self.types.types[namespace][t].get_local_fields()
				local_fields = [field[0] for field in fields]
				dups = []
				non_dups = []
				for field in local_fields:
					if field not in non_dups:
						non_dups.append(field)
					else:
						dups.append(field)
				if len(dups) > 0:
					if namespace not in duplicate_fields:
						duplicate_fields[namespace] = {}
					duplicate_fields[namespace][t] = dups

		assert len(duplicate_fields) == 0, "These types have duplicate local fields. NOT ALLOWED: {}".format(str(duplicate_fields))

		# TODO: Fix this section
		# Check the type fields against the fields doc.
		for namespace in self.types.types:
			for t in self.types.types[namespace]:
				fields = self.types.types[namespace][t].get_local_fields()
				
				for field in fields:
					invalid_fields = []
					strip_field = '_'.join([sf for sf in field[0].split('_') if not sf.isnumeric()])
					
					#for field in self.fields.fields: print(field)
					if strip_field not in self.fields.fields:
						if strip_field not in invalid_fields:
							invalid_fields.append(strip_field)

				assert len(invalid_fields)==0, "The type '{}' has invalid fields: {}".format(t,str(invalid_fields))

		# Check for duplicate parents.
		duplicate_parents = {}
		for namespace in self.types.types:
			for t in self.types.types[namespace]:
				parents = self.types.types[namespace][t].get_parents()
				dups = []
				non_dups = []
				for parent in parents:
					if parent not in non_dups:
						non_dups.append(parent)
					else:
						dups.append(parent)
				if len(dups) > 0:
					if namespace not in duplicate_parents:
						duplicate_parents[namespace] = {}
					duplicate_parents[namespace][t] = dups

		assert len(duplicate_parents) == 0, "These types have duplicate local fields. NOT ALLOWED: {}".format(str(duplicate_parents))

	def validate_without_errors(self):
		""" Perform all-up ontology validation (without erroring out) now that the key components are in hand. 
		Things to validate:
			Subfields:
			- unique
			- correct form (no illegal characters)

			Fields:
			- unique

			Types:
			- unique fields
			- unique parents (no dupe implements)

		"""
		
		# Check the fields. 
		invalid_fields = {}
		for field in self.fields.fields:
			subfields = self.fields.fields[field].name.split('_')
			for subfield in subfields:
				if subfield not in self.subfields.subfields:
					if field not in invalid_fields:
						invalid_fields[field] = [subfield]
					else:
						invalid_fields[field].append(subfield)
		if len(invalid_fields) > 0:
			print("These fields are invalid: {}".format(str(invalid_fields)))

		# Check types for duplicate fields. 
		duplicate_fields = {}
		for namespace in self.types.types:
			for t in self.types.types[namespace]:
				fields = self.types.types[namespace][t].get_local_fields()
				local_fields = [field[0] for field in fields]
				dups = []
				non_dups = []
				for field in local_fields:
					if field not in non_dups:
						non_dups.append(field)
					else:
						dups.append(field)
				if len(dups) > 0:
					if namespace not in duplicate_fields:
						duplicate_fields[namespace] = {}
					duplicate_fields[namespace][t] = dups

		if len(duplicate_fields) > 0:
			print("These types have duplicate local fields. NOT ALLOWED: {}".format(str(duplicate_fields)))

		for namespace in self.types.types:
			for t in self.types.types[namespace]:
				fields = self.types.types[namespace][t].get_local_fields()
				invalid_type_fields = []

				for field in fields:
					invalid_type_fields = []
					strip_field = '_'.join([sf for sf in field[0].split('_') if not sf.isnumeric()])
					
					#for field in self.fields.fields: print(field)
					if strip_field not in self.fields.fields:
						if strip_field not in invalid_type_fields:
							invalid_type_fields.append(strip_field)

				if len(invalid_type_fields)>0: 
					print("The type '{}' has invalid fields: {}".format(t,str(invalid_type_fields)))

		# Check for duplicate parents.
		duplicate_parents = {}
		for namespace in self.types.types:
			for t in self.types.types[namespace]:
				parents = self.types.types[namespace][t].get_parents()
				dups = []
				non_dups = []
				for parent in parents:
					if parent not in non_dups:
						non_dups.append(parent)
					else:
						dups.append(parent)
				if len(dups) > 0:
					if namespace not in duplicate_parents:
						duplicate_parents[namespace] = {}
					duplicate_parents[namespace][t] = dups

		if len(duplicate_parents) > 0:
			print("These types have duplicate local fields. NOT ALLOWED: {}".format(str(duplicate_parents)))

		if len(duplicate_parents) == 0 and len(duplicate_fields) == 0 and len(invalid_fields) == 0:
			print("[INFO]\tNo ontology errors!")

	def check_subfield(self,subfield_name):
		""" Check that a subfield is defined in the ontology. """

		try:
			self.subfields.get_subfield(subfield_name)
			return True
		except:
			return False

	def check_subfields(self,field_names):
		""" Check that the fields contains only valid subfields. Collect any invalid ones. """
		invalid_subfields = []
		for field_name in field_names:
			for subfield in field_name.split('_'):
				if not subfield.isdigit():
					if not self.check_subfield(subfield):
						invalid_subfields.append(subfield)
		return invalid_subfields

	def check_field(self,field_name):
		""" Check that a field is defined in the ontology. Dont worry about enumerations at the end. """
		try:
			subfields = field_name.split('_')
			for subfield in subfields:
				if subfield.isdigit():
					subfields.remove(subfield)
			field_name = '_'.join(subfields)
			# Remove enumerations. 

			self.fields.get_field(field_name)
			return True
		except:
			return False

	def check_fields(self,fields_list):
		""" Check that a list of fields are defined in the ontology. Returns a dict of True/Falses."""
		invalid_fields = [field for field in fields_list if self.check_field(field)==False]
		return invalid_fields

	def get_all_namespaces(self):
		""" Get all namespaces in the ontology. """

		return self.types.namespaces

	def get_type_fields(self,namespace,type_name):
		""" Get the fields of a type by name. """
		return self.types.get_all_fields(namespace,type_name)

	def _match_fields_to_type(self,fields,namespace,type_name):
		""" Check that a a type is in the ontology. For the type to be applied properly, the real type needs 
		to cover all required fields from the canonical, and all real type fields must be covered by the 
		canonical. The conditions that can be returned are:
			1. Exact match: all canonical required fields covered and all real type fields covered. 
			2. Close match: all required fields are covered but not all real type fields are covered.
			3. Incomplete match: all real type fields covered but not all canonical required fields covered. 
			4. No match: neither real types nor required fields are completely covered. """

		canonical_fields = set(self.get_type_fields(namespace,type_name))
		all_fields = set()
		optional_fields = set()
		required_fields = set()

		if isinstance(fields,list): fields = set(fields)

		for field, req in canonical_fields:
			all_fields.add(field)
			if req == True:
				required_fields.add(field)
			if req == False:
				optional_fields.add(field)		

		if fields.issubset(all_fields) and required_fields.issubset(fields): 
			match_type = 'EXACT'
			matched = fields.intersection(required_fields)
			unmatched_real = set()
			unmatched_required = set()

		if not fields.issubset(all_fields) and required_fields.issubset(fields):
			match_type = 'CLOSE'
			matched = fields.intersection(required_fields)			
			unmatched_real = fields.difference(all_fields) 
			unmatched_required = set()

		if fields.issubset(all_fields) and not required_fields.issubset(fields):
			match_type = 'INCOMPLETE'
			matched = fields.intersection(required_fields)
			unmatched_real = set()
			unmatched_required = required_fields.difference(fields)

		if not fields.issubset(all_fields) and not required_fields.issubset(fields):
			match_type = 'NOT'
			matched = fields.intersection(required_fields)
			unmatched_real = fields.difference(all_fields) 
			unmatched_required = required_fields.difference(fields)

		output = {
			'match_type':match_type, 
			'matched':list(matched), 
			'unmatched_real':list(unmatched_real),
			'unmatched_required':list(unmatched_required), 
			'total_matched':len(matched),
			'total_real':len(unmatched_real),
			'total_required':len(unmatched_required)
		}		

		return output

	def _match_to_canonical_types(self,fields,namespace,general_type):

		matches = {}
		for t in self.types.types[namespace]:
			# TODO make better by inheriting general types instead.
			# TODO actually do above
			# TODO really really do it
			if t.startswith(general_type):
				if self.types.types[namespace][t].is_canonical == False:
					continue
				mt = self._match_fields_to_type(fields,namespace,t)
				matches[t] = mt
		return matches

	def find_best_fit_type(self,fields,namespace,general_type,real_entities_list=[]):
		""" Find the best fitting type for a given set of fields. Returns a list of Match 
		objects which can facilitate a comparison between the real and ontology types. """

		if isinstance(fields,list): fields = set(fields)

		mt = self._match_to_canonical_types(fields,namespace,general_type)
		output = {}
		# If an exact match is found, just break the loop. No need to go further. 
		for m in mt:
			if mt[m]['match_type'] == 'EXACT':
				output['EXACT'] = {m:mt[m]}

		# If the match isnt exact, a new type needs to be made. Find the
		# incomplete- and close-matched types that have the fewest fields 
		# needed to make them complete (incomplete based on required fields
		# and close from real). In the event of a tie, use close match since you want a fully
		# defined type instead of an incomplete type.

		real = {m:mt[m]['total_real'] for m in mt if mt[m]['total_matched'] > 0 and mt[m]['match_type']=='CLOSE'}
		if len(real) > 0:
			min_real = min(real.values())
			best_real = [k for k,v in real.items() if v==min_real]
			matched_real = {m:mt[m]['total_matched'] for m in best_real}
			best_matched_real = max(matched_real,key=matched_real.get)
			output['CLOSE']={best_matched_real:mt[best_matched_real]}

		required = {m:mt[m]['total_required'] for m in mt if mt[m]['total_matched'] > 0 and mt[m]['match_type']=='INCOMPLETE'}
		if len(required) > 0: 
			min_req = min(required.values())
			best_req = [k for k,v in required.items() if v==min_req]
			matched_req = {m:mt[m]['total_matched'] for m in best_req}
			best_matched_req = max(matched_req,key=matched_req.get)
			output['INCOMPLETE']={best_matched_req:mt[best_matched_req]}

		# If at this point there are no exact, incomplete, or close guesses, give up. 
		if len(output) == 0:
			output['NONE']={"NONE":"NO GOOD GUESS"}

		if 'EXACT' in output:
			match_type_name = [k for k in output['EXACT'].keys()][0]
			match = Match()
			match.set_match_type('EXACT')
			match.set_real_type_fields(fields)
			match.set_real_type_assets(real_entities_list)			
			match.set_ont_type_name(match_type_name) # Real dumb way of getting only key in the structure.
			match.set_ont_type_fields(self.get_type_fields(namespace,match_type_name))


		elif 'INCOMPLETE' in output:
			match_type_name = [k for k in output['INCOMPLETE'].keys()][0]
			match = Match()
			match.set_match_type('INCOMPLETE')
			match.set_real_type_fields(fields)
			match.set_real_type_assets(real_entities_list)			
			match.set_ont_type_name(match_type_name) # Real dumb way of getting only key in the structure.
			match.set_ont_type_fields(self.get_type_fields(namespace,match_type_name))
				
		elif 'CLOSE' in output:
			match_type_name = [k for k in output['CLOSE'].keys()][0]
			match = Match()
			match.set_match_type('CLOSE')
			match.set_real_type_fields(fields)
			match.set_real_type_assets(real_entities_list)			
			match.set_ont_type_name(match_type_name) # Real dumb way of getting only key in the structure.
			match.set_ont_type_fields(self.get_type_fields(namespace,match_type_name))

		else:
			match = Match()
			match.set_match_type('NONE')
			match.set_real_type_fields(fields)
			match.set_real_type_assets(real_entities_list)			

		return match

	def get_all_types(self,namespace):
		""" Get all types from the ontology. """
		type_list = self.types.get_all_types(namespace)
		return type_list

	def compare_to_type(self,fields,namespace,type_name,show_optional=False):
		""" Print a formatted comparison between the real type and the matched ontology type. """

		real_fields = fields
		type_fields = self.get_type_fields(namespace,type_name)

		# Refactor ontology fields object into a more useful shape (key value pairs). 
		ont_type_fields = {field[0]:field[1] for field in type_fields}
		
		all_fields = list(set([field for field in ont_type_fields])|set(real_fields))
		all_fields.sort()

		match_matrix = []
		for field in all_fields:
			if field in real_fields:
				real_field = field
			else:
				real_field = ''

			if field in ont_type_fields:
				ont_field = field
				ont_field_req = str(ont_type_fields[field])
			else:
				ont_field = ''
				ont_field_req = ''

			match_matrix.append([real_field,ont_field,ont_field_req])

		# Print only required if show_optional is False (except if theres a real field that is defined).
		final_matrix = []
		if not show_optional:
			for row in match_matrix:
				# Only return Trues or actual fields that have a value.
				if row[2] == 'True' or len(row[0])>0: 
					final_matrix.append(row)

		else:
			# Print required first and then append optional.
			for row in match_matrix:
				if row[2] == 'True':
					final_matrix.append(row)
			for row in match_matrix:
				if row[2] == 'False': 
					final_matrix.append(row)
			for row in match_matrix:
				if row[2] == '':
					final_matrix.append(row)

		# Set padding for pretty printing
		padding = 3
		col_width = max(len(field) for field in all_fields) + padding	

		print("TYPE BEING MATCHED: '{}'".format(namespace+'/'+type_name))
		print('\n')
		print("".join(field.ljust(col_width) for field in ['ACTUAL FIELDS','TYPE FIELDS','REQUIRED']))
		print("".join(field.ljust(col_width) for field in ['='*(col_width-padding),'='*(col_width-padding),'='*(col_width-padding)]))
		for row in final_matrix:
		    print("".join(field.ljust(col_width) for field in row))
		print('\n')

class Match:

	""" An object to hold match information. Allows for easy comparison between a real type defined in the loadsheet
	with any given ontology type. Provides a bit of valdation and functionality for reviewing the type comparison as
	well...

	Real Type Fields: the fields defined for the real-world (i.e. loadsheet) type.
	Ont Type: the fields defined for the ontology-defined type. """

	def __init__(self):
		self.match_type = ''
		self.real_type_fields = []
		self.real_type_assets = []
		self.ont_type_fields = [] # Tuple (<field_name>,<True/False required>)
		self.ont_type_name = ''
		self.unmatched_real = []
		self.unmatched_required = []

	def set_match_type(self,match_type):
		""" Set the match type. """
		assert match_type in ['EXACT','CLOSE','INCOMPLETE','NONE'], "{} is not a valid match type!".format(match_type)
		self.match_type = match_type

	def set_ont_type_name(self,ont_type_name):
		""" Set the match type name. """
		self.ont_type_name = ont_type_name

	def set_ont_type_fields(self,fields):
		""" Set the ontology type fields. This will be used later to perform on-demand comparisons. """
		self.ont_type_fields = fields

	def set_real_type_fields(self,fields):
		""" Set the real type fields. This will be used later to perform on-demand comparisons. """
		self.real_type_fields = fields

	def set_real_type_assets(self,assets):
		""" Set the real type assets. This will be used to know the impact of a type match in terms of matched assets. """
		self.real_type_assets = assets

	def get_match_type(self):
		""" Get the match type. """
		return self.match_type

	def print_comparison(self,show_optional=False):
		""" Print a formatted comparison between the real type and the matched ontology type. """

		# If the field is in the real type, it must be shown... regardless of its optionality

		# Refactor ontology fields object into a more useful shape (key value pairs). 
		ont_type_fields = {field[0]:field[1] for field in self.ont_type_fields}
		
		all_fields = list(set([field for field in ont_type_fields])|set(self.real_type_fields))
		all_fields.sort()

		match_matrix = []
		for field in all_fields:
			if field in self.real_type_fields:
				real_field = field
			else:
				real_field = ''

			if field in ont_type_fields:
				ont_field = field
				ont_field_req = str(ont_type_fields[field])
			else:
				ont_field = ''
				ont_field_req = ''

			match_matrix.append([real_field,ont_field,ont_field_req])

		# Print only required if show_optional is False (except if theres a real field that is defined).
		final_matrix = []
		if not show_optional:
			for row in match_matrix:
				# Only return Trues or actual fields that have a value.
				if row[2] == 'True' or len(row[0])>0: 
					final_matrix.append(row)

		else:
			# Print required first and then append optional.
			for row in match_matrix:
				if row[2] == 'True':
					final_matrix.append(row)
			for row in match_matrix:
				if row[2] == 'False': 
					final_matrix.append(row)
			for row in match_matrix:
				if row[2] == '':
					final_matrix.append(row)

		# Set padding for pretty printing
		padding = 3
		col_width = max(len(field) for field in all_fields) + padding	


		print('TOTAL ASSETS IN THIS TYPE: ',len(self.real_type_assets),'\n')
		print("MATCH COMPLETENESS: '{}'".format(self.match_type))
		print("MATCHED TYPE: '{}'".format(self.ont_type_name))
		print('\n')
		print("".join(field.ljust(col_width) for field in ['ACTUAL FIELDS','TYPE FIELDS','REQUIRED']))
		print("".join(field.ljust(col_width) for field in ['='*(col_width-padding),'='*(col_width-padding),'='*(col_width-padding)]))
		for row in final_matrix:
		    print("".join(field.ljust(col_width) for field in row))
		print('\n')
