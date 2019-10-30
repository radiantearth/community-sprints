# Staccato Implementation Details

## Query
Staccato has never been compliant with the proposed Query extensions.  Since before any official query extension was proposed/published, Staccato has implemented CQL query filters.  A version of this implementation was deployed at customer sites and has been very successful in allowing users to quickly construct complex queries and easily share links to these queries without the need to construct difficult-to-read GET URLs containing JSON strings in request parameters.  Staccato does not currently implement the proposed JSON query structure for POST requests, as the CQL implementation seems to be simpler and just as effective.  Once the final specification stabalizes, Staccato will be updated accordingly.

Staccato is a Java application using Elasticsearch on the backend.  Originally it used the GeoTools ECQL library, but there were many nuances that prompted a significant amount of customization.  As a result, Staccato switched to use the [xbib CQL library](https://github.com/xbib/cql), which only supports standard CQL.

It is interesting to note that query parameters are assumed to be property fields.  Querying root-level fields is not supported.  This can be a bit confusing as the Fields and Sort extensions do support root-level properties.  This means a CQL filter such as `?query=id any "1 2 3"` is not supported and using a mix of URL parameters that use different specifications looks a bit odd, eg: `?query=myProp>100&fields=id,properties.myProp`. 

### Query Sample Requests:

* Landsat scene LC82030282019133LGN00
GET https://stac.boundlessgeo.io/stac/search?query=landsat:scene_id=LC82030282019133LGN00

* Any item where `eo:instrument` starts with `OLI`
GET https://stac.boundlessgeo.io/stac/search?query=eo:instrument=OLI*

* Landsat items in path 153, 154, or 155 (with fields restrictions and limit)
GET [https://stac.boundlessgeo.io/stac/search?query=landsat:wrs_path any "153 154 155"&fields=properties.landsat:wrs_path&limit=2000](https://stac.boundlessgeo.io/stac/search?query=landsat:wrs_path%20any%20%22153%20154%20155%22&fields=properties.landsat:wrs_path&limit=2000)

* Cloud cover less than 0.1, Landsat row 28, Landsat path 203
GET [https://stac.boundlessgeo.io/stac/search?query=eo:cloud_cover<0.1 AND landsat:wrs_row=28 AND landsat:wrs_path=203](https://stac.boundlessgeo.io/stac/search?query=eo:cloud_cover%3C0.1%20AND%20landsat:wrs_row=28%20AND%20landsat:wrs_path=203)

* Cloud cover equal to 0.1 or 0.2 (with fields restrictions and limit)
GET [https://stac.boundlessgeo.io/stac/search?query=eo:cloud_cover=0.1 OR eo:cloud_cover=0.2&fields=properties.eo:cloud_cover&limit=2000](https://stac.boundlessgeo.io/stac/search?query=eo:cloud_cover=0.1%20OR%20eo:cloud_cover=0.2&limit=2000&fields=properties.eo:cloud_cover)

* Cloud cover between 0.1 and 0.2, Landsat row 28, Landsat path 203
POST https://stac.boundlessgeo.io/stac/search

```
{
    "query": "eo:cloud_cover>0.1 AND eo:cloud_cover<0.2 AND landsat:wrs_row=28 AND landsat:wrs_path=203"
}
```

## Fields
Staccato implements the fields extension as [currently proposed](https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/fields).  The extension makes use of mixed syntax for GET and POST queries.  The POST syntax is self-explanitory.  The GET syntax uses an array of item field names.  When this property is defined, only the field names listed will be included in the response.  When a field name is prefixed with `-`, the field will be excluded from the response.

### Fields Sample Requests:

* Include only the `id` field:
GET https://stac.boundlessgeo.io/stac/search?fields=id

* Exclude the `id` field:
GET https://stac.boundlessgeo.io/stac/search?fields=-id

* Include only the `id`, `bbox`, and `type` fields:
GET https://stac.boundlessgeo.io/stac/search?fields=id,bbox,type

* Exclude `properties.datetime`
POST https://stac.boundlessgeo.io/stac/search
```
{
    "fields": {
        "exclude": [
            "properties.datetime"
	]
    }
}
```

* Include only the `id` and `geometry` field:
* POST https://stac.boundlessgeo.io/stac/search
```
{
    "fields": {
	"include": [
	    "id",
            "geometry"
	]
    }
}
```

## Other Interesting Bits

* At the FeatureCollection level, OAF defines the fields `numberMatched` and `numberReturned` (camelCase, oh my!).  Stac defines it's own fields in the `search:metadata` object, [as defined here](https://github.com/radiantearth/stac-spec/tree/master/api-spec/extensions/search).  Staccato currently implements both until a final decision is made.

* Staccato implements a root-level landing page (https://stac.boundlessgeo.io) that provides OAF endpoints, as well as the "STAC" landing page at https://stac.boundlessgio.io/stac that provides sub-catalog and search links, as well as OAF collections link.

* Staccato does not currently support query parameter limits:  http://docs.opengeospatial.org/DRAFTS/17-069r3.html#_parameter_limit

* Staccato does not currently support open ranges (eg the `..` syntax) for datetime queries:  http://docs.opengeospatial.org/DRAFTS/17-069r3.html#_parameter_datetime

* From Even Rouault: For a OGR or QGIS client point of view, accessing a formal schema describing the properties of a collection would be ideal. OGR or QGIS use a fixed schema for features of a layer. So for now, the OGR driver fetches the first page of features of the collection and analyses the geojson features to guess the schema. But this might be error prone if by bad luck, those features lack properties that are going to be in later features, or if the type has been badly guessed (the first values only contain integer values, but later features contain floating-point numbers) or could not be guessed (only null values for example). The OAPI-F spec suggests that a collection description could include a link "rel":"describedBy" to a JSON Schema.


