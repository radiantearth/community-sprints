### Overview

The main task of this group is to make sure that the core API has the proper extension mechanisms and core reusable components 
to apply to other problems. This should be a brainstorm, drawing on the types of options and services that might extend the 
core. Each does not need to be its own OpenAPI spec, but should be able fleshed out enough to figure out what extension points 
the core spec needs. And this group should also generally investigate how to report the 'capabilities' of a service that 
provides more than the core. A starting list of extensions would be transactions, statistics/aggregation, 'activation' of 
assets, coverage maps and additional metadata fields.

### Goals

**Day 1:** 

**Day 3:** 

**Stretch goals / Follow up:**

 
### Questions to discuss

* Extension mechanism
* Brainstorm on extensions (explore how they might work, and add more)
    * Assets and activation (Planet)
    * Stats
    * Coverage maps
    * Saved searches
    * Different fields
    * Transactions / catalog management
    * Subscription extensions for push updates / event stream
    * Links to tile servers of the data
    * Different format types (jp2, netcdf, etc)
    * Processing data on the fly (apply NDVI, surface reflectance)
    * Bulk download service
    * GRPC
 * In general how does a catalog work to make the core data available, but also can be transformed / processed.
 * Pieces needed in core spec to make records cacheable.
    * Just cache control headers?
    * Also update / publish time as a field?
 * Mobile catalog, is there a use case for running on a mobile device?
 * Disconnected scenario, shipping out hard drives of imagery with a catalog for first responders, etc.
    * How to refer back to source catalog?


 
### Background Reading / Prep work
 
#### Top

 
#### All


#### Above and Beyond

 
### Participants

 
### Notes 
(link to etherpad)
