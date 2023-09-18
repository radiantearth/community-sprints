# Overview

Without software, a specification is just a bunch of words.
The STAC ecosystem's software tooling provides implementation of the specification, enabling its use in products and services.
Implementations and tools also uncover issues with the specification, evolve extensions, and inform improvements to the spec.

The majority, but not all, of STAC software is housed in the [stac-utils Github organization](https://github.com/stac-utils).
This document will collect topics for the STAC sprint that relate to those softwares.
These topics might include:

- Bug fixes
- New features
- Documentation improvements
- FAQs and explainers
- New repositories

Please add your topic suggestions to the sections below, using Github pull requests.
If you see a software repository of interest, please add bullet points under that software.
If you don't see the software repository you're interested, please add it to the appropriate section (or start a new one).

During the sprint itself, we will be using [this project](https://github.com/orgs/stac-utils/projects/8/views/1) to coordinate work.

## Core implementations

Core implementations provide the base data structures and functionality for a variety of languages (e.g. **pystac** for Python, **stac-fields** for Javascript, etc).
If you'd like to propose work on a core implementation, please add it to the list below, along with the topics you'd like to address:

- [pystac](https://github.com/pystac)
  - Take up any changes for v1.1 of the STAC spec
  - [Supporting older STAC versions?](https://github.com/stac-utils/pystac/issues/441)
  - Extensions
    - <https://github.com/stac-utils/pystac/issues/448>
    - <https://github.com/stac-utils/pystac/issues/1051>
  - Use a serialization library
    - [Tracking issue](https://github.com/stac-utils/pystac/issues/1092)
    - Relatedly, [stac-pydantic](https://github.com/stac-utils/stac-pydantic) is currently very bitrotted, should we deprecate?
      If so, we'll need to rip it out of **stac-fastapi**.
- Add yours

## Testing and validation

- [stac-validator](https://github.com/stac-utils/stac-validator) and [stac-check](https://github.com/stac-utils/stac-check)
  - [https://github.com/s22s/stac-api-validator](https://github.com/s22s/stac-api-validator)
  - Discussion needed: [Validators report STAC as valid although it is not truly valid](https://github.com/radiantearth/stac-spec/discussions/1242)
  - Can these be pruned to make them lighter?
    They're currently a little dependency heavy to serve as core validation libraries (e.g. they require **click**).
- [stac-api-validator](https://github.com/stac-utils/stac-api-validator)
- Add yours

## Server software

- [stac-fastapi](https://github.com/stac-utils/stac-fastapi)
- [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac)
- [pgstac](https://github.com/stac-utils/pgstac)
- [stac-server](https://github.com/stac-utils/stac-server)
- Add yours

## Client software

A set of STAC software is dedicated to fetching data from STAC APIs and displaying it or doing work.

- [stac-browser](https://github.com/radiantearth/stac-browser)
- [pystac-client](https://github.com/stac-utils/pystac-client)
- **xarray**/**zarr** interoperability
  - [odc-stac](https://github.com/opendatacube/odc-stac) vs [stackstac](https://github.com/gjoseph92/stackstac)
  - Other supporting tooling
- Add yours
