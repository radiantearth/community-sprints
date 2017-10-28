## **GOALS**

   * Categorization of types of extensions
   * Sample spec for one or more extensions
   * Recommendations / best practices on those who want to extend.
## **Summary from Day 1**
**Provider Agnostic AOI Service**

   * Compose a single image for a user, pulling the 'best' image from a variety of catalogs.
   * Default 'best' definition of resolution, recency, etc.
   * Let users tweak 'best' by simple params, Let advanced users provide advanced param set (cut offs, orderings, etc)
   * Pulls from multiple catalogs, figures out what is 'best' from all of them.
   * Returns a set of geometries and source files (shapefile, geopackage, etc) that lets a client pull the images to make a mosaic with proper cutlines
   * Return the mosaic actually created, with web tiles and download views
   * No required extension points, but may send out DDOS requests to live services, so likely need either flat catalog, or pubsub so this service can cache 

**Saved Searches**

   * Dynamic saved search that continues to run, and also 'collections'

**Services for Geometries**

   * Option for searches to refer to a GeoJSON, instead of just including it.
   * Link to geocoded Url, that returns a generalized polygon - 'contra costa county'
   * Link to 'user geometries', where people can upload or draw the polygons of their area.
   * Extension point would be to let people input a link instead of just a geojson for AOI searches
       
**Organize results around AOI**

   * AOI Service from first, but be able to go forward and backwards in time.
   * Go to 'contra costa county' and see latest mosaic image of it. And hit 'previous' and get the mosaic from the previous day (week?, month?)

**Permissions**

   * Be able to request only results that I actually have download access to.
   * Need some construct in core that can support this, if a download link can't be returned.

**Pub/sub**

   * Be able to do processing when new images show up in the catalog, instead of bulk.
   * Query should be very similar or same as the main 'search'
   * Potential core spec change - 'published' or 'update' field for everything, so you can 'replay' by just querying all the latest updates.v

## **QUESTIONS TO DISCUSS**

   * WITH GROUP - 'Source of truth' should be a flat file. It will always stay up. Get it crawlable, make it so it never craps out.

## **NOTES**

   * Core search focus
       * Limited, don't get where did data come from, where was the sun, how many people were having tea
       * But can tell that this is san francisco.
   * Assume that core is going to provide enough information to do that search.
   * What applications beyond that do we want to do? What is the user trying to do.
   * We are building on top of the core - the core needs to not be directly exensible, but consider versioning and specificaiton of core capabilities as things progress.
       * Levels of compliance with the core. Simple features for SQL, there's an interface, as the interface evolves, people like this, but there's another thing that builds on top of it.
       * Not sure if those are extensions, or core evolution.
   * Assets and activation - potentially more than just Planet.
   * Will see core, optional functionality, and then extensions on top of that do specific business processes.
   * Extension would be the idea of giving more idea about the imagery that you're processing? 
       * Or is that core? Angle of sun. 
       * Core could have normalized representation of a lot of those things. Units, percision, etc.
       * not in core - firmware, version 3, at the time.
   * In core - what every satellite, company, exposes. 
   * View core as 'core commonality' between all things there's probably one set. If it's the most common set of parameters that users need to consume, then it's probably smaller. 
   * Satellite imagery schema - core attributes. 
       * Then mosaics. They don't have scenes, continous surface. You wouldn't want same schema to apply. 
       * You want provenance back, be able to trace back to the scenes.
       * 'core' of mosaics would be ones that all users can search. Extended is things general for mosaics, and then another level for very specific methodology.
   * Bucket stuff from list.
       * API semantics, 
       * Model extensions vs operations extensions.
   * First bi-furcation
       * Extra facts vs Relationships
           * This thing was derived from products, or sun angle was 5 degrees
   * Focus on 'operations'.
   * URN / ARN's - think of that as an important part of the core.
       * Can encode a lot of things in a URN / IRN, because each has their own components. 
       * Can know it came from this catalog, what platform collected it.
       * Use that to build out operation schemas, extensibly.
       * If there's an optional operation, that's part of core specification.
       * Tile service - some providers will say no. But most people will have it as a known protocol. Has well known meaning.
           * Think about that category - it's a service, it serves tiles, what type of service, etc.
           * Take that and look at other services. URN that specifies, what's the service archetype, but sets specific schema.
           * Get OpenAPI doc on how to interoperate with the spec endpoint.
           * **Loosely coupled framework, we can build core components.** But planet is first group to have stats service. URN to our service, so outside the core namespace, but can go to it.
           * At Planet - doesn't link from core catalog to tile server url. Could do it, but then it's what do you link to for the extent - draw that from the other information?
               * Doesn't fit in to openapi spec.
               * Have more information around operations could help this. And let users know they can do URL math, can define some programmatically. Like tile template url's. 
           * formalize URL templates?
           * Compositing tile server complexity - WMTS, you can't teach WMTS clients cool new tricks, like teach clients to read JWT stuff. Even though we can do it on the fly it benefits from a more transactional workflow - post body and redirect, in a much more efficient way.
       * Does this put us to leave spec at a general convention of 'here's a tile service'. 
           * Use a standard tile template for gets
           * Here's one with URL math, post a resource to this one, follow redirect.
   * Extension - security and authentication
       * This is authless catalog, until you hit this point.
       * Authenticate to even look at this catalog.
       * Requirements for certain applications
       * Pass API key
       * Proscripe OAuth 2 authentication
       * Specify 'core' as Oauth 2, but let others do stuff with it.
       * Tile service can reference stuff from the core. 
   * Spec a few
       * Tile Services
       * Coverage Stats
   * Give me the best image for this overall area on january 1st\url{https://gist.github.com/pramukta/5033592ae5f7681cb965d480edc32b4e} is code that tries to do this.

       * Search catalog for lots of stuff on date range
       * it's a 'point in time mosaic' - forget everything else.
           * I want it cloudless, in this date range.
           * At some point in time, what's the best picture I have of this.
               * I drove down here yesterday, I was in ft. collins a month ago - I have an image of what it is.
           * Putting together from DG, I want cloudless, clear imagery.
           * Punch holes in all the clouds and fill in all the gaps.
       *  Result should be to overlay / composite as a TMS from the source.
       * Fill in AOI with most recent good images, until it fills up the scene. 
           * Return to the user some shapefile / geometry specification, that specifies the cut out geometry.
           * It's the 'provenance file', without the actual data, by query.
       * When querying a catalog, consider factors in selection
           * 'material selection' - low off nadir, with few clouds, in certain season.
               * what factors/attributes influence the quality of the output product? could be core attributes or extension attributes of derived products
           * Most recent.
           * Data returned from that includes footprint. May know that satellites are right resolution to combine. 
               * Certain metadata about what the satellite can return.
               * Might want to do with just multi-spectral, with just panchromatic.
           * General filters
           * Extra service - addition on top of that 'set', that provides the AOI, and result is the information to create that provenance file.
           * Second step, use that to create the mosaic or dynamic tile services. 
           * Addition of one endpoint on metadata side should enable creation of 
           * It's a reduce operation on a query. Different aggregation than a coverage map.
               * Not saying how many, it's saying what is the most recent one that matches the criteria
       * Polygons / shapefile to the 
       * Does core spec need to change at all for this?
           * Probably doesn't?
           * Needs certain properties. Not necessarily how it's implemented.
           * Something like this can take small pieces loosely coupled and make them not work - hammer to the point that they don't work.
           * **Needs to cache / host. Or static hosting of all data. or it won't be able to scale.**
               * Instead of run your own elastic instance, run whatever you want.
               * Postgresql 10 has pub/sub table feature, that you can use directly.
               * Maybe some security thing, some authentication - source of truth being transferred something else. Views are appropriate to other things. All can be done separately.
               * DG platform catalog, they run the catalog in an elastic search cluster. 
               * Elastic search is a wonderfully scalable full text search engine. Catalog is a different thing.
                   * When you specify a flat file representation of stuff, if it something happens there's an 'out'. 
                   * API should not be the 'source of truth'. We should always have it be scrapeable. 
                   * Optimize a spark process by running it on your laptop.
                   * These catalogs aren't petabytes of information.
                   * Mobile device - why not?
   * ARN's (amazon web services)
       * Services - S3
       * Region
       * Account ID.
       * Federation - service is described by URN. 
           * Can you construct stuff other than looking at amazon?
           * Yeah, there are known separators, encodings, but is open to put whatever you want in it.
   * Unique identifiers? Did it come up yet?
       * Ian likes opaque identifiers, it makes people think about most important thing. You force people to standardize the metadata.
       * Might now have
       * Do we need unique ID's, or can we just assume that everything is 'web' - http
       * Navigable names / urls, vs not navigable.
           * Ideal world vs reality. If I paste s3:// in my browser it's going to barf. And then there's navigation, what is auth scheme, how is it passed around.
       * Chain of custody is important. To have some unique thing that doesn't change. So if a catalog goes down it still has a spot.
   * hashing for changing/dynamic content and index cueing
   * Saved Searches
       * Flat file - it's a flat file of what you care about. It doesn't get updated.
       * A 'search' is the source for a particular mosaic you care about.
       * A 'search' is a set of aggregation for stats.
       * Elastic search has an aggregation api that is pretty powerful
           * Every piece of information that you want you have to specify in your query.
           * If you want to aggregate them and also reference the underlying, you'll get the summary
               * But digging in to the extra data takes a lot of extra work.
           * Ability to drill in to record basis without having to hit microservice 100,000 times would be good.
       * Planet person was looking to save results of search, not the actual search.
           * Just a list of resources.
           * Static saved search, plus query I got it
           * Dynamic saved search, point to search to run.
       * Initial version could force clients to update the result.
       * Using DG, going through image carasoul and moving to top.
           * But no way of getting things I like and saving those off.
       * Saved search API's don't provide mechanism for the experience.
       * Coming up with spec here, you'd want to make sure 'order' is something you can set.
           * How can you 'set' the order, you've reviewed 15, come back.
       * Search parameters
           * Server side and client side settings.
       * Save the order of results, but also update the order of results.
           * Separate resources from the saved search.
           * Borrow a 'project'  concept from DG. Can order things, and save it off. 
               * Almost what robert wants, but can't create a cloudless projecct, or order an xyz package of it.
       * USE CASE
           * Select the images I care about, start with an AOI, usually pretty big area
               * Zoom in, using DG enhanced view web app, get to image carasoel. 
               * Select different images, bring to the top, then get rid of them.
               * Can't keep track of images I want to keep. 
               * How can you 'set' the order, you've reviewed 15, come back.
               * I want to order it, but not lose track of everything I've done.
           * persist a collection, revisit it later
           * Looking to create an XYZ cache of data for offline use.
               * Create a cloudless mosaic
                   * Need more order, needs fallback.
               * Generate a geopackage
       * Collections vs saved searches
           * Hand curated, vs updating
           * If we're doing the mosaic case, this is an intermediate, something that a user doesn't hit.
       * Saved searches not used all that often. 
           * Changes to core needed? Likely not, likely just the same query as the core, that gets persisted, and can report back.
       * Analysts doing long running things are the ones who likely need it most.
           * Describe the difference between saved search as filter to always be refreshed, vs augementing with stuff you've looked at, want to keep, throw away.
           * 'saved workflow' with a specific goal.
       * HTTP - pipelining \& interleaving
           * Aggregate query problem should go away.
           * Could be implemented as 100k hits at database layer, but but not at the web application layer, which is the one that usually falls over.
       * Gazeteer about giving places a name, don't want to give a name that's meaningful to all, vs one meaningful to you.
       * Indexing of AOI's and how you refer to it.
       * Fundamental operation in search is specifying an AOI.
           * Placenames plus 'your places' - to you, or to your group.
           * Ought to integrate relationships between all those entities, traversal
               * Denver -> Highlands, close to Colorado -> Bouder - make them the same thing.
           * GET vs POST - have to POST large geometries 
   * **Service for Geometries and Names**
       * could use GET with known registry of named geometries, e.g. country borders
       * Core is GeoJSON, but extension is a a known URL
           * #json-path to actual URL of geojson of things I want to extract
       * Placename based stuff
       * Also things that aren't official place names
       * Should be URL, get to a GeoJSON
       * Say we have this dynamic service, get search results from it.
           * Go back to 'previous one' - the previous image.
               * You get the latest. From the record go 'back'
       * From 'aoi' / saved 'aoi'. 
     * **Organize results for users around AOI's they care about, enable 'back' to go back through the mosaics on the fly from above'**
             * Links to 'previous' / 'next' - history of AOI; HATEOAS
         * Pointer to a query, that is constructed as an image.
         * Take that core URL 'result', and the AOI
     * If all these specs fit together, be able to 'go back'. Put the 
   * Event Stream
       * Use cases
           * From startup at Timbr
               * DG has 100 petabytes etc.
               * Way it becomes a lot when images come in and get stored somewhere.
               * A week later you have lots of images that haven't done anything.
               * When you do this work you just work on your image, 15 minutes later you have somethinig.
               * Event stream lets you process image when it comes in. It lets you process image when you come in.
           * Agriculture use case
               * They don't want to once a day or once a week process data sources and figure out what is processed.
               * They want to have it processed when it arrives. Becomes easier and simpler
               * Don't scale up to 1000 instances to do bulk stuff, just keep processing on smaller nodes.
                   * For rare stuff it can trigger an analysis. Might go check.
           * Event stream is more relevant for Planet than DG
           * External sources vs derived catalog.
               * Boundless would do event stream internally, from external source reference catalog to derived.
           * Frustration at DG
               * Event stream you want is the collection event stream.
               * Event stream I can get is things people have ordered event stream.
               * Lots of regulation that goes in to stuff, makes it slow. There's lots of DG data that everyone can't see.
                   * Raw data needs to be well protected.
           * Permissions are tricky - one thing with public data sets, but not all of those are.
               * should just be filters on event streams
           * **DO I HAVE ACCESS - are there core permissions? Can I access the data?  Do this on things I can see, get in to core.**
       * Event stream with 'flat file catalog'
           * **Is this the next 'core' element? Take flat file catalog and make sure it's stored in the right way. - Input to flat file catalog**
           * S3 has it basically 'built' in. And can pretty quickly get in S3 the keys that changed. Gives you the 'diff' for subscription.
           * S3 to get from skiff to a public area. How could we publish something in a skiff. S3 worked for that, you know that an object can't be changed. So can know if an object was added. Can use that to know.
       * Pub/sub streaming thing should access as much as possible.
           * Should not just have to access it in a specific way.
           * GNIP / Twitter model - http streaming, new line deliminted. Some unification in query language, post filters vs normal search, gzipped stream (gets chunked, a little annoying). 
               * Probably not a gzip stream, not so much data that we need it.
           * Challenges
               * Replay, go back in time, fill in missing elements?
               * Start from when you connect.
               * Probably could just steal twitter spec.
           * Can we do 'replay' functionality in Core? **Have a 'published' date in core, so you don't have to figure out all the replay.**
       * Pubsub libraries let you do basic 'prefix filtering'.
           * Imagining sending json down the wire. From 0mq, doing things as bytes, streaming bytes, header is just streaming bytes. You can throw a prefix on it, and filter very efficiently based on it. Not sure how necessary, but is convenient to multi-plex a stream. Stream from 5 catalogs, prefix convention is to include the catalog as a header.
           * Could be good to make sure this in our specs.
           * Newline delimited json / jsonp - put a 'length' thing in the prefix, so you can know when the next line will be.
       * Put in 'source' of where event came from. Want to add an extra thing, a sliding window.
       * Could we abstract pubsub to 'realtime search'. 
           * Have it behave mostly as a normal search.
           * Normally have it give you filters.
           * Pubsub is a 'permaquery'.
       * Two models
           * One you set it up and hit rest end point and keep connection alive.
               * GET / Long lived connection.
               * In case of regular search you want well formed json
               * In streaming you can't.
               * Outer json is 'results'?
               * What's the difference?
                   * json.load(one thing) vs
                   * json.load(each json).
               * How pub-sub does it need to be? Many that are out there need to be really responsive, we probably don't need it for geospatial.
                   * Depends on use case, is an hour relevant.
                   * Activation on orders is sometimes needing to pound a lot.
           * Other (more annoying) server posts to your end point. (web hook).
           * Kinda just a delivery mechanism.
       * \url{https://github.com/timbr-io/idaho-streamer/tree/minimalist}
           * Example of some streaming end points, when you don't specify end date. Not real software.
       * Design things to be stateless. 'just reconnect to service and resume'
   * Derived products
       * ordering from source imagery/assets
       * user/org quotas
       * TTL of derived products
           * is TTL/expiration a core attribute?
   * Licensing
   * Product costs/pricing
   * Buckets
       * Tile server conceptually
       * Tile server instantiations / types
       * Special tile servers that aren't standard.
       * Links to various specs, etc.
       * Gets at URI/URN, allows sharing referencing, and also linking to PDF, soap/wsdl, etc.
       * Still something there for self-discovery.
   * Core glossary catalog
       * Not an API, just human words / links to spec, narrative.
       * But for like WMTS there's link to OGC spec, links to mapbox for xyz
       * Some of those links could be soap, or other api discovery mechanisms. OpenDAP.
       * Top level type
       * link to 
       * JSON-schema link, should follow and get json-schema
       * Use links, we don't know all that will come.
   * html rendering of flat-file catalog
       * possibly as the output of an indexer/crawler, along with others
Extension Points

Core/well-known/archetype

   *  a tile service delivers imagery to a client using a protocol
       * WMTS
       * XYZ/TMS
       * Idiosyncratic Vendor (Extension)
Rely on URI/URN for core concepts + extension concepts

   * Using above example, a tile service as a concept is a URN
   * The well-known implementations WMTS/XYZ are as well
   * Extension is an external URN
URI/URN 

   * allow sharing/referencing (both to extensions from core and back)
   * ill-defined external linking (non-json-schema specs, e.g SOAP or such) or even narrative (reference material, PDF, etc)
Operations/Services

   * Catalog Level
       * pub/sub
       * query
       * stats/coverage
       * ...
   * Multi-Entry (hard to represent as a link)
       * bulk download
       * OTF mosaic (tiles of multiple scenes)
   * Per-Entry (direct linkable)
       * thumbnal
AuthZN

   * Open Catalog or not
       * Reference/doc links likely all public
   * Auth methods
       * Token
       * Key
       * ?
   * Permissions in items/operations?
       * Could be confusing in an open or partially open catalog - e.g. I can find this but cannot download it
Day 2


   * focus on user
       * who is the user? catalog client developer? catalog client user? consider both
       * boil down core attributes to what is necessary to put image/item on a map
           * provider, geometry/footprint/coverage, acquisition date-time (nominal), type and/or format (image, point cloud, video, geotiff, mrsid, etc.)
           * remove format in favor of restricting first-order catalog items to cloud-optimized geotiff
   * Keep things super simple, just one time.
       * Time range or a single time?
       * Need to give people recommendations of how to represent their obscure use cases in one thing.
       * single time value
           * precision? 
       * 'search time' - the time of the thing you want to show up in search.
   * Core - the minimum needed to support it
       * Time - 'search time'
           * JSON doesn't represent it well, no primitive data type. JSON schema has a date-time format.
           * 8601 is safe
           * openapi data types include date-time based on json schema - winning
       * Place
       * UID
       * Source - where does this come from - just a reference, can include 'provider' information
           * Get to a list that is 'set', so there's not 
       * 'type' ? - search by 'link type', to get at format, etc.
           * Do we allow searching on like 'mrsid', or have the 'processing engine' do it? 
           * Specify initial to 'cloud optimized geotiff'. 
   * Interface vs 'extensions' for data types
       * C / Java concept, implement an 'interface' 
       * With an interface a set of tooling can validate it. 
       * List of strings that matches human thing to machine url
       * Extensions is a list of sub-operations, little api thing. Interface is a 'set' of things. 
   * responses should include what extensions apply to resource
   * Importance of self-describing API - schema or openapi
       * Return all the fields and how to query
       * If DG and planet both implement clients there may be an extension that only DG has, then using DG client against Planet api the response should be 'not implemented'.
       * From spec in payload, to reference to a common thing, to a canonical name.
       * Catalog implementation should have one end point, but vendors + communities can return more than the 'core' fields.
       * Can you query the additional fields?
           * Potentially, but need query extensions.
           * Core - always be able to view.
       * If you want to see extension data you specify the schema.
       * Get available attributes, do you want to query on them, are they indexed or not.
           * Could piecemale make indexes. 
           * Indexes as an extension
           * Advertise what you have indexed.

TMS Link for DG Records

<https://idaho.geobigdata.io/v1/tile/idaho-images/41bdf497-a8e1-4fea-8658-5fe30e301b63/}{z}/{x}/{y}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2RpZ2l0YWxnbG9iZS1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8Z2JkeHwxMDQ2IiwiYXVkIjoidmhhTkVKeW1MNG0xVUNvNFRxWG11S3RrbjlKQ1lEa1QiLCJleHAiOjE1MDg5NTg5NTYsImlhdCI6MTUwODM1NDE1NiwiYXpwIjoidmhhTkVKeW1MNG0xVUNvNFRxWG11S3RrbjlKQ1lEa1QifQ.s4tqr0rGqF7UXBlBty0oHK-W24X7EVv\_wKi3xyTkRRY>




<https://github.com/radiantearth/imagery-metadata-spec/blob/dev/json-spec/sample.json>
--
Collaborate seamlessly on documents! This pad text is synchronized as you type, so that everyone viewing this page sees the same text. 
Create your own board and a (secret) name for it here: \url{http://board.net} This service is provided on fair-use with open source technology by fairkom. 
Consider a donation in Euro or FairCoin \url{https://www.fairkom.eu/en/sponsoring#Donations} for disk space and new features. Virtual hug guaranteed! 

