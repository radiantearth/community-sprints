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

(TODO: Add summary of what happened with pystac) 

[Enable code coverage](https://github.com/stac-utils/pystac/pull/164) so we can understand how well the tests are doing in covering every bit of code.

[Build and Test under Ubuntu Focal LTS / Universe py3 Stack](https://github.com/stac-utils/pystac/issues/143)
(link to issue / PR's completed)

### ESA FedEO (ESE-ERGO)
* Updated ESE-ERGO STAC catalog interface to 1.0.0-beta.2. See [landing page](https://ergo.spacebel.be/).
* Added [collection asset extension](https://github.com/radiantearth/stac-spec/tree/master/extensions/collection-assets) to provide access to collection-level metadata representations (DIF10, ISO19139-2, OGC 17-084r1).  See example [TropForest](https://ergo.spacebel.be/series/eo:platform/ALOS-1/TropForest).
* Interoperability test with [STAC-BROWSER](https://geo.spacebel.be/?t=catalogs) supporting 1.0.0-beta.
* Preliminary tests with [Rocket SnapPlanet Client](https://rocket.snapplanet.io/home?_url=https:%2F%2Fergo.spacebel.be%2F).

### STAC Index

Still very much WIP, have implemented a basic server and UI, but no crawling yet: https://github.com/stac-utils/stac-index

### (add any software you worked on)

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

**Name:**

**Description:**

**Link**
