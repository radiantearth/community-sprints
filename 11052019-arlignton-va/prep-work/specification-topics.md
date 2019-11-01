## Overview

TODO: Flesh this out.

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



## Describing data

* Both full JSON Schema as well as lighterweight 'summaries' that are just field names and potential values/ranges. 
[DescribeFeatureType issue](https://github.com/opengeospatial/ogcapi-features/issues/56)
STAC Summaries

## Static OGC Features

* What's the equivalent to a static STAC? 
* OGC Collection (in Commons repo), plus link to geopackage / geojson(+newline+cloud-optimized?) / avro (w/ wkb) - for bigquery import

## OACat

OGC API - Catalog(ue) aka CAT4 aka OACat. SWG is formed, should align with all these efforts well. Someone from the
community please help fleshing out a page with top topics to discuss, and relevant links of work done.
