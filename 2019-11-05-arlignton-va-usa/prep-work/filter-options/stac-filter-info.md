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

The most interesting piece is likely how it was designed to be quite extensible. So more geometry, time, logical and array 
options could easily be added, with just inserting more openapi fragments. The idea of making a relative concise core with a
set of easily defined extensions (and hopefully a community of interest to define them), is likely one of the ideas most
worth preserving if another route is chosen. 

**Note**

It should be noted that the STAC community is not super tied to the initial solution - it's not at 1.0 and doesn't necessarily
need to move forward if there is something that is more standardized as a key OAFeat default. But new API implementations
have found it can be implemented in 1-2 days, so was generally felt to be quite powerful, while also being easy to implement.


#### Links

* https://github.com/radiantearth/stac-spec/blob/v0.6.2/api-spec/filters.md is probably the fullest explanation, and some
of what is talked about there fell off in the 0.7.0 re-orginization. 
* https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/query is the latest specification piece.


### Considerations

* **POST vs GET** was discussed extensively, and it has felt like there is no great solution. It was important that GET and POST
did not each require their own parser, and that one is clearly marked as 'required', so that every client implementation could
expect that one to be there. POST was selected as the required one, as it doesn't have the browser size limitations, which
are pretty easy to hit if you're doing a geometry operation against any reasonably complex geometry. There was an 
acknowledgement that POST in a pure REST reading is just for creating new objects, but the semantics of the STAC POST is on a 
/search/ resource, so it can be thought of us POSTing to create an implicit search object that is then read right away with a 
GET. It seemed onerous to require users to POST a new search object and then request it back in a GET. This argument obviously
works less well on collections endpoints directly.

* **Work well with nosql / document stores** - Most of the catalog implementors who contributed to STAC were using 
elasticsearch, with a number of other nosql stores mixed in, along with some postgis. So the STAC filtering drew directly
on elastic and mongodb syntaxes, and inherited their features and limitations. Other solutions should likely be sure that
any required constructs very easily map in nosql stores. 

* **JSON** - JSON is generally seen as the goto format for modern web apis, so there are clear wins using it, as most every
developer will grok it pretty easily. The STAC community isn't so set on the exact syntax that was created, but having some
option for filtering that is json based is likely a win.

* **Powerful and extensible** - As mentioned above the STAC community would prefer that there's a solid OGC API filter and 
query that can just be used. STAC desires the 'right' amount of simplicity vs power, and that is roughly expecting an rbdms or 
nosql backend, but not going overboard with tons of options. The core filter should be quite easy to map into any reasonable
backend, but STAC use cases include logical property comparisons in its very basic use cases - return all images with 
resolution under 5 meters and under 20 percent cloud cover. Ideally there is a clear core for interoperability, as well as
good extensibility for more advanced geometric, string and time operations.

* **Multiple collection query** - This is more at the 'query' level, but it should be mentioned that at the filter level it
should be possible to use 'shared' properties (in STAC case these are community defined), and behave properly with the other
fields being mixed. Like we should be able to query across heterogeneous collections, as long as they share the properties 
being queried. 

* **Exploring CQL / GET options** - At the last STAC sprint there was enthusiasm for pure GET stuff, to make the API more
'explorable' by people just using a browser. A lot of this was more at the query level, like using 'fields'. Interestingly
Staccato actually never implemented the POST filter query stuff, since its very early implementations used CQL, and that
worked well enough for its users. See [staccato-impl.md](../staccato-impl.md) for more information.


### Examples

1. Floors greater than 5
```
{
  "query": {
    "floor": {
      "gt": 5
    }
}
```

2. Taxes less than or equal to 500
```
{
  "query": {
    "floor": {
      "lte": 500
    }
}
```

3. Owner name contains 'Jones'
```
{
  "query": {
    "owner_name": {
      "contains": "Jones",
    }
}
```

4. Owner name starts with 'Mike'
```
{
  "query": {
    "owner_name": {
      "startsWith": "Mike",
    }
}
```

5. Owner name does not contain 'Mike'
```
{
  "query": {
    "not" {
      "owner_name": {
       "startsWith": "Mike",
    }
  }
}
```
*speculative - NOT's have not been specified. Generally taking inspiration from OGC filter spec*

6. A swimming pool
```
{
  "query": {
    "swimming_pool": {
      "eq": "TRUE",
    }
}
```
(not sure that this is actually specified)


7. More than 5 floors and a swimming pool
```
{
  "query": {
    "swimming_pool": {
      "eq": "TRUE",
    },
    "floor": {
      "gt": 5
    }
}
```

8. A swimming pool and (more than five floors or material is brick)
```
{
  "query": {
      "swimming_pool": {
        "eq": "TRUE",
      }, 
      "or":{
        "floor": {
          "gt": 5
      },
      "material":{
         "startsWith": "brick",
         "endsWith": "brick"
    }
}
```
*Speculative - or's and logic order has not been specified yet. And I dont think we have string equality, and that example
could match 'brickbrick', so probably should put something more speculative there.*

9. (More than five floors and material is brick) or swimming pool is true
```
//TODO: make a speculative OR query
```
*Speculative - or's and logic order has not been specified yet*


10. Not under 5 floors or a swimming pool
```
//TODO: make a speculative NOT query
```
Or's, Not's and logic order has not been specified yet - should find a good inspiration.

**TODO: update the rest**


11. Owner name starts with 'mike' or 'Mike' and is less than 4 floors
```

```

12. Built before 2015
```

```

13. Built after June 5, 2012
```

```

14. Updated between 7:30am June 10, 2017 and 10:30am June 11, 2017
```

```

15. Location in the box between -118,33.8 and -117.9,34 in lat/long (geometry 1)
```

```

16. Geometry that intersects with geometry 2 (below)
```

```

17. More than 5 floors and is within geometry 1 (below)
```

```
