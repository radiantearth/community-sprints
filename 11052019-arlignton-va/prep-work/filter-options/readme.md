## About

One of the major topics at the sprint is to align and make progress on a recommended filter language. The Features API core
has very lightweight filters, but many users want more. STAC has pushed ahead with its own query, while others have adapted
CQL to meet their needs, and experimented with GraphQL.

This space should be used as proposals for those at the sprint to consider. This should help us to hit the ground running, so
that the time is spent examining differences and filling gaps, instead of just trying to commuicate core ideas. Each file
in this directory should be a deep examination of a filter option, so that everyone participating can get a full idea of what
it offers, and what needs improvement. We welcome new ideas, so don't hesitate to add a new option that you'd like to bring to
the table, just be sure to flesh out all the sections and examples that the others have.

Note that we don't need to fully align on exactly **one** filter language, indeed the Features API specification makes it 
quite easy to swap out different ones. But to increase interoperability we should aim for one that can be recommended as the
first one implementors should consider. STAC will likely fully adopt it as required. And we should propose it to be a
'building block' for OGC API's, perhaps even a part of the Commons spec.

## Filter Goals

*The following are draft goals - if any are controversial move them to 'stretch goals'*

* Handle common comparisons for numbers - greater than, greater than or equal to, etc.
* Have at least basic string handling capabilities - starts with, ends with, contains
* Handle logical filters (AND / OR / NOT) so that users can combine other comparisons for more powerful requests
* Handle time to the level that the core Features API spec does (so they can be used in logical filters)
* Supports geometry comparisons - at least intersects/bbox
* Is easily specified and validated, the full core specification should be a few pages
* Draws at least inspiration from existing filtering options that many people know / understand


**stretch goals**

Some of these goals should explicitly be in 'extensions' to the core filter specification, so that we have clear specification
of them, but don't require immediate understanding by all users looking at the filter language for the first time.

* Has a mechanism to handle large geometries (larger than can fit in a GET request)
* Support all 9 geometry comparison operations - EQUALS, DISJOINT, INTERSECTS, TOUCHES, CROSSES, WITHIN, CONTAINS, OVERLAPS, RELATE, DWITHIN, BEYOND
* Advanced string handling capabilities - regular expression or ? 
* Advanced time capabilities
* Querying features based on properties of related or nested objects or structured data types (one level & several levels)
* Access to and query of solid geometries and other geometries in a 3D CRS
* Accessing different versions (including historic representations) of features


## Example operations

These are the operations that potential implementations should write up so that everyone can get a sense of how they are used.

Let's assume a building example like in the core Features API spec, but with a few additional fields:

(todo, put in a table)

| Property  | Type | Example|
|-----------|------|---------|
| function | string | "public use" |
| material | string | "brick" |
| owner_name | string | "Mike Jones" |
| floors   | int | 10 |
| swimming_pool | boolean | true |
| taxes    | float | 3404.23 |
| built  | datetime |  2013-12-03T10:15:37 |
| updated | datetime | 2018-10-13T11:23:21 |

Return all buildings with:

1. Floors greater than 5
2. Taxes less than or equal to 500
3. Owner name contains 'Jones'
4. Owner name starts with 'Mike'
5. Owner name does not contain 'Mike'
6. A swimming pool
7. More than 5 floors and a swimming pool
8. A swimming pool and (more than five floors or material is brick)
9. (More than five floors and material is brick) or swimming pool is true
10. Not under 5 floors or a swimming pool
11. Owner name starts with 'mike' or 'Mike' and is less than 4 floors
12. Built before 2015
13. Built after June 5, 2012
14. Updated between 7:30am June 10, 2017 and 10:30am June 11, 2017
15. Location in the box between -118,33.8 and -117.9,34 in lat/long (geometry 1)



**Geometry 1**
```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -118,
              33.8
            ],
            [
              -117.9,
              33.8
            ],
            [
              -117.9,
              34
            ],
            [
              -118,
              34
            ],
            [
              -118,
              33.8
            ]
          ]
        ]
      }
    }
  ]
}
```

