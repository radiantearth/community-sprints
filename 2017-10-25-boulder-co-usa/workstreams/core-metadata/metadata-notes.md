## **GOALS**

**Day 1:** Get to an abstract and JSON specification of a primary metadata fields to enable effective search of imagery in catalogs. This should aim at the 80% of imagery, and should be focused on search - not on getting across every metadata field that advanced software might use. This will be used by the Core API group to build the first spec core 

Why not use another standard?  What is not applicable?   Examples:

*   CMR  mulitple standards to deal with (backwards compliant).  May have awkward usabilty aspects.  Was not designed from a user perspective. 
*   OAM spec - search oriented spec.  Other items associated with properties.

The goal is to have one that is simple and allows for extensions.  This metadata core is focused on what is needed for the API.

**Day 3:** By the end of the sprint should have a nice ‘extension’ mechanism that gives vendors and communities (for example ‘elevation’) a way to build on the core fields with additional metadata they care about. The core spec should be well documented, with good examples.

## **NOTES**

Discussion about goals: 

*   questions about search vs usability/extension
*   agreement that search is the driver of the core

we need common language 

how much do we need another standard? 

stretch goal: implementation profile for geotiff 

why not use an existing standard? 

*   what is it about those?
    *   CMR at least 4 metadata versions that needed to be dealt with
        *   uses UMM to map between these formats 
        *   extended UMM
    *   issues about CMR
        *   metadata naming details a big issue
        *   humanizers help fix the metadata 
        *   providers didn't go back and fix it
    *   preservation vs serach and use -- keep everything
    *   search and use may vary by product as well as by use 

are we talking about raw or corrected? 

type of product is useful core data 

making sure a descriptor is part of the spec 

review of the OIN / proposed spec

nominal date should be included

may need to include resolution + gsd 

say nominal_gsd 

platform discussion: 

*   platform
*   instrument
*   sensor
*   & type
*   platform is the specific name for the platform that the sensor is on 
    *   some not convinced that we need to separate instru and sensor
    *   agreed: platform_type, platform, instrument, product, processing level

bands -- may need a dictionary for common names 

video?

band_map maps band numbers to comman band names (optional)

accuracy -- should be second order. sometimes its not available 

sun angle -- is this relevant for core? 

*   probably for an extension 

projection -- what's a good term for it?

*   SRS/CRS in WKT
*   format -- 

footprint and bbox

*   1 bbox - in lat/lon 
*   1 footprint - in WKT in SRS 

version - of the spec

revision of the record 

product_version - of the data 

cloud cover

*   per scene, since it's common enough 
*   should be included in the 

links

*   links to docs, use, other resources 

naming: 

    image -- 

    scene -- 

    collection -- 

[](http://board.net/p/metadata-spec)[http://board.net/p/metadata-spec](http://board.net/p/metadata-spec)