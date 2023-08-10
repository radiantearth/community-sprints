## Overview

As STAC and OGC API - Features are aiming to be much more implementation-lead than previous geospatial specifications, the
key activity at any sprint is to actually build - not just talk about specifications. Obviously 3 days isn't enough to
build a full solution from scratch, but it can provide the space to start and bring together collaborators. Indeed the
[pygeoapi](https://pygeoapi.io/) project started at the first [STAC / OGC joint sprint](https://medium.com/@cholmes/wfs-3-0-and-spatiotemporal-asset-catalog-stac-in-person-collaboration-609e10d7f714).

As both specs are maturing we hope to see lots of cross-implementation testing, and hopefully more clients built as we
finally have a number of stable services to rely upon. And you can also work on specific testing tools, like the STAC
validator or the OGC CITE tests, or make new, innovative testing tools.

We also are really excited about standing up more **data** - as the end goal of this work is to make more geospatial data
available to people. So don't feel like you need to be coding, using someone else's software to make a new service or
static catalog is a *huge* contribution to the community. More details on all these topics below.


## Implementing a Features API Server or Client

Start a new project or evolve an existing one with the latest spec and experimental features - client and servers both
welcome.

### Service Endpoints

Clients can hit these endpoints to ensure their client works.

* https://beta-paikkatieto.maanmittauslaitos.fi/maastotiedot/wfs3/v1
* http://www.pvretano.com/cubewerx/cubeserv/default/wfs/3.0.0/framework  
* https://services.interactive-instruments.de/t15/daraa
* https://www.ldproxy.nrw.de/kataster
* https://demo.pygeoapi.io/master
* https://geo.weather.gc.ca/geomet-beta/features
* https://stac.boundlessgeo.io/
* https://tamn.snapplanet.io
* https://eod-catalog-svc-prod.astraea.earth/api/v2/
* https://databio.spacebel.be/eo-features/ (Work in progress)

### Clients

Servers can use these clients to make sure they're working right.

* GDAL/OGR - https://gdal.org/drivers/vector/oapif.html#vector-oapif (GDAL 3.0.2 is OAPIF 1.0. GDAL master Docker images are also usable such as osgeo/gdal:alpine-normal-latest . See https://github.com/OSGeo/gdal/tree/master/gdal/docker )
* QGIS - https://qgis.org/en/site/forusers/alldownloads.html#qgis-nightly-release
* Leaflet-based - https://opengeogroep.github.io/ogc-api-features-testclient/src/index.html
* rocket - https://rocket.snapplanet.io
* OpenLayers? Leaflet? Esri Koop?
* Are CITE tests up to date with 1.0?

### Classifieds

#### Projects to contribute to
*Add your project or project idea here if you'd like people to help out during the sprint*

* pygeoapi - https://pygeoapi.io/ (Tom/Angelos/Just/Francesco - what types of things would be good for people to work on?)
  * Would like to flesh out and add more features to the postgres provider. Some things I have been thinking of: mapping column names to key names; ability to specify more complex queries for the collection rather than having to put a collection into a single table; can we add something like a count of features (right now I don't know of a way to get in a single query the number of items in a collection) - Mary Bucknell
* pystac - https://pystac.readthedocs.io
  * Python library for core stac. Could use contribution for implementations of additional extensions, as well as general kicking-the-tires usage to ensure it fits the Python STAC community's use cases. Interested in how this can be integrated into existing or new Python tooling to help enable Client and Service Endpoint projects. Ping Rob Emanuele (@lossyrob) if interested.
* franklin - https://github.com/azavea/franklin
  * Franklin is (will be) a STAC and OGC API Features compliant web service focused on ease-of-use for end-users. It's goal is to enable the following workflow: start server, POST catalog.json, browse and query STAC catalog. Written in Scala, backed by [geotrellis-server](https://github.com/geotrellis/geotrellis-server), [http4s](https://github.com/http4s/http4s), and [tapir](https://github.com/softwaremill/tapir). Find Aaron Su (@aaronxsu) in VA or ping Chris Brown (@notthatbreezy) or James Santucci (@jisantuc) for remotes if you're interested. 
* [@koopjs/provider-ogcapi-features](https://github.com/koopjs/provider-ogcapi-features)
  * [KoopJS provider plugin](https://koopjs.github.io/docs/basics/overview#provider) to fetch and query features from the OGC API - Feature. This provider allows the developer to translates the OGC API into [Esri GeoService](https://geoservices.github.io/), which can be consumed by Esri softwares. With existing KoopJS [outputs](https://koopjs.github.io/docs/available-plugins/outputs), data from OGC API can be translated into many other formats. Find Haoliang Yu (@haoliangyu) or Andrew Turner if interested.
* koop-output-ogc-api-features
  * [KoopJS output plugin](https://koopjs.github.io/docs/basics/overview#output) to return data in OGC API - Feature spec. This output allows the developer to expose any data fetched by [Koop providers](https://koopjs.github.io/docs/available-plugins/providers) as OGC API. Find Haoliang Yu (@haoliangyu) or Andrew Turner if interested.
* Add yours

### Interested people
*Add your name and interests here if you'd like to work*


## STAC Implementation - create or improve a compliant Catalog

Get more data that is publicly available as a STAC catalog, or enhance an existing one. Enhancements include getting
a STAC Browser, custom-styling a STAC Browser, indexing in a STAC API, and getting it working with clients like QGIS,
[sat-api-browser](https://github.com/sat-utils/sat-api-browser), sat-search, etc.

### Potential Data to stand-up

 * Astraea MODIS MCD43A4, MxD11A1, and MxD13A1 COGs (all time, global) at s3://astraea-opendata (currently being moved from an internal bucket in AWS us-east-1 to a public requester-pays bucket in us-west-2)
 * United States Geological Survey (USGS) has a large amount of timeseries data collected at locations through the United States and territories. It would be great to work on figuring how use STAC with hydrologic data as a starting point to making this data more discoverable.


### Existing Data to enhance

 * To add

## Testing and Validation

* STAC Validator / STAC Lint
    * [https://github.com/s22s/stac-api-validator]
* OGC CITE
* Rumbles about a python-based test suite as a community-lead alternative to CITE
