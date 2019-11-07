## Overview

This document should link to all work happening at the sprint. Links to PR's and proposals


## Filter
- filter capabilities: https://github.com/opengeospatial/ogcapi-features/blob/master/extensions/cql/filter_capabilities.json
  - full text search: https://github.com/opengeospatial/ogcapi-features/pull/284
  
## Query
- sorting - change the name of the sort parameter to `sortby` to align with OGC specs, provide a simplified, non-JSON syntax for use by GET
  - https://github.com/radiantearth/stac-spec/pull/513
  - https://github.com/opengeospatial/ogcapi-features/issues/157
  - needs harmonization
  

## Item
- [Added purpose field to Asset](https://github.com/radiantearth/stac-spec/pull/637) - added field `purpose` as a corollary field to Links `rel`, to describe a common set of usages for specific assets in an item, for example `thumbnail`.  

## Implementations
- pygeoapi STAC support
  - https://github.com/radiantearth/community-sprints/pull/19/files
  - discussion: https://github.com/geopython/pygeoapi/issues/221

* [Aligned STAC-specific endpoints more with OAF](https://github.com/radiantearth/stac-spec/pull/632) - also mentioned in a related [OAF issue](https://github.com/opengeospatial/ogcapi-features/issues/154).
* [Franklin](https://github.com/azavea/franklin) work ongoing around filling in OFeat / STAC endpoints and an importer. Endpoint progress is visible in the README, open work is visible in the [PRs](https://github.com/azavea/franklin/pulls)
* [Converted search metadata to context object](https://github.com/radiantearth/stac-spec/pull/633) - consolidated search metadata into a context object that the root level of the FeatureCollection. Slimmed down property names.
* [JSON Filter Expression](https://github.com/opengeospatial/ogcapi-features/pull/283) - Work in progress proposal to use JSON arrays as filter expressions.
* [Collection Summary](https://github.com/opengeospatial/ogcapi-features/pull/287) - Draft proposal to add a collection summary to the Features spec.
* [PySTAC tutorial](https://github.com/azavea/pystac/pull/48) - Fixed the PySTAC SpaceNet tutorial to point to the right places in the re-organized SpaceNet S3 bucket.

