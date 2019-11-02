## OGC CommonQL

### Overview

OGC's CommonQL (aka CQL / Common Query Language, though the [parent spec](https://www.loc.gov/standards/sru/cql/) 
is now referred to as Contextual Query Language) is based on a library information retrieval standard that 'tries to 
combine simplicity and intuitiveness of expression for simple, every day queries, with the 
richness of more expressive languages to accomodate complex concepts when necessary.'

OGC added in the ability to use Well Known Text the 11 geometry filter operations (9 comparisons, plus beyond + dwithin), 
and the result is a pretty intuitive little language for filters. It has never really been promoted outside of the catalog
specification, where its definition is quite buried. There is no official specification for using it in a WFS, but 
a number of servers do, including GeoServer - the open source reference implementation for WFS 1 and 2.

#### Links

* [OGC
CommonQL](https://github.com/opengeospatial/ogcapi-features/tree/master/extensions/cql) is now in the OAFeat 
'extensions' folder. It includes a BNF for CQL that is intended to supersede the BNF from the
[CSW 3.0 specification](http://docs.opengeospatial.org/is/12-168r6/12-168r6.html).
It is meant to be somewhat backward compatible with the CSW CQL but it
also extends that CQL to support the full set of spatial and temporal
operators that are supported in OGC filter.  It also support stuff like
logically connected predicates, regular expression searching (i.e. LIKE)
and functions/methods, etc. Since we don't yet have a document
describing this updated CQL, I (pvretano@cubewerx.com) have added
comments to the cql.bnf file to help understand what is going on.  This
work may start life as an extension to OGC API - Features but ultimately
it may end up in OGC Common because it is likely that a number of OGC
specifications will need this functionality.
* [CSW 3.0 specification](http://docs.opengeospatial.org/is/12-168r6/12-168r6.html) - the Annex B that actually contains the
formal BNF definition does not have a link, go to http://docs.opengeospatial.org/is/12-168r6/12-168r6.html#62 and then scroll down a bit.
I believe this is the official definition, and you can see it's not too developer friendly.
* [GeoServer CQL Tutorial](https://docs.geoserver.org/latest/en/user/tutorials/cql/cql_tutorial.html) and 
[ECQL Reference](https://docs.geoserver.org/latest/en/user/filter/ecql_reference.html#filter-ecql-reference) is the best 
overview I could find online. GeoServer extends the core standard a bit for more flexibility, like encoding ID's and not
requiring attributes to be on the left side.
* [Wikipedia Contextual Query Language](https://en.wikipedia.org/wiki/Contextual_Query_Language) article, on the parent standard.
* [Official CQL Spec](https://www.loc.gov/standards/sru/cql/)?
* [OASIS CQL Spec](http://docs.oasis-open.org/search-ws/searchRetrieve/v1.0/os/part5-cql/searchRetrieve-v1.0-os-part5-cql.html) (maybe more used? Seems to be java library support of it)
* [OGC Testbed 14 report on CQL as a query option](https://docs.opengeospatial.org/per/18-021.html#cql) - this was a report
on more complex query requirements for features API, and includes a nice overview of CQL, as well as sample queries for the
more complex requirements being considered.



### Considerations 

**Clearer Spec** - One of the biggest problems with CQL is how buried any information about it is. The main task to make
use of it as the core OGC API filter language would be make it an independent spec, part of the OGC API baseline. This should
solve that main concern, and give us freedom to solve other concerns. Hopefully we could get a draft spec proposal during
the sprint.

**NoSQL Backends** - One of the major concerns about CQL is that it was designed more for relational databases, so 
we are less sure of how well document store / nosql backends work with it. [Staccato](https://github.com/planetlabs/staccato)
is a STAC API implementation that is backed by elasticsearch and implements CQL, so should be a good test. Ideally we have
some others also test with OGC CQL as well. This could result in a more abbreviated 'core' of CQL, with some extended optional operations.

**Geometry + Other advanced Operations** - Related to the above point, CQL specifies 11 geometry operations, including more obscure ones like 
CROSSES and BEYOND that many of the more recent geospatial backends (like [BigQuery](https://cloud.google.com/bigquery/docs/gis-data#using_joins_with_spatial_data)
[MongoDB](https://docs.mongodb.com/manual/reference/operator/query-geospatial/) and [Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-geo-shape-query.html).
See [backend spatial support overview](backend-spatial-support.md) for more. There are also a lot of time options, that
are more extensive than many backends support (though arguably they wouldn't be that hard to code up). 
We should consider subsetting the full power in favor of a set that most all the backends we can imagine would support without 
too much trouble. What is the set of CQL operations that make sense in a 'core', and then how do we put in extension points
and specify additional operations?

**Well Known Text spec** - Similar to CQL, the [Well Known Text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) (WKT) 
format that CQL uses is buried in specs - behind an ISO paywall seems to be the official, or buried in Simple Features for SQL
specification. So it should likely be elevated to be its own baseline OGC API specification as well.

**GET vs POST** - Most uses of CQL have been in GET strings, but the problem with GET is that large geometries can hit
browser limits. So do we allow POST of the same CQL if it's too big? Or adopt some other strategy?

### Examples

CQL just specifies the WHERE clause, so it does not need its own endpoint or fuller query. Using the same notation that 
Clemens did in the testbed report will be like:

```
/collection/buildings/items?where-lang=cql-extended&where=floors > 12
```

For examples we will just concentrate on the 'where', so the above will be:

1. Floors greater than 5
```
floors > 12
```

2. Taxes less than or equal to 500
```
taxes <= 500
```

3. Owner name contains 'Jones'
```
owner_name LIKE '%Jones%'
```

4. Owner name starts with 'Mike'
```
owner_name LIKE 'Mike%'
```

5. Owner name does not contain 'Mike'
```
owner_name NOT LIKE '%Mike&'
```

6. A swimming pool
```
swimming_pool = TRUE
```
(not sure about that one)

7. Less than 5 floors and a swimming pool
```
floors < 5 AND swimming_pool = TRUE
```

8. A swimming pool and (exactly five floors or material is brick)
```
swimming_pool = TRUE AND (floors = 5 OR material LIKE 'brick')
```
(not 100% sure on this one, if you have to do like, or can do a string =.

9. (Five floors or more and material is brick) or swimming pool is true
```
(floors >= 5 AND material LIKE 'brick') OR swimming_pool = TRUE
```

10. Not under 4 floors or under 5000 in taxes
```
NOT( floors < 4 OR taxes < 5000)

```

11. Owner name starts with 'mike' or 'Mike' and is not 3 floors
```
(owner_name LIKE 'mike%' OR owner_name LIKE 'Mike%) AND floors <> 3
```
Note - GeoServer can do strToLowerCase(owner_name), but it is a 'filter function', so not part of CQL spec

12. Built before 2015
```
built BEFORE 2015-01-01
```
Note - I'm not actually sure if CQL 'rounds' time, or if you have to specify an exact time

13. Built after June 5, 2012
```
built AFTER 2012-06-05
```

14. Updated between 7:30am June 10, 2017 and 10:30am June 11, 2017
```
updated DURING 2017-06-10T07:30:00Z/2017-06-11T10:30:00Z
```

15. Location in the box between -118,33.8 and -117.9,34 in lat/long (geometry 1)
```
INTERSECTS(footprint, ENVELOPE(-118,33.8,-117.9,34))
```

16. Geometry that intersects with geometry 2 
```
INTERSECTS(footprint, POLYGON((-118.023 34.068, -118.039 34.079, -118.041 34.075, -118.033 34.072, -118.042 34.072, -118.043 34.069))
```

17. More than 5 floors and is within geometry 1 
```
floors > 5 AND WITHIN(footprint, ENVELOPE(-118,33.8,-117.9,34))
```
