# About

This directory is a workspace to collaborative prepare for the joint STAC + OGC API - Features sprint. Everyone is welcome
to edit files and make new workspaces - just make a PR and then we'll give you edit access on master. Work will also take place 
on other repositories specific to projects or specifications - this just serves as very lightweight collaboration space 
with a low barrier to entry. 

# Topics

There are three main categories of topics, and each has their own page or directory to go deeper on. These should serve
to get people working on the topic on the same page before the sprint. Each should have a number of links to give a newer
user the appropriate background, and should attempt to frame the major points of decision. These will likely be various
degrees of WIP (work in progress), as everyone is too busy ahead of the sprint, but something started is better than nothing.

* **[Implementations](implementation-topics.md)** - The goal of these sprints is to build - software, hosted datasets, testing 
tools, etc - with the specification being a side-effect of people working together. So if people are not sure where to 
contribute then jumping on this area is one of the best. The [implementations page](implementations.md) details the various 
projects people are working on, as well as ideas of new datasets / software, and you can also offer up your skills there. 
Testing and validation is also a part of this. It includes both STAC and Features API projects.

* **[Specification Topics](specification-topics.md)** - Since we are bringing together both STAC and OGC API communities, the 
primary goal is to work on topics that are relevance for both groups. So all of these should be detailed ahead of time
as much as possible. The STAC community will also have a set of topics that they aim to tackle. And we will also provide
a space for OGC API - Catalogue, as it aligns so closely aligns, and 5 of 8 members of the SWG will be participating.

* **[Outreach](outreach-topics.md)** - The third major topic is outreach, broadly defined. How do we get more people aware
of OGC API - Features and STAC? What can we write and present to raise awareness? Where should we be? Past sprints have done
things like create the http://stacspec.org website. Could try to start on an ogc api - features website, and there's lots
more improvements possible on stacspec.org. 



* https://beta-paikkatieto.maanmittauslaitos.fi/maastotiedot/wfs3/v1
* http://www.pvretano.com/cubewerx/cubeserv/default/wfs/3.0.0/framework  
* https://services.interactive-instruments.de/t15/daraa
* https://www.ldproxy.nrw.de/kataster
* https://demo.pygeoapi.io/master
* https://stac.boundlessgeo.io/
* https://tamn.snapplanet.io
* http://databio.spacebel.be/eo-features/ (In progress)
* https://eod-catalog-svc-prod.astraea.earth/api/v2/

### Clients

Servers can use these clients to make sure they're working right.

* GDAL/OGR - https://gdal.org/drivers/vector/oapif.html#vector-oapif (GDAL 3.1 is OAPIF 1.0, not yet released)
* QGIS - https://qgis.org/en/site/forusers/alldownloads.html#qgis-nightly-release
* OpenLayers? Leaflet? Esri Koop? 
* Are CITE tests up to date with 1.0?

### Classifieds

#### Projects to contribute to
*Add your project or project idea here if you'd like people to help out during the sprint*

* pygeoapi - https://pygeoapi.io/ (Tom/Angelos/Just/Francesco - what types of things would be good for people to work on?)
  * Would like to flesh out and add more features to the postgres provider. Some things I have been thinking of: mapping column names to key names; ability to specify more complex queries for the collection rather than having to put a collection into a single table; can we add something like a count of features (right now I don't know of a way to get in a single query the number of items in a collection) - Mary Bucknell
* Add yours

### Interested people
*Add your name and interests here if you'd like to work*
 
## Query

Getting to a standardized, easy to implement and powerful query (with filter) is the main thing that has brought these two
groups together. The OAFeat core spec is deliberately minimal, and many users need more powerful options from it. STAC is 
one of those that needs more, and it has been working on its own query/filter, but would be happy to go with another path
that meets its needs and gets fully standardized.

Though obviously quite linked to the Filter, we are going to try to make parallel progress on both 'everything but filter' and
filters.

Related PR: [https://github.com/radiantearth/stac-spec/pull/500]

### Query Topics

TODO: Turn this into its own page / directory, and add examples of potential proposals to discuss ahead of meeting in person.

* *Paging & Search Metadata* - OAFeat 1.0 has a good bit speced on this, and aligning has always been a bit confusing with STAC,
so we need to properly align the two. STAC has https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/search
which specifies the 'search metadata', and the community generally wants a clear mechanism to specify an offset - at least as 
an option. In OAFeat land, there is an [issue](https://github.com/opengeospatial/ogcapi-features/issues/75)
for bringing back startIndex. The STAC group would like to pick a name that is a single word, so it doesn't have to be 
camelCase. See also https://github.com/opengeospatial/ogcapi-features/issues/251 and https://github.com/opengeospatial/ogcapi-features/issues/253
* *Sorting* - There is desire for OAFeat to [support sorting](https://github.com/opengeospatial/ogcapi-features/issues/157). 
STAC has an extension for this in use, see https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/sort 
[Staccato](https://github.com/planetlabs/staccato) also experimented with a simpler GET syntax for sorting and ordering. Relevant PR: [https://github.com/radiantearth/stac-spec/pull/513] Note
also the original ogc filter specification has a [section on sortBy](http://docs.opengeospatial.org/is/09-026r2/09-026r2.html#88) which should also be reviewed.
* *Ordering* - Though pretty implicit in both of the above topics, we need to specify exactly how to specify an order, and be
clear on what the default order of things is.
* *Fields* - Another key capability is the ability for a client to request for the server to only return certain fields,
instead of returning the whole payload each time. See the [STAC Fields extension](https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/fields)
and https://github.com/opengeospatial/ogcapi-features/issues/16 - This was known as 'propertyNames' in previous WFS version I believe. See discussion on [Staccato's approach](staccato-impl.md#fields)
* *Cross-collection queries* - Default in STAC, as most everything people want spans collections. See https://github.com/opengeospatial/ogcapi-features/issues/154
* *Aggregations* Queries that return aggregated statistics over the result sets rather than in Items. One example is [Astraea Earth OnDemand API](https://eod-catalog-svc-prod.astraea.earth/api/v2/), that takes the same parameters as search, but returns result identitical to an Elasticsearch aggregation, with the addition of a `search:metadata` attribute

See https://github.com/radiantearth/community-sprints/blob/master/11052019-arlignton-va/prep-work/staccato-impl.md#query for
lots of good information of how Staccato (a STAC API) is handling a number of these topics.

## Filter

Filter options are fully explored in [filter_options directory](filter-options/).

# Help Wanted

All of the below need quite a bit more fleshing out. Most are just headings and a couple relevant links of things
to discuss.

## STAC

STAC Community - please help with a page about sprint topics we want to discuss.

## STAC Label Extension

* Lots of good energy on this at the last STAC sprint - what do we do next?
* Would be awesome to at least have a demo of a STAC Item with Label extension that is powered by WFS requests instead of static.

## Transactions

https://github.com/opengeospatial/ogcapi-features/issues/140
https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/transaction

## Reprojection / additional projection information

* OAFeat CRS extension - is it sufficient? Does it need more?
* STAC proposal on EPSG stuff from Phil Varner. See PR [https://github.com/radiantearth/stac-spec/pull/485]

## STAC Implementation - create or improve a compliant Catalog

Get more data that is publicly available as a STAC catalog, or enhance an existing one. Enhancements include getting 
a STAC Browser, custom-styling a STAC Browser, indexing in a STAC API, and getting it working with clients like QGIS, 
[sat-api-browser](https://github.com/sat-utils/sat-api-browser), sat-search, etc.

### Potential Data to stand-up
 
 * Astraea MODIS MCD43A4, MxD11A1, and MxD13A1 COGs (all time, global) at s3://astraea-opendata (currently being moved from an internal bucket in AWS us-east-1 to a public requester-pays bucket in us-west-2)

### Existing Data to enhance

 * To add

## Describing data

* Both full JSON Schema as well as lighterweight 'summaries' that are just field names and potential values/ranges. 
[DescribeFeatureType issue](https://github.com/opengeospatial/ogcapi-features/issues/56)
STAC Summaries

## Static OGC Features

* What's the equivalent to a static STAC? 
* OGC Collection (in Commons repo), plus link to geopackage / geojson(+newline+cloud-optimized?) / avro (w/ wkb) - for bigquery import
* OGC 14-055r2 OWC:Context and OWC:Resource (http://docs.opengeospatial.org/is/14-055r2/14-055r2.html) to be algned with minimal OGC API -Features requirements for (static) Feature (e.g. "id" (no URI), "self" link, Links object, xy.links instead of xy.properties.links, "rel" attribute of Link etc.)

## OACat

OGC API - Catalog(ue) aka CAT4 aka OACat. SWG is formed, should align with all these efforts well. Someone from the
community please help fleshing out a page with top topics to discuss, and relevant links of work done.

## Testing and Validation

* STAC Validator / STAC Lint
    * [https://github.com/s22s/stac-api-validator]
* OGC CITE
* Rumbles about a python-based test suite as a community-lead alternative to CITE

## Outreach

TODO: Good write-ups on outreach projects.
* stacspec.org improvements
* features api website? Tutorials?
* stac tutorials
* Blog posts / promotion opportunities - podcasts? videos? speaking opportunities?
* Good overview decks for people to reuse

