## Overview

This is a rough agenda for the STAC work during the [WFS 3 sprint](https://github.com/opengeospatial/wfs3hackathon/) and on
the dedicated STAC day.

## STAC during WFS 3 sprint

*9:30 am* - STAC + WFS alignment

*1:00 pm* - Earth Observation Profile

## STAC day (March 8)

*9:00 am* - Welcome, agenda overview Chris Holmes (and airport ride coordination)

*9:15 am* - Logistics for the day, Scott Simmons

*9:20* - Presentations / introductions

### ~9:30 State of STAC implementation Presentations
Keep to five minutes or less of pure presentation, will cap discussion to additional 5 minutes (but can schedule 
additional breakout topics)

* **Boundless** - Experiences implementing STAC. Overview of functionality extensions - transactions, querying grpc, kafka, etc.
* **DigitalGlobe** - Static Catalogs at DG, walk through of data and decisions made. Usage / reception in DG.
* **Harris** - Experiences implementing STAC, details on using content insertion extensions from Boundless.
* **Planet** - Planet Disaster Data static catalog, walk through & decisions made.
* **Azavea / Radiant Earth** - IServ static catalog & pystac.
* **Geocatalago** - (not sure if we have anyone to present this)
* **DevSeed** Present on sat-api and its implementation of STAC, experience implementing and next steps / improvements.

### ~10:15 Groupwide discussions
Discussion of several topics that are good for the whole group to discuss. Happy to take some more suggestions on these, but goal is to limit they prevent parallel progress. Aim to limit each to no more than 5-10 minutes, and if conclusion can't be reached then a small group will be assigned to write up a concrete proposal as a PR for all to see. Each should conclude with a volunteer to create the PR.

* **thumbnails in assets** - The first spec put thumbnail in 'links', though it feels more like an 'asset'. Should we just move
it to 'assets'? Does anyone have good reasons not to? 
* **observed / duration vs start / end** - Planet internals ended up using observed + duration. This is probably our last opportunity to change something so substantial.
* **relative vs absolute links** - We decided to allow both relative and absolute links. Should we adopt one or the other? Or at least a convention of when it is ok to use each? Should 'self' be required to be an absolute link?
* **process & momentum** - What process should we use for making improvements? PR's/ issues / ? Do we start doing 'releases'?
What determines a release point? How can we make more progress on the spec virtually? Remote only hack days? other ideas?

### Breakout groups

Breakout groups should aim to deliver real updates to the specification, discussing the best way to do things but then actually
getting things down in to a real change to the spec. 

#### Earth Observation Profile
**Lead**: Matt Hanson

**Overview**: Yesterday the group made great progress on an earth observation profile. But there's still work to be done to 
write it all up, which will likely lead to a number of smaller decisions on how to do things.

**Tasks**

* Figure out appropriate 'ranges' for our data types (like cloud cover 0-1 vs 0-100), and nadir -90 to 90.
* Work out naming and defined 'scope' for the extension (does it include radar or not? how do we define what it does cover?)
* Go through [OpenSearch for EO](http://docs.opengeospatial.org/is/13-026r8/13-026r8.html) and align naming and ranges with those.
* Create a JSON Schema validator for EO profile conformance
* Write up 'spec' with narrative description and field tables + overview
* Write up the 'asset definition' functionality, both for core and for EO profile. Create and merge PR for it.
* Create and merge PR for turning 'assets' in to a 'dict' instead of an array, with all examples updated.
* Code a server or static catalog to implement the profile
 
#### STAC API
**Lead**: Josh Fix & Michael Smith

**Overview**: The main task here is to update the openapi spec to follow the WFS, as discussed on wednesday. The other main
task is to discuss the filter language, and perhaps take a lead on it for WFS instead of waiting for them. It would also be 
good to create an extension for 'transactions', ideally submitted to WFS. And any other good discussions to have.

**Tasks**

* Go through the STAC OpenAPI document and get it up to date with all the new WFS decisions. Ideally PR, review and merge.
* Add a better narrative description, detailing how we start with WFS, what opinionated decisions we made, and what additions we made. At https://github.com/radiantearth/stac-spec/tree/dev/api-spec
* Filter Language - Kasey to present on Planet ideas, Josh what boundless did and Michael what harris has done, and discuss other options, try to pick one.
* Transactions extension - pull the openapi snippets out of Boundless & Harris implementations, write up a narrative on adding
/ using it, and add to https://github.com/opengeospatial/WFS_FES/issues/72
* Code updates to servers to reflect latest spec changes, make sure they're all sane.

#### Static STAC
**Lead**: Jeff Naus

**Overview:** Main task is figuring out how to make static STAC's more compatible with the dynamic api and WFS. And just 
dive deeper on issues that are highlighted by static catalogs / need improvements in the spec.

**Tasks**

* Can we make an OpenAPI entry that doesn't respond to any dynamic requests? Can this replace the catalog.json? If we do
need the root catalog.json then how do we bring that concept in to stac api, or at least make the two more crawl compatible. 
And should better spec the catalog.json and make a tool.
* Should we link features to the 'root' catalog (or whatever we use for collection level metadata) instead of their parent catalog?
* What should go in to collection level metadata? Do we make a spot for static catalogs to reference schemas?
* Update static catalogs for 'asset definitions' (make PR and merge) and try out EO profile
* Update static catalog examples and narratives for other changes agreed upon.
* Explore html for static catalogs
* Create / improve static catalogs for the latest spec changes (thumbnails, asset dict, etc)

#### Intro to STAC

**Lead**: volunteers?

**Overview:** For those who have not been deep on STAC it'd be great to evaluate the specification by trying out an implementation of it. Try it out, see how easy it is to implement, report any errors or improvements.

**Potential Tasks**

* Code a STAC API server (or take a WFS 3 server worked on this week and try to put in imagery data and STAC fields, and
add the STAC endpoint, etc)
* Code a STAC client to try out the spec. See https://github.com/radiantearth/stac-spec/blob/dev/implementations.md for some to hit
* Create a static catalog. Can try to do it by hand to try out with a few records and get a feel. Or can create a new tool
or adapt an existing one (pystac or go-stac) to do more or work with new data
* Create a test validator. Could crawl static catalogs and check the json schema and links, reporting what's not compliant 
(this would be an amazing contribution that many would use). Or could do basic interaction with a stac API, testing its
responses.

### Group Discussion

Individual groups should record any issues they feel are important to discuss with the whole group. Can call an ad hoc session to dive in to it.

### Wrap up

Conclusions & next steps.
