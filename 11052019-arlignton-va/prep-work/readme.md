# About

This directory is a workspace to collaborative prepare for the joint STAC + OGC API - Features sprint. Everyone is welcome
to edit files and make new workspaces - just make a PR and then we'll give you edit access on master. Work will also take place 
on other repositories specific to projects or specifications - this just serves as very lightweight collaboration space 
with a low barrier to entry. 

# Topics

This is a non-exhaustive list of topics that people would like to discuss and collaborate on during the sprint. Each section
should contain a set of links that are useful for someone to get up to speed, and any preparatory work that would be useful.
These will start on this page, but once it becomes too unweildly we can break things out to their own pages / directories. 

## Implementing a Features API Server or Client

Start a new project or evolve an existing one with the latest spec and experimental features - client and servers both 
welcome. 

### Service Endpoints

Clients can hit these endpoints to ensure their client works.

https://beta-paikkatieto.maanmittauslaitos.fi/maastotiedot/wfs3/v1
http://www.pvretano.com/cubewerx/cubeserv/default/wfs/3.0.0/framework  
https://services.interactive-instruments.de/t15/daraa
https://www.ldproxy.nrw.de/kataster
https://demo.pygeoapi.io/master
https://stac.boundlessgeo.io/

### Clients

Servers can use these clients to make sure they're working right.

GDAL/OGR - https://gdal.org/drivers/vector/oapif.html#vector-oapif (GDAL 3.1 is OAPIF 1.0, not yet released)
QGIS - https://qgis.org/en/site/forusers/alldownloads.html#qgis-nightly-release
OpenLayers? Leaflet? Esri Koop? 

## STAC Implementation - create or improve a compliant Catalog

Get more data that is publicly available as a STAC catalog, or enhance an existing one. Enhancements include getting 
a STAC Browser, custom-styling a STAC Browser, indexing in a STAC API, and getting it working with clients like QGIS, 
[sat-api-browser](https://github.com/sat-utils/sat-api-browser), sat-search, etc.

### Potential Data to stand-up
 
 * To add

### Existing Data to enhance

 * To add
 
## Query

Getting to a standardized, easy to implement and powerful query (with filter) is the main thing that has brought these two
groups together. The OAFeat core spec is deliberately minimal, and many users need more powerful options from it. STAC is 
one of those that needs more, and it has been working on its own query/filter, but would be happy to go with another path
that meets its needs and gets fully standardized.

Though obviously quite linked to the Filter, we are going to try to make parallel progress on both 'everything but filter' and
filters.

### Query Topics

(these ideally should expand out with lots of examples on the various proposals)

* *Paging & Search Metadata* - OAFeat 1.0 has a good bit speced on this, and aligning has always been a bit confusing with STAC,
so we need to properly align the two. STAC has https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/search
which specifies the 'search metadata', and the community generally wants a clear mechanism to specify an offset - at least as 
an option. In OAFeat land, there is an [issue](https://github.com/opengeospatial/ogcapi-features/issues/75)
for bringing back startIndex. The STAC group would like to pick a name that is a single word, so it doesn't have to be 
camelCase. See also https://github.com/opengeospatial/ogcapi-features/issues/251 and https://github.com/opengeospatial/ogcapi-features/issues/253
* *Sorting* - There is desire for OAFeat to [support sorting](https://github.com/opengeospatial/ogcapi-features/issues/157). 
STAC has an extension for this in use, see https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/sort 
[Staccato](https://github.com/planetlabs/staccato) also experimented with a simpler GET syntax for sorting and ordering. 
* *Ordering* - Though pretty implicit in both of the above topics, we need to specify exactly how to specify an order, and be
clear on what the default order of things is.
* *Fields* - Another key capability is the ability for a client to request for the server to only return certain fields,
instead of returning the whole payload each time. See the [STAC Fields extension](https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/fields)
and https://github.com/opengeospatial/ogcapi-features/issues/16 - This was known as 'propertyNames' in previous WFS version 
I believe.
* *Cross-collection queries* - Default in STAC, as most everything people want spans collections. See https://github.com/opengeospatial/ogcapi-features/issues/154

## Filter

TODO: Intro. And each of these should get a much fuller page with lots of examples to get a feel of it.

* CQL - https://docs.geoserver.org/latest/en/user/tutorials/cql/cql_tutorial.html & https://docs.geoserver.org/latest/en/user/filter/ecql_reference.html#filter-ecql-reference
 and buried in some OGC Catalog spec. See also https://docs.opengeospatial.org/per/18-021.html#cql - Questions: Will it work
 well enough with nosql backends? Are there assumptions about rbdms backends that are implicit that we should remove? 
* STAC - https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/query (and didn't we have at least some ideas
for a GET one? And staccato perhaps implemented).
* GraphQL - See https://docs.opengeospatial.org/per/18-021.html#_graphql - and sat-api has experimented with this, hopefully
Sean Harkins can do a writeup on this.
* Other inspirations / candidates: https://github.com/araddon/qlbridge/blob/master/FilterQL.md plus mongo's and elastic's 
query languages (which were generally the inspiration for STAC's).


## Transactions

https://github.com/opengeospatial/ogcapi-features/issues/140
https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/transaction

## Reprojection / additional projection information

* OAFeat CRS extension - is it sufficient? Does it need more?
* STAC proposal on EPSG stuff from Phil Varner

## Describing data

* Both full JSON Schema as well as lighterweight 'summaries' that are just field names and potential values/ranges. 
[DescribeFeatureType issue](https://github.com/opengeospatial/ogcapi-features/issues/56)
STAC Summaries

## Static OGC Features

* What's the equivalent to a static STAC? 
* OGC Collection (in Commons repo), plus link to geopackage / geojson(+newline+cloud-optimized?) / avro (w/ wkb) - for bigquery import

## OACat

OGC API - Catalog(ue) aka CAT4 aka OACat. SWG is formed, should align with all these efforts well.

## Label Extension

* Lots of good energy on this at the last STAC sprint - what do we do next?
* Would be awesome to at least have a demo of a STAC Item with Label extension that is powered by WFS requests instead of static.



