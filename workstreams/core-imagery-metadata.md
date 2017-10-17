### Overview
 
The starting point for this is OIN-metadata and the Radiant draft Imagery Metadata Spec. The goal is to get to a core set of metadata fields that power the main API, as a lowest common denominator everyone can support. Will also explore extension mechanisms (how vendors can use the core fields and add in their own, and how to get more specific additional common fields), schema description + linked data, tracking provenance & duplications, and a number of smaller issues. Anyone deep in consuming lots of imagery is ideal for this group.
 
### Goals

**Day 1:** Get to an abstract and JSON specification of a primary metadata fields to enable effective search of imagery in catalogs. This should aim at the 80% of imagery, and should be focused on search - not on getting across every metadata field that advanced software might use. This will be used by the Core API group to build the first spec.

**Day 3:** By the end of the sprint should have a nice ‘extension’ mechanism that gives vendors and communities (for example ‘elevation’) a way to build on the core fields with additional metadata they care about. The core spec should be well documented, with good examples. 

**Stretch goals / Follow up:**
Have a dedicated website that has the core specification in html as well as one or two ‘guides’ on using it. And links to the spec, and how to give feedback to it and extend it.
Code and online service to validate conformance with the spec. 
HTML, Linked data and GeoTIFF version of the spec (if the group decides these are valuable).
 
### Questions to discuss

* What is the fewest number of fields for a simple core that we can get away with to be valuable to experts but also understandable by people new to geospatial + imagery?
* Single start date, vs acquisition start and end? All? https://github.com/radiantearth/imagery-metadata-spec/issues/17 
* https://github.com/radiantearth/imagery-metadata-spec/issues/18 
    * Versioning - semantic versioning? When to lock into a start and version? Do we do every change made in github? Or ‘releases’? 
    * Granule / scene vs ‘file’? How do we handle ‘level 0’ with that? Just a link to multiple files? 
    * ID’s - UUID vs SceneID vs ?  
    * Do we need a Title? 
    * Platform - general ‘type’ (satellite / uav), vs specific platform ‘landsat-8, aqua, planetscope’. How does 
    * this work for a random drone operator with a homebrew drone? What do we have them fill out? 
    * Sensor - do we want this plus platform? Will drone operators and others know what to do? 
    * How do we make this accessible to people with little imagery experience but who want to contribute data to OAM? Obviously it’s decently on OAM to get the user experience and fill out defaults well, but can we help?
* What is the extension mechanism to have a well specified core that can also be compatible with additional fields. It should be easily usable by many tools (not require lots of custom code), and also verifiable, like in a simple test engine. Do people just reuse the fields but have a different ‘document’ that refers to the same source for metadata ‘definitions’, that is a different api end-point? Or can they extend the same document to add their own fields and also be compliant?
* How to extend for a ‘community of interest’ instead of just a vendor. Like ‘elevation’ or ‘derived data’ or ‘mosaics’. Or even ‘drone’ and ‘satellite’, as they may have some specific fields that make sense for the class of providers, but not for the most general + flexible one.
* What would specific extensions for various domains look like? Elevation, mosaics, derived analytics, vendor specific records, etc.
* Will this handle other data types? SAR, hyperspectral, elevation, point clouds, etc?
‘Schema’ - how do we define a schema for this stuff? That is flexible to adapt, but also can be verified. Can we specify enumerations of fields (must select from uav, plane, balloon or satellite), but also make them flexible enough that people _could_ add their own. But so people who use ‘landsat8’ have a way to know everyone refers to the same landsat8? 
* Does JSON-LD and/or linked data in general have potential to help the above? Not necessarily getting all crazy with RDF, but setting up something like http://schema.org or http://purl.org/goodrelations/v1#
How can we track provenance in a simple way? Like to describe a processed image (like NDVI), and have it refer back to the source image it came from? Or for a mosaic to link back to all the catalog items that went into it? This feels very important as we get to cloud processing and want to also have the derived data products in catalogs (many would likely use same API mechanisms but different metadata profiles).
* How do we handle and track record duplication? Ideally there is just one catalog record for each ‘item’ online, but it’s also may be useful to have local indexes of other catalogs. How can a record describe itself as a duplicate and refer back to a ‘canonical’ one. Is this valuable or overkill?
* How do we handle and track data duplication. Landsat is on USGS, Amazon and Google Cloud. Do we represent the additional data as mirrors? Provide links to all of them from the main imagery item record? Or have mirror catalogs that refer to both the mirror data and the source data? The mirror catalogs are likely valuable for local cloud access. (These catalogs may be ‘level 0’, none interactive, just sidecar data).
* Licensing - can we get to a core standard set. An enumeration instead of a totally open string? To help nudge people towards a more limited set of options. Does it make sense to get to linking to license terms? Or maybe this is something schema definitions can help with?

 
### Background Reading / Prep work
 
**Top:** Please contribute any good imagery metadata files you’ve worked with to https://github.com/radiantearth/imagery-metadata-spec/tree/dev/non-standard-implementations. Ideally JSON, but others also accepted.
 
**All:** Everyone in this group should read over all the implementations https://github.com/radiantearth/imagery-metadata-spec/tree/dev/non-standard-implementations 
 
If at least a couple people could dive deep on what linked data in general and JSON-LD in particular could offer us in the way of schema definition that would be really great. It seems like it has potential, but also seems like the linked data advocates get way to deep in obscure architectures. Is there something practical there for us to use?
 
### Participants
 
* Paul Smith, Harris
* Rob Emanuele, Azavea / GeoTrellis
* Nate Smith, HOT / OAM
* Matt Hanson, DevSeed / sat-api
 
### Notes (link to etherpad)
