# Tools of the trade

* ide
* VCS(version control software)
* Coverage and verification tools(help you during test)

# Life Cycle Models
## What is the software lifecycle?

Sequence of decisions that determine the history of your software. There are many ways in which you can make these decisions.

It includes: what should I do next? How long should I do it for?

It is important to understand which models are good for which situations.

Criticality of the software also plays an important role when choosing a model. And so does the expected variability in the requirements.

Small projects are usually appropriate for agile. Larger projects may require a more rigorous approach.

You may even use multiple lifecycle models within a single project.

## Traditional Software Phases

Requirements Engineering -> Design -> Implementation -> verification and validation -> maintenance

## Requirements Engineering

RE is the process of establishing the needs of stakeholders that are to be solved by software.

AIM: to reduce the cost of late correction

## Design

Software is the design where software requirements are analyzed in order to produce a description of the internal structure and organization of the system.

Design activities: architectural design -> abstract specification -> interface design -> component design -> data structure -> algorithm design.

Design products: system structure -> software specification -> interface specification -> component specification -> data structure specification -> algorithm specification

## Implementation

* Reduction of complexity
* Anticipation of diversity
* Structuring for validation
* Use of (external) standards

## Verification & validation

validation: did we build the right system? Fit the customer's require.

verification: did we build the system right? Fit our demands.

Check: Unit test, integration test, system test.

## Maintenance

* The environment may change.
* feature request.
* bug report.

Then we may need: corrective maintenance, perfective maintenance, adaptive maintenance.

Very expansive because regression maintenance.

# Waterfall Model

waterfall model the project :

software concept -> requirement analysis -> architectural design -> detailed design -> coding and debugging -> system testing

Advantage: Finds errors early

Disadvantage: Not flexible

# Spiral Model

1. Determine objectives
2. Identify and resolve risks
3. Development and test
4. Plan the next iteration

And then iterating

Ads: risk reduction; functionality can be added; software produced early

Disadvantages: specific expertise; highly dependent on risk analysis; complex

# Evolutionary prototyping

Initial concept -> design and implement initial prototype -> refine prototype until acceptable -> complete and release prototype

Advantages: immediate feedback

Disadvantages: difficult to plan

# rational unified process(RUP)

popular, based on UML.

# Agile

based on highly iterative and incremental development. Test driven development: TDD.

1. Write a test that fails : RED(fail)
2. Make only enough code for it to pass: GREEN(pass)
3. Refactor: Improve code quality

# Choosing a model

requirement understanding/ Expected lifetime/ Risk/ Schedule constraints/ interaction with customers/ expertise

# Classic mistakes: people

Heroics: take risks, discourage cooperation, finally fail.

Work environment: not create the right working environment. Nice, quiet, warm, welcoming.

People management: lack of leadership, adding people which is behind schedule, which never works.

# Classic mistakes: process

scheduling issues, planning issues, failures

# Classic mistakes: products

Gold plating: more requirements than they actually need.

Feature creep: adding more and more features to a product that were not initially planned and are not really need in most cases.

Research not equals to development. Research have a highly unpredictable schedule.

# Classic mistakes: technology

Silver-bullet syndrome: too much reliance on the advertised benefits of some previously unused technology.

Switching tools: switching or adding tools in the middle of a object.

No version control: lack of an automated version control system.

#
