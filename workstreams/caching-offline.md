### Overview

Make sure that the core spec is cachable, which may just be getting the cache control headers right, could be an 'update' 
field. But then explore how a second catalog could cache a master catalog, perhaps subscribing to an event stream to stay 
up to date, perhaps caching records and/or actual imagery. And how do records work in this situation, where data may live 
on one cloud but a local catalog copies the data for faster access, but wants to make it clear that it is only a copy. This 
group should also explore offline / disconnected scenarios - like how first responders might have a mini-catalog on their 
phone, or a deployed appliance of imagery that isn't connected to the network.
 
### Goals

**Day 1:** 

**Day 3:** 

**Stretch goals / Follow up:**

 
### Questions to discuss

* Pieces needed in core spec to make records cacheable.
    * Just cache control headers?
    * Also update / publish time as a field?
* Subscription extensions for push updates / event stream
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
