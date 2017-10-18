### Overview

AKA 'level 0', aka 'no code catalog'


To make imagery catalogs as accessible as possible we should have a version that other advanced catalogs can just 'crawl'. 
It should be possible to implement it with no interactive code, not even AWS Lambda. A user should be able to just put core imagery metadata with cloud optimized geotiff's on S3 and set up links to be crawled. 
For example Landsat PDS should be able to implement the spec, without standing up a server. This team should also 
investigate the HTML version of imagery metadata records, to follow [Spatial Data on the Web Best Practices](https://www.w3.org/TR/sdw-bp/) from WC3 
(which will be more crawlable by search engines). Ideally it's a very trimmed version of the main spec.
 
### Goals

**Day 1:** A specification for the link structure of a catalog that does not need code to run, and can be easily crawled. With a default type decided by the group. JSON, HTML, JSON-LD?

**Day 3:** Decide on a solid name for this, with a clear spec, that is aligned with main specs (api + metadata). Stand up an example implementation with data to be crawled (can just use landsat or OAM data).

**Stretch goals / Follow up:** Get a full dataset on AWS or GCP (like Landsat, NAIP, Open Aerial Map, etc) represented in this crawlable structure, including generating this on new updates.

 
### Questions to discuss

* Do we want to optimize for internet search engines? This would likely mean HTML as the main format, and ideally even
figure out SEO for it.

* What is the default / recommended 'best practice' format - HTML or JSON?

* Should we try to make it [Linked Data](https://www.w3.org/standards/semanticweb/data)? Or at least a light weight with [JSON-LD](https://json-ld.org/) with a published schema? The [metadata](core-imagery-metadata.md) workstream will also
hopefully be investigating this deeply.

* Specify in OpenAPI 3.0? And a swagger 2.0 version? Can it be a clean subset of the core api? This will need dialog with
them the [core api workstream](core-api-mechanics.md).

* What is the core link structure, to direct crawlers to all the resources? Do catalog items link to one another? Are there
pages for large catalogs? 

* Are the core catalog items the exact same as a fully featured api? Or a subset? Are there less links? etc.

* What does the HTML version look like? Does it have a thumbnail? What does it look like? 



 
### Background Reading / Prep work
 
#### Top

 
#### All


#### Above and Beyond

 
### Participants

 
### Notes 
(link to etherpad)
