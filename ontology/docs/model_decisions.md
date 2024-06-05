# Model Decisions Documentation

## Overview

This document outlines the model decisions made in the last few months, providing details and rationale for each category. These decisions were made to enhance the system's efficiency, reliability, and performance.

## 1. ASHP (Air Source Heat Pump)

### Decision:
- **Model Selection:**
  - **ASHP_SS_HP6SWC_CPC2X_RWISOVM**
    - **GUID:** 11ecef31-d11d-496b-9d39-f35fe9307a82
    - **Description:** Six-stage air source heat pump with 2 circulation pumps and return isolation valve.
  - **ASHP_SS_SHWTC_SCHWTC_HWRWISOVM_CHWRWISOVM_HCPC2X_CHCPC2X**
    - **GUID:** 8f9741a1-1066-406b-86fa-6ca239e215f4
    - **Description:** Air source heat pump for a hydronic system providing chilled and heating water.


### Reasoning:
- Improved energy efficiency and performance
- Enhanced compatibility with existing infrastructure
- Support for both heating and cooling applications
- Integration with various system components and alarms

### Implementation Details:
- **Installation:** [Details of installation procedures for each model]
- **Configuration:** 
  - **ASHP_SS_HP6SWC_CPC2X_RWISOVM:**
    - Implements: ASHP, SS, HP6SWC, CPC2X, RWISOVM
    - Optional Uses: low_refrigerant_pressure_alarm_1, low_refrigerant_pressure_alarm_2, high_refrigerant_pressure_alarm_1, high_refrigerant_pressure_alarm_2
  - **ASHP_SS_SHWTC_SCHWTC_HWRWISOVM_CHWRWISOVM_HCPC2X_CHCPC2X:**
    - Implements: ASHP, SS, SHWTC, SCHWTC, HWRWISOVM, CHWRWISOVM, HCPC2X, CHCPC2X

### Expected Benefits:
- Significant reduction in energy consumption
- Lower operational costs
- Enhanced system reliability and flexibility for various heating and cooling requirements

## 2. Alarm Selection

### Decision:
- **Types of Alarms:**
  - Low refrigerant pressure alarms
  - High refrigerant pressure alarms


### Reasoning:
- Enhanced safety measures and early fault detection
- Improved system monitoring and maintenance efficiency
- Compliance with industry standards

### Implementation Details:
- **Installation:** Integration of alarms into ASHP systems
- **Configuration:** Specific alarms configured for each ASHP model

### Expected Benefits:
- Increased safety and security
- Prompt issue identification and resolution
- Reduced downtime and maintenance costs

## 3. Energy Meters vs Heat Meters

### Decision:
- **Meter Selection:** [Energy meters, Heat meters, or both]
- **Date:** [Date of decision]

### Reasoning:
- Accurate measurement of energy consumption and heat output
- Better data for analysis and optimization
- Compliance with regulatory requirements

### Implementation Details:
- **Installation:** [Details of meter installations]
- **Configuration:** [Configuration and calibration settings]

### Expected Benefits:
- Improved energy management
- Enhanced monitoring and reporting
- Better cost control and savings

## 4. Generators

### Decision:
- **Model Selection:** [Specify the model selected]
- **Date:** [Date of decision]

### Reasoning:
- Reliable backup power supply
- Efficient fuel consumption
- Compatibility with existing power systems

### Implementation Details:
- **Installation:** [Details of generator installations]
- **Configuration:** [Configuration settings and adjustments]

### Expected Benefits:
- Uninterrupted power supply
- Increased system reliability
- Reduced risk of power outages

## 5. ATS (Automatic Transfer Switch)

### Decision:
- **Model Selection:** [Specify the model selected]

### Reasoning:
- Seamless switching between power sources
- Improved system resilience
- Enhanced operational continuity

### Implementation Details:
- **Installation:** [Details of ATS installations]
- **Configuration:** [Configuration settings and adjustments]

### Expected Benefits:
- Reduced downtime during power transitions
- Enhanced safety and reliability
- Improved operational efficiency

## 6. Fan Speed Modes

### Decision:
- **Modes Implemented:** TWENTY_PERCENT, FIFTY_PERCENT, SEVENTY-FIVE_PERCENT, HUNDRED_PERCENT

### Reasoning:
- Improved control over environmental conditions
- Enhanced energy efficiency
- Better system performance and longevity

### Implementation Details:
- **Installation:** Fan speed control modules installed in each fan unit.
- **Configuration:** 
  - TWENTY_PERCENT: Set to operate at 20% of maximum speed for minimal ventilation needs.
  - FIFTY_PERCENT: Configured to run at 50% of maximum speed for moderate ventilation requirements.
  - SEVENTY-FIVE_PERCENT: Adjusted to operate at 75% of maximum speed for increased ventilation demand.
  - HUNDRED_PERCENT: Set to run at full speed for maximum ventilation output.

### Expected Benefits:
- Optimized fan operation and energy use according to varying ventilation needs.
- Enhanced comfort and environmental control by adjusting airflow as per occupancy and activity levels.
- Extended lifespan of fan units due to reduced wear and tear from running at lower speeds when possible.
## Conclusion




These model decisions were made to optimize the system’s performance, efficiency, and reliability. Continuous monitoring and evaluation will ensure that these decisions achieve the desired outcomes and adapt to any future needs or challenges.

---
