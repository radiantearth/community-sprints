## Overview

This document should link to all work happening at the sprint. Links to PR's and proposals

## Core
* [Aligned STAC-specific endpoints with OAF](https://github.com/radiantearth/stac-spec/pull/632) - also mentioned in a related [OAF issue](https://github.com/opengeospatial/ogcapi-features/issues/154).
* [Converted search metadata to context object](https://github.com/radiantearth/stac-spec/pull/633) - consolidated search metadata into a context object that the root level of the FeatureCollection. Slimmed down property names.
  
## Query
- sorting - change the name of the sort parameter to `sortby` to align with OGC specs, provide a simplified, non-JSON syntax for use by GET
  - https://github.com/radiantearth/stac-spec/pull/513
  - https://github.com/opengeospatial/ogcapi-features/issues/157
  - needs harmonization
- Pagination is now using hypermedia links exclusively to align with OAFeat
  - https://github.com/radiantearth/stac-spec/pull/631

## Item
- [Added purpose field to Asset](https://github.com/radiantearth/stac-spec/pull/637) - added field `purpose` as a corollary field to Links `rel`, to describe a common set of usages for specific assets in an item, for example `thumbnail`.  

## Extensions
- [WIP Aerial Extension](https://github.com/radiantearth/stac-spec/pull/639)
- [API Version Extension](https://github.com/radiantearth/stac-spec/pull/635): Provides endpoints and semantics for keeping and viewing previous vesions of Collections and Items
- [Item and Collection Version Extension](https://github.com/radiantearth/stac-spec/pull/643): Provides a version and deprecated field for Item and Collections. Removes collection field from Collection spec.
- [WIP DateTime Range Extension](https://github.com/radiantearth/stac-spec/pull/638)
- [WIP Sat Extension](https://github.com/radiantearth/stac-spec/pull/644)
- [WIP Update Maturity Levels](https://github.com/radiantearth/stac-spec/pull/636) - Need to add implementations for each extension to accurately determine maturity level

## Implementations
- pygeoapi
  - STAC support
    - https://github.com/radiantearth/community-sprints/pull/19/files
    - discussion: https://github.com/geopython/pygeoapi/issues/221
    - [WIP code](https://github.com/geopython/pygeoapi/tree/stac)
  - features
    - discussion around a `search/` endpoint to match the STAC `/search` across collections https://github.com/geopython/pygeoapi/issues/292
    - allowing many:many feature:collection connections: https://github.com/geopython/pygeoapi/issues/293 @mbucknell is working on an implementation for postgres
    - allowing `properties` to be added to a collection: https://github.com/geopython/pygeoapi/issues/294
    - more sophisticated postgres connections: https://github.com/geopython/pygeoapi/pull/283
    - issue to use `theme` to group related collections together: https://github.com/geopython/pygeoapi/issues/298
  - OGC API - Catalogue
    - generate catalogue/search index atop pygeoapi collection level metadata in configuration: https://github.com/geopython/pygeoapi/pull/297

- USGS WMA and USGS Landsat/EROS are going to work together via STAC. https://code.usgs.gov/stac

- Java Spring Boot https://os-ogc-features-api.azurewebsites.net
  -https://os-ogc-features-api.azurewebsites.net/collections/buildings/items?f=application/json&bbox=440515,112486,441400,113020
  
* [Franklin](https://github.com/azavea/franklin) work ongoing around filling in OFeat / STAC endpoints and an importer. Endpoint progress is visible in the README, open work is visible in the [PRs](https://github.com/azavea/franklin/pulls). Documentation for running Franklin is [here](https://azavea.github.io/franklin). Franklin is capable of importing local STACs, then querying them at the following endpoints:

  CAPABILITIES
  - [x] `GET /`
  - [x] `GET /conformance`
  - [x] `GET /collections`
  - [x] `GET /collections/{collectionId}`

  DATA
  - [x] `GET /collections/{collectionId}/items`
  - [x] `GET /collections/{collectionId}/items/{featureId}`

  STAC
  - [x] `GET /stac`
  - [x] `GET /stac/search` -- responds but does not yet actually search
  - [x] `POST /stac/search` -- responds but does not yet actually search

* Completed some initial work on Python client for Maxar STAC catalog API
* Created a [SpaceNet 2 static STAC catalog](https://spacenet-dataset.s3.amazonaws.com/spacenet-stac/SN2_buildings/catalog.json) with label extension integrated
- Validation Group
  - Created validation Circle CI script ([WIP PR](https://github.com/radiantearth/stac-spec/pull/642))
  - PySTAC implementation to identify object type, verion and extensions from JSON, to be used in CircleCI script ([PR](https://github.com/azavea/pystac/pull/50))
  - Stac-Validator will import and use PySTAC to identify object type, version, and extensions and will use this information to infer paths to schemas on [cdn.staclint.com](cdn.staclint.com). CDN contains schemas for all versions, extensions.
  - Extension schema filenames will be adjusted to consistently infer path to schema during validation `extensions/extension-name/json-schema/extension-name.json`, for example `extensions/eo/json-schema/eo.json`. [Issue 624](https://github.com/radiantearth/stac-spec/issues/624)
  - Stac-validator will have an exit on failure mode for CICD implementations.
- Training Data
  - [OSM Generated Training Data](http://demo-mlhub-earth.s3-website-us-west-2.amazonaws.com)
  - [Landcover Classification / Building Footprints / African Crops](http://browser.radiant.earth)
  
- GDAL: https://github.com/rouault/gdal/tree/oapif_hackathon
  * can use XML Schema to create the OGR layer field structure
  * can use JSON Schema to create the OGR layer field structure
  * can use a rel=queryables end point (as implemented by GeoServer or https://services.interactive-instruments.de/t15/daraa) to get the list of queryables property. This is probably a temporary measure, pending a rel=summary endpoint is defined
  * can detect a filter-lang=cql-text parameter advertized by the OpenAPI document, and then turn OGR SQL attribute filters as CQL text. Tested against http://ows.geo-solutions.it/geoserver/ne/ogc/features

- nls-fi Features server (https://beta-paikkatieto.maanmittauslaitos.fi/maastotiedot/features/v1/)
  * added support for two filter language variants: [json-filter-expr](https://github.com/tschaub/ogcapi-features/blob/json-array-expression/extensions/cql/jfe/readme.md) and cql-json-array (what later became json-filter-expr, same as json-filter-expr but with different op codes)
  * [tieviiva (roadlink) features in bbox 24.00,66.00,24.05,66.05 and kohdeluokka >= 121111 and kohdeluokka <= 12132](https://beta-paikkatieto.maanmittauslaitos.fi/maastotiedot/features/v1/collections/tieviiva/items?bbox=24.00,66.00,24.05,66.05&filter-lang=json-filter-expr&filter=[%22all%22,[%22%3E=%22,[%22get%22,%22kohdeluokka%22],12111],[%22%3C=%22,[%22get%22,%22kohdeluokka%22],12132]]) 

* KoopJS
  * work focuses on fetch/output dataset from the data APIs in the core spec:
    * `/collections/:collectionId/items`
    * `/collections/:collectionId/items/:featureId`
  * provider plugin [@koopjs/provider-ogcapi-features](https://github.com/koopjs/provider-ogcapi-features) to read features from a collection.
  * output plugin [@koopjs/output-ogcapi-features](https://github.com/koopjs/output-ogcapi-features) to expose data from providers with data APIs. 
  * see the demo app https://github.com/haoliangyu/koop-ogcapi-features-demo-app
  
 - sat-api-pg Added OGC endpoints for [sat-api-pg](https://github.com/developmentseed/sat-api-pg).

- QGIS Server:
  * Simple transactions: implemented POST and PUT https://github.com/qgis/QGIS/pull/32694
  * Bug fixes and template enhancements: https://github.com/qgis/QGIS/pull/32596 , https://github.com/qgis/QGIS/pull/32645 , https://github.com/qgis/QGIS/pull/32656 
  * Support for `properties` https://github.com/qgis/QGIS/pull/32655
  * Documentation on `datetime` and `properties`: https://github.com/qgis/QGIS-Documentation/pull/4364
 
- GeoServer CQL implementation:
  * Presentation slides: https://drive.google.com/file/d/1bs0mGMtV4wVk8i8_J7u4IRn-kAfKZMon/view?usp=sharing
  * Landing page: http://ows.geo-solutions.it/geoserver/ne/ogc/features
  * API: http://ows.geo-solutions.it/geoserver/ne/ogc/features/api?f=text%2Fhtml
  * Queryables WIP: http://ows.geo-solutions.it/geoserver/ne/ogc/features/collections/popplaces50m/queryables?f=json
  * Filter on Megacities: https://ows.geo-solutions.it/geoserver/ne/ogc/features/collections/popplaces50m/items?limit=50&filter=MEGACITY=1&filter-lang=cql-text
  * Cities starting with "Bo": https://ows.geo-solutions.it/geoserver/ne/ogc/features/collections/popplaces50m/items?limit=50&filter=NAME%20LIKE%20%27Bo%25%27&filter-lang=cql-text
  * Cities starting with "Bo" in north america, using a separate BBOX filter: https://ows.geo-solutions.it/geoserver/ne/ogc/features/collections/popplaces50m/items?limit=50&filter=NAME%20LIKE%20%27Bo%25%27&filter-lang=cql-text&bbox=-130,20,-60,60
  * Sample filter capabilities output (not yet available on the server online): https://gist.github.com/aaime/b6ebe137b2dc318cfd31348c7e1749a3

- Open Data COGs for MODIS https://registry.opendata.aws/modis-astraea/ indexed into the Astraea [public STAC API](https://eod-catalog-svc-prod.astraea.earth/api/v2/search), also containing Landsat-8, Sentinel-2 L1C and L2a, driving [Earth OnDemand](https://earthondemand.astraea.earth/)
  * mcd43a4: 1,841,556 scenes, 4.6005327188038E13 bytes 
  * sentinel2 l1c: 9,390,229 scenes, 4.039931462003551E15 bytes
  * sentinel2_l2a: 3,184,645 scenes, 2.175544669008515E15 bytes
  * landsat8_l1tp 952,227 scenes, 7.94090302270726E14 bytes

<span id="DataBio"></span>
- **Spacebel DataBio Catalog Server Implementation**
  * Presentation slides: https://docs.google.com/presentation/d/1YJH274rWtkAw_IVtNctLfoXluh2wzNw7F_VaCGiejgU/edit#slide=id.p1
  * Evolution of the Catalog Server used in Testbed-15 EOPAD [Engineering Report OGC 19-020](https://portal.opengeospatial.org/files/90614)
    * Compliant with OGC API - Features, STAC 0.8.0 and OpenSearch (OGC 17-047).
    * On-the-fly alignment of GeoJSON objects (OGC 17-003, OGC 17-047, OGC 17-084, OGC 19-020) to GeoJSON Feature expected by OGC API Features and STAC (e.g. different Link objects, extraction of `assets`, `id`, `self` link.
  * Interoperability tested with SnapPlanet Client: https://rocket.snapplanet.io/#!/home?_url=https:%2F%2Fdatabio.spacebel.be%2Feo-features%2F
  * `/`
    - https://databio.spacebel.be/eo-features/ (Landing Page)
  * `/collections`
    - https://databio.spacebel.be/eo-features/collections  ("series", "datasets", "services", "resources"), including service and application descriptions from [OGC Testbed-15](https://www.opengeospatial.org/projects/initiatives/testbed15) EOPAD and [H2020 DataBio Hub](https://www.databiohub.eu/registry/).
  * `/collections/{collection-id}/items` 
    - DataBio: https://databio.spacebel.be/eo-features/collections/services/items?subject=databio
    - TestBed-15: https://databio.spacebel.be/eo-features/collections/services/items?subject=testbed-15
  * `/collections/{collection-id}/items/{feature-id}`  
    - EO Collection: https://databio.spacebel.be/eo-features/collections/series/items/EOP:ESA:Sentinel-2
    - EO Product: https://databio.spacebel.be/eo-features/collections/datasets/items/LS07_RMPS_ETM_GTC_1P_20000123T112001_20000123T112030_004119_0205_0050_A02A
    - EO Application: https://databio.spacebel.be/eo-features/collections/services/items/59ce3e48e4b006858838270d 
  * `/stac` 
    - STAC Catalog: https://databio.spacebel.be/eo-features/stac
  * `/stac/search` (GET)
    - Integration of Faceted Search queryable `facetLimit` and `facetedResults` response object as defined in OGC 19-020 [Testbed-15 EOPAD Engineering Report](https://portal.opengeospatial.org/files/90614) which reuses syntax from [SRU Extension for OpenSearch](https://web.archive.org/web/20180410065429/http://www.opensearch.org/Community/Proposal/Specifications/OpenSearch/Extensions/SRU/1.0/Draft_1) and [OASIS searchRetrieve](http://docs.oasis-open.org/search-ws/searchRetrieve/v1.0/os/part3-sru2.0/searchRetrieve-v1.0-os-part3-sru2.0.html#_Toc324162453).  We believe this could become a separate faceted search extension to both OpenSearch (OGC 17-047) and STAC.
        * https://databio.spacebel.be/eo-features/stac/search?platform=landsat
        * https://databio.spacebel.be/eo-features/stac/search?cloudCover=[5,10]  (supports query syntax from OpenSearch [OGC 13-026r8](http://docs.opengeospatial.org/is/13-026r8/13-026r8.html))
        * https://databio.spacebel.be/eo-features/stac/search?facetLimit=1 (Only one value per facet in response)
	* https://databio.spacebel.be/eo-features/stac/search?facetLimit=0 (Do not include facet avlues in response)
        * https://databio.spacebel.be/eo-features/stac/search?facetLimit=eo:platform (only include facet values for platform)
        * https://databio.spacebel.be/eo-features/stac/search?facetLimit=eo:platform:5 (limit number of facet values for platform to 5)
   * `/stac/search` (POST)
     - Implementation of [STAC Query Extension](https://github.com/radiantearth/stac-spec/blob/master/api-spec/extensions/query/README.md) done.  Using OGC 13-026r8 queryable names (e.g. eo:cloudCover) to identify the properties to be searched.  See example below.  GeoJSON features returned represent EO Products (OGC 17-003), EO Collections (OGC 17-084) or EO Applications (OGC 19-020).   Implementation with proposed CQL-JSON still to do.
    
 ```
 {
	"query": {
		"eo:cloudCover": {
			"gte": 5,
			"lte": 10
		},
		"eo:platform": {
			"startsWith": "landsat"
		},
		"eo:orbitDirection": {
			"eq": "DESCENDING"
		}
	}
}
```
    
    

- Client implementations:
  * Set up an online client to test stac endpoints: https://rocket.snapplanet.io
  

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

### OGC CAT 4.0

* OGC stuff: the charter for the standards working group (SWG) was approved and so work on CAT 4.0 (OGC API - Cataglogue/Records - Part 1: Core) will begin shortly
* There is already an OpenAPI document describing an initial API and examples [here](https://github.com/opengeospatial/CAT4.0/tree/master/core/code).
* There is an initial VERY, VERY, VERY rough implementation developed during the SPRINT [here](http://www.pvretano.com/cubewerx/cubeserv/default/wrs/4.0?f=xml).
** NOTE: pvretano.com is my development machine so it is Heisenberg-stable!
* The CAT 4.0 group met during the sprint to discuss CAT 4.0/STAC relationship.  STAC catalogues the spatial temporal assets.  OGC CAT 4.0 catalogues collections of assets and every else that STAC does not care about (e.g. code lists, coordinate reference system definitions, etc).
* Observation offered that a common pattern is use of WFS as a searchable catalog of footprints for coverages. This may help scope the roles of STAC API features and coverages.
* First meeting of the SWG will be announced soon.

### STAC path to 1.0

[STAC 1.0 plan](STAC-1.0-plan) is a path to get to 1.0.0-beta by end of January that everyone has agreed to.
