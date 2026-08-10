# Overview

Specification specific discussions to be had and work to be done. 

## STAC Specification

**GitHub Page:** [https://github.com/radiantearth/stac-spec](https://github.com/radiantearth/stac-spec)

* [RFC: A common construct to replace raster:bands and eo:bands](https://github.com/radiantearth/stac-spec/discussions/1213)
  * Discuss a general rule about properties inheritance and overrides (item->asset->band) that could state that the child object overrides the same properties.
* Build New Extensions
  * Proposed new extensions found [here](https://github.com/radiantearth/stac-spec/issues?q=is%3Aopen+is%3Aissue+label%3A%22new+extension%22)
* Discuss a strategy about OGC specification alignement
* @m-mohr to add more details here.
* ...

## STAC API

**GitHub Page:** [https://github.com/radiantearth/stac-api-spec](https://github.com/radiantearth/stac-api-spec)

* Criteria for promoting extensions to Stable / 1.0.0
* Extensions
  * Transaction
    * Collection transaction operations <https://github.com/stac-api-extensions/transaction/pull/4>
    * Clarify content type headers <https://github.com/stac-api-extensions/transaction/issues/6>
    * Ready for 1.0.0?
  * Children
    * Only implementation is Resto. What about stac-server and stac-fastapi
  * Fields
    * ready for 1.0.0?
  * Filter
    * should we pin to a version of CQL / Part 3 and release 1.0.0, or wait?
  * Query
    * Optional queryables endpoint like Filter <https://github.com/stac-api-extensions/query/issues/4>
  * Sort
    * Alignment with  DRAFT OGC API - Records - Part 1: Core
    * Maybe ready for 1.0.0? 

## STAC Extensions

**GitHub Page:** [github.com/stac-extensions](https://github.com/stac-extensions)

* Support for IAU Codes
  * Discussion found at: [PR #12](https://github.com/stac-extensions/projection/pull/12)
* Discuss and support references between assets and links (e.g. https://github.com/stac-extensions/web-map-links/pull/9)
  * Release virtual-assets extension : https://github.com/stac-extensions/virtual-assets (
  * Release composite extension: https://github.com/stac-extensions/composite
