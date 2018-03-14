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

The main goal was to align the [STAC API](https://github.com/radiantearth/stac-spec/tree/dev/api-spec), which the team
made great progress on. Having the WFS spec editors in the room at the end really helped make a great interchange, and
both specs should be stronger as a result. STAC will be an opinionated set of WFS options, with a couple extensions. The 
main one is to enable cross 'collection' search, as STAC users expect to search all imagery, not just a particular collection.
So an additional search endpoint will be added as a WFS extension. STAC will also likely help push forward some particular
WFS extensions, like simple transactions and the query language.

##### Earth Observation 'profile'
([summary and notes](notes/stac-eo.md))

The other session on wednesday was talking about additional metadata fields for catalogs that are serving up satellite imagery
and related products. The core STAC fields aimed to not preclude any data, but most of the providers have fields like 
'cloud cover', 'off nadir angle' and 'sun elevation'. So to help interoperability this group aimed to standardize that set
of additional fields. It turned out most fields are more at the 'collection' level, and having them all at an Item level would
mean a lot of repetition. So the group pushed towards an 'asset definition' where more common metadata could live. This also
lead to some improvements in the core spec, like changing the 'assets' from an array to a dict.

#### STAC Day

##### Introductions

Chris Holmes on behalf of Radiant Earth and Scott Simmons of OGC welcomed the participants, covered logistics and laid out the 
agenda and  goals for the day. The aim was to improve the specification in real concrete ways, informed by the implementation 
work people had done so far. To keep things out of the abstract and ground them in what has been built or could be added 
without too much work. The win of aligning WFS and STAC was also celebrated. From there the group went straight in to 
presentations by everyone who had built STAC implementations in the past four months.

###### STAC implementation Presentations 
([summary and notes](notes/presentations.md))

This session went deep in to all the work various organizations have done for the past few months. **Harris** built a full
prototype with node.js and elastic search serving up landsat data, and has also started incorprating STAC in to a 
production-oriented catalog project they've been working on for awhile. **DigitalGlobe** has been working with static 
STAC's internally, including some cool experiments with buiding quadkeys to make it searchable with no moving parts. 
**Boundless** has a reactive Java server with a number of extensions including simple transactions, gRPC and Kafka bindings,
and 5 different content extensions in a hierarchical model. **Planet** has been using STAC ideas internally, and showed 
a [Go client](http://github.com/planet/go-stac) that can generate schemas and do validation, along with a hand built static 
STAC. **Azavea** shared a [python library](https://github.com/raster-foundry/pystac) that they used to generate a [static 
catalog of IServ data](https://s3-us-west-2.amazonaws.com/radiant-nasa-iserv/iserv.json) hosted by **RadiantEarth**. 
**DevSeed** talked about [sat-api](https://github.com/sat-utils/sat-api) and [sat-search](https://github.com/sat-utils/sat-search) which will both soon be adapted to STAC. And **Pixia** shared their internal catalog work that is getting up to speed 
with STAC and WFS 3.

#### Groupwide discussions 
([summary and notes](notes/group-discussion.md))

The whole group spent about an hour on cross cutting topics, making a number of concrete decisions to improve the specification. 

* It was decided to move thumbnails from 'links' to 'assets', and also to make them not required (though strongly recommended)
* Some decisions from the [EO profile](notes/stac-eo.md) were presented to the group. One was moving 'assets' from an array
to a 'dict', so keys could be used for lookup. And the notion of an 'asset definition' file was also discussed. Both were 
accepted by the group as good ideas, and will become part of the spec.
* Deep discussion on the naming of time fields went through several iterations and emerged on simplifying the core time field
to a single field.
* Relative vs absolute links were discussed. The group punted on specifying everything with them, but agreed that the 'self'
link at the very least should be required to be absolute.
* Naming of profiles / extension - no real conclusion was reached on how to refer to the schemas vendors and communities make, 
though 'traits' and 'traitsets' were popular ideas.

#### Breakout groups

Three breakout groups delved deeper in to various aspects of the specification.

##### STAC API 
([summary and notes](notes/stac-api.md))

Discussion continued from the [STAC + WFS session](notes/wfs-stac.md), getting into all the details about endpoints. The
group dug deep in to query languages and transactions.


#### Static STAC 
([summary and notes](notes/static-stac.md))

The group had a good session, diving deep in to how to make static STAC's and STAC API's be 'crawl compatible' - enabling
a naive crawler to easily crawl both. The group actually decided that doing it on JSON is too hard to achieve, without
massive changes that would lose advantages somewhere. But stepping back it was realized that the goal of crawling was for
search engines, which crawl HTML. So the next focus will be on making the HTML output of each be crawlable. Also examined
was offline usage and syncing.

#### Beginners Luck
 ([summary and notes](notes/stac-beginners.md))

A group of participants who were new to STAC had a session exploring the spec and thinking about where it could all lead.

#### Wrap up

The day wrapped up a bit early, since the group had all been going quite hard the previous two days on WFS. But everyone
felt great about the decisions made and the progress on STAC overall. The STAC day and collaborations with WFS were a big
success, and we should see lots of great improvements. The group hopes to come together in a few months, to continue
momentum. 

