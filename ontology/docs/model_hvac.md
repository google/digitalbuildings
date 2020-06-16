# Digital Buildings HVAC Model

This document intends to outline best practices for modeling things in the HVAC
namespace, based on implementations for Google's own corporate real estate. As
stated elsewhere, modeling is somewhat arbitrary, and different, equally valid
models could be created for the same physical thing. However, there are certain
preferences which manifest as one begins to model the systems and justification
for certain choices will be made here.

- [Digital Buildings HVAC Model](#digital-buildings-hvac-model)
  * [Guiding Principles](#guiding-principles)
  * [Fields](#fields)
  * [Types](#types)
    + [Umbrella Types](#umbrella-types)
      - [Umbrella Equipment Types](#umbrella-equipment-types)
      - [Umbrella System Types](#umbrella-system-types)
        * [Notes on System Design](#notes-on-system-design)
      - [Abstract Types](#abstract-types)
        * [Specific Abstract Type Models](#specific-abstract-type-models)
          + [Air Flow Control](#air-flow-control)
          + [Air Temperature Control and Monitoring](#air-temperature-control-and-monitoring)
          + [Air Pressure Control](#air-pressure-control)
          + [Humidity Control](#humidity-control)
          + [Air Quality Control](#air-quality-control)
          + [Fan Control](#fan-control)
          + [Mechanical Heating and Cooling Controls](#mechanical-heating-and-cooling-controls)
          + [Economizer Control](#economizer-control)
          + [Water Temperature Control](#water-temperature-control)
          + [Water Differential Pressure Control](#water-differential-pressure-control)
          + [Flow Control](#flow-control)
          + [Isolation Damper and Valve Control](#isolation-damper-and-valve-control)
  * [Connections](#connections)

## Guiding Principles

Our philosophy follows a few basic principles (with certain exceptions that we
will call out as they occur):

*   **Model with an end use in mind**: know *why* you are modeling a device
    before doing so. For this deployment, the purpose of modeling was to enable
    machine learning, engineering analytics, and intraoperative app development;
    therefore, the fields we mapped were those we anticipated most relevant to
    those uses. It's not necessary to integrate every available field (for
    instance, PID gains may be available but are rarely required for analysis);
    what is required varies by use case, so have those use cases in mind before
    setting out to model.
*   **Brevity is preferred**: avoid extraneous subfields, fields, or
    relationships unless they are necessary within the context. For example,
    when modeling a fan, run_command is sufficient, whereas fan_run_command
    would be redundant. See the discussion on model flexibility and ambiguity
    [here](ontology.md#structural-flexibility-and-ambiguity) for more detail.
*   **Consistency is paramount**: avoid adding new types, new fields, etc.,
    except where it is necessary to define novel concepts. If a novel concept
    does emerge, push that concept to its logical limits and apply it
    consistently.
*   **Rely on precedent**: the models currently defined encode large amounts of
    institutional knowledge, thought, and experience that may not be
    superficially obvious. Wherever possible, defer to precedent on how to model
    a particular device, field, or system.
*   **Do more with less**: apply the fewest number of abstract concepts to match
    the modeling goal. As an example, take an AHU with chilled water that
    controls to supply temperature: it would be valid to apply **STC** (which
    contains supply temp and setpoint) and add an additional type for the
    chilled water valve control; it would also be valid to apply the **CHWSC**
    type (which contains all of those fields). In this instance, the *most*
    correct solution is to apply **CHWSC** and describe the device with fewer
    inherited abstract types.
*   **Avoid single-field type definitions**: to avoid blowing up the ontology by
    defining a different abstract type for every field, avoid creating types
    without at least a few sensors or setpoints. There are some notable
    exceptions to this, but only where ubiquity necessitates it.
*   **Deviate minimally from industry standard terminology**: The purpose of the
    standard field is to provide concise and descriptive information about what
    it is, and the more this diverges from common industry terminology, the
    harder it is for industry professionals to navigate. For example, `supply`
    is much more common than `outlet`, even though semantically they would be
    identical on most assets.
*   **Use your best judgment**: these are guidelines, and it is up to the
    modeler to understand what ramifications their decisions will have on the
    end-use of the applied ontology.

## Fields

This section outlines some frequently asked questions on how to properly build
certain fields, specifically which subfields should be used in different
circumstances (Note: for consistency, the decisions here apply across all
models, not just the particular model to which they are useful):

*   **Prefer Return and Supply to Inlet and Outlet**: It would be
    straightforward to model all devices with the generic `inlet` and `outlet`
    subfields, but this breaks the rule of attempting to maintain consistency
    with industry practice. The use of `inlet` and `outlet` also breaks down
    when equipment with more complex process control (e.g. an AHU has `return`,
    `mixed`, `exhaust`, and `supply` sensors) are modeled, because then it would
    require a mix of common and uncommon terminology; therefore, `supply` and
    `return` are preferred to `inlet` and `outlet`.
*   **Differentiate Supply and Discharge**: It is not typical to distinguish
    supply and discharge within the industry, but there are good modeling
    reasons to prefer some distinction, primarily with the case of VAV devices.
    Because VAVs commonly temper incoming air before it is output into the
    space, it is necessary to differentiate between `supply` air and `discharge`
    air. This does add some complexity to AHU modeling (where the application
    must be carried for logical consistency) because some units serve multiple
    zones through VAVs and others serve zone directly; in these cases the
    leaving air temperature would be `supply` and `discharge`, respectively.
*   **Qualifying Isolation Dampers and Valves with Process Location**: It is not
    strictly required that isolating components be labeled with process location
    information (e.g. `supply_air_isolation_damper` where `supply` indicates
    process location), but is preferred. There will be examples that, based
    purely on entity context, do not require any location qualification (for
    example, a boiler with a single isolation valve). However, it is preferred
    to add these qualifiers regardless of whether it's needed based purely on
    entity context. (Note: this is an exception to the philosophy of brevity
    because it has the added benefit of simplifying queries to retrieve all
    permutations of isolation valves or dampers).
*   **Limit vs. Max**: Designate boundary conditions with `limit` instead of
    `max`, which is reserved for aggregation. For example, suppose a supply
    temperature setpoint resets between a high and low value: the fields should
    be `high_limit_supply_air_temperature_setpoint` and
    `low_limit_supply_air_temperature_setpoint`;
    `max_supply_air_temperature_setpoint` and
    `min_supply_air_temperature_setpoint` imply aggregations across several
    different instances of `supply_air_temperature_setpoint`.
*   **Setpoint Directionality**: Sometimes directionality is ambiguous in
    control logic. Use additional descriptors to differentiate directionality
    where it is ambiguous: the quintessential example of this is zone
    temperature setpoint versus zone cooling and heating temperature setpoints;
    the former is non-directional (the zone attempts to maintain *to* the
    setpoint), whereas the latter define boundary conditions which dictate which
    conditioning mode the unit will engage upon breach; it would be ambiguous
    without the `cooling` and `heating` descriptors. For things like
    `zone_air_co2_concentration_setpoint`, where it is very clearly an upper
    boundary condition, it is unnecessary to add additional descriptors.

## Types

As stated previously, types define the properties and behavior of entities in
the real world. In a basic sense, they are the set of all standard fields of a
device; in a deeper sense, they also represent what the set of fields mean about
the device’s behavior (that it controls to a setpoint, that it heat and cool,
etc.). The functional types (which do not themselves get applied directly to
real-world devices) are **abstract** (i.e.
[functional groups](model.md#functional-groups)). Types that are applied
directly are made up from combinations of those functional types; these should
try to be **canonical** ([canonical types](ontology.md#canonical-types)) where
possible, but this is not a strict requirement.

The syntax for defining these types is discussed in
[entity types](ontology_config.md#entitytypes); this section discusses actual
application and provides basic guidelines for constructing new types.

### Umbrella Types

The concept of an **umbrella type** (see
[umbrella types](model.md#umbrella-types) for model details) is used to broadly
classify equipment based on its holistic function. Because types with very
similar function (such as fans or AHUs) can be extremely varied, it is important
to have an umbrella concept that allows *similar enough* devices to be
considered together, even when their specific type definitions otherwise
wouldn’t strongly group them.

Below is the list of umbrella types, and the *'smell test'* that would make
entities viable candidates for each. Note that any of the defining
characteristics for each class may or may not be present in the fields for that
unit (e.g. a unit with outside air dampers is considered an AHU, even if the
device doesn't report the damper commands or positions); the modeler should
apply the umbrella type that properly describes the physical device, not simply
the telemetry representation of the device:

#### Umbrella Equipment Types

This section outlines **umbrella types** for specific equipment.

*   **Air Handling Unit (`AHU`)**: an air-side device that provides air to a
    zone directly or indirectly via terminal units, providing recirculated and
    fresh air. It must have both outside air and return air capabilities to be
    considered part of this class.
*   **Boiler (`BLR`)**: a water-side device that heats domestic or heating
    water. Must produce hot water.
*   **Chiller(`CH`)**: a water-side device that chills (cools) water utilizing
    the refrigeration cycle and compressors. Can be either air-condensing or
    water-condensing. Must produced cool water.
*   **Compartment Unit (`CU`)**: an airside device that delivers both outside
    and return air but which does not source the outside air itself (i.e. it
    lives downstream from some other device, like a DOAS, which pre-conditions
    its outside air for it). This is typical in colder climates, or where
    ventilation heat recovery is routinely practiced.
*   **Cooling Tower (`CT`)**: a water-side device that cools water through the
    direct or indirect evaporation of water. Typically (but not always)
    associated with a chiller or water-source fan coil units. Must produce
    condensing water.
*   **Dry Cooler (`DC`)**: a water-side device that cools water sensibly through
    air flow over its coil.
*   **Dedicated Outside Air System Unit (`DOAS`)**: an air-side device that
    typically provides conditioned air to other downstream distribution
    equipment. They typically have heat recover between the supply and exhaust
    air streams. They must have both supply and exhaust sides, and must provide
    single pass air flow (i.e. they do not allow recirculation of air). TODO:
    Define these in the ontology.
*   **Duct Furnace (`DFR`)**: an air-side device that provides heat to the hot
    deck of a dual-duct system. Must provide hot air to a hot deck.
*   **Duct Heater (`DH`)**: an air-side device that provides heat to an
    airstream in a duct. It does not move the air itself; it is simply an
    independent heating mechanism in stream.
*   **Fan (`FAN`)**: a stand-alone, air-side device that moves air from one
    location to another. They must be stand-alone (i.e. not a subcomponent of
    another device, such as an AHU) in order to qualify for this category (as
    stated elsewhere, it was chosen to model the total physical device as a
    whole, as opposed to nesting subcomponents -- this is a logical outflow of
    that choice).
*   **Fan Coil Unit (`FCU`)**: an air-side device which provides conditioning to
    a space. It must be recirculation only (i.e. no integral fresh air
    capabilities) in order to be considered part of this class.
*   **Heat Exchanger (`HX`)**: a device which provides heat exchange interface
    between two fluid streams. It isn't responsible for its own fluid flow.
*   **Humidifier (`HUM`)**: an air-side device which is responsible for
    providing humidification to a space. This must be a stand-alone humidifier;
    an AHU can have humidification, but would be classified an AHU and not a
    HUM.
*   **Make-Up Air Unit (`MAU`)**: an air-side device which provides outside air
    to a space (directly or indirectly). It must have only fresh air, and must
    have no integral exhaust capabilities to be considered part of this class.
*   **Pump (PMP)**: a stand-alone, water-side device that moves liquid (water,
    glycol, liquid CO2) from one location to another. As with FANS, it must not
    be a subcomponent of any other device (e.g. not onboard a boiler) in order
    to qualify for this class.
*   **Terminal Unit (`VAV`)**: an air-side device that serves as the end-point
    to a ducted air distribution system. May be attached to multiple duct
    systems (e.g. a dual-duct VAV) and may have pressure-independent or
    pressure- dependent control; it can be overhead or underfloor; it can also
    be constant volume. The only requirement is that it terminates the air
    distribution system. TODO: update VAV to TU for improved generality (?).
*   **Unit Heater (`UH`)**: a stand-alone, air-side device that heats air. It
    must not be part of any larger air-side distribution system.
*   **Weather Station (WEATHER)**: a group of sensors used to measure ambient
    weather conditions (dry bulb temperature, relative humidity, enthalpy,
    carbon dioxide levels, etc.).
*   **Zone (`ZONE`)**: a group of sensors associated to an individual zone,
    rather than to an HVAC asset.

#### Umbrella System Types

This section defines **umbrella types** for systems (interconnected groups of
equipment, but not the equipment itself):

*   CONDENSING WATER SYSTEM (`CDWS`): a system that produces sensibly- or
    evaporatively-cooled water by means of cooling towers or dry coolers. Must
    serve as condensing source for heat pumps or chillers.
*   CHILLED WATER SYSTEM (`CHWS`): a system that produces (or can produce)
    mechanically cooled water and distributes it to end-use devices. Can be
    composed of pumps, chillers, heat exchangers, etc.
*   HEATING WATER SYSTEM (`HWS`): a system that produces heated water for the
    purpose of conditioning air.

##### Notes on System Design

All equipment is interconnected in some way to other equipment via systems; this
can be indirect (such as FCUs serving adjacent zones) or direct (a pump serves a
chiller). A typical approach to modeling is generally to draw the boundary
around individual equipment, and create relationships between those equipment,
but a few problems arise from this:

*   Equipment may serve multiple other devices, or be served by multiple devices
    and in some complex way (e.g. primary and secondary pump headers).
*   Certain sensors and setpoints do not rightfully apply to any one piece of
    equipment (such as header temperature sensors).

In these cases, model the system as an independent entity and map the system
fields directly to it, and connect the relevant equipment to the system entity.
For more complex systems (imagine a chilled water system with multiple secondary
risers and a production loop) it is valid to break the system down into multiple
individual systems (e.g. `PRODUCTION`, `SECONDARY_UPPER_FLOORS`,
`SECONDARY_LOWER_FLOORS`) and then link them to a common system.

#### Abstract Types

Modeling types begins with defining functional groups based on what particular
pieces of equipment (or systems) typically possess. For HVAC, these can be
divided into a few basic categories:

*   MONITORING: The subtype has fields that monitor the current state of the
    entity, such as run command, temp sensors, pressure sensors, valve
    positions, etc.
*   OPERATIONAL: The subtype holds the operating condition of the entity, and
    always includes a sensor and setpoint pair (e.g. supply air temp sensor and
    supply air temp setpoint).
*   CONTROLS: The subtype holds the fields necessary to analyse the performance
    of the entity’s control system. For example, supply air temp sensor, supply
    air temp setpoint, and chilled water valve command.

Because a major goal of modeling is to provide structure for analysis, the above
categories are defined as **analysis types**, which can be found in the HVAC
namespace under `analysis.yaml`.

In general, attempt to follow a few rules when creating new abstract types:

1.  Abstract types should be based on the function of the data points in the set
    as a whole.
    1.  They should roughly map to control strategy.
    2.  When not specifically used for control, they should encompass a logical
        grouping of points (e.g. a stand-alone VFD should have start/stop and
        speed commands/feedbacks in the same abstract type, since they function
        together).
2.  An abstract type should not be created or applied solely to handle omitted
    fields (incomplete translations should be utilized for this). Sometimes it
    does make sense to have more atomic abstract types (e.g. ZHM is common where
    a zone humidity sensor is nice to have for a device but isn't used for any
    control) but this is not because the control sensor is missing; it is simply
    an extra field.
3.  Sometimes (particularly in legacy systems with incomplete integrations) the
    fields available for the device are not the complete set (e.g. a setpoint is
    not BACnet-available but the sensor is). In such a case the following
    applies:
    1.  It is highly advisable to apply the correct type and leave the
        unavailable fields unmapped in the translation; do not create new,
        incomplete abstract types simply to support a bespoke 1:1 field mapping
        for a device.

##### Specific Abstract Type Models

The following sections will outline some of (but expressly not all) defined
**abstract types** found most commonly within this deployment. This forms the
body of precedent which will be extended to model different, novel scenarios.

(Note the small variations in acronyms among the defined abstract types; it is
acknowledged that some variations will exist, but consistency should be
attempted when adding new types here.)

###### Air Flow Control

This section outlines typical air-side control. Some were intended to apply to
specific mechanical devices (e.g. VAVs) and others were intended to be more
portable; note that just because an abstract type was designed for a particular
device does not mean it can't be extended to some other device.

**Single Damper Flow Control (`SD`, `ED`, `RD`, etc.)** The most important
feature of a terminal unit is its damper, and the controls associated with it.
These have impacts on upstream distribution equipment (the air-handler will
increase airflow if the number of fully open dampers exceeds a threshold) and
failure in these components can lead to system inefficiency or space discomfort.
Almost all VAVs measure airflow and control their damper to a flow setpoint.
This forms the basic nucleus of a VAV type. Other such flow control types (`ED`
and `RD`) where, instead of supplying air, they facilitate the movement of
exhaust or return air, respectively. These subtypes are much less common, but do
occur in more sophisticated systems.

**Dual Duct Terminals (`DD`)** In older systems, it is possible for there to be
two separate ducts for heating and cooling air. If the space requires cooling,
the cooling damper opens to maintain flow setpoint; vice versa in heating mode.
Therefore, in order to be fully developed, it requires that both sets of damper
control points and measurements be available.

**Outside Air Damper (`OADM`, `VOADM`, `MOADM`)** Outside air damper position is
monitored, either as a binary open/closed command (OADM) or a percentage command
(VOADM). Some dampers also have a minimum percentage command (`MOADM`). Outside
air dampers modulate to provide fresh outside air to the building for
ventilation and to provide cooling air for economization. Note that if the unit
does utilize economizer control, there are other, more comprehensive types
specifically for that. See below.

**Outside Air Flow (`OAFC`, `OAFMC`, `MOAFC`)** A flow sensor is mounted in the
outside air duct, and the outside air damper modulates to control flow to a
setpoint (`OAFC`). Sometimes the damper will control to a minimum flow setpoint
(`OAFMC`). Some entities will control to a lower limit flow and lower limit flow
setpoint with a lower limit damper position (`MOAFC`).

**Bypass Air Damper (`BYPDM`)** The air damper position is monitored as a
percentage command. Bypass dampers are typically located in the supply duct
after the supply fan and temperature control, and bypass the air from the supply
duct into the return/exhaust duct. Bypass dampers are used in older units to
control supply duct pressure when the supply fan does not have a VFD (and cannot
modulate speed).

**Supply and Return Air Flow (`SFM`, `SFC`, `RFC`)** The supply or return air
flow is either monitored by a flow sensor in the duct (`SFM`) or controlled by
the flow sensor and flow setpoint (`SFC`, `RFC`). Most entities control to duct
static pressure rather than air flow.

###### Air Temperature Control and Monitoring

This section outlines different types of temperature control for air-side
processes. Most types have heating and cooling components (like chilled water
valves) that control to temp. Zone temp controlled subtypes are represented with
the suffixes `ZTC` (eg. `CHWZTC`) and `DSP` as `ZC` (e.g. `CHWZC`).

**Zone Temp Control (`ZTC`)** Zone is maintained to a fixed setpoint, and will
cool if the zone drifts above setpoint or heat if it falls below the setpoint.
There is often a deadband used to prevent erratic fluctuation between heating
and cooling; this is often hard-coded into the programming, and unavailable;
therefore it is normally listed as optional to reduce the number of incomplete
translations.

**Zone Temp Monitoring (`ZTM`)** There is only a zone temperature sensor, and
not tied to a particular control strategy. This is a notable exception to the
rule about avoiding overly simplistic type definitions, and this is due to it
being a common occurrence in certain systems.

**Cooling Setpoint Control (`CSP`)** The zone is cooled only by the VAV (typical
of IDF, cable, or electrical rooms) and so no consideration needs to be made for
heating mode (the space never gets cold and has no heating capability). A single
lower-bound cooling setpoint is used.

**Dual Setpoint Control (`DSP`)** The zone maintains between upper- and
lower-bounds (cooling and heating setpoint, respectively). The deadband (i.e.
distance between the boundaries) is implied.

**Return Air Temp Control (`RTC`)** The return air temp maintains between upper-
and lower-bounds (cooling and heating setpoint, respectively). The deadband
(i.e. distance between the boundaries) is implied. Very similar to DSP control,
but oriented around the return temperature sensor.

**Discharge Air Temp (`DTM`, `DTC`)** Discharge air temp is either monitored by
a temp sensor (`DTM`) or controlled by a sensor and setpoint (`DTC`).

**Supply Air Temp (`STM`, `STC`, `STDSPC`)** Supply air temp is either monitored
by a temp sensor (`STM`) or controlled by a sensor and setpoint (`STC`). Some
supply air temps have dual-setpoint control, where the supply air temp is kept
between a heating setpoint and cooling setpoint (`STDSPC`).

**Return Air Temp (`RTM`, `RTC`)** Return air temp is either monitored by a temp
sensor (`RTM`) or controlled by a sensor and setpoint (`RTC`). Entities of
certain umbrella types typically do not control return air temp, such as AHUs.

**Mixed Air Temp (`MTM`, `MTC`)** Mixed air temp is either monitored by a temp
sensor (`MTM`) or controlled by a sensor and setpoint (`MTC`). Mixed air
temperature sensors are typically located in the duct where the outside air and
return air have combined, before the supply fan and mechanical heating/cooling
components. Entities typically do not control mixed air temp. Again, `MTM` is
not preferred since other types contain mixed air temp as parts of larger
analysis groups, but can be used where necessary.

**Exhaust Air Temp (`ETM`)** Exhaust air temp can be standalone in certain
instances, but should normally be considered as part of a larger component (such
as a heat recovery section).

**Outside Air Temp and Enthalpy (`OA`)** Outside air temp and enthalpy are
monitored by sensors. Weather stations monitor outside air, along with some
boilers, chillers, and air handler units. Some weather stations also measure
outside air dewpoint and wetbulb temps, which are included as optional fields.

###### Air Pressure Control

**Supply Air Static Pressure Control (`SSPC`,`SSPM`)** Supply air static
pressure (in the duct) is either monitored by a pressure sensor (`SSPM`) or
controlled by a sensor and setpoint (`SSPC`). Entities control their supply air
static pressure through the modulation of their supply fan speed or through the
modulation of bypass dampers.

**Building Static Pressure (`BSPM`, `BSPC`)** Building air static pressure (in
the duct) is either monitored by a pressure sensor (`BSPM`) or controlled by a
sensor and setpoint (`BSPC`). Entities control building static pressure through
the modulation of exhaust fan, exhaust dampers, and in certain instances,
outside air dampers.

**Zone Static Pressure (`ZSPM`, `ZSPC`)** Zone static pressure is either
monitored by a pressure sensor (`ZSPM`) or controlled by a sensor and setpoint
(`ZSPC`). Note that zone and building static are not the same thing, see
subfield definitions for more clarification.

**Exhaust or Return Air Static Pressure (`ESPC`, `RSPC`)** Exhaust air or return
air static pressure (in the duct) is controlled by a sensor and setpoint.
Entities do not typically control exhaust or return air static pressure.

**Filter Differential Pressure (`FDPM`)** Filter differential pressure sensors
monitor the pressure across in-duct air filters. As filters collect dust,
debris, and other particulates, their differential pressure increases. Pressure
sensors indicate when the filter requires cleaning or replacement. This is an
example of a stand-alone sensor that warrants its own type.

###### Humidity Control

**Zone Humidity (`ZHM`, `ZHC`)** Zone humidity is monitored by a sensor, or
controls to a humidification or dehumidification setpoint. Most units with `ZHC`
serve labs or cafeteria spaces for the buildings currently modeled.

**Return Air Humidity (`RHM`, `RHC`)** Return air humidity is monitored by a
sensor, and controls to a humidification or dehumidification setpoint. Most
units with `RHC` serve labs or cafeteria spaces.

**Supply Air Humidity (`SHC`)** Supply air humidity is monitored by a sensor, or
controls to a humidification or dehumidification setpoint. Most units with `RHC`
serve labs or cafeteria spaces.

###### Air Quality Control

**Carbon Dioxide Control (`CO2M`, `CO2C`, `CO2C2X`)** The concentration of
carbon dioxide in the zone air is monitored by sensors. For units that control
CO2, CO2 levels are used to determine when additional ventilation is required
(when levels exceed the setpoint) and increase the ventilation. Some zones have
multiple CO2 sensors (`CO2C2X`). TODO: explain how virtual fields to reduce the
number of redundant sensors in the types.

**Carbon Monoxide Control (`COC`)** Carbon monoxide sensors are used to
determine when additional ventilation is required (when levels exceed the
setpoint) and increase the ventilation. Typical of parking garages with variable
ventilation.

**Volatile Organic Compound Control (`VOCM`, `VOCC`)** Similar to CO2C, but unit
monitors or controls zone volatile organic compound levels.

###### Fan Control

**Fan Types (`SS`, `SFSS`, `DFSS`, `EFSS`, `RFSS`)** There are four basic fan
types. Supply fans (`SF`) deliver air from the unit to downstream units (such as
an AHU providing supply air to VAVs). Discharge fans (`DF`) deliver air from the
unit directly into the zone (without downstream units). Exhaust fans (`EF`) pull
air out of the zone and exhaust it out of the building. Return fans (`RF`) draw
the air back to the return box of AHUs, predominantly. The SS type is the basic
command (start-stop) and status (feedback) for equipment (and is modified by the
appropriate additional descriptors, such as `SF` or `EF`). Current and power
sensors are also included as optional fields. Some fans have multiple supply or
exhaust fans (e.g. `SFSS2X`).

**Variable Speed Control (`VSC`)** Some fans and entities have variable speed
control (typically measured by percentage) through a variable frequency drive
(VFD). VFDs will usually also have run command and run status fields. Some fans
have multiple supply or exhaust fans (e.g `SFVSC2X`).

**Mode Speed Control (`DFHMC`,`DFHLC`,`DFHML`)** Some fans control their speed
to a discrete set of fixed speed positions (`MC`), rather than a percentage.
Some also operate with high and low speed commands (`HLC`), or high, medium, and
low speed commands (`HMLC`). These subtypes also optionally used run command and
run status fields.

###### Mechanical Heating and Cooling Controls

**Chilled Water Valve Control (`CHWSC`, `CHWDC`, etc.)** Chilled water valve
control based on a specific temperature sensor. All iterations of this abstract
type include the chilled water valve command, and its associate control temp
sensor and setpoint pair (`SC`, `DC`, `ZC`, `ZTC`, `RC`).

**Direct Expansion Control (`DXSC`, `DXDC`, etc.)** Direct expansion cooling
(basic self-contained refrigeration cycle). Like chilled water valves,
compressor control to temp sensor and setpoint pairs. A type can have multiple
compressors, but typically does not have both a compressor and chilled water
coil.

**Heat Pumps (`HPDC`, `HPRC`, etc.)** Direct expansion units with reversing
valves. The reversing valve allows the refrigeration cycle to run in either
direction, so the heat pump can provide either heating or cooling. Heat pump
types consist of the reversing valve command, compressor run command, and temp
sensor and setpoint pair.

**Heating Water Valve Control (`HWZC`, `HWSC`, `HWDC`, etc)** Contains the
heating water valve, temp sensor and setpoint pair.

**Gas and Electric Heater Control (`HTSC`, `HTVSC`, etc)** Gas and electric
heaters integral to the unit. Electric heaters have an electric coil in the duct
that transfers heat to the air. Gas heaters use natural gas to serve a heat
exchanger in the duct. From an operational standpoint, gas and electric are
identical. Heaters control to temp sensor and setpoint pairs. Heaters are either
on/off command (`HT`) or have variable control (`HTV`). Some entities have
multiple heaters (`HT2X`), but will not typically have a heater and heating
water coil. Note that the fields don't include the keywords `gas` or `electric`
because there isn't often a reason to differentiate between them on the same
unit.

###### Economizer Control

**Economizer Control (`ECON`, `ECOND`, `ECONM`)** Economizer is an energy saving
control strategy where the AHU brings in more outside air than is necessary for
ventilation purposes in order to provide supplemental free cooling. The entities
economization performance is assessed by looking at the outside air damper,
outside air temp, return air temp, mixed air temp, and supply air temp setpoint.
The type variants indicate which sensor and setpoint pair are used for outside
air damper control (D = discharge, etc.).

###### Water Temperature Control

**Supply Water Temp (`SWTM`, `SWTC`, `CHWSTM`, `CHWSTC`)** Supply water temp is
either monitored by a temp sensor (`SWTM`) or controlled by a sensor and
setpoint (`SWTC`). Depending on the entity, supply water can refer to heating or
chilled water (context dictates which).

**Return Water Temp (`RWTM`, `CHWRTM`)** Return water temp is monitored by a
temp sensor. Depending on the entity, return water can refer to heating or
chilled water.

**Process Water Supply and Return Temp (`PWSTC`)** Process water is just water
used for process cooling (i.e. sensible). This is sometimes needed for process
side modeling on heat exchangers.

###### Water Differential Pressure Control

**Differential Pressure Control (`WDPC`)** Differential pressure sensors are
mounted on water pipes and measure the pressure drop between two points along
the pipe. Most commonly, this DP measures pressure drop between supply and
return water lines. Differential pressure is controlled to a setpoint through
the modulation of pump speed and bypass valve position.

###### Flow Control

**Water Flow Rate (`WFRM`, `WFRC`, `CHWFRM`)** A water flow sensor is mounted on
or in the pipe and monitors water flow rate (`WFRM`). Some entities and systems
control to a flow sensor and setpoint through pump speed modulation (`WFRC`).
The flow sensor may also be labeled chilled water flowrate sensor (`CHWFRM`).

**Minimum Water Flow Rate (`MWFRC`)** Chillers have a minimum required (i.e.
lower limit) flowrate when they are in operation. Some systems guarantee this
through a minimum flow setpoint and modulating bypass valve. This type has flow
sensor, min flowrate setpoint, and bypass valve command as required fields.

###### Isolation Damper and Valve Control

**Isolation Valves (`ISOVM`, `ISOVPM`)** Isolation dampers and valves allow
components of an HVAC system to be isolated during certain parts of the
sequence. Many chillers, boilers and cooling towers have isolation valves so
that they will not receive water flow when they are not in operation. Isolating
boilers, chillers, and cooling towers during inoperation saves pump energy. Heat
exchangers and other components of HVAC water systems may also have isolation
valves. Isolation valves control to a start/stop command (`ISOVM`) or a
percentage command (`ISOVPM`). They may also be labeled SWISOVM (supply water
isolation valve), `CHWSWISOVM` (chilled water supply isolation valve),
`CDWSWISOVM` (condensing water supply isolation valve), `HXSWISOVM` (heat
exchanger isolation valve) or `RWISOVM` (return water isolation valve). Note: it
is *highly* recommended to associate the isolation valve with the process side
it serves (return or supply), see [above](#fields-faqs) for justification.

**Bypass Valves (`BYPVPM`)** Bypass valves allow supply water to bypass the
distribution side and flow directly back into the return water line. Bypass
valves allow the system to maintain minimum flow (for the boilers or chillers)
even during times of low heating or cooling demand from downstream units. Bypass
valves may also be labeled `CHWBYPVPM` (chilled water bypass valve).

**Makeup Water Valves (`MWVPM`)** Some cooling towers are equipped with makeup
water valves that supply additional water to the system to make for water losses
from evaporation.

## Connections

This section discusses (what will be) required connections for particular types
of entities. More details to be added when this feature is implemented.

*   `VAV` entities will require connections to the equipment which serve them
    (`AHU`, `CU`, `DOAS`, etc.)
*   All equipment served by a hydronic source (e.g. a chilled water `FCU`)
    requires a connection to that system.
*   `CHL`, `BLR`, `CT`, and `HX` entities must be connected to a hydronic
    system.
*   `PMP` entities must be connected either to their associated hydronic system
    (in the event of headered pumps) or to the specific entity which they serve
    (such as a production pump which serves a single chiller).
