# Digital Buildings Ontology

The Digital Buildings Ontology defines both
[semantic data](https://en.wikipedia.org/wiki/Semantic_data_model) primitives
and concrete constructions of these primitives to model physical spaces and
equipment. The sections below outline the conceptual model of the ontology.

*   For an explanation of the concrete model see [model](model.md)
*   For an explanation of the model configuration files see
    [config](ontology_config.md)

[TOC]

## Overview {#overview}

The Digital Buildings project is concerned with modeling the characteristics and
telemtry of **entities**, and their relationships with each other. An entity is
any instance of a "thing" in the model. The ontology is concerned with
"describing the thing".

The ontology describes entities using **entity types**. An entity type indicates
both a place within the ontology's composable taxonomy and a set of semantically
defined data **fields** that are expected for that entity. Fields are composed
of structured groupings of **subfields** that provide them with specific
meaning.

Relationships between entities are defined by directed, named **connections**.

Other components of the model stack, such as translations and links are
discussed in [onboarding](building_config.md)

## Namespaces {#namespaces}

All elements of the ontology are organized into namespaces, with some
constriants. There is a global namespace that all other namespaces can reference
directly. Below the global namespace, the ontology allows exactly one level of
additional namespaces. Hie rarchical namespacing is explicitly disallowed. In
the interest of cross-compatibility, certain components are elevated to the
global namespace when possible (more details on this in individual component
sections)

## Components

### Subfields {#subfields}

The subfield is the basic unit of meaning in the ontology. Each subfield
consists of a single or compounded word[^5] with a very specific human-readable
definition. Subfields are largely analogous to the concept of a "tag" in Brick
or Haystack, but with a few more constraints.

Subfields:

*   are typically globally defined
*   are uniqely named in their namespace (typically the global namepspace)
*   each have a unique and specific meaning.
*   may be camelCased for readability, but are not case sensitive.
*   should be used nearly universally across different namespaces and
    applications.
*   cannot be referred to with a namespace identifier.
*   are grouped into categories that dictate their grouping with each other.
*   are combined into sets to form fields.

There is no explicit namespacing for subfields, so an individual field's
namespace can only use one definition of a subfield[^6]. It is expected that the
vast majority of subfields will be defined in the global namespace. Defining a
subfield locally prevents any field using it from being elevated to the global
namespace[^7].

Subfields are grouped into categories that add structure to field composition:

<table>
  <tr>
   <td><strong>Category</strong></td>
   <td><strong>Description</strong></td>
   <td><strong>Examples</strong></td>
  </tr>
  <tr>
   <td><p style="text-align: right">Aggregation</p></td>
   <td>
     An aggregation in the spatial domain, for instance the average value of multiple tepmerature sensors. This is not the same as an operating limit.
   </td>
   <td>Average, Max, Min</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Descriptor</p></td>
   <td>General puprose modifier that specifies the exact function of the field within the context of the entity. The number of descriptors used should be limited by the context (i.e., if a descriptor is extraneous it should be omitted).
   </td>
   <td>Discharge, Return, Zone, Primary, Chilled etc...</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Component</p></td>
   <td>Specifies the specific subcomponent of the entity being represented (e.g. the fan of a fan-coil unit). As with descriptors, context drives necessity; supply_fan_run_command is necessary for an AHU because it routinely will have an exhaust_fan_run_command that needs to be distinguished from, but it is clear from the context of a FAN (that’s all it is) that run_command applies to the fan, and therefore no component subfield is necessary to describe it.
</td>
   <td>Valve, fan, damper...</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Measurement Descriptor</p></td>
   <td>
     A modifier of the measurement which adds necessary context. The classic example of this is pressure, which must be distinguished between differential and absolute.
   </td>
   <td>Differential, relative, static</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Measurement</p></td>
   <td>A field that implies the type of measurement being performed. Each measurement is exclusive to a particular physical quantity (e.g. temperature), but which may have multiple valid units of measurement (*F, R, *C, K).  This subfield is required for any numeric field with a point type other than `count`.
   </td>
   <td>Temperature, flowrate, flowvolume</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Point Type</p></td>
   <td>Defines the function of the point, across several layers of context: directionality (input/output), reading type (analog, input, multistate), telemetric versus static data (label and capacity being static; sensor and setpoint being active), etc. This is the one component that is required for every field.
   </td>
   <td>Sensor, Setpoint, Status, Command, Count, Accumulator</td>
  </tr>
</table>

### Fields {#fields}

Fields are constructed by combining subfields in a structured way to define very
specific semantic concepts. Field names are intended to read naturally and be
self-describing based on the composition of subfield definitions.

A field:

*   is unique per-namespace
*   has subfields used in their correct locations based on their categories.
*   follows the construction format
*   has each subfield used no more than once
*   does not have the same set of subfields as another field with different
    ordering
*   specifies a measurement subfield for any numeric point unless point type is
    `count`

The format of a field is a follows:

`(<Agg>_)?(<descr>_)*(<component>_)?(<meas.
descr>_)?(<meas>_)?<PointType>(_<num> )*`[^13]

Ex: `max_discharge_air_temperature_setpoint`

#### Equivalence {#equivalence}

While the ordering of subfields within a field has value in communicating the
field's semantic meaning to a human reader, we enforce that it is only the set
of contained subfields that is necessary for equivalence testing[^14].
Applications should depend on the field set, not the string value.

#### Namespace Elevation {#namespace-elevation}

The ontology prefers elevating fields to the global namepsace whenever possible.
This means that any field using only globally defined subfields and multistate
values can be referenced by any namespace as if it is global, even if it is
defined in a child namespace. Identically defined fields in different child
namespaces are therefore equivalent[^23] (equivalence is defined by the subfield
set)

#### Enumeration {#enumeration}

In some cases a device may have two point s with semantically identical meaning
(ex: if a device has two identical zone temperature sensors). In this case, the
two sensors must use the same field name. To differentiate them we allow a
numeric increment to be added to the name, ex: `<field>_1`. Multiple increments
are allowed to indecate subgrouping as well, ex: `<field>_2_1`.

#### Structural Flexibility and Ambiguity {#structural-flexibility-and-ambiguity}

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

#### Implicit Inheritance {#implicit-inheritance}

Any set of adjacent subfields can be considered a root concept from which fields
with longer names inherit. Depending on the fields added, this relationship can
extend on multiple axes, forming a graph of related concepts. This graph can be
used to navigate related concepts with different names. For instance a search
engine could use the graph to fan out the search for `zone_air_temperature`out
across all fields that have a superset of the tags `zone`, `air` and
`temperature`[^18].

#### Alternate Approaches and Future Extensions {#alternate-approaches-and-future-extensions}

##### Equipment Composition {#equipment-composition}

As with most systems models, the decision of how to draw boundaries around
entities is subjective, and to some degree arbitrary. In building the ontology,
we face the common trade off between a flatter graph with fewer, more complex
entities or a deep graph of simpler interconnected ones. The former results in a
smaller, easier to manage set of components and relationships. The latter
encourages smaller, more easily comparable components.

In the Digital Buildings model, this decision applies to how we model complex
equipment. For instance. If a device has two identical fans with different
purposes (supply and exhaust) the model needs to somehow differentiate them. In
a flat approach, we could represent this device as a single entity type with
fields for both fans and add descriptors to all the fan fields such that
everything for each fan has the same descriptor prefix (`supply_`, `exhaust_`).
Alternately, we could model this device as a graph that includes two identical
fans connected to a parent entity via relationships (minimally `HAS_PART`, in
this case).

In the former model we end up with a larger fan-out of field names (ex:
`supply_fan_run_status` and `exhaust_fan_run_status` vs `fan_run_status`), but a
smaller number of entities to represent the device (one instead of three in this
case) and lower expressivity requirements for relationships.

The concrete models and existing primitives of the Digital Building ontology
generally favor the flatter modeling approach. This decision is driven by the
reality that each piece of equipment is generally analyzed as a unit, and
therefore decomposing it simply means more difficult retrieval.

##### Display Name {#display-name}

The current design imposes that the entire set of subfields associated with a
field be part of the visible field name. The challenge with this approach is
that imparting a complete and nuanced meaning to a field could result in a very
long field name that feels unnecessarily complex in context. A potential future
solution to this is to allow types to define display names for fields that omit
component subfields or subset descriptors. This would allow fields to be more
fully qualified on the backend for lookup and comparison without making them
unwieldy for the user.

### Dimensional Units {#dimensional-units}

In the ontology, measurement subfields identify what dimensional units apply to
a field. the meaurement subfield must be provided any time a field describes a
numeric value, unless the point type is `count`

Each measurement subfield maps to one and only one quantity kind. For instance
data for a field with the `temperature` subfield could be assigned units of
Kelvin or Fahrenheit, but not pounds. The units configuration for each subfield
calls out all the supported units for each subfield as well as a _standard_ unit
for each. Standard units should all be from the same unit family to ease
standardization. The ontology currently standardizes on SI as the unit family.

While the current ontology configuration does not explixtly call out conversion
factors, it gnerally tries to conform to unit names from
[QUDT](http://www.qudt.org/release2/qudt-catalog.html) so that their conversion
factors can be used. Future development may integrate a unit ontology more
directly.

### Multi-State Values {#multi-state-values}

A multi-state is a data type that consists of an enumerated set of states with
specific meanings, such as {ON, OFF, AUTO}.

#### Individual States {#individual-states}

Like subfields, states are intended to be global whenever possible, but can be
defined only within a namespace as well. Each state has a specifc definition
that is the same wherever it is used.

In order to maximize interoperability each possible state must have one
canonical definition. For flexibility we would also like to allow modification
of the set of states without needing to update the global namespace.

#### Multi-State groups {#multi-state-groups}

Multi-state groups are defined on a field-by-field basis. Fields with point type
`status` or `mode` are always multistates whereas ones with type `command`
should be if not given a measurement subfield. All allowed states for a field
across all devices are listed, however individual devices may or may not use all
states (TODO: link to translations doc).

#### Effect on Namespace Elevation {#effect-on-namespace-elevation}

States can affect whether fields are elevated to the global namespace. Like with
subfields, only fields having globally defined states can be elevated to the
global namespace.

### Entity types {#entity-types}

An entity type is a grouping of fields with a specific description that
represents a "thing" in the building model. Obvious examples include a room, an
air conditioner or a camera. It is also possible to define an entity that maps
to a defined functionality that is a subset of a complete device. For instance,
we might want to define the fields needed for high/low setpoint temperature
control as its own entity type in the ontology.

Entities have:

*   name
*   description
*   abstract flag
*   canonical flag
*   list of zero or more parent types
*   GUID (Coming soon)
*   required fields
*   optional fields
*   Required Relationships (Coming soon)

A type has meaning beyond its defined fields. For instance an entity of type X
and type Y, bothi having field A are distiguishable from each other, even though
they have the exact same fields.

#### GUIDs {#guids}

Each type has a numeric ID that is version independent

TODO

#### Type names {#type-names}

Type names have no structureal meaning in the ontology, but because this is the
most visibile identifier of the type, the concrete types adhere to the
convention of starting with an equipment class (TODO: structurally define how
equipment classes are identified) followed by an `_` separated list of parent
types[^24]. Type names my change from version to version independent of
[GUID](#guid).

#### Field Definitions {#field-definitions}

Fields on types can be defined either as required or optional. The intent of
this is to minimize the number of distinct entity types that are required to
cover the equipment set. This is especially true in the HVAC domain when there
may be a large number of minor (unimportant) variations in a perticular
equipment class but there is a set of common fields across all of the devices
that ware used for analysis.

#### Inheritance {#inheritance}

Types in the ontology can inherit field associations from other types. Multiple
inheritance is allowed with the following combination rules:

*   A field inherited from multiple parents is considered to exist only once in
    the child
*   If a field is associated to a type directly or through inheritance as both
    required and optional, the resulting definition shows the field as required.
*   field increments are preserved and same fields with different increments are
    considered unique
*   relationship requirements are additive, with the strictest requirement
    prevailing
*   conflicting relationships constraints are construction errors
*   attributes (`description`, `id`, `is_canonical`, `is_abstract`) are not
    inherited.

As with individual types, inheritance trees are meaningful independent of
resulting field set. For instance Type X, inherting from V and W is
distinguishable from type Y inheriting from only V, even if both types only have
field A.

Composable inheritance is primarily inteded to encourage users to define
subunits of functionality with associated fields, and build types by composing
the subunits.

#### Abstract Types {#abstract-types}

Designating a type as abstract indicates that it should only be used in
inheritance and not directly associated with any entities. This is typically
used for abstract units of functionality that are used to compose other types.

#### Canonical Types {#canonical-types}

In real modeling environments we find there are often exceptions to our
idelaized picture of the world. When this occurs we need to create one-off
constructions to cover the excepetions. To take a concrete example, we often see
device controllers in the HVAC world that carry sets of points for multiple
logical pieces of equipment. Because we use the convention of creating a type
for every device that sends data to the system, we end up with a lot of types
that have odd collections of points that don't map to any specirfic equipment
concept.

the `is_canonical` flag lets the modeler differentiate between 'official'
curated types (canonical) and everything else (not canonical).

#### Relationship Constraints {#relationships}

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
entities are connected. This may be a physical (ex: `FEEDS`) or logical (ex:
`HAS_PART`). Connections are always global. Connections and their descriptions
can be found here. **TODO add link**.

### Change Management {#change-management}

Versioning is anticipated for the ontology, though the exact process and
constrains are TBD.

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
    for certain configuration linter warnings. This should be replced with a
    check on some aspect of the type structure rather than the name.
