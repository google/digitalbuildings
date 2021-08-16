"""Helper Field model classes for Ontology explorer"""

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

  def GetIncrement(self) -> str:
    """Returns the EntityType Field's increment as a string"""
    return self._increment

  def IsRequired(self) -> bool:
    """Returns the optionality of the field as a boolean"""
    return self._is_required
