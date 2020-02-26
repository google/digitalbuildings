# Ontology

The Digital Building Ontology is organized as following


## Terminology

Field the name of a single value within an entity type.  Equivalent to Brick "tagset".
Subfield a single component term in a field.  Equivalent to Brick "tag".
Entity Type a grouping of fields with a specific definition.

## Requirements
Fields must:
* be unique within each namespace
* have unique, specific definitions within each namespace
* have all subfields and their definitions residing in the same namespace
* Allow the assignment of a measurement type or multi-state definition

Subfields must:
* be unique within each namespace
* have unique, specific definitions within each namespace
* allow assignment of a subfield category [media, modifier, type] for validation

## Subfields
Each subfield consists of a single or compounded word with a very specific human-readable definition. While subfields may be camelCased for readability, they should not be case sensitive.  Subfields should be used nearly universally across different namespaces and applications.  There is no explicit namespacing for subfields, so an individual field's namespace can only use one definition of a subfield.  It is expected that the vast majority of subfields will be defined in the global namespace.  Defining a subfield prevents any field using it from being up-leveled to the global namespace. 

In addition to a textual definition, it is also useful to broadly categorize subfields based on how they are used in field composition:

| Category  | Examples |
| :--- | :--- |
| Aggregation  | Average, Max, Min  |
| Descriptor | Discharge, Return, Zone, Primary, Chilled, others |
| Component | Valve, fan, damper, others |
| Measurement Descriptor | Differential, relative, static, alarm |
| Measurement | Temperature, flowrate, flowvolume, position, occupancy |
| Point Type | Sensor, Meter, count, Setpoint, Status, Command, count |


### Non-Measurement Subfields
Most categories of subfields can be defined in any structured format of the form:
```
<Name><delim><Category><delim><Definition>
```

### Measurement Subfields
Config for measurements will need a form similar to:
```
<Name><delim><Category><delim><measurementType><delim><Definition>
```
The above format assumes that names for enumeration definitions and measurement types are non-overlapping

The "measurementType" (which includes physical measurement types such as "thermodynamic temperature"  as well as multi-state, boolean and non-dimensional numbers) is a constraint on the specific types that can later be used for validation. Valid measurement Types and Multi-state definitions will be defined separately or pulled from other ontologies (see following sections).

### Descriptor Types
One of the challenges of making a human-readable name is that in natural language we have complex rules for how we order terms that would be difficult to achieve in a simple naming convention.  To address this we allow a lot of flexibility in field construction. There is only one required field and most terms are arbitrarily grouped "descriptors" that clarify meaning.

The flexibility of the naming convention limits our ability to validate fields.  For instance, we would be unable to identify that:
```
heating_discharge_air_temperature_sensor
heating_discharge_temperature_sensor
discharge_heating_temperature_sensor
```
Were all likely referring to the same thing, and that one is ambiguous, unless the media "air" was a separate type.  In order to address this we use the concept of descriptor types to help us make these differentiations.  With types, we can create smaller semantically-related groups of descriptors to compare during validation while not restricting the construction order.  In the example above, placing "air" in a media descriptor type allows us to see that the rest of the descriptors are the same across all three fields and mark them for disambiguation.

## Fields
In the Digital Buildings Ontology, fields are constructed by combining subfields in a structured way to define very specific semantic concepts.  Composed field names are intended to read naturally and be self-describing based on the composition of subfield definitions.  It is not, however, expected that fields be trivially decomposable or substrings thereof comparable, though the latter is likely to be meaningful in the proposed design.  The field format provides enough structure to keep names relatively consistent, but some flexibility in the ordering of terms is allowed, and would have to be dealt with in a separate validation process.

The format of a field is a follows:
```
(<Agg>_)?(<descr>_)*(<component>_)?(<meas. descr>_)?<meas><PointType>(_<num>)*

Ex: max_discharge_air_temperature_setpoint

```

### Equivalence
While the ordering of subfields within a field has value in communicating the field's semantic meaning to a human reader, we enforce that it is only the set of contained subfields that is necessary for equivalence testing.  This feature is extremely useful for increasing interoperability distributed construction of the field list, as explained in the next subsection.

### Up-leveling Namespaces
In order to maximize interoperability we prefer to keep as many fields as possible mapped to a global namespace.  As a result, the framework attempts to up-level every field it can to the global namespace.  This is possible because subfields are generally global.  As a result, it is possible to validate in a distributed manner that any two fields using only global subfields have the same construction.  By the first-principles of semantic naming, this should mean they have the same meaning.  Thus, up-leveling is safe as long as fields are using only globally-defined subfields.

Though equivalence is defined only by the subfield set, it is confusing to the reader (and potentially to a program, without some additional constructs) if two equivalent fields have different descriptor ordering.  When the entire ontology is constructed monolithically, it is possible to prevent such cases through validation.  However, if the ontology is compiled from independently maintained sources, reversals may occur.  As a result, the ontology must adopt a way of standardizing these terms for applications.  One such method is to maintain an alias for each field with alpha-ordered descriptors.  Such an alias is universal, and as long as programs use compiled code to access data, we can abstract away the ordering implementation details.

### Scripted Construction
A consequence of the requirement for each field to represent a specific unique concept is fan-out of field names that are predictable permutations of other field names:
```
Discharge_air_temperature_setpoint
Discharge_air_temperature_sensor
Discharge_air_temperature_alarm
Max_discharge_air_temperature_setpoint
Min_discharge_air_temperature_setpoint
```
In order to minimize duplicate work, the tooling for the ontology should support automatic composure of subfields based on a minimal configuration.

For example, fields above (as well as other fields)  could be configured with a yaml block something like this: 
```
Aggregation:["",min,max]
Descriptors: // order matters when combining groups
[return, discharge] // can be composite like "primary_building"
Cooling
Component: ["", valve}
Measurement_descriptor: ["",differential"]
Measurement: temperature
Type: [sensor,setpoint]
```

In the construction above everything except Point Type is optional, but measurement is generally expected except in the case of a label, which is always a string, or boolean value (the default data type).   The script iterates through all the terms, creating all the possible combinations.  Descriptors can be a nested array to allow ordering of the terms to be specified.

Like multi-state values, fields can be namespaced but we desire as many fields as possible to be at the top level.

### Structural Flexibility and Ambiguity
A very strict naming convention can have the unintended consequence of creating redundant or unnecessarily long names.  For instance, a `discharge_air_fan_power_sensor` is redundant because fans deal only with Air. It could be easily shortened to discharge_fan_power_sensor without losing clarity.

We allow the user to use the shortest name that uniquely defines the concept within the scope.  For components, we can use the defined default media to check for duplicate fields with and without the media defined.  Some ambiguity is likely to remain, however.  See Alternate Approaches and Future Extensions for further discussion.
Implicit Inheritance
Regardless of how strictly one enforces the modeling of equipment as collections of simple components, it will always be impossible to use field names literally for comparisons across devices and ensure 100% capture of like fields.  This is due to the fact that more complicated equipment may have additional descriptors to describe a field than simple equipment with the same point.

In this case we need some way to find similarities between fields that are semantically meaningful.
Example: `zone_air_temperature_sensor_1`, `secondary_zone_air_temperature_sensor` and `zone_air_temperature_sensor` are all measuring the same thing, but have different names.
The names are, however, related. 

Any set of adjacent subfields can be considered a root concept from which fields with longer names inherit.  Depending on the fields added, this relationship can extend in multiple axes, forming a graph of related concepts. This graph can be used to navigate related concepts with different names.  For instance a search engine could use the graph to fan out the search for `zone_air_temperature` out across all the child fields.

### Validation
Ensure that:
* all fields are unique per-namespace
* subfields are all used in their correct location based on their types.
* all required components of a field are specified
* each subfield is only used once in a field
* no two fields have the exact same set of subfields (i.e. check for reversals of descriptor fields)
* call out when a set of defined fields for a type are defined by another type (suggest parent type relationships)

