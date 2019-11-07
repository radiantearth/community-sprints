## Overview

This document should link to all work happening at the sprint. Links to PR's and proposals
  
## Query
- sorting - change the name of the sort parameter to `sortby` to align with OGC specs, provide a simplified, non-JSON syntax for use by GET
  - https://github.com/radiantearth/stac-spec/pull/513
  - https://github.com/opengeospatial/ogcapi-features/issues/157
  - needs harmonization

## Item
- [Added purpose field to Asset](https://github.com/radiantearth/stac-spec/pull/637) - added field `purpose` as a corollary field to Links `rel`, to describe a common set of usages for specific assets in an item, for example `thumbnail`.  

## Extensions
- [WIP Aerial Extension](https://github.com/radiantearth/stac-spec/pull/639)

## Implementations
- pygeoapi STAC support
  - https://github.com/radiantearth/community-sprints/pull/19/files
  - discussion: https://github.com/geopython/pygeoapi/issues/221

* [Aligned STAC-specific endpoints more with OAF](https://github.com/radiantearth/stac-spec/pull/632) - also mentioned in a related [OAF issue](https://github.com/opengeospatial/ogcapi-features/issues/154).
* [Franklin](https://github.com/azavea/franklin) work ongoing around filling in OFeat / STAC endpoints and an importer. Endpoint progress is visible in the README, open work is visible in the [PRs](https://github.com/azavea/franklin/pulls)
* [Converted search metadata to context object](https://github.com/radiantearth/stac-spec/pull/633) - consolidated search metadata into a context object that the root level of the FeatureCollection. Slimmed down property names.
* Completed some initial work on Python client for Maxar STAC catalog API

## Filter (Common Query Language)

* [Cleaned up BNF from OGC Catalgue](https://github.com/opengeospatial/ogcapi-features/blob/master/extensions/cql/schema/cql.bnf)
* [Developed equivalent JSON encoding](https://github.com/opengeospatial/ogcapi-features/blob/master/extensions/cql/schema/cql.json)
* [Developed and alternate equivalent JSON encoding of CQL](https://github.com/tschaub/ogcapi-features/blob/json-array-expression/extensions/cql/jfe/readme.md)
* Examples of each can be found [here](https://github.com/opengeospatial/ogcapi-features/tree/master/extensions/cql/examples) and [here](https://github.com/tschaub/ogcapi-features/blob/json-array-expression/extensions/cql/jfe/examples.md)
* [JSON Filter Expression](https://github.com/opengeospatial/ogcapi-features/pull/283) - Work in progress proposal to use JSON arrays as filter expressions.
* A filter capabilties document was also developed [here](https://github.com/opengeospatial/ogcapi-features/blob/master/extensions/cql/schema/filter-capabilities.json) with an example [here](https://github.com/opengeospatial/ogcapi-features/blob/master/extensions/cql/examples/filter-capabilities-example-full.json)
* Full text search: https://github.com/opengeospatial/ogcapi-features/pull/284
* Trivial point, there is an OGC document number of the CQL extension document: OGC 19-079.

### Transactions

* A detailed outline of the OGC transactions, based on OGC work, was posted [here](https://github.com/opengeospatial/ogcapi-features/blob/master/extensions/transactions/TX_Notes.adoc)

### Collections Summary

* [Collection Summary](https://github.com/opengeospatial/ogcapi-features/pull/287) - Draft proposal to add a collection summary to the Features spec.


* [PySTAC tutorial](https://github.com/azavea/pystac/pull/48) - Fixed the PySTAC SpaceNet tutorial to point to the right places in the re-organized SpaceNet S3 bucket.

