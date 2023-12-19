# Digital Buildings Ontology

The Digital Buildings Ontology defines both
[semantic data](https://en.wikipedia.org/wiki/Semantic_data_model) primitives
and concrete constructions of these primitives to model physical spaces and
equipment. The sections below outline the conceptual model of the ontology.

*   For an explanation of the existing abstract model see [model](model.md).
*   For an explanation of the model configuration files see
    [config](ontology_config.md).

- [Digital Buildings Ontology](#digital-buildings-ontology)
  * [Overview](#overview)
  * [Namespaces](#namespaces)
  * [Components](#components)
    + [Subfields](#subfields)
    + [Fields](#fields)
      - [Equivalence](#equivalence)
      - [Namespace Elevation](#namespace-elevation)
      - [Enumeration](#enumeration)
      - [Structural Flexibility and Ambiguity](#structural-flexibility-and-ambiguity)
      - [Implicit Inheritance](#implicit-inheritance)
      - [Alternate Approaches and Future Extensions](#alternate-approaches-and-future-extensions)
        * [Equipment Composition](#equipment-composition)
        * [Display Name](#display-name)
    + [Dimensional Units](#dimensional-units)
    + [Multi-State Values](#multi-state-values)
      - [Individual States](#individual-states)
      - [Multi-State groups](#multi-state-groups)
      - [Effect on Namespace Elevation](#effect-on-namespace-elevation)
    + [Entity types](#entity-types)
      - [GUIDs](#guids)
      - [Type names](#type-names)
      - [Field Definitions](#field-definitions)
      - [Inheritance](#inheritance)
      - [Abstract Types](#abstract-types)
      - [Canonical Types](#canonical-types)
      - [Relationship Constraints](#relationship-constraints)
    + [Relationships](#relationships)
    + [Change Management](#change-management)
    + [Notes](#notes)


## Overview

The Digital Buildings project is concerned with modeling the characteristics and
telemetry of **entities**, and their relationships with each other. An entity is
any instance of a "thing" in the model; for example a building, a floor, or a piece of equipment (like an energy meter). The ontology is concerned with
"describing the thing."

The ontology describes entities using **entity types**. An entity type indicates
both a place within the ontology's composable taxonomy and a set of semantically
defined data **fields** that are expected for that entity. Fields are composed
of structured groupings of **subfields** that provide them with specific
meaning.

Relationships between entities are defined by directed, named **connections**.

Other components of the model stack, such as translations and links, are
discussed in [onboarding](building_config.md).

## Namespaces

All elements of the ontology are organized into namespaces, with some
constraints. There is a global namespace that all other namespaces can reference
directly. Below the global namespace, the ontology allows exactly one level of
additional namespaces. Hierarchical namespacing is explicitly disallowed. In
the interest of cross-compatibility, certain components are elevated to the
global namespace when possible (more details on this in individual component
sections).

## Components

### Subfields

The subfield is the basic unit of meaning in the ontology. Each subfield
consists of a single or compounded word[^5] with a very specific human-readable
definition. Subfields are largely analogous to the concept of a "tag" in Brick
or Haystack, but with a few more constraints.

Subfields have the following attributes:

*   Subfields are typically globally defined (i.e., defined in the global namespace).
*   Subfields must be unique within their namespace (typically the global namespace).
*   Each subfield have a unique and specific meaning.
*   Subfield names may be camelCased for readability, but are not case sensitive.
*   Subfields should be used nearly universally across different namespaces and
    applications.
*   Subfields cannot be referred to with a namespace identifier (e.g., HVAC/subfield is not a valid reference).
*   Subfields are grouped into categories that dictate their grouping with each other when they are combined into sets to form fields.

There is no explicit namespacing for subfields, so an individual field's
namespace can only use one definition of a subfield.[^6] It is expected that the
vast majority of subfields will be defined in the global namespace. Defining a
subfield locally prevents any field using it from being elevated to the global
namespace.[^7]

Subfields are grouped into categories that add structure to field composition (note that the ordering of this table reflects the expected ordering of subfields in field construction).

<table>
  <tr>
   <td><strong>Category</strong></td>
   <td><strong>Description</strong></td>
   <td><strong>Examples</strong></td>
   <td><strong>Allowed Per Field</strong></td>
   <td><strong>Required</strong></td>
  </tr>
  <tr>
   <td><p style="text-align: right">Aggregation Descriptor</p></td>
   <td>
     A subfield that modifies aggregations to explicitly differentiate temporal aggregation (e.g., daily max) from spatial aggregation (e.g., the max of 3 zone temperature sensors in a space). Note that windowing specifics are added into this subfield, and omitting them implies a fixed window (e.g., the max over the day boundary if `daily` is used). (Note: the window time is always spelled out to avoid subfield validation errors.) This subfield can only used when accompanied by an aggregation subfield.
   </td>
   <td>daily, fivesecond, fivesecondrolling</td>
   <td>1</td>
   <td>Optional (Required if Aggregation is used)</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Aggregation</p></td>
   <td>
     An aggregation such as minimum, maximum, rootmeansquare, etc. It is implied that aggregations are spatial (e.g., the max of 3 zone temperature sensors in a space) except when accompanied by a defined aggregation descriptor. In any case, this is not the same as an operating limit (e.g., the max flowrate for a valve); these are treated separately (see note below).
   </td>
   <td>Average, Max, Min</td>
   <td>1</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Descriptor</p></td>
   <td>General purpose modifier that specifies the exact function of the field within the context of the entity. The number of descriptors used should be limited by the context (i.e., if a descriptor is extraneous it should be omitted).
   </td>
   <td>Discharge, Return, Zone, Primary, Chilled etc...</td>
   <td>10</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Component</p></td>
   <td>Specifies the specific subcomponent of the entity being represented (e.g., the fan of a fan-coil unit). As with descriptors, context drives necessity; supply_fan_run_command is necessary for an AHU because there will routinely be an exhaust_fan_run_command that it needs to be distinguished from, but it is clear from the context of a FAN (that’s all it is) that run_command applies to the fan, and therefore no component subfield is necessary to describe it.
</td>
   <td>Valve, fan, damper...</td>
   <td>10</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Measurement Descriptor</p></td>
   <td>
     A modifier of the measurement which adds necessary context. The classic example of this is pressure, which must be distinguished between differential and absolute.
   </td>
   <td>Differential, relative, static</td>
   <td>1</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Measurement</p></td>
   <td>A field that implies the type of measurement being performed. Each measurement is exclusive to a particular physical quantity (e.g., temperature), but which may have multiple valid units of measurement (*F, R, *C, K). This subfield is required for any numeric field with a point type other than `count`.
   </td>
   <td>Temperature, flowrate, flowvolume</td>
   <td>1</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Point Type</p></td>
   <td>Defines the function of the point across several layers of context: directionality (input/output), reading type (analog, input, multistate), telemetric versus static data (label and capacity being static; sensor and setpoint being active), etc. This is the one component that is required for every field.
   </td>
   <td>Sensor, Setpoint, Status, Command, Count, Accumulator</td>
   <td>1</td>
   <td>Required</td>
  </tr>
</table>

**Note:** See [HVAC model](model_hvac.md) for details on operating limits.

### Fields

Fields are constructed by combining subfields in a structured way to define very
specific semantic concepts. Field names are intended to read naturally and be
self-describing based on the composition of subfield definitions.

A field adheres to the following rules:

*   The field must be unique within its namespace.
*   The field's subfields must used in their correct locations based on their categories (i.e., the complete field name must follow the construction format).
*   Each subfield can be used no more than once in the field name.
*   The field cannot have the same set of subfields as another field with different
    ordering.
*   The field must specify a measurement subfield for any numeric point (unless the point type is
    `count`).

The format of a field is as follows:

`(<agg_desc>_)?(<agg>_)?(<descr>_)*(<component>_)?(<meas.
descr>_)?(<meas>_)?<pointtype>(_<num> )*`[^13]

Example: `max_discharge_air_temperature_setpoint`

#### Equivalence

While the ordering of subfields within a field has value in communicating the
field's semantic meaning to a human reader, we enforce that it is only the set
of contained subfields that is necessary for equivalence testing.[^14]
Applications should depend on the field set, not the string value.

#### Namespace Elevation

The ontology prefers elevating fields to the global namespace whenever possible.
This means that any field using only globally defined subfields and multistate
values can be referenced by any namespace as if it is global, even if it is
defined in a child namespace. Identically defined fields in different child
namespaces are therefore equivalent[^23] (equivalence is defined by the subfield
set).

#### Enumeration

In some cases a device may have two points with semantically identical meaning
(i.e., if a device has two identical zone temperature sensors). In this case, the
two sensors must use the same field name. To differentiate them we allow a
numeric increment to be added to the name, i.e., `<field>_1`. Multiple increments
are allowed to indicate subgrouping as well, i.e., `<field>_2_1`.

NB: Modelers should be careful with applying enumerations, as the analysis
applied will be unable to apply meaningful distinctions to such fields. This
shouldn't be a problem normally since, if two points are functionally different,
they shouldn't have the same name. For example, if supply_air_temperature_sensor_1 is
the real control sensor while supply_air_temperature_sensor_2 is redundant for
monitoring, they should have separate names. For ease of integration, omission
of the redundant point is acceptable, but if that is not desired an additional
descriptor should be added.

#### Structural Flexibility and Ambiguity

A very strict naming convention can have the unintended consequence of creating
redundant or unnecessarily long names. For instance, a
`discharge_air_fan_power_sensor`is redundant because fans deal only with Air. It
could be easily shortened to `discharge_fan_power_sensor` without losing
clarity.

When constructing field names, the user should choose the smallest set of
subfields that uniquely defines the concept within the scope. Because device
scope is defined arbitrarily, there is not necessarily one correct way to
construct a point. Each individual implementation will have to adopt its own
conventions for how to break up equipment and name points. See
[Alternate Approaches and Future Extensions](#alternate-approaches-and-future-extensions)
for further discussion.

#### Implicit Inheritance

Any set of adjacent subfields can be considered a root concept from which fields
with longer names inherit. Depending on the fields added, this relationship can
extend on multiple axes, forming a graph of related concepts. This graph can be
used to navigate related concepts with different names. For instance, a search
engine could use the graph to fan out the search for `zone_air_temperature` out
across all fields that have a superset of the tags `zone`, `air` and
`temperature`.[^18]

#### Alternate Approaches and Future Extensions

##### Equipment Composition

As with most systems models, the decision of how to draw boundaries around
entities is subjective and, to some degree, arbitrary. In building the ontology,
we face the common trade off between a flatter graph with fewer, more complex
entities or a deep graph of simpler interconnected ones. The former results in a
smaller and easier to manage set of components and relationships. The latter
encourages smaller and more easily comparable components.

In the Digital Buildings model, this decision applies to how we model complex
equipment. For instance. If a device has two identical fans with different
purposes (e.g., supply and exhaust) the model needs to somehow differentiate them. In
a flat approach, we could represent this device as a single entity type with
fields for both fans and add descriptors to all the fan fields such that
everything for each fan has the same descriptor prefix (`supply_`, `exhaust_`).
Alternately, we could model this device as a graph that includes two identical
fans connected to a parent entity via relationships (minimally `HAS_PART`, in
this case).

In the former model we end up with a larger fan-out of field names (e.g.,
`supply_fan_run_status` and `exhaust_fan_run_status` vs. just `fan_run_status`), but a
smaller number of entities to represent the device (one instead of three in this
case) and lower expressivity requirements for relationships.

The concrete models and existing primitives of the Digital Building ontology
generally favor the flatter modeling approach. This decision is driven by the
reality that each piece of equipment is generally analyzed as a unit, and
therefore decomposing it simply means more difficult retrieval.

##### Display Name

The current design imposes that the entire set of subfields associated with a
field be part of the visible field name. The challenge with this approach is
that imparting a complete and nuanced meaning to a field could result in a very
long field name that feels unnecessarily complex in context. A potential future
solution to this is to allow types to define display names for fields that omit
component subfields or subset descriptors. This would allow fields to be more
fully qualified on the backend for lookup and comparison without making them
unwieldy for the user.

### Dimensional Units

In the ontology, measurement subfields identify what dimensional units apply to
a field. the measurement subfield must be provided any time a field describes a
numeric value (unless the point type is `count`).

Each measurement subfield maps to one and only one quantity kind. For instance
data for a field with the `temperature` subfield could be assigned units of
Kelvin or Fahrenheit, but not pounds. The units configuration for each subfield
calls out all the supported units for each subfield as well as a _standard_ unit
for each. Standard units should all be from the same unit family to ease
standardization. The ontology currently standardizes on SI as the unit family.

While the current ontology configuration does not explicitly call out conversion
factors, it generally tries to conform to unit names from
[QUDT](https://www.qudt.org/) so that their conversion
factors can be used. Future development may integrate a unit ontology more
directly.

### Multi-State Values

A multi-state is a data type that consists of an enumerated set of states with
specific meanings, such as {ON, OFF, AUTO}.

#### Individual States

Like subfields, states are intended to be global whenever possible, but can be
defined only within a namespace as well. Each state has a specific definition
that is the same wherever it is used.

In order to maximize interoperability each possible state must have one
canonical definition. For flexibility we would also like to allow modification
of the set of states without needing to update the global namespace.

#### Multi-State groups

Multi-state groups are defined on a field-by-field basis. Fields with point type
`status` or `mode` are always multistates whereas ones with type `command`
should be interpreted as multistate if not given a measurement subfield. All
allowed states for a field across all devices are listed, however individual
devices may or may not use all states (TODO: link to translations doc).

#### Effect on Namespace Elevation

States can affect whether fields are elevated to the global namespace. Like with
subfields, only fields having globally defined states can be elevated to the
global namespace.

### Entity types

An entity type is a grouping of fields with a specific description that
represents a "thing" in the building model. Obvious examples include a room, an
air conditioner, or a camera. It is also possible to define an entity that maps
to a defined functionality that is a subset of a complete device. For instance,
we might want to define the fields needed for high/low setpoint temperature
control as its own entity type in the ontology.

Entity types can have any of the following attributes:

*   A name (e.g., VAV_SD_DSP), which is the visible identifier for the type but has no structural meaning.
*   A UUID4 GUID, which is version-independent and is automatically set by the system.
*   A description giving a short and human-readable summary of the type and its meaning.
*   An abstract or canonical flag.
*   An allow undefined fields flag.
*   A list of zero or more parent types.
*   Required and/or optional fields (if the fields are not already inherited by one of the parent types).
*   Required Relationships (coming soon).

A type has meaning beyond its defined fields. For instance, an entity of type X
and type Y, both having field A are distinguishable from each other, even though
they have the exact same fields.

#### GUIDs
Each type has a GUID (UUID4) that is version-independent.

#### Type names

Type names have no structural meaning in the ontology, but because this is the
most visible identifier of the type, the concrete types adhere to the
convention of starting with a general type (TODO: structurally define how
general types are identified) followed by an `_` separated list of parent
types.[^24] Type names may change from version to version, independent of
[GUID](#guid).

#### Field Definitions

Fields on types can be defined either as required or optional. The intent of
this is to minimize the number of distinct entity types that are required to
cover the equipment set. This is especially true in the HVAC domain when there
may be a large number of minor (unimportant) variations in a particular
general type but there is a set of common fields across all of the devices
that are used for analysis.

#### Inheritance

Types in the ontology can inherit field associations from other types. Multiple
inheritance is allowed with the following combination rules.

*   A field inherited from multiple parents is considered to exist only once in
    the child.
*   If a field is associated to a type directly or through inheritance as both
    required and optional, the resulting definition shows the field as required.
*   Field increments are preserved and same fields with different increments are
    considered unique.
*   Relationship requirements are additive, with the strictest requirement
    prevailing.
*   Conflicting relationships constraints are construction errors.
*   Attributes (`description`, `guid`, `is_canonical`, `is_abstract`) are not
    inherited.

As with individual types, inheritance trees are meaningfully independent of
the resulting field set. For instance, Type X inheriting from V and W is
distinguishable from type Y inheriting from only V, even if both types only have
field A.

Composable inheritance is primarily intended to encourage users to define
subunits of functionality with associated fields, and build types by composing
the subunits.

#### Abstract Types

Designating a type as abstract indicates that it should only be used in
inheritance and not directly associated with any entities. This is typically
used for abstract units of functionality that are used to compose other types.

#### Passthrough Types

The `allow_undefined_fields` flag can be used to define a passthrough type,
which does not directly correspond to a logical entity in the model. Instead, a
passthrough entity provides translations that will be linked to one or more
other entities. When `allow_undefined_fields` is true, entities of this type are
allowed to define translations for fields that are not listed as required or
optional on this type.

Passthrough types cannot be inherited by other types, which makes the
`allow_undefined_fields` flag mutually exclusive with the `is_abstract` flag.

#### Canonical Types

In real modeling environments we find there are often exceptions to our
idealized picture of the world. When this occurs we need to create one-off
constructions to cover the exceptions. To take a concrete example, we often see
device controllers in the HVAC world that carry sets of points for multiple
logical pieces of equipment. Because we use the convention of creating a type
for every device that sends data to the system, we end up with a lot of types
that have odd collections of points that don't map to any specific equipment
concept.

The `is_canonical` flag lets the modeler differentiate between 'official'
curated types (canonical) and everything else (not canonical).

#### Relationship Constraints

Each entity type may define requirements for what connections must be made
between an entity of a certain type and entities of other types. For instance,
it might be a requirement that a `VAV` terminal in a HVAC connection have a
`FEEDS` connection from an Air Handler (`AHU`). Connections requirements are
always defined on the destination entity to avoid validation deadlocks when
building models.

NB: This functionality is still in development.

### Relationships

The ontology supports named relationships between entities called connections.
Each relationship has a specific definition that defines the how the two
entities are connected. This may be a physical (e.g., `FEEDS`) or logical (e.g.,
`HAS_PART`). Connections are always global. Connections and their descriptions
can be found here. **TODO add link**.

### Change Management

Versioning is anticipated for the ontology, though the exact process and
constraints are TBD.

<!-- Footnotes themselves at the bottom. -->

### Notes

[^5]: We deliberately do not use camel case here because it makes conversion of
    _ to Camels ambiguous. \
[^6]: We do allow individual namespaces to override global definitions, as this
    does not break globally unique naming and has unambiguous meaning (the
    relevant subfield definition can be found directly in the namespace of the
    field). We do not, however, anticipate needing namespaced subfields in
    Carson. \
[^7]: see a discussion of namespace elevation in [Fields](#fields). \
[^13]: The `_<num>` field is used for cases when a particular entity type has
    more than one field with a particular semantic value. Any field may have
    this suffix. It does not need to be explicitly defined in the
    configuration. \
[^14]: This is the case because we explicitly prohibit different orderings of
    the same descriptors to have meaning and actively purge them at
    validation time. \
[^18]: NB: there is likely some additional logic needed here to deal with
    different types of subfields, ex: `max_zone_air_temperature_sensor`might
    be treated differently because it is an aggregation. \
[^23]: The configuration syntax takes this ambiguity into account in such a way
    to minimize the amount of namespace qualification required. \
[^24]: Validation currently depends on comparing the fist segment of the name
    for determining whether certain types should be compared with each other
    for certain configuration linter warnings. This should be replaced with a
    check on some aspect of the type structure rather than the name.
