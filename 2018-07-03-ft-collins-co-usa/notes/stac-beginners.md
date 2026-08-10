## Overview

This session was for people who had not been exposed to STAC before, but came to the day as a follow on from 
the WFS 3 hackathon. Raw notes at http://board.net/p/BeginnersLuck, and pasted in below.

The team reached many of the same places as the original STAC group. Indeed they realized that all catalogs
could pretty easily be connected to be one global catalog, which is certainly a long term aspiration of STAC, though
the immediate goal is to just get more data in STAC. 

There was exploration of what federating data would look like, keeping catalogs in sync. And from there some 
interesting discussion about provenance - tracking where data came from.

And then some interest in p2p technology, and things like ipfs.

## Raw notes


The namespace indications are not clear  for example the eo and l8,  we know that eo is earth observation and l8 is landsat but we need a link to namespace defintion (https://github.com/radiantearth/stac-spec/blob/dev/static-catalog/static-recommendations.md)

In one server (or mutiple servers)  how  do  we know  what catalogues we have? (and what catalogue an item belongs to) All the examples now is 1 server --> 1 catalogue 

We are always working with 1 server --> 1 catalogue for the future  when we have federated systems we will require that each catalogue has a uuid

In a federeated catalogue system, we would start to crawl catalogues with different extensions and that could pose a problem, 

Could digital consensus algorithms be used to find and agree on data authenticity and integrity? 
Would a p2p technology help find other STAC services? Like https://ipfs.io/ . Maybe since it's a standard on top of http(s), consensus and linkage need to be extensions not even in the standard.

Lineage and ownership  of data 

New  network technologies like HTTP2 and websockets href is not enough (e.g indication  if we have http1.1 or http2) 
