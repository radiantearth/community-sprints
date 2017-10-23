### Overview

The main task of this group is to make sure that the core API has the proper extension mechanisms and core reusable components 
to apply to other problems. This should be a brainstorm, drawing on the types of options and services that might extend the 
core. Each does not need to be its own OpenAPI spec, but should be able fleshed out enough to figure out what extension points 
the core spec needs. And this group should also generally investigate how to report the 'capabilities' of a service that 
provides more than the core. A starting list of extensions would be transactions, statistics/aggregation, 'activation' of 
assets, coverage maps and additional metadata fields.

### Goals

**Day 1:** Get to a comprehensive list of related services people have created and prioritize which ones could make sense to standardize soon. Think through what type of extension mechanisms and granular components for parallel services will make sense.

**Day 3:** Ensure the core imagery catalog API has the proper extension points and/or granular components to support the types of services people would like to build around the core API. Potentially specify one or two extensions or parallel services. Like 'stats' might be a parallel services that uses the same 'query' mechanism, but responds differently.

**Stretch goals / Follow up:** Build 3 or more related or extended services that use the core spec or its granular components and take it past its originally functionality. This could be taking an existing service, like Planet's [stats enpoint](https://www.planet.com/docs/api-quickstart-examples/step-1-search/#stats), coded to be in line with the core open spec concepts (reuse query / filter, etc), as its own microservice. Or it could be an 'extension' to the core service, like an alternate return type to the core imagery catalog that returns stats, or GML, or a shapefile. Each service built should document itself in OpenAPI (but doesn't necessarily have to be standardized yet).

 
### Questions to discuss

* Extension mechanisms - how can we let the core service be extended in various directions? What constructs and recommendations do we provide to people? How do we keep it so it's not so extensible as to lose interoperability? 
* How can we enable validation testing on the core, that is flexible to handle various extensions that people build?
* Brainstorm on extensions - Explore how each might work as an extension or complementary service re-uses core components. The below list is just a starting point, should come up with more based on services people have seen or build.
    * Assets and activation - Planet is the main organization doing this, where assets (imagery files) aren't always instantly available for download as they are constructed on the fly. So how can the core spec account for this - not assume that every asset listed for download is instantly available, but can be created.
    * Stats - Return a histogram or total for a search, to create graphs for users to visualize results over time, or to group in to other buckets of information for cross-filtering type capabilities.
    * Coverage maps - A spatial aggregation of results - display the depth of results in heatmap type visualizations, given a user's filter / query.
    * Saved searches - Persist a search to be able to revisit it and see up to date results.
    * Different fields - Enable vendors or communities a way to have their own metadata fields as results.
    * Transactions / catalog management - Enable the editing of catalog records through the API, likely in CRUD type manner.
    * Subscription extensions for push updates / event stream - Stream out the results of persistent searches, to update people as new imagery comes in.
    * Links to tile servers of the data - A standard extension to link to a web tile server that visualizes the data.
    * Different format types (jp2, netcdf, etc) - Enable output of imagery to be in alternate formats.
    * Processing data on the fly (apply NDVI, surface reflectance) - Enable processing of data, figure out if/how to represent this in the catalog / how a processing plus catalog workflow fits in.
    * Bulk download service - Enable download of large record sets, like millions of rows, as an async operation, and to be able to output to formats like shapefile and geopackage. So that people don't have to go through lots of pages of results to construct a visualization of the catalog items on their GIS.
    * GRPC - Alternate endpoint versions in GRPC, to enable faster payloads in binary.
    * Generalization - Be able to return simplified polygons or just points when data is to displayed at lower zoom levels.
 * In general how does a catalog work to make the core data available, but also can be transformed / processed.
 * Pieces needed in core spec to make records cacheable.
    * Just cache control headers?
    * Also update / publish time as a field?
 * Mobile catalog, is there a use case for running on a mobile device?
 * Disconnected scenario, shipping out hard drives of imagery with a catalog for first responders, etc.
    * How to refer back to source catalog?
 * Global catalog network functionality. Could we have an extension where a catalog reports its number of records, number of non-duplicative records (like if it's just caching landsat or something it could report that), and perhaps even number of searches performed? And then a meta-catalog could crawl and report on the network health, like total number of imagery records served by the spec.
 * Functionality on popular searches served by this catalog? Report back heatmaps of usage, and most searched queries.


 
### Background Reading / Prep work
 
#### Top
Research various imagery catalog API's and what other services they provide.
 
#### All
Look in to extension mechanisms best practices in web API design.

 
### Participants
* Pramukta Kumar
* Robert St. John
* Ami Rahav
* Dan Lopez
* Ian Schneider
 
 
### Notes 
Use https://board.net/p/icapi-extensions for collaborative note taking. Please take great notes! This will enable those who want to collaborate with us in the future to be aware of all the initial discussions.
