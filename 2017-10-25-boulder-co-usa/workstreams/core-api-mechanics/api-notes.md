# GOALS
(no notes on new ones)


# NON GOALS
 * Publishing / Modifications
 * counting results
   * some implementations may need to iterate across the result set in order to count hits
 * wfs style pagination
   *offset style pagination can create a burdon on implemetions vs a continuation parameter (next in links). next can style use offset internally, but does not push that decision onto the implementor

 
## QUESTIONS TO DISCUSS
 * how to coherently represent different collections across apis
 * how to represent schema
 * query api - we may want to adopt an existing standard for querying
   * Filtering grammar
 * differences between tabular and imagery data sets
 * what are the use cases
   * slippy map + clip and ship
   * scraping - extensions
   * monitoring - show me things in this aoi
     * may not know what they are looking at, want to query across collections
   * Find out what's there - core
     * archaeologist wants to see what's in the location
   * exploratory analysis, want to find aois that fit some criteria - core
     * want to find aois where i can use coreferenced data sets
   * Aggregate results from multiple catalogs
   * Understand how to use the API
   * Lightweight clients
     * Using JSON API (style?)
   * api mechanics - like _next _previous as part of standard
     * json-api could be a good source of opinions/standard 
   * How is this different from WFS
   * is geo-json a stable standard -- do we embrace new geo-json?
   * do we talk about projections in catalogs
   * we can shield end-users from projections by assuming all the gemetric operations are in one projection
     * pick good defaults
     * handle projections as extensions?
   * versioning - the version of an item is part of it's identity in the real world - is it part of its identity as well? does this belong in core.
   * collection metadata - should the collection itself have metadata that describes
     * is the collection 1:1 w/ a schema of feature properties?
   * schemas could be embedded in responses, making them self-describing, but this could be a burdon on implementors


## NOTES
   * FeatureCollections are a great response type
   * json-schema featurecollections are used as a container because they can be natively loaded by eg qgis
   * properties is assumed to contain the 
   * schema as sibling to properties


## ROUGH API SKETCH
 * /items
   * GET - Retrieve Items matching filters
     * Sorting
       * TODO
     * Filters
       * arbitrary property filters?
       * boolean combinations (and scoping parens)? (Recommend for advanced extension)
       * bbox
       * geojson 
       * type (The item type)
       * time_min
       * time_max
     * Paging
       * TODO
       * page_size
       * nextPage token
         * May have zero-result size with nextPage token
         * For next page: Respond with same query plus nextPage token
     * Response
       * items - array of Items (See description below)
         * Link to self
       * next - link to next page or body of POST request to get next page
       * previous - link to previous page or body of POST request to get next page
    * POST - Search for items matching filters that may exceed URL lengths
       * Form encoded parameters in the same style as GET
 * /items/{id}
   * GET - Retrieve item by id
 * /types
   * GET - Retrieve all types
 * /types/{id}
   * GET - Retrieve a type
 * /extensions
   * GET - Returns a set of extensions that are supported. 
     * Potentially an association between extension name and the types that supports the extension?
 * Core Types
   * Item
     * id
     * footprint
     * type
     * time_range
     * extensions??
       * Map of unique extension names to data associated with extension??
     * attributes
       * Type specific attributes
 * Item Types
   * Image
     * ~~Spatial~~ (Part of item)
     * ~~Temporal~~  (Part of item)
     * URL to image
     * spectral
     * quality (cloud cover, etc)
     * Access (cost, logistics, ...)
   * RelatedImages (aka Collection, ImageGroup, Aggregates)
 * ID is unique to the catalog, but does not have any constraints on format
   * Alternative: format constrained to a-zA-Z0-9[-] \(url safe\)
 * Extensions
   * Filters Extensions
     * Boolean logic (AND, OR, NOT) of conditions
     * Text
     * Temporal Predicates (Before, During, After)
  * Possible Type Extensions
    * Sensor
    * Tile
 * Access Methods - core defined a few required access model, like download
   * extensions that can specify additional access methods, like activation, or tiling
 * thumbnails part of the core api - optional url in the response?
 * collection vs item types - gsd may not be uniform for all items in a collection


#### Open Questions
 * What kinds of ids do we have? Do we have system defined ids and user defined ids? Are ids unique within a group?
 * Should the API provide authorization and access control? Extension?


#### Reference Info: 
 * PIXIA Types:
   * String A text string
   * Text A text string with text-search index
   * Integer 32-bit integer
   * Long 64-bit integer
   * Float IEEE double-precision floating-point number
   * Time A timestamp with millisecond precision
   * StringSet A set made of text entities
   * IntegerSet A set made of integers
   * TimeRange A time range with begin and end
   * IntegerRange A integer range with begin and end
   * FloatRange A floating-point range with begin and end
   * Doc Document storage, implemented as CLOB or JSON depending on database
   * Geo Geospatial field
   * ECQL: http://docs.geoserver.org/latest/en/user/filter/ecql_reference.html
