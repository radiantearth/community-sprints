# Spatio-Temporal Asset Catalog Boulder Sprint 

This repository was used to organize a sprint in boulder that brought together 13 organizations in the general imagery and geospatial domain to collaborate on new standards for searching observed assets. The effort was roughly focused on imagery from satellites, but the goal was to design a core set of search fields that could handle a wider variety of assets - imagery from drones, balloons, etc., point clouds/LiDAR, derived data (like NDVI), mosaics, synthetic aperture radar, hyperspectral, etc. 

The resulting specifications are continuing to evolve, in the Spatio-Temporal Asset Catalog and Spatio-Temporal Asset Metadata repositories. 

This repository serves as a historical record, so others can see what was discussed and created during the sprint.

## Repository Layout

### Workstreams

[workstreams/](workstreams/) contains information about the 4 major groups the sprint was divided in to. Each folder contains an overview of the major goals, questions, background work and participants in each workstream. Notes from the main two days are also in the folder.

* [Core Metadata](workstreams/core-metadata/) worked on defining the main fields of metadata records to be searched and crawled, serving as input to the other groups. They established a core set of fields that all spatio-temporal assets should have, and also made progress towards an eo profile for satellite imagery. The work can be found in their [draft-spec](workstreams/core-metadata/draft-spec.md) 

* [Static Catalog](workstreams/static-catalog/) defined a version of the catalog that could be served just using files sitting on an object store like S3. It wouldn't index fields and respond to queries, but could be crawled by a search engine, or serve as input to a more active api. This group defined a number of [specs](specs/flat_file/) with examples, as well as a first crawler implementation in the [catalog-crawler](catalog-crawler/) folder.

* [Core API Mechanics](workstreams/core-api-mechanics) worked on the core API that enables active querying, defining an OpenAPI 2.0 definition for servers to implement. They got to a solid [draft spec](https://github.com/radiantearth/catalog-api-spec/blob/dev/spec/spec-draft-sprint-day-2.yaml) and even a first [implementation](https://github.com/radiantearth/catalog-api-spec/pull/18) serving as proxy to [NASA's CMR](https://cmr.earthdata.nasa.gov/search/).

* [Extensions](workstreams/core-api-mechanics) explored how the core metadata could be extended with more fields, as well as investigated what types of operations might want to build upon the core API spec. They built a [spec, samples and tools](https://github.com/radiantearth/boulder-sprint/tree/master/extensions) to show how the core could be extended to cover all the metadata providers like Planet and DigitalGlobe, as well as adding in tile serving as an extension.

#### Other folders

[catalog-crawler/](catalog-crawler/) contains a first implementation of a crawler of the static catalog spec.

[extensions/](extensions/) contains work done by the extensions group to take records from both DigitalGlobe & Planet and converts them to the common format, with samples for each. They each also include an extension mechanism that lets them link to web tile servers.

[specs/](specs/) contains the [static catalog](specs/flat_file/) specs and examples, as well as a [set of record examples](specs/core-api) of how to represent DG, NAIP and Landsat in the spec. Those each are a bit different, it was an exercise to see how people interpreted the core. There is also an early draft spec of the [core api](specs/core-api/core-api-schema.yaml)
