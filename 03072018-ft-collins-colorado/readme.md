## STAC Community Sprint March 2017

For the second in person collaboration on [SpatioTemporal Asset Catalogs](https://github.com/radiantearth/stac-spec) 
the group combined forces with the [WFS 3 Hackathon](https://github.com/opengeospatial/wfs3hackathon/), to enable 
cross-specification collaboration. The first two days were focused on WFS 3, though on Day 2 there were a couple break 
out sessions that focused on STAC.

Day 3 was the dedicated STAC Day, sponsored by [Radiant.Earth](http://radiant.earth). Lots of progress was made, with 
numerous specification improvements coming out of great discussions.

### Background

The SpatioTemporal Asset Catalog specification was the main outcome of the [Boulder Sprint](../10252017-boulder-co/). The
goal for the second gathering was to work with a smaller group of those who have actually implemented the specification. 
This would ground discussions in the practical, instead of imagining everything that is possible. While thinking about
organizing the [OGC](http://opengeospatial.org) was moving ahead on organizing a hackathon on 
[WFS 3.0](https://github.com/opengeospatial/WFS_FES), and the decision was made to combine the two events. 
STAC used WFS 3.0 as a starting point, but then diverged it a bit. Having both groups in the same room would help to 
bring the two together, improving both.

### Overview

To see all the details on what happened see the [agenda](agenda.md), and check out the [notes/](notes/) folder. But for
those who want the higher level summary read on (and follow the links to the individual 'notes' pages which have more in
depth overviews.

#### STAC during WFS 3 hackathon

During the WFS 3 hacakthon there were two solid sessions with smaller groups of people working on STAC.

##### STAC + WFS Alignment
([summary and notes](notes/wfs-stac.md))

The main goal was to align the [STAC API](https://github.com/radiantearth/stac-spec/tree/dev/api-spec

*1:00 pm* - Earth Observation Profile ([notes](notes/stac-eo.md))

## STAC day (March 8)

*9:00 am* - Welcome, agenda overview Chris Holmes (and airport ride coordination) ([presentation](notes/stac-intro.pdf))

*9:15 am* - Logistics for the day, Scott Simmons

*9:20* - Introductions

### ~9:30 State of STAC implementation Presentations ([notes](notes/presentations.md))
Keep to five minutes or less of pure presentation, will cap discussion to additional 5 minutes (but can schedule 
additional breakout topics)

* **Harris** - Experiences implementing STAC, details on using content insertion extensions from Boundless.
* **DigitalGlobe** - Static Catalogs at DG, walk through of data and decisions made. Usage / reception in DG.
* **Boundless** - Experiences implementing STAC. Overview of functionality extensions - transactions, querying grpc, kafka, etc.
* **Planet** - Planet Disaster Data static catalog, walk through & decisions made.
* **Azavea / Radiant Earth** - IServ static catalog & pystac.
* **DevSeed** Present on sat-api and its implementation of STAC, experience implementing and next steps / improvements.
* **David Hemphill** Javascript stac browser, and experience with static catalog for a customer.
* **Pixia** - Update on pixia catalog.
* **Tim from Harris** - Mongodb based catalog, converting a pre-stac.

### ~10:15 Groupwide discussions ([notes](notes/group-discussion.md))
Discussion of several topics that are good for the whole group to discuss. Happy to take some more suggestions on these, but goal is to limit they prevent parallel progress. Aim to limit each to no more than 5-10 minutes, and if conclusion can't be reached then a small group will be assigned to write up a concrete proposal as a PR for all to see. Each should conclude with a volunteer to create the PR.

* **thumbnails in assets** - The first spec put thumbnail in 'links', though it feels more like an 'asset'. Should we just move
it to 'assets'? Does anyone have good reasons not to?
* **observed / duration vs start / end** - Planet internals ended up using observed + duration. This is probably our last opportunity to change something so substantial.
* **relative vs absolute links** - We decided to allow both relative and absolute links. Should we adopt one or the other? Or at least a convention of when it is ok to use each? Should 'self' be required to be an absolute link?
* **assets to dict, asset definition** - A couple items from the EO profile discussion with broader relevance
* **naming of content extension / profiles / ?** - We don't have a clear name for when someone is using all the same api / static json mechanisms but is making their own validating schema - both community & vendor specific.
* **process & momentum** - What process should we use for making improvements? PR's/ issues / ? Do we start doing 'releases'?
What determines a release point? How can we make more progress on the spec virtually? Remote only hack days? other ideas?

### Breakout groups

Breakout groups should aim to deliver real updates to the specification, discussing the best way to do things but then actually
getting things down in to a real change to the spec. 


 
#### STAC API ([notes](notes/stac-api.md))
**Lead**: Josh Fix & Michael Smith


#### Static STAC ([notes](notes/static-stac.md))
**Lead**: Jeff Naus



#### Intro to STAC ([notes](notes/stac-beginners.md))


