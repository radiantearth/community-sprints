# Overview

The big topic that is bringing this diverse group of people together is aligning the SpatioTemporal Asset Catalog
specificiation with the OGC API - Features standard. STAC implements the Features API, but adds on quite a bit of
extra things, and has ideas to add on even more as extensions. OAFeat has been hyper-focused on the core, keeping it
as tight as possible. But as it has reached 1.0 that group is quite interested in the next set of functionality to come, 
in extensions. Some of those are seen as 'core' to STAC, but there is a happy end state where all extensions for both
are defined at the Features API level, and STAC requires some of those in its 'core', and then both share a robust
ecosystem of additional extensions that are easily used in both STAC and non-STAC Features API implementations.

This page is broken down into 3 sections. These joint topics are at the top, and the hope is all of these end up as
extensions to OGC API - Features, and we walk out of the sprint with clear proposals on many of these topics. The second
section is STAC-specific topics. STAC is stablizing, and should work to approach version 1.0-beta, before too long.
So this sprint will hopefully serve as a chance to decide on that exact path, and there will be some sessions that are
just for the STAC community.

The third section is some additional topics, that are of interest to both groups, but a little bit outside. The main one
is OACat - OGC API - Catalogues, as we'll have 5 of the 8 SWG members participating in the sprint, and it should hopefully
mirror STAC as a Features API core + required extensions, with a well-defined content model. Also in there is the idea of
a feature equivalent to STAC's 'static catalog', which likely leverages the OGC Common 'collections' building block, but
links to static resources instead of an API.

## Joint Topics

### Query

Getting to a standardized, easy to implement and powerful query (with filter) is the main thing that has brought these two
groups together. The OAFeat core spec is deliberately minimal, and many users need more powerful options from it. STAC is 
one of those that needs more, and it has been working on its own query/filter, but would be happy to go with another path
that meets its needs and gets fully standardized.

Though obviously quite linked to the Filter, we are going to try to make parallel progress on both 'everything but filter' and
filters.

Related PR: [https://github.com/radiantearth/stac-spec/pull/500]

#### Query Topics

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
also the original ogc filter specification has a [section on sortBy](http://docs.opengeospatial.org/is/09-026r2/09-026r2.html#88) which should also be reviewed.  The SRU Extension for OpenSearch () and OASIS searchRetrieve Part 3 - SRU 2.0 (http://docs.oasis-open.org/search-ws/searchRetrieve/v1.0/os/part3-sru2.0/searchRetrieve-v1.0-os-part3-sru2.0.html#_Toc324162458) also propose a syntax for sorting which was borrowed by the EO Extension of OpenSearch (OGC 13-026r9).
* *Ordering* - Though pretty implicit in both of the above topics, we need to specify exactly how to specify an order, and be
clear on what the default order of things is.
* *Fields* - Another key capability is the ability for a client to request for the server to only return certain fields,
instead of returning the whole payload each time. See the [STAC Fields extension](https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/fields)
and https://github.com/opengeospatial/ogcapi-features/issues/16 - This was known as 'propertyNames' in previous WFS version I believe. See discussion on [Staccato's approach](staccato-impl.md#fields)
* *Cross-collection queries* - Default in STAC, as most everything people want spans collections. See https://github.com/opengeospatial/ogcapi-features/issues/154
* *Aggregations* Queries that return aggregated statistics over the result sets rather than in Items. One example is [Astraea Earth OnDemand API](https://eod-catalog-svc-prod.astraea.earth/api/v2/), that takes the same parameters as search, but returns result identitical to an Elasticsearch aggregation, with the addition of a `search:metadata` attribute.
* *Query by Example (QBE)* - Would GraphQL be a possible approach ?

See https://github.com/radiantearth/community-sprints/blob/master/11052019-arlignton-va/prep-work/staccato-impl.md#query for
lots of good information of how Staccato (a STAC API) is handling a number of these topics.

### Filter

Filter options are fully explored in [filter_options directory](filter-options/).

### Transactions

https://github.com/opengeospatial/ogcapi-features/issues/140
https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/transaction

### Reprojection / additional projection information

* OAFeat CRS extension - is it sufficient? Does it need more?
* STAC proposal on EPSG stuff from Phil Varner. See PR [https://github.com/radiantearth/stac-spec/pull/485]

### Describing data

* Both full JSON Schema as well as lighterweight 'summaries' that are just field names and potential values/ranges. 
[DescribeFeatureType issue](https://github.com/opengeospatial/ogcapi-features/issues/56)
STAC Summaries


## STAC Topics

STAC Community - please help with a page about sprint topics we want to discuss.

## STAC Label Extension

* Lots of good energy on this at the last STAC sprint - what do we do next?
* Would be awesome to at least have a demo of a STAC Item with Label extension that is powered by WFS requests instead of static.

## Additional OGC Topics

## Static OGC Features

* What's the equivalent to a static STAC? 
* OGC Collection (in Commons repo), plus link to geopackage / geojson(+newline+cloud-optimized?) / avro (w/ wkb) - for bigquery import
* Make OWC:Context and OWC:Resource (https://docs.opengeospatial.org/is/14-055r2/14-055r2.html#14) consistent with the minimal Feature requirements from OGC API Features (e.g. "self" link, "id" not a URI, Link model, "rel" attribute of link, $.links instead of $.properties.links) for use as static features.

## OACat

OGC API - Catalog(ue) aka CAT4 aka OACat. SWG is formed, should align with all these efforts well. Someone from the
community please help fleshing out a page with top topics to discuss, and relevant links of work done.

* As part of EOPAD activities in Testbed-15, several catalog endpoints serving EO application/services metadata were setup by participants which combined OGC API Common and OpenSearch (OGC 13-026r8).  See the https://portal.opengeospatial.org/wiki/pub/Testbed15/ConvertDocsOutputTestbed15/testbed15/T-15-D010-Catalog_ER.pdf[Engineering Report] for details.  DataBio implementation available at https://databio.spacebel.be/eo-catalog/.
