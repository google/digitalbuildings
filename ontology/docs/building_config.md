Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@cstirdivant 
google
/
digitalbuildings
Public
Fork your own copy of google/digitalbuildings
Code
Issues
14
Pull requests
17
Discussions
Actions
Projects
3
Wiki
Security
Insights
digitalbuildings
/
ontology
/
docs
/
building_config.md
 

Spaces

4

Soft wrap
1
# Model Instance Configuration (building configuration file)
2
​
3
**Prerequisite** Please review the [Learning Modules](../../README.md#learning-modules).
4
This readme assumes that the audience is familiar with the high level concepts
5
which comprise the building config.
6
​
7
In addition to a language and primitives for configuring an abstract building
8
model, the Digital Buildings project provides a YAML configuration syntax for
9
mapping concrete assets to the abstract model in a lightweight way. The intent
10
of providing this syntax is to make "manual" onboarding faster and easier
11
(because the resulting data file is machine readable and can be machine
12
validated) as well as provide a clean interface format for machine-assisted
13
onboarding to use.
14
​
15
NB: Some of the instructions here details that are specific to Google's
16
implementation of this stack on its own campuses (such as references to CloudIoT
17
registration). These should be relatively obvious to a critical reader, but if
18
they are confusing feel free to post an issue in the project.
19
​
20
*   For an explanation of types in the Digital Buildings abstract model see
21
    [model](model.md)
22
*   For a conceptual explanation of the ontology see [ontology](ontology.md)
23
​
24
- [Model Instance Configuration](#model-instance-configuration)
25
  * [Key Concepts](#key-concepts)
26
  * [Typical Data Elements](#typical-data-elements)
27
  * [Configuration Detail](#configuration-detail)
28
    + [Contents](#contents)
29
    + [Config Format](#config-format)
30
    + [Spaces](#spaces)
31
    + [Devices](#devices)
32
      - [Reporting Physical Devices](#reporting-physical-devices)
33
        * [Defining Translations](#defining-translations)
34
          + [Translation Shortcuts](#translation-shortcuts)
35
          <!--- + [Compliant Short forms](#compliant-short-forms) --->
36
        <!-- * [Metadata](#metadata) -->
37
      - [Virtual Devices](#virtual-devices)
38
      - [Device Relationships](#device-relationships)
39
    + [Zones and Control Groups](#zones-and-control-groups)
40
  * [Building Configuration Modes](#building-configuration-modes)
41
    + [INITIALIZE](#initialize)
42
    + [UPDATE](#update)
43
      - [General](#general-updates)
44
      - [Special Cases](#special-cases)
45
  * [Validation](#validation)
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
@cstirdivant
Propose changes
Commit summary
Create building_config.md
Optional extended description
Add an optional extended description…
 You can’t commit to master because it is a protected branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
cstirdivant-patch-2
 
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
