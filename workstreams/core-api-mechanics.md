### Overview

This will be the core API specification, with eventual input from the other groups. Ideally the API mechanics are 
flexible to handle content from any vendor with whatever fields they want, and there's a way that they can be 
self-describing for clients to make sense of them. This group should also investigate breaking out reusable components 
like queries, filtering, and whatever small loosely coupled pieces could be reused in other services (like statistics, 
rendering tiles of footprints, etc). Ideally it's also evaluating the OpenAPI specs of WFS 3.0 and giving feedback to 
that, to see if this could be compatible. People who have designed and built imagery search API's are ideal here. 
Depending on interest we may also break out Query / Filter components in to its own group, or just make this group larger 
and give it the option to break out.

 
### Goals

**Day 1:** Get to an swagger 2.0 specification of a solid API structure, ready to incorporate metadata fields from core imagery 
metadata workstream. Ideally there is also a way to define a vendor specific set of fields using the same API structure.

**Day 3:** An OpenAPI 3.0 version of the specification that is validated by running code. With coherent granular components 
also defined as OpenAPI snippets that can be reused. Plus feedback to WFS 3.0 group of what works and doesn't in their spec. Also a solid name for the specification, and a clear mechanism for reporting / validating the metadata schema.

**Stretch goals / Follow up:** 
* 3 working servers and 2 working clients (and aiming for 7+ servers and 4+ clients in 3 months)
* A test engine that can validate specification compliance
* Solid schema definition in a good online location, that can be validated against.

 
### Questions to discuss

* How can we make the metadata fields returned be self-describing, for people to make it an imagery catalog that 
isn’t using the core fields. Like a vendor would be able to use the same API mechanism, but put in their own fields, and have
a smart client be able to actually filter on those metadata fields.

* GET vs POST for queries, especially geometries. Do we just support one or both? Should definitely make one the default. 
Geometries can be over the GET limit, so what is the strategy for enabling that? Link to a posted geometry? Named places / catalog that provides common shapes?

* HTTP Codes for responses, how to make them informative. What are the recommended best practices and important codes to use?
This may end up more as a 'guide' for people who aren't up to speed on this (which includes most Geo people as OGC standards
didn't do much leveraging of HTTP Codes)

* Paging - What's the default page size? Are overrides possible? If so what's the range of size?

* Links, what do the defaults look like? What additional links might people want to have? How do we enable download?

* Thumbnails - required? Set size? Let people size thumbnails? 

* What are the reusable components that might be interesting constructs for other specifications, or extensions. What have 
people seen that they've reused, or wanted to reuse, in other API's.

* Filters - what is the mechanism to filter by fields (buildings taller than 10 stories, images in delaware). 
Describe in BNF notation? GET vs POST? 

* Query mechansim - How do you specify additional query configuration past just the filter? What options do people want to specify in their queries?

* Cross catalog searches - Can you search common metadata and vendor specific metadata in one search? 

* Evaluation of WFS 3.0 spec components, feedback to them.

* GRPC version of spec? What would that look like? Should we specify it as well?

* Projections - only return records in one projection? Reprojection as an extension? How to handle data that is delivered in different projections?

* How can the user specify a bbox query that crosses the anti-meridian?  Could define bbox as (westLon, southLat, eastLon, northLat)

* Should geometry queries be performed on a flat earth or a sphere? It affects how a bbox query behaves and what a radius search means.

* Streaming - Could the api support streaming the results rather than pagination for clients that apply their own 

* List and Sets - Support for lists in the result set using a native format rather use putting things into csv strings.

* Configurable fields returned -  What if a user only wants id and title and to exclude the large the fields like footprint?

* Mutliple images in one file - how to represent that a file that contains multiple distinct imagery, E.g., NITF

* One image split into multiple files  - how to group imagery into a logical image when there are multiple physical files

* How might derived products be linked with the original image?  E.g., Dem product of LIDAR

* What do we call this specification? 

* Schema - Is there a way to report global schemas, or at least adherence to a global schema? How can we know that one catalog's 'cloud cover' means the same thing as another's, and that they use the same range (0 - 100 vs 0 - 1). 
 
### Background Reading / Prep work
 
#### Top
Read up on all the implementations in <https://github.com/radiantearth/catalog-api-spec/tree/dev/implementations>

#### All
Read [Google's API Design Guide](https://cloud.google.com/apis/design/), [JSON-API](http://jsonapi.org/) and other anti-[bikeshedding](http://bikeshed.org/) tools (feel free to add more to this list).

#### Above and Beyond
Set up a dev environment and start trying to build draft API's. Join <https://gitter.im/Imagery-Catalog-API-Team/presprint-planning> 
to discuss attempts to build with others.

 
### Participants
* Josh Fix, Boundless
* Paul Wideman, Hexagon Geospatial / Erdas Apollo
* Kasey Kirkham, Planet
* Matt Hancher, Google / Earth Engine
* Alex Kaminsky, Azavea / RasterFoundry
* Jason Gilman, Element84
* Jeff Naus, DigitalGlobe
* Ryan Osial, Pixia


(Yes, this group is a bit large, if it feels to large it should break out, perhaps one on core granular components, one on overall api for imagery)
 
### Notes 
Use https://board.net/p/core-api-mechanics for collaborative note taking. Please take great notes! This will enable those who want to collaborate with us in the future to be aware of all the initial discussions.
