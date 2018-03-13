## Overview

This session discussed how to merge STAC with the latest from WFS 3.0. Raw notes taken from http://board.net/p/wfs-stac

After participants were exposed to the WFS 3.0 specification many realized that it's quite close to what STAC does. So 
this session was convened to figure out exactly how to make it so STAC fully implements WFS. Most everyone felt it should
be possible, but needed to sit down and see what changes were needed for each.

The overall thought was that STAC should be an opinionated implementation of WFS, plus a set of extensions. So a STAC compliant
server should also be compliant with WFS. But a user of STAC server could make a few more assumptions. Like they can rely
on GeoJSON as a format, and openapi as the spec description, and the way of doing content negotiation. Basically make some
more concrete decisions.

#### Changes to each spec

The group went through the endpoints of each spec. For WFS this was assumed to be the new structure discussed the previous day
which is detailed in [WFS Issue #64](https://github.com/opengeospatial/WFS_FES/issues/64). Thankfully this has already been
adopted, so it is the right basis of comparison. 

On the STAC side it was decided to kill the 'next' parameter, to just follow what WFS does, with an optional startId (still
needs to be put in a WFS extension). And the two specs also called one parameter differently, though it's functionality
was the same - count vs. limit. The STAC group was fine to change it to 'count', but felt limit was a bit more in line
with the meaning. It's a client request, and the server may answer with less. And 'count' is also a potential 'resultType'
response. This was brought up with the core WFS editors, but they agreed with the semantics, and were happy for [an issue](https://github.com/opengeospatial/WFS_FES/issues/78)
to change 'count' to 'limit' in WFS3, which has been accepted.

On the WFS side, the group was working with information that was a bit outdated. So there was desire to get rid of a few
WFS parameters, like the 'f' parameter for format. But when the WFS editors were brought in they said that most all the
changes desired had already been changed, so it was all quite ready to go.

STAC does add a 'time' parameter, which is not in the WFS specification, so that can be a STAC extension, though there is 
also discussion of adding it to WFS as well. 

The other major difference between STAC and WFS collections is that STAC enables cross collection search. This was felt to 
be quite important, as users of imagery catalogs want to search all the holdings - they don't want to have to search a 
'landsat' endpoint and a 'sentinel' endpoint or even endpoints for different landsat missions. So STAC carved out a 
```/stac/``` endpoint where one could do a filter against the core stac fields and return results from any collection that was
'stac compliant'. Content profiles could be done under that endpoint to, like ```/stac/eo/```, which would do cross collection
search of any collection implementing the EO profile. 

Talking to the WFS editors they thought we should put it under a ```/search/stac/``` endpoint, as they want to sort out
a 'search' extension before too long, and are happy to share ideas.

So a STAC implementation would be an OpenAPI snippet for the cross catalog search, plus a set of recommendations for how
to do the core WFS implementation. A follow-up session the next day (notes at [stac-api.md](stac-api.md)) went deeper
in to some of these issues and got to a very solid place.

## Raw Notes 


STAC API is close to core of WFS.

Cloud STAC be a profile of WFS 3.0? Most likely -- a profile being a set of extensions

Walk through WFS core API and stac api and reconcile the differences.

Haven't been thinking much about schema and metadata model of it. But Kasey has more.

Goal: Issues on WFS and STAC repos

#### STAC Dynamic API
```
/api

/items/{id}

/items/ (query endpoint)

 bbox
 time
 filter
 limit
``` 
 
#### WFS

```
/api - 
/ - 
/collections
/collections/{collectionId} -- e.g. /collections/landsat8, /collections/sentinel2
/collections/{collectionId}/items
/collections/{collectionId}/items/{itemId}
/collections/{collectionId}/schema
```

WFS has collections, which are a particular feature type. STAC is more flexible on return type.

Namespace collision right now. STAC name for all stuff is 'items'. But /collections/items/items/id 


Kasey proposes using /stac as the extension route -- would emphasize heterogeneous collections

stac/ becomes search end point. Can search across end point. Move id to collection.

/stac/items? Or kill items? kill items.

/stac/search - not paint ourselves into a corner.

Boundless /api/{type} return json schema for item properties. Those would go to collections EO.

Discussion over usefulness of returning everything vs particular types.

Idea is that /search lets you see everything. And /collections/ are strongly typed. And you can have /stac/{ext}/search

collection says 'I implement these stac types' - EO extension.

Content extension mechanism. STAC can be more opinionated. 

Core consensus on STAC as just 'using' collections as strongly typed, and then a /search endpoint that is heterogenous.

'next' - not in WFS. Do we need it in STAC?




#### WFS TODO's:

* f? - kill
* /search/ - where do we put /stac/ end point? 
* file issue on 'limit' instead of 'count'

####STAC TODO's:

* limit change to count?
* kill next


STAC response.

Extensions to stac for authoring / transactions.


*****

Temporal discussion - definitely want a temporal extent. Do we make a 'time' parameter at the level of BBOX?
 - iso 8601 is basis of both. 
 
 syntax of time range / bbox
 is bbox totally inclusive. In WFS it's not disjoint. 
 3d bbox? No, you want more control over time.
 If you come from geoapi backgrounds you understand bbox. If you see bbox and time you may not understand
 makes sense to keep it separate, as lots of data doesn't have time.
