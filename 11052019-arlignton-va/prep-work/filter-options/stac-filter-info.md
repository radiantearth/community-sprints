## STAC API filter language

### Overview

The STAC community has tried to always stay in line with WFS3 (OAFeat), but from the beginning the most common STAC searches
needed more than the core specification offered. The community evaluated the existing array of options, but found nothing
that matched the ease of implementation and power that were sought. So decided to create something new, mostly inspired
by elasticsearch / mongodb style queries, as document store backends were already popular among those standing up production
imagery catalogs. 

It is pure JSON, and uses the same JSON structure for POST and GET. POST is the required end point, to be sure it handles
huge geometries well (more discussion in considerations section below), and GET is an optional implementation. Clients include
the exact same JSON string for the GET, which is reminescent of OGC filter in WFS, where one would include the filter xml 
directly.

It comes with the standard number comparisons, plus 4 string operators - startsWith, endsWith, in and
contains. Time and BBOX filtering were to be done with the exact same mechanism as OAFeat, but wrapped in JSON for POST
operations. Time additional has a 'duration'. By default compound statements would be AND'ed together logically

The most interesting piece is likely how it was designed to be quite extensible. So more geometry, time, logical and array options
could easily be added, with just inserting more openapi fragments. The idea of making a relative concise core with a
set of easily defined extensions (and hopefully a community of interest to define them), is likely one of the ideas most
worth preserving if another route is chosen. 

#### Links

* https://github.com/radiantearth/stac-spec/blob/v0.6.2/api-spec/filters.md is probably the fullest explanation, and some
of what is talked about there fell off in the 0.7.0 re-orginization. 
* https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/query is the latest specification piece.

**Note**

It should be noted that the STAC community is not super tied to the initial solution - it's not at 1.0 and doesn't necessarily
need to move forward if there is something that is more standardized as a key OAFeat default. But new API implementations
have found it can be implemented in 1-2 days, so was generally felt to be quite powerful, while also being easy to implement


**TODOs**

So worked some on an option, though it wasn't designed
to be *the* solution, but more to advance the dialog

staccato note


considerations

post vs get - json so that it doesn't need to be parsed, Though POST in a pure REST sense is just for creating new objects, the semantics of this POST is on a /search/ resource, so it can be thought of us POSTing to create an implicit search object that is then read right away with a GET. It seemed onerous to require users to POST a new search object and then request it back in a GET.

work well with nosql datastores

decision making

how powerful - needs more than what is in OAFeat, but needs to be easy to implement.
