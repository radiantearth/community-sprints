### Overview

AKA 'level 0', aka 'no code catalog'


To make imagery catalogs as accessible as possible we should have a version that other advanced catalogs can just 'crawl'. 
It should be possible to implement it with no interactive code, not even AWS Lambda. A user should be able to just put core imagery metadata with cloud optimized geotiff's on S3 and set up links to be crawled. 
For example Landsat PDS should be able to implement the spec, without standing up a server. This team should also 
investigate the HTML version of imagery metadata records, to follow [Spatial Data on the Web Best Practices](https://www.w3.org/TR/sdw-bp/) from WC3 
(which will be more crawlable by search engines). Ideally it's a very trimmed version of the main spec.
 
### Goals

**Day 1:** A specification for the link structure of a catalog that does not need code to run, and can be easily crawled. With a default type decided by the group. JSON, HTML, etc

**Day 3:** Decide on a solid name for this, with a clear spec, that is aligned with main specs (api + metadata). Stand up an example implementation with data to be crawled (can just use landsat or OAM data).

**Stretch goals / Follow up:** Get a full dataset on AWS or GCP (like Landsat, NAIP, Open Aerial Map, etc) represented in this crawlable structure, including generating this on new updates.

 
### Questions to discuss

* Do we want to optimize for internet search engines? This would likely mean HTML as the main format, and ideally even
figure out SEO for it.

* What is the default / recommended 'best practice' format - HTML or JSON?

* Should we try to make it [Linked Data](https://www.w3.org/standards/semanticweb/data)? Or at least a light weight linked
data approach with [JSON-LD](https://json-ld.org/) with a published schema? The [metadata](core-imagery-metadata.md) 
workstream will alsohopefully be investigating this deeply.

* Specify in OpenAPI 3.0? And a swagger 2.0 version? Can it be a clean subset of the core api? This will need dialog with
them the [core api workstream](core-api-mechanics.md).

* What is the core link structure, to direct crawlers to all the resources? Do catalog items link to one another? Are there
pages for large catalogs? 

* Are the core catalog items the exact same as a fully featured api? Or a subset? Are there less links? etc.

* What does the HTML version look like? Does it have a thumbnail? Formatting? Links? 

* Do we want to try to make a registry? Or at least some way to publish links to catalogs? Like https://github.com/openimagerynetwork/oin-register/ Is that the right form? Something else? Should be simple, and OIN is probably a good start?

* Should we pick up and push Open Imagery Network more? As a registry of all openly licensed catalogs? Should we constrain
to 'level 0' catalogs, like the original? Or also let more advanced catalogs be part of the network? If the two are compatible
it could be cool to query the advanced catalogs with just a license=open (or a set of open licenses), to have DG, Planet, etc. 
return their openly licensed data records.

* What is the name of this thing? How closely do we brand it with the main catalog API spec? (probably depends in part how similar they are)

 
### Background Reading / Prep work
 
#### Top
Read the first three best practices in : [unique-ids](https://www.w3.org/TR/sdw-bp/#globally-unique-ids), [indexable by search engines](https://www.w3.org/TR/sdw-bp/#indexable-by-search-engines) and [linking](https://www.w3.org/TR/sdw-bp/#linking). Also read up on [Open Imagery Network](https://openimagerynetwork.github.io/) if you aren't already familiar.

 
#### All

Read the full [Spatial Data on the Web Best Practices](https://www.w3.org/TR/sdw-bp/). Dig in to the repos in Open Imagery
Network, and also get familiar with the structure of [Landsat PDS on AWS](https://aws.amazon.com/public-datasets/landsat/) as well as other public datasets, if you aren't already.

#### Above and Beyond

If at least a couple people could dive deep on what linked data in general and JSON-LD in particular could offer us in the way of schema definition that would be really great. It seems like it has potential, but also seems like the linked data advocates get way to deep in obscure architectures. Is there something practical there for us to use?

A proposed implementation or spec for this, for others to give feedback on.

If someone can turn the questions above to issues and link to them that would also be awesome.

 
### Participants
* Seth Fitzsimmons 
* Mark Korver
* Sasha Hart
* Beau Legeer
* Rob Emanuele
 
### Notes 
(link to etherpad)
