# Lightning Talk Notes

(stored here for posterity, copied from https://board.net/p/icapi-lightning-talk-notes)

### RasterFoundry

Get answers from earth imagery quickly and repeatably

* Product of Azavea - software shop that caters to civic applications, stress open data, b-corp and take values seriously.
* Got funding for raster foundry from 2 grants, DOE + NASA
   * DOE - bring in imagery from various sources and do some operations - stitching, cloud removal, and present to users easily.
   * NASA - Do advanced processing on imagery. Do NDVI, NDWI, etc.Made sense to combine them in to one product.
* Integrating multiple catalogs with a unified query API
* Can compare different stages of an algorithm with a slider, see what the effect of a wild fire is.
* One problem - spectral bands aren't well indicated, don't know what wavelengths work
* Other problem - how do we track a scene to an image in a scene. A scene has many images. 
   * Extra large tiffs that users upload that need to be pre-tiled, make them in to one scene
   * Landsat has one tiff per band, make sure people find those.Built spec on swagger 2.0. Liked the spec, can autogenerate a python client, which we used as a base.
* Every time we deploy we make a new docs site
* open source docs/swagger api - docs.rasterfoundry.com
* Partnering with RasterVision (ask Rob about it)
   * Harness machine learning to detect changes in certain models.
   * Annotate ships that we're finding.Feed in to machine learning platform, in to 'information feeds'

### Google Earth Engine

Bring data center scale computing to global challenges

Examples:
  * First big scientific result was full landsat time series analysis on forest change. Maryland doing primary science, GEE makes it easy to process at that scale.
  * SERVIR building tools for agriculture / monitoring

* About bringing data and computation together and making it easy to use for scientists.
* Data in catalog:
    * 200 public datasets, 11 million images, over 10 petabytes of public data
    * Users can bring private data
    * Landsat, MODIS, Sentinel VIRS
    * Land cover, forest and surface time series (built in earth engine)
    * Not just imagery, also things that are like imagery
* Be sure we don't just focus on imagery and hard bake assumptions about imagery gathered from a sensor.
* Data Catalog - make it easy for non-developers to use
   * GDAL bindings for it, so those users can use it
   * Tensorflow, easy integration to data.
  
* Key API concepts
  * Folder - contain images or large image collections
  * Image - raster, any bands, arbitrary key/value metadata
  * Image Collection - container of related images, indexed by their metadata.
* Endpoints
  * List a folder or collection in a paginated way.
  * Have seen every way that people can mess up the data.
  * Get information about an asset
  * Filter an image collection
  * Fetch pixels
* Early lessons
   * keep it simple
   * more than just satellite imagery
   * filter by space, time, properties 
* How best to search what data is available?
  * indexing existing open data sets
  * using google search or similar free text input
* Google Research Blog post on Google's new work on searching open datasets via Google search: https://goo.gl/iuHBey
  * Make your archive crawler friendly
  * Embrace and extend schema.org
  * W3C dta catalog vocabulary (DCAT)

JSON spec for describing how to combine related imagery products, e.g. separate-banded geotiffs

### DigitalGlobe

* As the group that collects the images there's a huge chain of products that goes in to producing.
* Issues with accessing is not knowing what value a user can get out of each part of the chain.
* If you compensate for the atmosphere with surface reflectance you can get higher accuracy geolocation
* Platform groups at DG have worked on having that chain be configurable by a client, have processing chain occur on demand for specific areas.
   * Deferring computation until you want to access something.
   * Similar to tensorflow - it's a delayed computation graph.Another library leveraged is Dask (\url{https://dask.pydata.org/en/latest/)} gives you basically numpy style access.
* Big thing about the processing chain is it maintains the transformation of metadata in its own convention.
* Any transformation has lots of information - georeferencing system, etc.
* Is 'way too much stuff'. But Beau might care about it.
* This is the biggest problem. Index I might want for machine learning set up than it is for someone producing DSM's to do high resolution time series (dubai palm islands being created).
* As part of spec there's a way to separate the indexing of metadata and the metadata itself.
* A way to encourage to quickly generate / standardize to generate specific indexes for the type of operations we want to do.

### DevSeed / Sat-API

* Collection of tools called sat-utils
  * github organization https://github.com/sat-utils
  * the idea was that it would be a simple repository and CLI that users would be able to search and download and process the landsat data into formats
  * the real goal is not to create own product, viewer, interface - rather build small tools that other people can use and integrate into their own applications
  * expanded sat-utils to be smaller and more microservice-oriented, modular

* **sat-api**
   * github repo https://github.com/sat-utils/sat-api
   * live instance at https://api.developmentseed.org/satellites
   * combines landsat 8, sentinel 2
   * deployed on AWS
   * API gateway
   * lambda functions
   * elasticsearch backed 
* **libra** - simple viewer and search interface for landsat 8
   * Wasn't intended to be its own product, but is a nice interface
   * meant to be an example of what you can do.
* **Sat-search** - python library and command line tool, companion for sat-api
   * github repo \url{https://github.com/sat-utils/sat-search}
   * Goal is if there's a common api end point then it could connect to any of them.
   * Search and download stuff
   * Goal is for things to remain small. Not lots of dependencies, use it as a library but depends on command line stuff.

### OpenAerialMap

* 7 years ago after Haiti the idea was born.
* Right license of imagery + tools to access and searh.
* on the website you can easily search for imagery (open license), visualize and import to OSM.
* Imagery from any source (including UAV and drones) can be uploaded to the platform.
* Highly available infrastructure, e.g., S3 + JSON registry
* expose TMS to combine with OSM
* can include commercially licensed imagery as well

Successes:
 * Levereaging S3 for storing and indexing imagery and metadata    
 * simple seaerch API
 * AWS Lambda + COG for tile generation

Pains:
 * Getting other providers to set up S3 or similar buckets
 * managing metadata without API
 * metadata updates
 * scenes vs imagery tiles 
 * how to integrate/motivate legacy providers, like FTP, non-cloud-native?
 
OIN imagery metadata
  * Good:
     * JSON worked great (api.openaerialmap.org)
  * Bad:
    * WKT in GeoJSON
    * RGB only
  * Aspirations/Goals
   * federation, including third-party indexing and different "browsers" with different use cases for the imagery
   * cross-service discovery
 
Have been incorporating a lot of UAV imagery


### Element84

* Common Metadata Repository API (CMR)
  * Search index for NASA EOSDIS
  * 30 data providers, 380M metadata records 
  * What We Like about API
    * Performance - CMR came about for faster search performance.
      * Sub-second searches, spatial and temporal, across 380M records
      * Can search over top of pole, will give them data under search area.
    * API's designed with clients. Asked clients to design the API they want. Pull out ideas they want.
    * Faceting API that reduces client logic.
      * Earth data search. Can click on keyword, and it'll send search to CMR, with updating counts, etc.
      * Earth data search doesn't know about the data there - the API gives links to apply filters, inside the facet values.
      * Get back a new search document, with a 'remove' link to take out facet. Can add new facets and no client code needs to be changed.
    * Tagging metadata records - allow client namespace tags.
      * OpeNDAP may want to tag that it can be used in OpenDAP
      * Review client says if it's approved, inreview. Each gets its own view of it.
      * can include arbitrary JSON metadata, and it gets indexed. So you don't have to store in own client specific database.
        * Will avoid collisions, each client can do their own 'WCS'
  * Lessons learned
    * Legacy API concerns - too many sins of the past carried forward. Could have done more to build separate facade.
    * Embrace standards more. It's more custom api's instead of standard ones. Designed 4 years ago, doesn't have newer features.
    * HATEOAS - document tells you how to navigate to the site. More links for granular searching. A client friendly feature.
    * Understand point of view of client developer - build a lightweight client to help.Most important thing to get right
  * User Experience
    * Client Developers
    * Users that use those clients - what do they get out of it, what do they need to get out of it. For client devs to get what they need for their users.
    * How hard is the API to use.
    * Great paper 'Achieving Usability Through Software Architecture' (\url{https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=5605)}
       * Seperation of presentation from application is insufficient to achieve usability. Changes in the core ripple out to users and impact them.
       * Undo - can't add that in later, if the system doesn't do it.
       * Aggregate commands.
       * Cancel long running system
       * validation

### Amazon

* Talking as a core member of the storage team, understand what customer wants from S3
* Catalog + Catalog API is 'the problem'. 
* Most implementations, state \& local government, assume we're still in shipping and clipping data. Put in shopping cart.
* Conversation around data scientist users and developers is thinking about machines, from an AI sense. Not enough attention paid to that.
* Living in a world of schema on the fly. We don't know what's going to be in the bucket tomorrow. Need to be able to build indexes, build catalog systems of our own, on the fly, as a function of what came in the bucket 2 seconds ago.
* Need to spend more time thinking about key value store. It's not a flat file with simple naming. It's a prefix we can leverage over time. Object store is a defacto standard already. Initial things on S3 was TMS, in a restful type way. What could get simpler? Not storing data on S3, rather staging or sharing data on the object store. Talking public or totally monetized.
* automatically respond to dynamically changing schemas/metadata to index and expose catalogs - "catalog on the fly"
* Human walkable prefix name / key value. Really important that we protect the walkability of the data, so developers who understand the data can run an S3 client and get value out of it immediate. 
  * Does it lay out in a way where pagination is a problem.Don't rely on external indexes to go in to deep archives - that's broken. Worked on federal projects where something was broken, because it was wrong. Supporting it for petabyte class data is untenable. What's in the object store should go in to index. 
* Pubsub model - about serverless and eventing, think strong pattern when stuff shows up in object store it gets publicized - whoever cares about it can subscribe to that. Add to index, do operations against it. Works because it's shared.
* Petabyte class data forces conversation not just about technology, but about the economics of the data - who pays for the data storage? Most object stores have a data egress charge. 
* Traditionally you query the catalog and you can pull data out of it. But when you have Dex? moving to cloud, there are loosely coupled architectures on the backend. You can go around the index to the backend. But if you fire off 10,000 nodes to do deep querying they're not going to let you get to the object store.
   * Requestor pays offloads risk of egress to whoever is running those machines.
   * Without that there is no petabyte access for anyone.
   
### Boundless

* Large amount of imagery that comes in from various sources
* How do they deal with new imagery coming in, what kind of metadata does that imagery get them, and then they need to do some sort of processing of it.
  * Keep a record of imagery that they've already looked at.
  * At any point in time they may want to process source imagery, need a catalog of the source imagery (Planet, Landsat8, NAIP, anything).
  * Do some processing in Spark - NDVI and TOA
  * Keep a record of processed imagery
  * Keep a catalog that records both source imagery and the processed imagery.
  * Boundless is hoping this group can help deal with catalog of source imagery.
  * Plus a catalog for the processed imagery. 
* Wanted to start in OpenAPI 3, but the tooling is not mainstream, no way to generate code from an OpenAPI 3 document. 
* Segment of WFS 3 spec, that was originally in openapi 3, but did a swagger 2 version of it.
* Josh edited the wfs 3 document, stripped out buildings, put in some imagery metadata.
* Had it generated, was able to run swagger codegen.
* Built spring boot application. Took artifacts it generated, and moved in to springboot.
* Created separate modules, controllers, DTO's. Use library to convert catalog to domain entities. 
* Added little bit to generate HTML
* Concerns, how closely to stick to swagger generated:
    * Controller - f format lets you pick html or json. The code generated by swagger responds with a featureCollection DTO or an image DTO. So that's a bit hardcoded in to the spring controller system. How do you have a parameter change that to html?
    * End up duplicating methods generated, put in own methods. Return string, and build html output. Having to tweak and modify what swagger tells me to use.
* Mongo on backend, but may swap backend

### Pixia

* More than imagery - strips, mosaics, lidar, imagery containers (NITF's that are group of images. Just because it's a file doesn't mean there's one image in a catalog)
* Support data type specific metadata queries.
  * Lidar point classificationsSupport mosaics made form different images.
* Key Features
  * Document based - made arbitrary stuff easier.
  * ECQL for query
  * Results in GeoJSON and document
    * Retrieve partial views of documents - get ID and time, or ID and name, so you don't have to throw it away.
    * Assets grouped in to things when relevant.
  * Data-type specific metadata
    * strips can have beginning and end. And they can be broken up in to more files.
    * LiDAR, points in time aren't all from a single collect. Mosaics of LiDar
    * Mosaics Vendor may deliver a shapefile of strips that make up mosaic. Sidecar file helps.
    * Image contianers - nitfAPI - straight restful, with groups and assets, 
  * CRUD and document search results.
    * Query - bbox, time and fields - what do you want result to look like. 
  * Wrote WMTS on top of it, for footprints.
    * motivation - get in to arcmap, plus cacheable tiles. Millions of footprints you can't do on the fly all the time.
    * Custom search, will generate a WMTS based on ECQL encoded query.
  * Important capabilities
    * Hierarchy of assets, and able to preserve relationships.
    * support search on ranges, sets and lists - many data types can't be reduced.
    * It is the imagery catalog, but support non-imagery types.
 * Design considerations
   * Many users have browsers with 1 vpu and 1gb ran vm.
   * Avoid user defined parameters. Stick to server provided ids.
   * Time should have millisecond resolution.
   * Globe is sphere, but a user has a bbox. See query in proper geometry warped on to sphere. When a user draws a circle they expect a circle.

### ENVI
* Core is geospatial analytics
* Important move is to position to be easily consumable on the cloud
* Underneath all of it IDL is still the programming language of choice.
* A few forays in to data management
  * Jagwire
  * Harris Geospatial Marketplace (mapmart)Representing consumer
* Traditionally have served geospatial expert, people who understand geospatial data, and the power of analytics
   * they did mind owning data, they managed it.They aren't dead, they're still there, but they're a shrinking part of the market.
* **Data -> Analytics -> Answers**
* Fundamental problem with this model is it doesn't scale. Very slow, manual process.
* Seeing more consumer being non geospatial expert. 
  * Precision agriculture - automatically process geospatial imagery, extract counts and health of crops
  * Insurance and real estate - who can get insight from geospatial.
  * Much larger marketBut to reach this market we must change 
* Understand what customer questions are they want to answer, then to put in tool set and feed optimal data.
* Data search and access should be oriented around consumer's needs - AOI
* Not collect or scene. We traditionally start from this perspective - needs to change.
* Data search and access should be standardized, and preferably federated
* Data should not be moved, if possible. Run analytics next to the data.
* Wrong with existing model
  * Every data provider has their own api
  * No federated source of available data
  * No common compute pattern
  * Implied ownership model. Consumers actually want a data service, not a data product.
  * Oriented around needs of provider, not the consumer.
* People don't care about cloud cover in the Scene, just in their AOI.
* What should we try to accomplish?
* Applications use different catalogs.
* Would be great to have single openAPI, and only one catalog we have to deal with.
* End state - should be services that discovers and delivers data optimized to deliver answers.
* An 'answer service' on top of analytics and data services.
* Vast majority of users will likely want Data Services level, not the data catalog level.
* What does an effective catalog api look like?
   * Metadata in 3 tiers.
     * Minimal metadata model to support discovery
     * Rich standard metadata to support analytics
     * Custom metadata to meet special needs
* Core Metadata Suggestions:
   * Spatial
   * Temporal
   * Spectral
   * Quality (cloud cover, etc)
   * Access (cost, logistics, ...)
   
### Planet

* Clear through other lightning talks - how much common problem solving and thinking has gone on in this domain.
   * Thought there'd be lots of proprietary 'we have this' and 'we have that'
   * There's lots of shared context.Work on API services, mostly on tile server. Taking imagery and getting it to clients.
     * WMTS is a great example. Planet started using defacto XYZ / TMS.
   * This is 3rd WMTS implementation. You can open in qgis and arcmap. WMTS brings a lot to table.First standard ever worked on was shapefile
     * Spec became very obvious that it was not a spec written to be open, byte order changes with deliberate obfuscation.
     * Made updated, refreshed version in short period of time.
     * That format suffers, but no one can argue that shapefile hasn't served us all well.GML 3 - Ian is a proponent of XML. Would argue we should step back and look at it
   * Wasn't XML itself, but the experiences at the time. Factory Delegate Delegate. 
     * JSON is javascript object notation. Took something handy, part of the parser, and built tools.
     * Why is XML so painful - link to schemas, link to schemas, embed third party data. XSD's that can model entire ecosystems.
     * GML 3 without implementation, because it was so brutal. GML simple schema was understandable.
     * GML3 came from good meaning people.
     * But it was dropped - it could model everything, but using it / comprehending was hard.
     * JSON - easy to get started, linking format. 
     * XML is still at version 1, but everything on top - links, XSD, XSLT.
     * JQ - xslt with nice tools.
     * React server rendering, to render for browser.Paradigm shift - moving from 'this is an image' to 'how do users want this imagery'
   * What are other aspects of that.
     * Tile service guy - reasons I want highly accessible metadata.
     * We have 12 bit floating point imagery in 16 bit imagery, how do we express that.
     * How do we have deep key value stores that can express themselves.
   * Metadata mosaics - pixel provenance at Planet, where did data come from, which scenes. How can we expose this in a good way?
       * Best way so far is UTFgrid, since it can be tiled in the client.
   * Worked on python API client. User experience lessons learned are important to keep raising and bringing to the fore.Planet's challenges
   * Search, Items (representing a scene)
      * Assets, would represent UDM, cloud mask, etc.
      * So much data we couldn't keep it ready to use and 'hot'
      * So using the API, there's an async workflow.
      * Something we would like to avoid. Make a thing alive, notify me of it, let me download.
      * Generally a restful api, but has one bit of async.
   * Python client Planet did write hides that API level issue.
   
### Hexagon

Apollo - geospatial data catalog and delivery platform. 
   * Support more than just imagery, problem is bigger than just imagery
   * Imagery, vector databases, shapefiles, gml, fgdb, pointcloud and video support.
   * Users - government, defense, municipalities
   * Catalog is a manual crawl or a 'dropbox'.
       * Catalog - point at file system and discover data.
       * Dropbox - longterm automated workflow. As you throw things in there they will ingest and come in catalog.
   * Delivery is through standard OGC services. Plus custom API's, like clip, zip + ship.Liked about API
   * Profile mechanism to specify schema of documents you get out of it.
       * JSON is a big player, but our API's are a bit older, product has been around 8 or 9 years. Did before standardized work around json.
       * Doesn't change shape of what you get out of it, but what pieces you get out of it.
       * Backend is relational database. For performance want to let people get different summaries.
   * Some catalog functionality is somewhat old school. Accept header parsing, get HTML, KML, JSON, etc.
   * Can browse the catalog as HTML

Goals for the week

* Extensibility and backwards compatibility - not backwards to things out there, but have ours be versionable. Vendors will want to differentiate product and add extensions - make sure we don't break the spec when they do that. And be able to do different versions and maintain.
* Federation - Apollo does not have a federation, customers want it.
* Profile/user-defined schema.
* Support for any geospatial data.
* AOI searches/notifications.

Gitter Channel - https://gitter.im/Imagery-Catalog-API-Team/Lobby


