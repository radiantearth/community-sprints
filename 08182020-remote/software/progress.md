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

Moved PySTAC to the [stac-utils](https://github.com/stac-utils) GitHub org.

[Enable code coverage](https://github.com/stac-utils/pystac/pull/164) so we can understand how well the tests are doing in covering every bit of code.

[Build and Test under Ubuntu Focal LTS / Universe py3 Stack](https://github.com/stac-utils/pystac/issues/143)
link

[Add ability to update collection extent from Items](https://github.com/stac-utils/pystac/pull/168) - New feature that allows for updating of collection extents once items are added.

[Added the Timestamps extension](https://github.com/stac-utils/pystac/pull/161)

[Fix ExtensionIndex internal docstring retrieval](https://github.com/stac-utils/pystac/pull/159) - Fixed bug that was causing help dialog on ExtensionIndex to fail.

Fixed [a bug](https://github.com/stac-utils/pystac/pull/172) with link resolution.  

### ESA FedEO (ESE-ERGO)
* Updated ESE-ERGO STAC catalog interface to 1.0.0-beta.2. See [landing page](https://ergo.spacebel.be/).
* Added [collection asset extension](https://github.com/radiantearth/stac-spec/tree/master/extensions/collection-assets) to provide access to collection-level metadata representations (DIF10, ISO19139-2, OGC 17-084r1).  See example [TropForest](https://ergo.spacebel.be/series/eo:platform/ALOS-1/TropForest).
* Completed adding paging links (previous/next) in catalogs with too many subcatalogs.  Example [ESA/ESRIN](https://ergo.spacebel.be/series/eo:organisationName/ESA@ESRIN?startRecord=51).  Having this understood by STAC-BROWSER would be very useful.
* Interoperability test with [STAC-BROWSER](https://geo.spacebel.be/?t=catalogs) supporting 1.0.0-beta.
* Preliminary tests with [Rocket SnapPlanet Client](https://rocket.snapplanet.io/home?_url=https:%2F%2Fergo.spacebel.be%2F).
* Validation tests of endpoint with https://staclint.com/.  Only copy/paste of responses as access via URL not working due to invalid SSL certificates on our server.

### STAC Index

Still very much WIP, have implemented a basic server and UI, but no crawling yet: https://github.com/stac-utils/stac-index

### STAC GeoServer/GeoTools Coverage Store
The store is functional and capable of pointing to any STAC API service and rendering any asset in a specified collection.
I was hoping to have it working with the new imageio-ext COG code, but those modules are still in snapshot which causes 
massive conflicts with GeoServer when attempting to point to multiple versions of the same dependency.

When the new imageio-ext COG reader is released, the store will work with any accessible asset, and will allow for 
custom client implementations to read COG byte ranges from any source.  

### STAC-Search-JPA

New project, WIP:  https://github.com/turingtestfail/stac-search-jpa  So far this sprint got JPA modeling for Catalog, Collections, Collection and children.  Today is all about FeatureCollections, Features, and querying/filtering with the basic use case (datetime, bbox, limit).  Tomorrow is about converting Query Extension to CQL to SQL.

### DotNetStac

.Net library for working with Spatio Temporal Asset Catalogs (STAC) 

First public release of DotNetStac (0.2.0-beta) https://github.com/Terradue/DotNetStac with NuGet package available at https://www.nuget.org/packages/DotNetStac/

Current features

* (De)Serialization engine supporting current and older versions of the specifications with an upgrade mechanism
* Navigation methods to seamlessly traverse from a root STAC catalog through children (csubcat, collections and items) up to assets
* Enhanced extensions support with plugin system for embedding extension related functions (e.g. sat: orbit file download, sar: interferometric search, eo: calibration parameters)

### (add any software you worked on)

### stactools

Created a (currently) barebones repository in the stac-utils org called [stactools](https://github.com/stac-utils/stactools). This will be a CLI that exposes features of PySTAC in combination with heavier dependencies through library methods and a CLI, including validation, migration, copying, and converting from other sources like Landsat, Sentinel, or Planet.

### stac-validator.  

Brought in validation from PySTAC. Started a branch with cli functionality provided by click. Talked about combining efforts with stactools which is obviously a good idea. Worked on better error handling. 


## Data

### CBERS

* Updated the CBERS AWS static catalog to 1.0.0-beta.1 (Fred to add more details)

## Specification

### Rendering Hints Extension

Started a Pull Request on [Rendering Hints](https://github.com/radiantearth/stac-spec/pull/879), to help dynamic tile services and other renderers be able to 
portray STAC data more easily and efficiently. Lots of good discussion and ideas.

## Other

[STAC Datasets](https://docs.google.com/spreadsheets/d/1f-qpoGHohTdY9BVi9drb4mCRX8OLzZhlmKMJi9AEW20/edit#gid=0) spreadsheet was created to track the existence and status of the various public STAC datasets.

# Demo Videos

Traditionally STAC Sprints have ended with a wrap up sessions where everyone talks about what they worked on and shows demos of anything they made. Since we're
not all in person we'll do this virtually, by recording videos. Think of them as STAC sprint specific lightning talks - not serious high-production-value 
finished-project demonstrations. Just what you'd talk about with a small room of fellow developers. Ideally this is a demo of some sort, showing off some new 
functionality built during the sprint - it can even just be using the command line. If there's nothing interactive to show you can just talk about what you did, and
perhaps show on your screen any text or code written. This doesn't have to be fancy at all, it's just really nice to see what everyone did. Some portion of
these will likely evolve into lightning talks to be given at 'outreach day' on September 8th, for those who are interested.

Use any way to record it that you'd like. Can record in Zoom, or use your favorite screen-recording software of choice; [SimpleScreenRecorder](https://www.maartenbaert.be/simplescreenrecorder/) is a great solution for Linux users. (Please add other suggestions here)

To share just add a link in the section below, it can be a google drive or dropbox file, up on youtube, or any other way it's easy to get. If you don't want
to put it up publicly but still want to be eligible for prizes and voting you can also just email it directly to cholmes [at] radiant dot earth.

## Video links

**Name: ESA FedEO STAC Catalog (ESE-ERGO)**

**Description:** The ESA FedEO Catalog software, prepared as part of the ESE-ERGO project, was extended to support STAC catalog interface version 1.0.0-beta.2.  Interoperability tests with [STACLINT](https://staclint.com/), [STAC-BROWSER](https://github.com/radiantearth/stac-browser) and [Rocket](https://rocket.snapplanet.io/home) clients were performed.

**Link:** https://www.youtube.com/watch?v=pABgI2udfxM

**Name:**

**Description:**

**Link**
