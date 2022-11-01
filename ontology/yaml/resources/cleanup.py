
import renames
import yaml

for row in renames.renames:
	current_name = row[0]
	namespace = row[1]
	general_type = row[2]
	new_name = row[3]

	if general_type != 'BLR': continue

	filepath = '{namespace}\\entity_types\\{general_type}.yaml'.format(namespace=namespace,general_type=general_type)

	with open(filepath, 'r') as file:
		file_yaml = yaml.load(file,Loader=yaml.FullLoader)
		print("UPDATE: {current_name} --> {new_name}".format(current_name=current_name,new_name=new_name))

		file_yaml[new_name] = file_yaml.pop(current_name)

		with open(filepath,'w') as wfile:
			wfile.write(yaml.dump(file_yaml))