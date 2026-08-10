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

* **Paging & Search Metadata** - OAFeat 1.0 has a good bit speced on this, and aligning has always been a bit confusing with STAC,
so we need to properly align the two. STAC has https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/search
which specifies the 'search metadata', and the community generally wants a clear mechanism to specify an offset - at least as 
an option. In OAFeat land, there is an [issue](https://github.com/opengeospatial/ogcapi-features/issues/75)
for bringing back startIndex. The STAC group would like to pick a name that is a single word, so it doesn't have to be 
camelCase. See also https://github.com/opengeospatial/ogcapi-features/issues/251 and https://github.com/opengeospatial/ogcapi-features/issues/253
* **Sorting** - There is desire for OAFeat to [support sorting](https://github.com/opengeospatial/ogcapi-features/issues/157). 
STAC has an extension for this in use, see https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/sort 
[Staccato](https://github.com/planetlabs/staccato) also experimented with a simpler GET syntax for sorting and ordering. Relevant PR: [https://github.com/radiantearth/stac-spec/pull/513] Note
also the original ogc filter specification has a [section on sortBy](http://docs.opengeospatial.org/is/09-026r2/09-026r2.html#88) which should also be reviewed.  
The SRU Extension for OpenSearch () and [OASIS search Retrieve Part 3 - SRU 2.0](http://docs.oasis-open.org/search-ws/searchRetrieve/v1.0/os/part3-sru2.0/searchRetrieve-v1.0-os-part3-sru2.0.html#_Toc324162458) also propose a syntax for sorting which was borrowed by the EO Extension of OpenSearch (OGC 13-026r9).
* **Ordering** - Though pretty implicit in both of the above topics, we need to specify exactly how to specify an order, and be
clear on what the default order of things is.
* **Fields** - Another key capability is the ability for a client to request for the server to only return certain fields,
instead of returning the whole payload each time. See the [STAC Fields extension](https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/fields)
and https://github.com/opengeospatial/ogcapi-features/issues/16 - This was known as 'propertyNames' in previous WFS version I believe. See discussion on [Staccato's approach](staccato-impl.md#fields)
* **Cross-collection queries** - Default in STAC, as most everything people want spans collections. See https://github.com/opengeospatial/ogcapi-features/issues/154
* *Aggregations* Queries that return aggregated statistics over the result sets rather than in Items. One example is [Astraea Earth OnDemand API](https://eod-catalog-svc-prod.astraea.earth/api/v2/), that takes the same parameters as search, but returns result identitical to an Elasticsearch aggregation, with the addition of a `search:metadata` attribute.
* **Query by Example (QBE)** - Would GraphQL be a possible approach ?
* **Faceted search** - The OGC Testbed-15 EOPAD ER proposes an approach compatible with GeoJSON FeatureCollection responses (derived from OASIS searchRetrieve).  See https://portal.opengeospatial.org/wiki/pub/Testbed15/ConvertDocsOutputTestbed15/testbed15/T-15-D010-Catalog_ER.pdf.
* **Authentication** - we've made the decision to be agnostic on authentication in the specification, but we should discuss ensuring that auth will work with our decisions, and possibly defining HATEOS-style behaviors that are predicated on authorization (e.g., different users have access to different collections or behaviors)

See https://github.com/radiantearth/community-sprints/blob/master/11052019-arlignton-va/prep-work/staccato-impl.md#query for
lots of good information of how Staccato (a STAC API) is handling a number of these topics.

### Filter

Filter options are fully explored in [filter_options directory](filter-options/).

### Transactions (& versioning)

The ability to modify (insert, update, delete) items through the REST API is a key requirement for many users. Without a clear
standard people have been exploring different approaches. There is [an 
issue](https://github.com/opengeospatial/ogcapi-features/issues/140) in features api to track things.

The STAC community specified a straight-forward REST interpretation of how to do transactions, see the [rendered 
OpenAPI](https://stacspec.org/STAC-ext-api.html#tag/Transaction-Extension) and [the 
specified extension](https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/transaction). 

The main thing that has not been specified, but for which there is clear need, is **bulk transactions**. The REST paradigm
operates on individual resources, but importing a dataset with millions of features (which is quite common) can be a huge
pain. 

[sat-api](https://github.com/sat-utils/sat-api) actually does not implement the transaction extension in STAC, but did build
endpoints for bulk import. So it is clear a prioritized use case that we should aim to specify. See their [ingestion 
docs](https://github.com/sat-utils/sat-api-deployment#ingesting-data) for some additional information.

[Staccato](http://github.com/planetlabs/staccato) and Harris both support the transaction extension. Harris has been using
it extensively, and found the need to [add etags](https://github.com/radiantearth/stac-spec/pull/534) for optimistic locking,
so that is also part of the spec.

Etags point to the general topic of **versioning** - as Tim from Harris pointed out that a 'version' field (which has been
discussed in STAC recently) is what should be used in the Etag. So we should decide on how we handle not only transactions
but also versioning. Likely transactions should be specified, and versioning should be a set of experiments that we do to
figure out what to standardize, as it is a lot less straightforward.

* *Others*? Anyone else implementing transactions for Features API? pygeoapi? 


### Projections 

Another key extension for OGC API - Features and STAC is reprojection. CRS is actually the first [extension](https://github.com/opengeospatial/ogcapi-features/tree/master/extensions) 
in the features api repository. It doesn't feel finished, as there are a number of empty sections. The key
information can be found in the [clause 6 ascii doc](https://github.com/opengeospatial/ogcapi-features/blob/master/extensions/crs/standard/clause_6_crs.adoc). 

It is mostly concerned with the mechanics of CRS in the API. The STAC community has been more focused on the
content side, how items can report the CRS they are in, and also represent their footprints in alternative CRS's. A lot
of imagery data is stored in UTM, with many diverse projections, and it's convenient to give the bounds in both lat/long
and the native projection. See discussion on the [pull request](https://github.com/radiantearth/stac-spec/pull/485).


### Describing data

One of the biggest challenges for many clients talking to a OGC API - Features server is the lack of a 'schema' for the data, 
to be able to know what data it is about to receive. See [issue 56](https://github.com/opengeospatial/ogcapi-features/issues/56)
for a good description of the issue. 

It sounds like there has been considerable progress in OAFeat, using OpenAPI to also serve as the schema, and to also 
leverage OpenAPI to [represent alternate schemas](https://github.com/opengeospatial/ogcapi-features/blob/master/proposals/001_Alternative-Schema-Proposal.md) 
(like JSONSchema and XMLSchema). There does not yet seem to be consensus on the path - a dedicated /schema/ or just a link
from collections. Staccato also has a [schema endpoint](https://github.com/planetlabs/staccato#schema-endpoints) that
returns the JSON schema for a collection. Hopefully we can make clear progress on this issue, and get it added as a
well documented extension.

There has also been interest in several directions in a lighterweight approach - not describing the whole schema in a 
complicated way (like above), but in just providing 'summaries'. These tend to be the names of the fields and the potential
values (a range and/or type). See the 'summaries' section of the [STAC Catalog 
spec](https://github.com/radiantearth/stac-spec/blob/master/catalog-spec/catalog-spec.md#catalog-fields). This should enable
many clients to get enough information to populate their data structures and even fill in a GUI, without making implementors
have to fully describe in full validating detail their data.

In STAC we decided that both approaches have value, and should be optional in all cases. Would be great to have solid,
interoperable (like on path each) Features API extensions for both approaches.

### Meta-topics

#### Extension workflow

The CRS extension has a *ton* of files, but most of them aren't actually useful - they are boilerplate for OGC specs. Can
we have a few 'maturity' steps before it has to be turned into an official 'spec', where it is just markdown and easier
to edit and consume? Or else we should have automated builds that create the documents, and those documents should have 'edit'
buttons that take you straight to the relevant file. It's just too burdensome right now to quickly iterate between seeing
a problem in the spec and suggesting and improvement. Chuck is working on this, should make it a clear goal for the sprint
to get something in the official repos. 

#### Basing other standards on OAFeat

STAC has been struggling to find a good path to have its specification based on the OGC API - Features specification. It'd be
good to work to make things like STAC easier, where we make use of features and a set of extensions, along with more set
content types. It should be easy to 'build' a reference OpenAPI document from the various parts, and have it make sense.
Should brainstorm on how to make it easier, and also what a future looks like where many components are part of OGC Commons.
OGC API - Catalogues should likely be another opportunity to try things out, as it ideally is a Features API in the same way
STAC is - just adds on some extensions and required content types. 

#### Content extensions in OAFeat

Much of what STAC has made progress on is actually the content of features, not just the API. There is a robust community
of '[content extensions](https://github.com/radiantearth/stac-spec/tree/master/extensions)' that are just fields for people
to reuse. It'd be good to extend that type of collaboration beyond just STAC. The OGC has a robust history of doing this,
with all the \*ML groups (like WaterML, CityGML, etc). JSON encodings actually allow for more flexibility and upfront
definition, but we should figure out ways that a community of interest can easily set shared schemas (and indeed just
sets of fields that can be used and combined with others).

## STAC-specific Topics

### Path to 1.0

Establish a clear roadmap and release path to STAC Version 1.0. The main idea floating in the community is to separate out
the API specification from the core Item/Catalog/Collection constructs, that can be implemented statically or dynamically. 
That core is feeling quite solid, and this would allow the API specification to take the time to fully align with OAFeat, 
including all the relevant extensions reaching maturity. We should triage all the additional topics to decide if they
need to be done pre-1.0, and then likely start work on separating out the API specification.

### Common extensions in 'core extensions'

Another much discussed issue in STAC is that different extensions are using the same or very similar fields and concepts, and
it could help interoperability to just have them defined once, and then particular extensions can reuse them. This could be
done as another set of 'component' extensions, like 'satellite' that has constellation and orbit direction, that can be used
in SAR and EO extensions. We've wanted to wait until there was substantial use and real implementations, but that has 
happened.

We should also consider whether we should drop the prefixes for the ones we do feel are core, putting them in like the 
default namespace. This does open up a can of worms about adding in more in the future. But it could be useful to have
new users go to a single page that is part of the core spec that lists 20 or so terms that they can use immediately without
having to dig through all the extensions, judging their maturity, etc. 

### Root catalog placement in STAC API's

Since STAC's integration with OAFeat has been a somewhat muddled path, it is not super clear the best practice to make
a fully crawlable catalog that implements the core specification, while also implementing the WFS collection endpoints.
The most common interpretation seems to be that the root catalog references collections that then just have an 'items'
endpoint. But they miss the 'child' structure that allows a search engine to crawl all the way down. This crawlability 
is one of the key features of the STAC specification, but most API's don't allow it. 

One idea is to make an explicit 'browse' endpoint, that is designed to be fully crawled and exactly implements the STAC
core structure. If a server is implemented by ingesting static catalogs one could also see the browse endpoint just linking
off directly to the source data. 

In general we do need to invest more in making it so STAC Catalogs get crawled and show up on public search engines like 
google. STAC Browser has had some success in this, but we should pursue it more, and make sure large catalogs show up in 
search engines.

### Ensure top OAFeat concerns are met

* cross collection search, more powerful query, standard filter language (that is easy for nosql to implement), describing
data, transactions, aggregations.

### Versioning and provenance

We've made a very light attempt at a nod to provenance, with the derived_from field in core. But people are starting to 
need more. Ideally static catalogs have a recommended method to create a static catalog that also captures the history, like
creating new files when things are modified, and marking previous versions so people know they are the same. And then STAC
API's should be able to import and stay in sync with a versioned static catalog, but have more sophisticated API mechanisms
to request particular versions. 


### STAC Label Extension

* Lots of good energy on this at the last STAC sprint - what do we do next?
* Would be awesome to at least have a demo of a STAC Item with Label extension that is powered by WFS requests instead of static.

## Additional OGC Topics

### Static OGC Features

* What's the equivalent to a static STAC? 
* OGC Collection (in Commons repo), plus link to geopackage / geojson(+newline+cloud-optimized?) / avro (w/ wkb) - for bigquery import
* Make OWC:Context and OWC:Resource (https://docs.opengeospatial.org/is/14-055r2/14-055r2.html#14) consistent with the minimal Feature requirements from OGC API Features (e.g. "self" link, "id" not a URI, Link model, "rel" attribute of link, $.links instead of $.properties.links) for use as static features.

### OACat

OGC API - Catalog(ue) aka CAT4 aka OACat. SWG is formed, should align with all these efforts well. Someone from the
community please help fleshing out a page with top topics to discuss, and relevant links of work done.

* As part of EOPAD activities in Testbed-15, several catalog endpoints serving a.o. EO application/services metadata were setup by participants which combined OGC API Common and OpenSearch (OGC 13-026r8).  See the ER at  https://portal.opengeospatial.org/wiki/pub/Testbed15/ConvertDocsOutputTestbed15/testbed15/T-15-D010-Catalog_ER.pdf for details.  DataBio endpoint available at https://databio.spacebel.be/eo-catalog/.
