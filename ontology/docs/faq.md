# Frequently Asked Questions

This document is intended to provide answers to frequently asked questions regarding the application of the Digital Buildings ontology to existing and novel (i.e. previously unmodeled) devices.

[TOC]

## What is a building model?
**A building model is a file that maps concrete real-world devices to the ontology.** 

The model takes the form of a building configuration file (see [here](building_config.md)). It contains all the relevant information for the building: what devices exist, what types they apply, which devices connect to which other devices, what devices serve which zone, etc.

## Why have a building model?
**It makes building data useful.** 

Smart building platforms can only give insights into things they can be made to understand -- either implicitly or explicitly. For example, an analysis of all VAV dampers on a floor requires that the data be structured in a way that makes clear what a VAV is, which VAVs have available damper data, and what floor those VAVs reside on. This information must be defined; without it, the analysis cannot be performed (or at least not in a straightforward, repeatable way). The building model provides these connections and definitions which make it easy -- with the right tooling -- to ask sophisticated questions of the relevant building data.  

## What is a logical device?
**A logical device -- sometimes called a physical device -- is the thing in the real world which you are trying to model.** 

For example, a VAV is a logical device because it makes sense to draw the box around it when modeling the system -- it typically controls itself independently, is usually self-contained, and is useful to anyone wishing to analyze the system. 

## What is a reporting device?
**In contrast to a logical device, which is a thing we care to model, a reporting device provides communication for one or more logical devices.**

Think again of a VAV which has its own controller: the VAV itself is the logical device, and its controller -- the aperture through which you see the VAV -- is a reporting device. Reporting devices can range from small controllers up to floor or building gateways, so mapping a reporting device to a logical device can sometimes be tricky; this is what virtual devices are for. See [here](building_config.md#reporting-physical-devices) for more information on reporting devices.

## What is a virtual device?
**A virtual device is a logical device which does not map perfectly to a single reporting device; it is virtual in the sense that it does not cleanly follow from the network topology.**

This is usually necessary for multiple logical devices that communicate via the same controller. For example, if two AHUs are exposed by a single gateway device (an ALC LGR, for instance) then they will appear as one network device. A virtual device is linked to the reporting devices from which it’s comprised. See [here](building_config.md#virtual-devices) for more information on virtual devices.

## Which devices should be modeled?
**This is based on whatever the requirements are for the model.**

In general, all logical devices should be modeled within their namespace (e.g. all HVAC equipment should be modeled). This usually extends only to the logical devices themselves; that is, we do not model the controllers for individual devices separately (as separate entities within the same namespace) from their logical devices. An example of this is with multiple units which communicate via common interface (a gateway). In such circumstances, we would model each individual logical device as a virtual entity with a passthrough network device receiving a throwaway type purely for translation support. If, however, it is desirable or necessary to model the controllers separately, this is also supported. 

## How do you determine if you should model devices independently or as a single entity?
**If the component is contained in another device, we typically model it as part of that device.**

It is unusual for us to model AHU chilled water valves or dampers independently; they are typically contained within the device, and are usually not designated separately. Hydronic systems are another example where, since pumps, cooling towers, and chillers are all separate elements, they are all modeled separately; the fans in the cooling tower would be modeled as part of that cooling tower. 

## What data should be made available at the gateway (or controller) level?
**Everything, insofar as is practical.**

It does not have to be translated into the model, but for extensibility purposes, all practical data should be exposed. The reason for this is that it is sometimes difficult (or impossible) to programmatically expose data once the system is configured. Certain BAS platforms are easy to expose after-the-fact (e.g. ALC) but some gateways require on-site work to expose, so better to be exposed and not used than not exposed and needed later on. Updating the translation layer is much easier in most cases than exposing more data in the gateway.  

## What device data should be modeled?
**Model what you need for the applications and analytics that are reasonably anticipated.** 

More data can always be added later (as long as it’s exposed in the gateway). The general rule is to model things that describe the device’s general behavior without superfluous detail regarding its low-level configuration; however, anything can be modeled, so if need arises then the ontology can be extended to accommodate. There are a few types of data that devices typically sends:

### Measured Telemetry
These are sensors associated with the device, such as `supply_air_temperature_sensor` and `chilled_water_valve_percentage_sensor`. They are directly measured (or calculated) by the device and return updated values as the state of the device changes through time. All measured telemetry is normally modeled. *NOTE: we do not consider calculated telemetry differently from raw telemetry.*

### Setpoint Telemetry
These are values to which measured telemetry values are being directly controlled, such as `zone_air_cooling_temperature_setpoint` and `supply_air_static_pressure_setpoint`. The measured values are compared to the setpoint values to provide some type of state comparison (e.g. the zone is cold), whereby the device can respond through adjustment of control values. All setpoints are normally modeled. 

### Control States
These are values that represent how the device is responding to measured deviations from setpoints or other changes in environmental/temporal conditions. Such fields as `supply_fan_run_command` and `chilled_water_valve_percentage_command` are examples of control states that the device may adjust directly or indirectly based on measured conditions (e.g. the time of day for scheduled operation of the fan, or setpoint deviation for position of the valve). Most control states are normally modeled.

### Interpreted States
These are states which the device interprets from underlying data (whether it is exposed or not). The best example of this is an alarm: for example, a fan mismatch alarm compares the status of the fan to the command and returns an alarm if they are no equal. Interpreted states are not normally modeled.

### Configuration Information
These are internal device points which are used to configure the way in which the device attempts to maintain control values, or how its components control internally. Stage up/down timers, PID gains, etc.; configuration information is rarely modeled. 

## How do you extend the ontology?
**This depends on what needs to be extended.** 

This section will outline how to extend certain components within the ontology.

## How do you extend subfields?
**Define the subfield in a pull request, with the subfield defined in the appropriate category, and make sure the definition is understandable to anyone reading it.** 

In the building space there is an endless supply of esoteric acronyms and counterintuitive terminology; avoid these insofar as possible. Our goal is to have as much in the global namespace as possible, so it is important to reuse existing terminology where it meets the definition of whatever is being modeled. See [here](ontology.md#subfields) for rules on what subfield categories are.

## How do you extend fields?
**Define the field in a pull request with the appropriate grammar; if new subfields are required, define those first.** 

Check to make sure the field to be defined isn’t already defined using some sub- or super-set of subfields. Note that each field is constructed with a grammar (for example, that point type is always the last subfield in the field), and it must be followed; see [here](ontology.md#fields) for further information. When deciding how to construct the field (that is, choosing how many and which subfields to use), there are some common situations covered [here](model_hvac.md#fields); keep in mind that it is best to be consistent, and so if a field already exists that follows a structure that can be reused, use it (for example, say you have a temperature sensor in a fireplace that you want to model: fields like `exhaust_air_temperature_sensor` exist, so reusing this form and replacing `exhaust` with `fireplace` will result in a consistent extension of the ontology).

## How do you extend abstract types?
**Construct the new abstract type by building it up from individual field combinations.** 

When new functionality is required, it should be defined as an abstract type. The type should tightly model the specific functionality it is intended for; do not be overbroad, and do not try to represent multiple distinct functionalities -- use multiple inheritance for that.

## How do you extend non-abstract types?
**Construct the type by building it up from abstract function.** 

If new subfields, fields, or abstract types are needed in order to be able to construct the type, then do so first. Types should try to be constructed such that all fields are applied via abstract types (that is, that no fields need to be defined directly on the type) but this is sometimes problematic; if a field is wanted, but does not merit being assigned to an abstract type, then it is acceptable to add it directly to the type (either as optional or required). For information on what is needed for a new type, see [here](ontology.md#entity-types).

## What is the process for accepting extensions to the ontology?
**If the extension passes the type validator and passes review by the team, it will be accepted.** 

The type validator checks that additions or changes to the ontology do not break existing rules or compatibility (for example, the type validator will raise errors if a new field is added which is composed of undefined subfields). A review of the proposed extensions will be performed by the Digital Buildings team, which include building systems subject matter experts and software developers. The review covers both the subject matter (e.g. is a subfield too broadly defined for the intended application) and its holistic effect on the ontology (e.g. does it set precedent that makes further extension difficult). These reviews may require some deliberation and can result in proposed changes to the pull request, so it is better to submit pull requests in phases. See the next question for what is advised on ordering of ontology updates.

## What is the best way to make ontology extensions without significant rework?
**For small updates, submit them all at once; otherwise, phase the updates, starting with subfields, then fields, then abstract types, and finally canonical types.** 

Since field definitions are dependent on underlying subfield definitions, it is best to have those accepted prior to defining the fields; otherwise, there is risk that the subfields will be adjusted and this will require the fields to be adjusted. The same applies to types, which are constructed from groups of fields. In general, rework can be avoided by getting acceptance for work before it is used in upstream constructions.   

## How do you model something that spans disciplines (namespaces)?
**Many devices that appear to span namespaces can actually be subdivided into namespace specific devices.** 

For example, a room controller may contain lighting, AV, HVAC (temperature), etc., data; simply splitting the reporting device into individual virtual devices for lighting, AV, HVAC and so on is the simplest solution, and any fields that are shared among these devices (such as occupancy sensors) can be mapped to each relevant device (that is, a reporting device field can map to more than one virtual device). If there’s a good reason to not split the namespace, it is also possible to define a new namespace and put new types in there, but this should be used sparingly, as the number of combinations of possible mixed namespaces could become problematic. 

## What tools are available for use with the ontology?
**The tooling available today validates changes to the ontology and validates building config files for conformance with the ontology.** 

There are tools being developed to support the application of the ontology to new and existing buildings, through BIM and BAS exports files respectively, but these are still under development. 

## How do I use them?
**The instructions for using them are documented in this repository.** 

The instance validator is [here](https://github.com/google/digitalbuildings/tree/master/tools/validators/instance_validator) and the building config ontology validator is [here](https://github.com/google/digitalbuildings/tree/master/tools/validators/ontology_validator).
