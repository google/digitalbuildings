# Digital Buildings Abstract Model

In addition to providing a general syntax and primitives for building a
smart-building ontology, Digital Buildings provides an abstract model with the
types generated when modeling Google's own buildings. This document describes
the conventions used in the concrete model and provides additional explanations
of individual types.[^1]

*   For a conceptual explanation of the ontology see [ontology](ontology.md)
*   For an explanation of the model configuration files see
    [config](ontology_config.md)

- [Digital Buildings Abstract Model](#digital-buildings-abstract-model)
  * [Model Origins and Design Philosophy](#model-origins-and-design-philosophy)
  * [Naming and Inheritance Conventions](#naming-and-inheritance-conventions)
    + [General Types](#general-types)
    + [Abstract Functional Groups](#abstract-functional-groups)
    + [Use of optional fields](#use-of-optional-fields)
    + [Type Composition and Naming](#type-composition-and-naming)
  * [Specific Model Details](#specific-model-details)
  * [Notes](#notes)

## Model Origins and Design Philosophy

The DB model was created with the intent of providing a consistent API to
Google's building portfolio for high-level analysis and control. The model is
intentionally reductionist, covering only the points necessary for operations
like gross fault detection, setpoint control, environmental and energy
monitoring. Building a full-featured BMS in the cloud was an explicit non-goal.
Instead, the model focuses on defining minimal set of fields for atomic units of
functionality and composing them into equipment in consistent and easy-to-follow
ways (we hope we succeeded).

## Naming and Inheritance Conventions

The concrete model uses some conventions that are not \[yet\] encoded into the
ontology structure. Due to the utility of these conventions, they will likely be
added to the model in a future revision.

### General Types

The first of these is the concept of a **General Type**. A general type is
simply a broad category of types for which there may be many variations. An
example might be an air handling unit (AHU) or a heat exchanger (HX). Each of these general types
is instantiated as an entity type (sometimes with no fields) and inherited by
any type that represents a specific variation on the class.

General types are given 1-4 character abbreviations as names (e.g., `AHU`, `HX`, `VAV`, etc.),
and each child (entity) type begins its name with `<general type>_` (e.g., `VAV_SD_...`).

Almost all general types are tagged as `is_abstract: true` and inherit from
`EQUIPMENT` (with the exception of systems, which are themselves general
types).[^2] General types can also inherit individual fields.

General types, by convention, are kept in a file called `GENERALTYPES.yaml` that is scoped to a particular namespace (e.g., `HVAC`, `METERS`, etc.).

### Abstract Functional Groups

Abstract functional groups (aka abstract types) are sets of fields required for understanding a
particular discrete device function. For example, airflow control would have a
field for the flow setpoint, flow sensor, and damper command. These field
sets are given short names, like `SD` (short for "supply damper") and marked as `is_abstract: true` so
they cannot be assigned directly to entities.

Functional groups, by convention, are contained in a file called
`ABSTRACT.yaml` that is scoped to a particular namespace.

### Use of optional fields

Optional fields are used for fields that provide nice-to-have information in a
type. For instance, a device may have an additional sensor that is used for
monitoring only. Adding these fields as optional to the general type or functional
groups they're likely to be seen with decreases the diversity of types without
affecting analysis.

### Type Composition and Naming

For the most part, types have one level of inheritance hierarchy below abstract
types. A typical type will implement its general type and the functional group(s)
that represent its functionality. Ideally, the constructed type will have no
fields directly assigned to it.

Typically the type is named by the general type and its inherited functional
groups with `_`. Functional groups are roughly ordered by significance, which is
somewhat subjective; the order is not inherently meaningful, but for readability
some type of ordering should be used (an alternative might be alphabetically).

Specific types are, by convention, organized into files by general type, named
by that class (ex: `VAV.yaml`).

## Specific Model Details

For further detail on types in specific namespaces see the following:

*   [HVAC](model_hvac.md)

## Notes

[^1]: Explanations are primarily for HVAC at this time, as it is one of the most
    complex systems to model. \
[^2]: Sometimes devices are so bespoke as to not be worth defining as
    `canonical`; however, it should be be the goal of the modeler to reduce
    these devices to sufficiently meaningful `abstract` concepts and to build
    the appropriate `canonical` representation for such combinations.
