## Introduction

This document serves as a summary of the work done at the boulder sprint. It was a 3 day event, bringing together
24 people from 14 different organizations, aimed at collaboration around specifications that increase the interoperability of
finding imagery and other captured geospatial information. See [sprint-background](sprint-background.md) for more details on the
background, goals, prep work and organizations involved.

## Day 1

### Opening & Welcome

The first day opened with a welcome by Dan Lopez, the CTO of Radiant Earth. Radiant was the convening sponsor of the event, and
Dan told the group about Radiant's goals and work. They are working to actively support open standards for imagery, particularly
to help NGO's. He showed their progress towards a platform for imagery, focused on disaster and developing world use cases.
It's built on [RasterFoundry](http://rasterfoundry.com), and will provide additional functionality. Radiant is also working
to form 'technical working groups' focused on various topics, lead by 'technical fellows'. 

Chris Holmes then went a bit deeper in to the task at hand. Everyone introduced themselves, where they were coming from, and
also shared a standard they loved and one they hated. There was some negativity around XML standards, but also some professing
love for XML, but less enthusiasm for all the things people have tried to add on top of it. Everyone acknolwedged where the 
XML ecosystem has evolved as a warning for our spec efforts - that JSON will not solve problems because it is simple now. 
It's just as easy to put all kinds of additional complexity on top of that simple core. And it's tempting to just port some
ideas straight from the XML world. It was agreed that the core of XML is still quite good. 

The other standards that attracted negativity were OGC standards in general. It was agreed that the core of OGC started
well, but they've just added more over the years, and have been less and less focused on developers. There were a higher
portion of people who code every day than at most standards meetings, which was a deliberate goal of bringing this group 
together. On the positive side a number of people indicated positive feelings towards swagger and its evolution to 
OpenAPI.

Chris then presented on a philosophy of standards creation, mostly drawn from the [principles](https://github.com/radiantearth/catalog-api-spec/blob/178c817220f9ca113cd380271b2649623ac7ac39/principles.md)
document that he wrote for the repository to work on the standards. He also highlighted why the timing for this set of 
work around standards felt so right. And also shared with the group recent progress by OGC on embracing more of the 
open collaboration tools that the sprint group took for granted, like using OpenAPI to specify API's and github
to work together online. They are working on a new approach to the Web Feature Service 3.0, rebooting the core to 
be much simpler and more implementable. And then he closed with some aspirations for the group - to actually ship functional
specifications, to be transparent with the work done through great notes, and to set an example of collaboration of how
companies can come together, and use the latest tools to get real work done.

### Lightning Talks

The next session was a set of lightning talks by most all the organizations involved. Decks that people used will be posted 
online. Going through each presentation exhaustively is probably a bit much. But the session was really valuable to get
everyone on the same page, and understanding the perspectives that everyone else was coming from. Overall most everyone
seemed pleasantly surprised with how close the different groups were already aligned. JSON and REST were definitely
a common theme in just about every presentation, so that was easily established as a baseline to work with. The technology
ran the gamut, from Java and relational database backends like Oracle, to Python and Go talking to ElasticSearch, and then
JVM languages like Scala and Clojure. ElasticSearch seemed to be the most common technology for people building catalogs
recently, with spatial database backends for those who have been in production for awhile. ElasticSearch seemed to solve
a number of problems initially, but those who have been running large ElasticSearch clusters have been looking for alternatives,
as maintaining large clusters is a pain, and there's little managed options that can handle the geospatial extensions, or
even the amount of data. 

There were good messages about focusing on both API clients and end-users, to get the design right - a few instances of people
building 'the perfect server' to only find that it wasn't meeting user needs. Element84 showed some nice features in their
catalog to do 'faceting' - giving narrowed searches based on categories the user had picked - and doing it on the server side. 
They found that it was best to enable clients to rely on the server, instead of baking lots of logic in to the client. ENVI 
also emphasized the importance of focusing on the user - they care about an area of interest, not about where your satellite
happened to take an image. And they also want answers, not data. So how can we as a group support that new user to imagery, 
by not making them figure out all the obscure stuff our community knows to work with imagery.

The other major thread that emerged from the talks was that to be a lot more useful the API should index far more than 
just imagery. Imagery should be a profile in the catalog, but don't make a bunch of fields specific to it required. If 
done well the API should be able to index derived data (like NDVI), point clouds, video, etc. People also raised that 
imagery can be indexed in lots of different ways - in individual files, in scenes that may be several files representing
bands and sidecar info like UDM's, in granules, in different groupings, and as part of mosaics. So we need to work out what 
level of abstraction is being searched and indexed.

There was also good discussion of making catalogs that don't do indexing but never fall over - just files on really secure
buckets. Both Amazon and DigitalGlobe brought this up, and others agreed it was a good pattern. It was aligned with the
workstream that was set up to look in to flat files, but it started to become clear that this should really be the core, not
an alternative.

But overall there was a lot more agreement and consensus than there was disagreement. The session took longer than planned,
but the discussion was very good so it seemed silly to cut people off when there was such good engagement.

### Afternoon

Since the lightning talks took longer and then the group went straigh into lunch the group decided to do less of a big 'goals'
session and to more dive in to the working groups. Nate from Humanitarian OpenStreetMap presented some themes that he saw from 
the group:

* flat file infrastructure. This is a good thing and what we want to pursue.
* scenes, images, groups. How do we define these? 
* data services spec vs catalog spec. Do we want a layer below a catalog that provides what we need instead of a catalog API
* json vs xml - consensus on JSON
* core for search and then add on more as extensions
* keep emphasis on user-centered; design for clients; they should drive the spec 

From there people broke up in to the various [workstreams](workstreams/) - 4 groups that had between 5 and 8 people each, so 
that deeper conversation could happen without slowing down the whole group. The energy during this portion was high, as
people were hungry to get to work. The 'static catalog' group (who did a nice renaming from 'flat file catalog' to static catalog
dove in to implementation sooner than anybody, writing out specs and even starting to code, to flesh out the ideas. The 
extensions team explored both content extensions and operation extensions. And the core api mechanics team got started on 
an OpenAPI 2.0 spec, but also needed to dive deep in to some fundamental alignment on approach. The core metadata group went
deep quickly, building the schema of data.

After a couple hours there was a group-wide check-in, to see if groups needed input from other groups. The core metadata 
group got up and presented their work, as the others wanted to start to incorporate it. This lead to a good early course
correction, as the metadata group went really detailed in to satellite imagery, in a way that would have precluded other
types of searches. So they were given feedback to get down to a really tight core that would be relevant to all geospatial
data with location and time. Another topic of discussion with all for the static catalog is whether JSON or HTML should
be the core. The core group had solid arguments that it should be JSON, since it's for machines, and that should be
the default. But the group agreed it'd be really good to have best practice be to include HTML for humans. And to build
tools that automatically generate nice HTML that have lots of good links and hopefully even include dynamic tiling of
data in to openlayers and leaflet maps. And perhaps even on the fly generation of derived products using like RasterFoundry.

There were then a number of good iterations with everyone heads down, and just about every group got to some draft documents
and some even wrote some code. There are notes from each group in the [workstreams/](workstreams/) folders. 
The penultimate session brought the group back together to talk through the major issues that had come up. 

### OGC Presentation

The first day closed with a presentation from Scott Simmons, the lead of OGC's standards program, who updated the group on
the progress they've been making to be more open and developer friendly. They realized that their documents are often more
designed for lawyers than developers, with tons of boilerplate legalese on the top. It is important that it's all there, 
to be a true standard, but they want to start making the documents more accessible. A first step was just making all documents
available as HTML, with the option for deep linking, while before it was all PDF's that made it impossible to reference
a clause online. The next major step is to take a new approach of first building standards with and for developers, focusing
on the core API definitions instead of all the text around it. OGC is embracing OpenAPI in a big way, as the main way to
define the standards - starting with the developer interface, and then moving towards all the extra text others need. He announced that the WFS specification was just
approved to be open, on github, available in the [OGC WFS_FES repository](https://github.com/opengeospatial/WFS_FES), and it
even includes OpenAPI (both 3.0 and 2.0) specs as the main definition. 

The presentation is available from [the OGC website](https://portal.opengeospatial.org/files/?artifact_id=76330).

## Day 2

The second day was much more heads down, and there's less in the way of notes and presentations to peruse. But a bulk of the
real work was done on day 2, getting to real specifications and code. 

* [Core Metadata](workstreams/core-metadata/) continued to iterate on core fields that weren't tied to satellite imagery,
while also working towards the 'EO' (earth observation) profile. They ended up with a good 
[draft-spec](workstreams/core-metadata/draft-spec.md), and dialoged with the other groups.

* [Static Catalog](workstreams/static-catalog/) advanced their specification, examples and code to create static catalogs,
that can be crawled by search engines. They used NAIP data as a way to flesh out how it would all look. They group defined 
a number of [specs](specs/flat_file/) with examples, as well as a first crawler implementation in the [catalog-crawler](catalog-crawler/) folder.

* [Core API Mechanics](workstreams/core-api-mechanics) continued on core discussions and movd to define an OpenAPI 2.0 
definition for servers to implement. They got to a solid [draft spec](https://github.com/radiantearth/catalog-api-spec/blob/dev/spec/spec-draft-sprint-day-2.yaml) 
and even a first [implementation](https://github.com/radiantearth/catalog-api-spec/pull/18) serving as proxy to [NASA's CMR](https://cmr.earthdata.nasa.gov/search/).

* [Extensions](workstreams/core-api-mechanics) got in to implementation to try out some of the ideas they talked about. 
They built a [spec, samples and tools](https://github.com/radiantearth/boulder-sprint/tree/master/extensions) to show how 
the core could be extended to cover all the metadata providers like Planet and DigitalGlobe, as well as adding in tile 
serving as an extension.

Joint sessions throughout the day went deeper into cross group issues. One examined the core metadata, which went down to 
11 fields. There was lots of discussion if
we should aim for 5 fields - a really small core that everyone could fill out - or 11 that most people would. Then Seth
suggested that it's just 5 required and 6 more that are optional. After that the group looked through the 11 fields again
and managed to eliminate a few more of them. A couple were baking the 'product definition' in to the core, when it was
decided that the product information, like the sensor and the processing, belongs outside of the core - ideally it is
eventually a standard that specifies API end points and fields that fully explain all the processing and sensor information. 
But the decision was made to take it out of the core for now, to be added in when it is more fleshed out.

The other topic of discussion was 'contact', and if it should be a nested map of information, or if it should attempt to keep
it as flat fields, possibly multiple flat fields. The former would be hard for most GIS systems to read automatically, since
they expect flat information, though it could make a little mapped string. There was also discussion of using some structured
field in the string, like a URN, to specify it. No great consensus was reached, but everyone felt some sort of contact
field is core, though it needs a good way to get at it.

One thing that did emerge was the importance of the static catalogs. All the groups who had tried to reliably stand up huge
clusters with millions of records found that static files on cloud storage were really the only thing you could truly rely 
upon. And that creating indexes on those should not be a requirement to join the open sharing of information. Indeed they
see the core static catalogs as the core 'backup' to standing up the more active API's. With the static catalogs being so
important it was seen as high priority to make sure that the active querying API is fully compatible with the static catalog,
so that a naive client crawling either could treat them as the same. It was contemplated if the static catalog should be 
a requirement - that in order to guarantee uptime catalogs should always have a fallback version. That was seen as too
high a barrier to get many traditional services on board - it's quite easy for a Hexagon Apollo or Pixia to write a new
interface that returns the proper JSON, but shifting their whole system to depend on static files written out somewhere
would need to change how they work. But if the representations are the same between static and active catalogs then it
can open up cool possibilities, like a naive crawler that can do a 'backup' of an active catalog - just crawl it all and
rewrite to S3, and then you have the same catalog, that won't go down.

The static catalogs also let users choose the indexes they want. Someone can just stick the fields and geography they want in a local PostGIS
database and do very fast queries there. In general the group sees a world where indexes are instantiated on demand, as 
opposed to always maintained, and the core static data is the source of truth. Starting from this point also made clear that
'subscription', like a pub/sub or event stream extension, becomes pretty important. An active catalog that's powered by a
static catalog should not need to crawl the whole catalog every day to check for updates - it should be able to subscribe
to a feed of changes and then update its records appropriately. It's relatively easy to [configure s3 for 
notifications](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in SNS or SQS, so quick implementations 
of this should not be hard. But there should be several implementations in the world before we push to standardize.

Another important topic is extensions, particularly how vendors and communities can extend for their needs. The extension
group came up with some nice flexible mechanisms, using URN's that are flexible but not totally free form. Things divided
in to 'operations' and 'content', with more focus on the content, as it seemed quite important to get right. 

The day ended with some attempts to figure out naming. There was success on calling the core json that includes the metadata
an 'item'. We considered 'feature' (too general for any geographic type), 'record' (like a record of a catalog, felt a bit
too old school', 'scene' (too imagery focused) and others. But we decided on an 'item' as the best balance between being
flexible, with good connotations. And then 'asset' was settled on as the thing linked to. Contemplated just calling them 
'links', but decided that links should also be used for other things, and assets could be a bit more specific. Naming
the overall specs didn't make much progress however.

The room and lunch were sponsored by Planet, and then DigitalGlobe treated the participants to dinner and drinks at Avery
Brewery in Boulder.

## Day 3

Day 3 was a smaller group, as many people had to leave, and the goal was to have most everyone there the first two days
and have the third day be some continued work. The third day as that the DG office. There were a number of good conversations
diving deeper and getting in to details, with continued momentum from most all the groups.

### Morning Conversations

The main groupwide conversation for the morning was about how to represent asset metadata. This arose from a practical
concern when Rob was trying to represent NAIP data in an item. Each item has two assets to download - an RGB visual
one and an analytic RGB+NIR. And ideally a client could have some way to 'know' about the band information, so it 
could automatically apply algorithms. The question was whether to try to make a special 'asset metadata' that is
populated in each item to give more information about each asset. An alternate idea was to give each major asset
its own 'item', and then describe more nuanced relationships between items. So you could have a 'parent' item that
defines the footprint and is the thing that shows up in catalogs, and then there are some child items that have the
particular assets with more information about them. One potential advantage of this is that parents don't necessarily
have to know about all their children, but processed assets could easily refer to their parents. Though that doesn't
necessarily solve the core problem.

The group went in lots of different directions with this, and it was getting very abstract, so instead decided to have people
sit down and make examples of what they were thinking with a dataset that they knew. 

* The [naip example](specs/core-api/naip-example/) demonstrates the idea of child items with a relationship to the parent.
* The [landsat example](specs/core-api/landsat-example/landsat.json) shows inline band definition, with the landsat 1 band per asset.
* The [DG Tiles example](specs/core-api/dg-tiles-examples) shows how it might work with a scene defined by lots of sub-tiles
* The [DG example](https://github.com/radiantearth/boulder-sprint/tree/master/specs/core-api/dg-example) shows representing all the DG metadata and sidecar files.

Some work needs to be done to consolidate these in to a solid core model that works for everything.

The discussion hit on some other topics. One was the potential usefulness of 'rel' links. This lets you specify what the
'relation' of an entity is to what it is linking to. A very common one is 'self', where you link to the canonical location
of something online. This was deemed quite useful, so that items could be downloaded but always refer back to where they came
from. The research done during the day seemed to indicate that you can put  most anything you want in the 'rel', as there
was no authoritative list of rel's. So we could define 'asset', 'item', 'parent', 'child', derived-from' and other type
of relationships to link together the various parts of a catalog.

Another thing that came up was the notion of items that have lots of tiles that make them up. So like a 'colorado' item
that is composed of lots of different strips and scenes. The consensus was that those should be considered 'mosaics', and
we'll need a metadata profile to extend the core item metadata with mosiac specific data. And that the core earth imagery
items should limit themselves to more core 'scenes' instead of putting everything in it. And then the cool thing is that
a mosaic could refer to its source scenes with a special 'rel' link, so each scene is an item, that is part of the bigger
mosaic item

### Afternoon conversations

The afternoon was an even smaller group, and focused on the product and project management pieces of the project. Rough
notes from this section are at https://board.net/p/boulder-sprint-pm (volunteers welcome to move that to the github repo).

The first part of the conversation focused on the various followups to do. These include posting all the notes, getting the readmes of the various repos in good shape, putting issues onto github, getting to json examples and the core specification,
etc. It was decided to put static catalog, the queryable api and the json instantiation of the metadata spec all in the 
same repository, so that they could more easily stay up to date with one another. The abstract metadata spec would go 
in its own repo, so that it might get other instantiations, like a representation in Tiff tags. It was also deemed 
important to just have one github issues, and to turn issues off in other repos. A flow diagram rendering was also desired, 
though no one knew good tooling on github for that.

There was also discussion of the project management. Do we eventually get to an RFC / improvement proposal type process? The
consensus was yes, eventually, but that for now it'd be too heavyweight. There was a volunteer to write up some lighterweight
process to put in the repo, to be clear to people how to participate.

Another interesting topic was the notion of connecting all the catalogs together, which would be relatively easy to do
with how the core is designed. There was agreement that the interconnectivity of all catalogs shouldn't be emphasized - 
we don't want to try to get people to 'join the network' of having their data be searchable by all. We just want them
to implement a standard, which leads to much more interoperability. It was also pointed out that some people have
all their data on internal networks and want to keep it that way, and would never connect to the network. But that at 
some point it would be cool to connect all the pieces.

The final discussion of the day was a solid naming attempt, where each person thought of and wrote down names for a minute, passed them and repeated putting names on the paper they got, and then passed and circled the best too. It got lots of ideas
flowing, but nothing emerged as a clear winner.

## Post Conference success

Most of the post conference work will be documented in the actual wikis. But one big win was actually reaching consensus
of good names online, on the [gitter channel for the sprint](https://gitter.im/Imagery-Catalog-API-Team/Lobby). This is
promising, showing the potential of the group to work together not in person. The final naming is the Spatio-Temporal Asset Catalog. And then the core metadata fields are the Spatio-Temporal Asset metadata.
