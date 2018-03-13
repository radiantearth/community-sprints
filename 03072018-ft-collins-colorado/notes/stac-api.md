## Overview

This document contains the raw notes from the STAC API session, notes originally taken at http://board.net/p/stac-api-notes

The session was a followon from the STAC-WFS session, going deep in to fleshing out how the API would actually work while 
being a full WFS implementation. There was in depth discussion about the various endpoints, and how to handle simple transactions
and querying.

#### Search Endpoint

A main decision to combine WFS and STAC is to make it so the main STAC addition is a cross-collection search. STAC users just
want records, they don't care that they came from different defined collections. This actually helped a core discussion about
POST, since the semantics of POST on the ```/items/``` endpoint imply a new feature, while STAC API originally defined it as
a search. But the semantics of POST on a ```/search/``` endpoint seem to imply that it's posting a search. 

The group decided that the POST should be the primary recommended way to search. GET will be an optional addition, but its 
parameters will be the exact same as the POST. 

It will have top level keys of BBOX, Time and Limit. 'Filter' as a top level 'name' will go away, in favor of just including
the actual name of the filters. Work will be done in the next couple weeks by Tim to flesh out what that query language
looks like, putting some stakes in the ground for numbers and test queries. It will be in line with what Kasey 
present for Planet - something inspired from mongo / elastic.

#### Transactions

Transactions will be done against the /collections/ endpoint, in line with WFS. This should be published as an 'extension' 
(not required to implement), to both STAC and WFS. Once it's a full WFS extension STAC can just say 'see this for transactions'

#### API Document & spec

One of the bigger things with the shift to being a WFS is that we can't just publish a single OpenAPI document, it has to be
an 'example' of how one can implement. The 'collections' resources for STAC can still be anything. STAC just says that there
should be an additional search endpoint, with required parameters, that does a search across items in its collections.

A 'naive' STAC implementation would be just a single WFS collection without a schema, and the search endpoint would just
search it in the same way. But implementations that want to be strongly typed can put more in collections. A nice feature is
that non-asset data, like normal vectors, can easily fit in to the WFS, and then it's just not searched across STAC.

STAC will also enable search extensions, like for earth observation, that specify additional parameters to search on.


## Raw Notes

Started with STAC defines GET, does not have search end point. We are expecting one through conformance with WFS.

Putting forward primary way is POST for search end point, GET is secondary. Focusing on discussion for POST, but not worried about all the other stuff.
   
   Not saying it's not required.
   
   POST has a JSON object, mapped to query parameters. So it's the same parsing internally.
   CH wants to be sure there is one required, seems like momentum for that to be POST.
   support one to one same query parameters on GET.
     
   Top level keys in POST:

  BBOX

  Time

  Limit


  Removing filter as a top level 'name', 


  How do you know which ones to do? 

  - Currently have traitsets for different kinds of properties available.

  - Need a similar way to specify filters, may be different.

  - CQL implementation could be defined as a parameter on search. 

     - but many will not be able to do that.




  Good follow on from EO.


  Goal is to get to an 'example' OpenAPI schema, with the OpenAPI 'fragments' that extend WFS 3 core, as well as a good narrative doc.

  - Josh and Tim to take on. 


  In WFS paradigm for stac the recommendation is that different sensors / traitsets go under 'collections'. They are strongly typed with schemas. And then /search/stac is the end point that lets

  you search everything, do it cross collection.


  A 'naive' WFS stac implementation could just contain a single WFS collection that is searched by the /stac endpoint. If it is heterogenous then it can just leave off the schema stuff.


  Transactions - post, put, delete go in to collections


  Query language - do gt / lte


  How to handle swagger fragments. Can get it with /api - it's full union of all the frragments. 


  Make schema definitions for right hand side of filters. Example of how to do an extension, to add two more parameters. 


  Put stake in a ground for numbers, text string
