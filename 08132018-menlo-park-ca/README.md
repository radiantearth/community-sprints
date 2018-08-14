## STAC Sprint #3

Taking place in Menlo Park, CA at USGS, as part of the Satellite Data Interoperability Workshop. 

Goals: 

* Work towards a stable 0.6.0 version of the spec based on resolving differences in existing implementations
* Create new data and software implementations, and align existing ones for full interoperability
    * And use these implementations to flesh out core changes and extensions needed
* Build and advance client libraries and test engines to exercise implementations

### Agenda

#### Tuesday

|**Time**|**Title**|**Description**|
|--------|------------|-------------------------------|
|9:00-9:30| Overview of Github Issues| Quick overview of the [stac-sprint-3-discuss](https://github.com/radiantearth/stac-spec/issues?q=is%3Aissue+is%3Aopen+label%3Astac-sprint-3-discuss) issues|
|9:30-11:45| Informal Presentations on Implementations | 5 minutes of content, up to 5 minutes of interspersed discussion. Share your implementation, what decisions you made about the spec, what you want to change, what you added.|
| | *STAC API’s* | *Harris, sat-api by DevSeed, NASA CMR Proxy by Element 84, Hexagon, Astraea* |
| | *Static STAC* | *CBERS (bridge with API), Spacenet, Google Earth Engine, DigitalGlobe, Planet, Azavea* |
| | *Clients* | *STAC Browser* | 
|10:20-10:40| **Break** | Coffee break, network with ARD folks|
|11:45-2:30| Small Group Sessions | Groups are formed to enable smaller discussions. Those with experience implementing the spec will be grouped to resolve specification issues, with github tickets assigned. Those who are newer to the spec can sprint on their own implementation or join an existing tool effort. See below for details on groups | 
|12:00-1:00| **Lunch** | Ideally small groups continue through lunch, or can break and network with other STAC and ARD people |
|2:30-2:50| Full Group Check-in | Check on status, report on progress, resolve any burning questions with the full group, figure out if we need to shift small groups |
|2:50-5:20| Small Group Sessions (continued)|Keep working in small groups, updating stac-spec repo|
|3:30-5:00| **Open STAC Session OPEN TO ALL!** | **OPEN TO ALL ARD ATTENDEES** Deep Dive on STAC overview, Q&A on how to use STAC, and show and tell of leading STAC implementations. A small group of STAC sprinters will present in an alternate room that anyone from the ARD tracks is welcome to attend and learn more. *Presented by Chris Holmes, Michael Smith, Frederico Liporace, Seth Fitzsimmons and others* |
|5:20-6:00| Review of Pull Requests with full group | Check in on progress on the [stac-sprint-3-discuss](https://github.com/radiantearth/stac-spec/issues?q=is%3Aissue+is%3Aopen+label%3Astac-sprint-3-discuss), with quick feedback, so we can get everyone thinking about them for discussion with everyone on Wednesday|

#### Wednesday

|**Time**|**Title**|**Description**|
|--------|------------|-------------------------------|
|9:00 - 11:00 | Full Group Spec Discussion| Review Pull Requests and their related discussions from the previous day, resolve differences and assign leads to move each aspect forward.|
|11:00 - 2:30| Small Group Sessions|Break in to small groups as makes sense from full group discussions, to move forward on writing up and making Pull Requests on the issues discussed.|
|12:00 - 1:00| Lunch|Ideally small groups continue through lunch, or can break and network with other STAC and ARD people|
|2:30 - 4:00| End With Delivery|Core group shifts to direct specification work – reviewing and merging pull requests, updating the spec copy, preparing for release, etc. Small group sessions on implementations continue, to be able to demo.|
|4:00 - 5:00|Demo Session & Wrap up| Everyone shows what they worked on during the sprint. Close with commitments on what people will continue to work on after.|

See https://github.com/radiantearth/community-sprints/raw/master/08132018-menlo-park-ca/Satellite%20Data%20Interoperability%20Workshop%20%20-%20Technical%20Program.pdf for day two (will port over to be here, and a pull request to include it is *much* appreciated)


### Small Groups

The majority of the time in the STAC sprint will be heads down working on advancing the specification or coding on 
implementations and supporting libraries. The 'spec advances' groups will be limited to those who have actually implemented 
the specification, so we can have conversations that are very grounded in the reality of implementing, instead of theoretical 
ideas of how the spec *could* advance. Such conversations will definitely happen in the evenings, but we want to keep our 
sprint focused on concrete steps forward.

These groups our tentative, and we'll form them when the time comes. But the aim is to have no more than 5 people in any one group, for efficient parallel conversations.

#### Static STAC Spec Advances 

Implementers of Static STACs will gather to compare their implementation notes, and discover where they differed. 
The core of the static spec needs a refresh, particularly in aligning with 'validation', and really fleshing out 
what each fields means. Should discuss relative vs absolute links – if we can align on one. Also the organization of 
sub-catalogs, if we want to make any recommendations. The group should also touch on what formats people used, and what 
recommendations on link types and asset definitions could be standardized. The group is also encouraged to explore additional
fields that can drive STAC Browser to make it more useful / interesting. A final topic is 'crawlability' – how to get google 
and other search engines to use pages generated by STAC Browser or other tools to index STAC Items. 

**People**: Michael Smith, Tim Rutherford, Alireza Jazayeri, Paul Wideman, Jason Gilman

#### STAC API Spec Advances 

There are a few solid STAC API implementations, but they've made some different choices. The group will discuss and resolve
those differences, and explore any extensions needed. A topic of top priority is alignment with WFS3, what is needed to stay 
aligned, or where we want to make Pull Requests to the WFS3 repo to align with how we are working. The query / filter language
is of particular interest. The group should also touch on what formats people used, and what recommendations on link types and 
asset definitions could be standardized. A stretch goal would be to explore how STAC Browser could be compatible with STAC 
API's – what to change in the spec or in the browser implementation to align.

**People**: Frederico Liporace, Chris Brown, Damien Ayers, David Lindenbaum, Jeff Naus

#### Client & Testing Tools

Now that there are a number of STAC server implementations it'd be good to get more clients. A key step is to get a validating 
client that can serve as a test engine, so that clients can expect consistent responses. There have been a couple javascript 
implementations. It'd be great to sprint to advance any number of those clients, as well as explore things like GDAL/OGR 
compatibility, QGIS support, OpenLayers/Leaflet, etc. WFS3 is working in OGR, so testing it against the existing STAC server 
implementations would be great. And recommending to the implementations what they need to be compliant, or extending OGR, 
would be awesome. 

**People**: Guillaume Morin, Alex Mandel, Seth Fitzsimmons, Wes Richardet

#### Collection Level Searching

One topic of interest, especially from OpenEO and Google Earth Engine, has been the search of collections, instead of within a 
collection. STAC is focused on search within a collection, but it includes some simple constructs to catalog collections. The 
ideal is an independent spec that STAC uses, and GEE and OpenEO can also use, to describe collections in a lightweight way. 
Ideally this aligns with other efforts like DCAT, CAT 4.0 and WFS 3.0

**People**: Simon Ilyushchenko, Matthias Mohr, Justin Poehnelt, Rinkal Patel

#### Spec Editing / Website / Outreach

Another way people can help advance the spec is reading it over and fixing any inconsistencies and errors. And ideally helping explain better how it works within the spec, with more examples / samples, etc. People are also welcome to sprint on making a website to explain STAC, or on other 'outreach' tasks like tutorials or blog posts to help raise STAC's awareness.

**People**: Chris Holmes, Karla King, David Gavin

#### Sprint on your own implementation 

Some participants have not managed to find the time to build their own implementation, but are excited for some dedicated time during the sprint to work. They are encouraged to, and to ask for help from those around who have already implemented.

**People**: Simeon Fitch, Kirk Larsen

#### Unassigned

*Currently Unassigned people*: , , Tom Jones, Tanushree Biswas, Jeremy Schoos

