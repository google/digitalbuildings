"""Helper Field model classes for Ontology explorer"""
from typing import List

from yamlformat.validator.entity_type_lib import EntityType

class StandardField(object):
  """
    A class to represent a generic field without increment or optionality

    Args:
        namespace_name: the name of the field's namespace as a string
        standard_field_name: the name of the field as a string

    Attributes:
        namespace: the name of the namespace as a string
        name: the field name as a string

    returns:
        An instance of the StandardField class

  """

  def __init__(self, namespace_name: str, standard_field_name: str):
    super().__init__()
    self._namespace = namespace_name
    self._name = standard_field_name

  def __hash__(self):
    return hash((self._namespace, self._name))

  def __eq__(self, other):
    namespace_eq = self._namespace == other.GetNamespaceName()
    name_eq = self._name == other.GetStandardFieldName()
    return name_eq and namespace_eq

  def __str__(self):
    return self._namespace + '/' + self._name

  def GetNamespaceName(self) -> str:
    """Returns namespace variable as a string"""
    return self._namespace

  def GetStandardFieldName(self) -> str:
    """Returns the unqualified field name
    without any increment as a string"""
    return self._name

class EntityTypeField(StandardField):
  """
  A class to represent a field assigned to a type and extends StandardField

  Args:
      namespace_name: the name of the field's namespace as a string
      standard_field_name: the name of the field as a string
      increment: the increment of the field as a string
      is_required: optionality of the field as a boolean

  Attributes:
      increment: the increment of the field under a type
      is_required: optionality of the field relative to it's Entity Type#
                   Configure the Azure provider

  Returns:
      An instance of the EntityTypeField class
  """

  def __init__(self,
               namespace_name: str,
               standard_field_name: str,
               is_required: bool,
               increment: str = ''):
    super().__init__(namespace_name, standard_field_name)
    self._increment = increment
    self._is_required = is_required

  def __hash__(self):
    return hash((
        self._namespace,
        self._name,
        self._increment,
        self._is_required
    ))

  def __eq__(self, other):
    standard_eq = super().__eq__(other)
    increment_eq = self._increment == other.GetIncrement()
    require_eq = self._is_required == other.IsRequired()
    return standard_eq and increment_eq and require_eq

  def __str__(self):
    standard_str = super().__str__()
    return standard_str + '_' + self._increment + ': ' + str(self._is_required)

  def GetIncrement(self) -> str:
    """Returns the EntityType Field's increment as a string"""
    return self._increment

  def IsRequired(self) -> bool:
    """Returns the optionality of the field as a boolean"""
    return self._is_required

class Match(object):
  """
  A class to hold the information about a match between a list of fields
  and an Entity Type

  Args:
    field_list: a list of fields and their optionality
    entity_type: the type to which it matches to
    match_type: the closeness of a match between fields and entity type

  Attributes:
    field_list
    entity_type
    match_type

  Returns:
    An instance of the Match class
  """

  def __init__(
      self,
      field_list: List[StandardField],
      entity_type: EntityType,
      match_type: str
  ):
    super().__init__()
    self._field_list = field_list
    self._entity_type = entity_type
    self._match_type = match_type

  def __eq__(self, other):
    field_eq = self._field_list == other.GetFieldList()
    type_eq = self._entity_type == other.GetEntityType()
    match_eq = self._match_type == other.GetMatchType()
    return field_eq and type_eq and match_eq

  def __str__(self):
    return str(self._match_type) + ' match: ' + str(self._entity_type.typename)

  def GetFieldList(self) -> List[StandardField]:
    """Returns the list of standard fields for a match"""
    return self._field_list

  def GetEntityType(self) -> EntityType:
    """Returns the entity type for a match"""
    return self._entity_type

  def GetMatchType(self) -> str:
    """Returns the Match Type for a match"""
    return self._match_type

def ConvertETFtoSF(field_list: List[EntityTypeField]) -> List[StandardField]:
  res = []
  for etf in field_list:
    res.append(StandardField(etf.GetNamespaceName(),
                             etf.GetStandardFieldName()))
  return res
