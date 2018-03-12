## Overview

This document is the raw notes from the STAC Implementations presentations. Original document was recorded at http://board.net/p/stac-day-notes

## Raw notes

### Harris

#### Internal Prototype at Harris
Presented by Michael Smith

Built a prototype, it is now starting to move more to production. The OpenAPI spec was great, used code generation to create the interfaces, and then did the mapping to elastic. 
Node.js talks to elastic search, tried out both managed elastic search service and own.
Was annoying to populate elastic. Josh F made post / put on items to do transactions. To really do this well we likely need a 'bulk' method. 
Used landsat8 collection 1 data, because they publish a manifest that is a CSV with all records in the dataset. So could download that, parse that and generate data to elastic search.
Did bulk load in to elastic search, as well through API. But the latter was impractically slow. 
2 broad categories for STAC - archival, get it all in the data, and daily update - everything collected in last 24 hours. 

#### Internal Catalog project adopting STAC
Presented by Tim Rutherford

About a year ago worked on catalog before stac. Have been working to convert that / merge together. Didn't take a lot of effort to get the basics together. GetItems is entry point for search. POST for adding records, DELETE for removing them. Main difference was wanted to make POST useful for search. Don't have search endpoint yet. Second approach was that bbox and time are just more filters. Took similar approach - json structure to do any type of filter you want. Configured a yaml description file that loads the filter types. Mongo data source connecting to. Filters is a plugin type, have a filter map concept. For each filter type have a mapping to a filter class, with an argument to pass in. Flexible for type of filters - text, time, etc. Implemented a bbox filter, which is light wrapper around the filter.

### DigitalGlobe
Put data in S3 bucket. Updated for latest stuff. Within a bucket played around with indexing. Made a quadkey index, 
generated for every quad. Took a static catalog, and with aws-cli commands could do a quadkey search. It does a prefix search.
Made a geospatial search on a static catalog with no server. Really slow, not the most efficient. Playing with Athena. 
Parqet - makes things queryable at rest on S3. Apache project. Have been keeping up the JSON schema. Can validate, if missing 
geometry will generate errors. Inherit a geojson schema, wrote a stac-schema, and am writing an eo-schema. Can enforce cloud 
cover to be an int. Python script will call a directory. All in github. Reception in DG is pretty good, people are wanting to 
movce forward with it. Useful for hosting - 'go stac or go home' for hosting other data. 

### Boundless
Wrote all the code in reactive file format. Framework for threading, non-blocking io. Can obtain thread for part of the 
processing. Also built out cool streaming responses, with server events. Don't have to build a full feature collection, as 
pulling stuff out of elastic search can automatically create links and stream responses as soon as they're available. Build 
out a kafka interface, will listen to some topic and will add a record, stick it in to elsatic search. Built gRPC and rest 
client, do streaming responses through gRPC. Most interesting thing that evolved was how you handle content extensions. 
Jaxon is serializer for json. Start with core properties (start, end, license). Just sub-class item properties, and then you 
get extensions built out. Then needs to know which to use. Introduced a 'type' field, giving each extension a type. And do 
mix-ins - core STAC does not know about specific extensions. Those are registered and can be added in to the core. Will 
automatically detect extensions as modules, so can add / remove modules, auto-detetcted. Built an annotation to define 
elastic search mappings for every given field. Create indexes and mappings, and you're good to go. Did a bulk insert with a 
bulk API. PATCH does partial updates, like update a time stamp. Also did partial returns of items with propertyname parameters. 

Question on multiple types, can you mix? Customer had 5-6 different types of metadata. Most of them were the same field. Made a first level of inheritance, of 'image' class. And extended for 'ndvi' and 'pca', etc. Used json namespace prefixes. Works well because it is clear which extensions fields are coming from. STAC is heavy with links, different content extension types. Most all relate to one or more fields. 

Used CQL for filter language. Each field builds a query derived product type. 

### Planet
Demoed go-stac tool, testing validation. Agree with bulk upload endpoint, as an extension. Showed internal API. When creating 
a collection embed a json fragment. Showed query language stuff, used intersection, to leave stuff open

Question on bulk import, why not on the feature collection, sending multiple feature collections.

Talked about small disaster data static STAC made by hand: https://storage.googleapis.com/pdd-stac/disasters/catalog.json

### Azavea / Radiant Earth
built pystac library, to form a static catalog. Generates a catalog, though things are messed up on permissions of leaf nodes 
at the moment. Worked on a stac browser. Plug in a url for static catalog, and can view items. Next step is to integrate 
gdal-js. Used emscripten port, to port gdal in to javascript. Is pretty complex, have to compile gdal and transpile to 
emscripten. On top of that library called loam, to give you promises and good javascript stuff. Have a static catalog with 
cloud optimized geotiff (or normal) and do tiling of those tiffs in the library. One thing ran in to was with static spec, 
you can use relative and absolute url's. Breaks down for relative URL's for self link. Then you're floating in the middle 
in the nowhere. Have no idea where you can go to get anything. Pystac right now just does relative. Did a year/month/day sub 
catalog structure, but it's not named well. 

### DevSeed / Sat-api 

Aiming to be an index for public datasets on aws. And easy to deploy, let people put on their own aws account, add their own data. WHole thing is written in node.js In process of updating for STAC. Most of work hasn't been STAC, it's been getting bulk stuff working with lambda functions and scale that up in node. Take the csv file that's on the landsat public bucket. Break that up in to seperate files. Put it in to 20 lambda functions (hits elastic limits). Each loads a file and inserts it. Currently ingests 100k an hour. A little slow, takes hours to ingest all data. CSV of landsat is wrong, has latest data from usgs, but data on aws was not updated (revision numbers prior to collection 1). For each record need to do a bunch of stuff to check the revision. Sentinel we get CSV from Earth Engine. Get csv and we have to fetch tile info. Post by synergise on billions of requests to tile info, just to get a geometry. Add a lambda ingestor file for stac catalog. on github, sat-utils organization. Also some other utilities - sat-search is a python client. Library and commandline utility. Give it the endpoint of a stac complaint api. Have worked with earth scientists, let them search and see what is available in unix style calendar has been valuable.

### David Hemphill 

Intruiged by portability of STAC. Most projects want a subset of a catalog and dump out in a format and take out in a 
remote area, farmer field or special ops or disaster release where there's not good connectivity. Take subset and work with it.
Wrote a simple browser. Project working is gathering data once an hour, and putting it on s3. Wanted to access data without 
server in the middle, so STAC lets us access that. Put it out in different catalogs. One is archival - year, day. 
Can also do another link catalog that just points at current data and point at current map view. Not large, dont' need to 
search by time and bounding box. Just throw server on s3 and good to go. 'parent' was a bit in conflict with the browser. 
JS library that lets you navigate, but not dealing with assets itself - let people download and put in to qgis, put in to 
openlayers, etc. 

### Pixia

Just coming in to STAC. At pixia working on a catalog. Worked on building a WFS on top of the catalog. Current catalog api isn't stac compliant, but have a proxy wrapper on top of it. Showing the WFS that is built on top of it. The STAC is the single collection in the WFS. Click on assets and it gives a feature collection. Uses a simple query language, shows cloud_cover less than 10%. In progress conversations on how it all fits together with search / WFS. 


