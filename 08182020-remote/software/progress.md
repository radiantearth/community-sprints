## Overview

This document aims to record any and all progress that was made during the sprint. We want place to catalog everything that happened, no matter how small. 
Put what you did during the sprint in the appropriate section, and add a link to your 'demo video' at the end of the document. Everyone who adds a video
and updates this document will get a t-shirt, and be eligible for the bigger prizes - hoodies, jackets and $5000 to continue your work. Voting for the 'community' 
$5000 prize will be done by everyone who adds their video.

## Software

Created an overview document that shows the different validators in comparison: https://github.com/m-mohr/stac-node-validator/blob/master/COMPARISON.md

### STAC Node Validator

Released a new version 0.4.0 which now includes support for:

- Validating external extension schemas (e.g. landsat extension)
- Read URLs and API responses (partial support for API responses only, see readme)
- Skipping SSL/TLS cert check for HTTPS requests

### PySTAC

Moved PySTAC to the [stac-utils](https://github.com/stac-utils) GitHub org. And released [0.5.2](https://pypi.org/project/pystac/0.5.2/)

[Enable code coverage](https://github.com/stac-utils/pystac/pull/164) so we can understand how well the tests are doing in covering every bit of code.

[Build and Test under Ubuntu Focal LTS / Universe py3 Stack](https://github.com/stac-utils/pystac/issues/143)
link

[Add ability to update collection extent from Items](https://github.com/stac-utils/pystac/pull/168) - New feature that allows for updating of collection extents once items are added.

[Added the Timestamps extension](https://github.com/stac-utils/pystac/pull/161)

[Fix ExtensionIndex internal docstring retrieval](https://github.com/stac-utils/pystac/pull/159) - Fixed bug that was causing help dialog on ExtensionIndex to fail.

Fixed [a bug](https://github.com/stac-utils/pystac/pull/172) with link resolution.  

### stactools

Created a (currently) barebones repository in the stac-utils org called [stactools](https://github.com/stac-utils/stactools). This will be a CLI that exposes features of PySTAC in combination with heavier dependencies through library methods and a CLI, including validation, migration, copying, and converting from other sources like Landsat, Sentinel, or Planet.

### stac-validator.  

Brought in validation from PySTAC. Started a branch with cli functionality provided by click. Talked about combining efforts with stactools which is obviously a good idea. Worked on better error handling. 

### ESA FedEO (ESE-ERGO)
* Updated ESE-ERGO STAC catalog interface to 1.0.0-beta.2. See [landing page](https://ergo.spacebel.be/).
* Added [collection asset extension](https://github.com/radiantearth/stac-spec/tree/master/extensions/collection-assets) to provide access to collection-level metadata representations (DIF10, ISO19139-2, OGC 17-084r1).  See example [TropForest](https://ergo.spacebel.be/series/eo:platform/ALOS-1/TropForest).
* Completed adding paging links (previous/next) in catalogs with too many subcatalogs.  Example [ESA/ESRIN](https://ergo.spacebel.be/series/eo:organisationName/ESA@ESRIN?startRecord=51).  Having this understood by STAC-BROWSER would be very useful.
* Interoperability test with [STAC-BROWSER](https://geo.spacebel.be/?t=catalogs) supporting 1.0.0-beta.
* Preliminary tests with [Rocket SnapPlanet Client](https://rocket.snapplanet.io/home?_url=https:%2F%2Fergo.spacebel.be%2F).
* Validation tests of endpoint with https://staclint.com/.  Only copy/paste of responses as access via URL not working due to invalid SSL certificates on our server.

### STAC Index

Still very much WIP, have implemented a basic server and UI, but no crawling yet. Ecosystem list is mostly done.
Homepage: http://stac-index.lutana.de (trying to get a better domain)
Repository: https://github.com/stac-utils/stac-index

### STAC GeoServer/GeoTools Coverage Store
The store is functional and capable of pointing to any STAC API service and rendering any asset in a specified collection.
I was hoping to have it working with the new imageio-ext COG code, but those modules are still in snapshot which causes 
massive conflicts with GeoServer when attempting to point to multiple versions of the same dependency.

When the new imageio-ext COG reader is released, the store will work with any accessible asset, and will allow for 
custom client implementations to read COG byte ranges from any source.  

### STAC-Search-JPA

New project, WIP:  https://github.com/turingtestfail/stac-search-jpa  This project aims to give Java, Spring, and JPA developers a jumpstart on creating their own STAC implementations by providing the basic object relational mappings and JSON serialization/deserialization tools.  So far this sprint got JPA modeling for Catalog, Collections, Collection, FeatureCollections, Features, and querying/filtering with the basic use case (datetime, bbox, limit).  
Implemented Endpoints:

STAC landing page (/)
/conformance
/collections
/collections/{collectionId}
/collections/{collectionId}/items
/collections/{collectionId}/items/{featureId}
/search
/filter?cql= (CQL is not officially part of the STAC API standard yet, but I hear it is coming soon. Note that this implementation is PostgreSQL specific and will have to be removed for other databases)

After you use JPA to create the tables you can load sample data from the data.sql

### DotNetStac

.Net library for working with Spatio Temporal Asset Catalogs (STAC) 

First public release of DotNetStac (0.2.0-beta) https://github.com/Terradue/DotNetStac with NuGet package available at https://www.nuget.org/packages/DotNetStac/

Current features

* (De)Serialization engine supporting current and older versions of the specifications with an upgrade mechanism
* Navigation methods to seamlessly traverse from a root STAC catalog through children (csubcat, collections and items) up to assets
* Enhanced extensions support with plugin system for embedding extension related functions (e.g. sat: orbit file download, sar: interferometric search, eo: calibration parameters)

### stac-server

0.2.0 release of [stac-server](https://github.com/stac-utils/stac-server), the evolution of sat-api. Now supports 1.0.0-beta.2.

### Franklin

[Enable read from http URLs](https://github.com/azavea/franklin/pull/385)
[Fix path relativization](https://github.com/azavea/franklin/pull/390)

### QGIS STAC Browser

Though not public yet @kbgg made some good progress getting [qgis-stac-browser](https://github.com/kbgg/qgis-stac-browser/) up to 1.0.0-beta.2

### resto

Update [resto](https://github.com/jjrom/resto) API to supports STAC 1.0.0-beta.2

### rocket

Update [rocket](https://rocket.snapplanet.io) Web client to supports STAC 1.0.0-beta.2 (note: online demo is still aligned on STAC 0.9.0 - will be updated for STAC data sprint in September)

### sat-search

[sat-search](https://github.com/sat-utils/sat-search) 0.3.0 was released, upgrading it to 1.0.0-beta.2. It's a python library and CLI to query STAC API's.

### SNAP STAC [Luis Veci SkyWatch]

* Java implementation of STAC Item spec within SNAP.
* SNAP STAC extension for common metadata used by SNAP.
* STAC writer converts any satellite data product supported by SNAP into a STAC Item.
* STAC reader injests a STAC Item into SNAP for processing.
https://github.com/senbox-org/s1tbx/tree/stac

### (add any software you worked on)

## Data

### CBERS

* Updated the CBERS AWS static catalog to 1.0.0-beta.2. Available at https://cbers-stac-1-0.s3.amazonaws.com/catalog.json

### 3DEP

* New STAC catalog up at https://3dep-stac.s3-us-west-2.amazonaws.com/catalog.json

### eBird Status and Trends Model Results

* Wasn't actually part of the sprint, but during the week there was the start of a new catalog at https://ebirdst-data.s3-us-west-2.amazonaws.com/catalog.json using 
COG's in an interesting way, and bringing a different data type into STAC.


## Specification

### Rendering Hints Extension

Started a Pull Request on [Rendering Hints](https://github.com/radiantearth/stac-spec/pull/879), to help dynamic tile services and other renderers be able to 
portray STAC data more easily and efficiently. Lots of good discussion and ideas. 

### Iterative improvements

Started a PR to [add via & canonical rel types](https://github.com/radiantearth/stac-spec/pull/884). And one to [clarify unique 
ids](https://github.com/radiantearth/stac-spec/pull/883). Both need a bit more work / discussion.

## Other

[STAC Datasets](https://docs.google.com/spreadsheets/d/1f-qpoGHohTdY9BVi9drb4mCRX8OLzZhlmKMJi9AEW20/edit#gid=0) spreadsheet was created to track the existence and status of the various public STAC datasets.

# Demo Videos

Traditionally STAC Sprints have ended with a wrap up sessions where everyone talks about what they worked on and shows demos of anything they made. Since we're
not all in person we'll do this virtually, by recording videos. Think of them as STAC sprint specific lightning talks - not serious high-production-value 
finished-project demonstrations. Just what you'd talk about with a small room of fellow developers. Ideally this is a demo of some sort, showing off some new 
functionality built during the sprint - it can even just be using the command line. If there's nothing interactive to show you can just talk about what you did, and
perhaps show on your screen any text or code written. This doesn't have to be fancy at all, it's just really nice to see what everyone did. Some portion of
these will likely evolve into lightning talks to be given at 'outreach day' on September 8th, for those who are interested.

Use any way to record it that you'd like. Can record in Zoom, or use your favorite screen-recording software of choice. Some options are:
* [SimpleScreenRecorder](https://www.maartenbaert.be/simplescreenrecorder/) - great solution for Linux users. 
* [OBS Studio](https://obsproject.com/) - Open source video streaming/recording.  Easy to setup and arrange multiple capture sources.
* Please add other suggestions here

To share just add a link in the section below, it can be a google drive or dropbox file, up on youtube, or any other way it's easy to get. If you don't want
to put it up publicly but still want to be eligible for prizes and voting you can also just email it directly to cholmes [at] radiant dot earth.

## Video links

### ESA FedEO STAC Catalog (ESE-ERGO)

**Description:** The ESA FedEO Catalog software, prepared as part of the ESE-ERGO project, was extended to support STAC catalog interface version 1.0.0-beta.2.  Interoperability tests with [STACLINT](https://staclint.com/), [STAC-BROWSER](https://github.com/radiantearth/stac-browser) and [Rocket](https://rocket.snapplanet.io/home) clients were performed.

**Link:** https://www.youtube.com/watch?v=pABgI2udfxM

### James Santucci

**Description:** Ergonomic fixes on Franklin.

**Link:** https://youtu.be/HGkHeNK8f4Y

--

#### MAPLABS  aka  Brian M Hamlin, Berkeley CA

**Description:**   pySTAC / edu / Jupyter  / OSGeoLive    (download file for better playback)

**Link:**  http://blog.light42.com/wordpress/wp-content/uploads/2020/08/STAC6-Code-MAPLABSF-aug2020.m4v

--

#### STAC GeoTools Raster Store [Josh Fix]

**Description:** The STAC GeoTools Raster Store is a store that allows users to build a store in GeoServer that points to a dynamic STAC catalog, definies a 
collection and an asset ID, and allows any asset in that collection to be dynamically rendered. 

**Link:** https://www.youtube.com/watch?v=B894TGefRjU 

--

#### Staccato [Josh Fix]

**Description:** Staccato is an open source implementation of the STAC spec. It is written in Java using Spring Boot and Project Reactor, backed by Elasticsearch. It has many unique capabilities and is battle-tested in production environments.

**Link:**  https://www.youtube.com/watch?v=rBbu9N6cHzw

--

#### STAC-Search-JPA [Joseph Miller]

**Description:** Spring Boot + Spring Data JPA implementation of STAC spec.  This project aims to give Java, Spring, and JPA developers a jumpstart on creating their own STAC implementations by providing the basic object relational mappings and JSON serialization/deserialization tools.

**Link:**  https://youtu.be/vTnovDQkC2w

#### STAC Index and STAC Node Validator (Matthias Mohr)

**Description:** STAC Node Validator additions in 0.4 (URLs, APIs, external schemas, disable cert check) and [STAC Index](http://stac-index.lutana.de), an index for STAC APIs, catalogs and the STAC ecosystem.

**Link:** https://youtu.be/M4vrUtcg3rw

--


#### SNAP STAC [Luis Veci]

**Description:** The SNAP STAC module implements the STAC Item spec within SNAP and provides a reader for interpreting STAC Items and a writer for converting any satellite data product supported by SNAP into a STAC Item.

**Link:**  https://youtu.be/Foa19gvlNqI

-

#### Chris Holmes

**Description:** Report out on minor tasks done this sprint. And realized I forgot one - [added via & canonical rel types](https://github.com/radiantearth/stac-spec/pull/884)

**Link:** https://youtu.be/xH7jcSIExSQ

#### Chris Helm

**Description:** Report on the pixel8earth pointcloud extension

**Link:** https://youtu.be/DmszNWvxkGs


--

#### Name

**Description:** 

**Link:** 


