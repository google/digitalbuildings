# Digital Buildings Concrete Model

In addition to providing a general syntax and primitives for building a
smart-building ontology, Digital Buildings provides a concrete model with the
types generated when modeling Google's own buildings. This document describes
the conventions used in the concrete model and provides additional explanations
of individual types[^1]

[TOC]

## Model Origins and Design Philosophy {#origins}

The DB model was created with the intent of providing a consistent API to
Google's building portfolio for high-level analysis and control. The model is
intentionally reductionist, covering only the points necessary for operations
like gross fault detection, setpoint control, environmental and enegy
monitoring. Building a full-featured BMS in the clould was an explicit non-goal.
Instead, the model focuses on defining minimal set of fields for atomic units of
functionality and composing them into equipment in consistent and easy-to-follow
ways (we hope we succeeded)

## Naming and Inheritance Conventions {#naming-and-inheritance}

The concrete model uses some conventions that are not \[yet\] encoded into the
ontology structure. Due to the utility of these conventions, they will likely be
added to the model in a future revision.

### Equipment Classes {#equipment-classes}

The first of these is the concept of an **Equipment class**. An equipment class
is simply broad category of equipment of which there may be many variations. An
example might be an Air-Handler or Heat Exchanger. Each of these is classes is
instantiated as an entity type (sometimes with no fields) and inherited by any
type that represents a specific variation on the class.

Equipment classes are given 1-4 character abbreviations as names (ex: AHU or
HX), and each child class begins its name with `<equipment class>_`.

All Equipment classes are `abstract`, `canonical` and inherit from `EQUIPMENT`.

Equipment classes, by convention are kept in a file called `GENERALTYPES.yaml`

### Abstract Functional Groups {#functional-groups}

Abstract funtional groups are sets of fields required for understanding a
particular discrete device function. For example, airflow control would have a
field for the flow setpoint and, flow sensor and damper position. These field
sets are given short names, like `SD` (supply damper) and marked `abstract` and
`canonical` so they casnnot be assigned directly to entities.

Functional groups, by convention, are contained in a file called
`ABSTRACT.yaml`.

### Use of optional fields {#optional-fields}

Optional fields are used for fields that provide nice-to-have information in a
type. For instance, a device may have an addditional sensor that is used for
monitoring only. Adding these fields as optional to the equipment or functional
groups they'ree likely to be seen with decreases the diversity of types without
affecting analysis.

### Type Composition and Naming {#composition}

For the most part, types have one level of inheritance hierarchy below abstract
types. A typical type will implement its equipment class and the functional
group that represent its functionality. Ideally, the constructed type will have
no fields directly assined to it.

Typically the type is named by the equipment class and its inherited functional
groups with `_`. Functional groups are roughly ordered by significance, which is
somewhat subjective.

Specific types are, by convention, organized into files by equipment class,
named by that class (ex: `VAV.yaml`)

## Specific Model Details

For further detail on types in specific namespaces see the following:

*   [HVAC](model_hvac.md)

## Notes

[^1]: Explanations are primarily for HVAC at this time,as it is one of the most
    complex systems to model.
