## Overview

These notes are from the small group session on static STAC. Raw notes pasted in from http://board.net/p/stac-static

The group discussed a number of varied subjects, and reached some solid decisions

#### Crawl Compatibility

Lots of time was spent on figuring out how data in both STAC API's and static STAC's could be crawled in the same way
by a naive crawler. The goal was to have an entry point that looks the same on both static and API, and can be traversed
in the same way.

After much discussion the conclusion was that it's not really possible with GeoJSON. STAC API is all about feature collections
that are traversed, and the links are at the FC level. There was a brainstorm on putting all static API's in to feature
collections, but the killer drawback of that is then there's no well accepted way to refer to the feature by itself. One needs
an XPath type thing for JSON, but those are all extensions, not part of the core. This was deemed vitally important due to 
the desire for meaningful 'self' links.

The group then pulled back to examine the crawl compatibility goal, and concluded that it's actually less important for JSON.
The key for crawling is really the HTML versions of things. It's ok if they refer to different JSON underneath them (between
the STAC API and static STAC). JSON is important to be the true programmatic unambiguous specification of the data (at some
point maybe there's a great HTML microformat that can become definitive, but that's not the case now). But HTML should be
the focus of crawling. 

So there is more to be done on HTML recommendations for both dynamic and static catalogs, but it seems like it should be easier
to just have entry points that are easily crawled by following links. 

#### HTML

Creating HTML pages from JSON STAC was discussed. A cool idea was to do the HTML all on the fly, with javascript. Then could
make that library available to anyone with a STAC catalog, and we'd get HTML versions of the same ideally.

#### Syncing

How to keep catalogs in sync was discussed a bit. It's the ideal 'next' extension, since it enables a STAC API to stay
up to date based on a static catalog. 

We aren't really ready to standardize on it. But encouraged participants to create AWS SNS version as well as a Google Cloud
version that tries out keeping catalogs in sync. Google and DigitalGlobe will prototype.

It was discussed that 'delete' is important, to know if a record went away.

#### Portability

Another topic discussed was the original goal of being able to just 'copy' a part of a catalog and take it remote. It seemed
like a nice idea, and could be done with all relative links. But earlier the whole group agreed that the 'self' link should
be required to be an absolute URL. So most copying of part of a tree will involve at least some rewriting of URL's.
 
So the hope now is that good tooling can make it easy to 'copy' a portion of a static catalog, but we won't try to design
for that use case.



## Raw Notes

Crawl compatibility
 - sub catalog. If you have sub-catalog.json with catalog by it then I have to open then what is it. 
 - use names, prefix with catalog, catalog.json
    - did /archive/catalog.json and /current/catalog.json
 
Deletes - add SNS
 Encouraged - publish the topic to the catalog.json
 Updates? 
 Changes in pixels, how do I show the changes. 
   - archive old item? Or 
   - changelog.json
 TODO: Simon and Jeff to prototype, document.
 
 Utility of catalog vs sub-catalog.
   - so things don't get too large. 
   
   link catalogs vs root catalogs
     - pages, that's what they are. 
     
    Doing drone collection, doing different clients. Don't share from root data, but share from node on down. 
    
    Single root catalog of millions of records, or partition
    
    This is just discovery, tracking everything.

        - Do I need to discover deleted stuff?

         - many people would, because they are ingesting the data. Can go back to changelog and go back to last update. 

    Haven't had to change 'sun angle'.

    People will publish at a particular revision. 

    
    
  Talk on feature collections Can we make it so all geojsons 
  
  Wrap all items in feature collections so they are crawlable
  
  TODO: Give up on goal of making static and API crawl compatible at JSON level. 

      - WHy? Seems too hard to get the links right. We really like each item being in its own json, so that 'self' links work and it has a canonical location. There's not a convention for referring to part of a JSON file.

     -   Focus on doing so at the HTML level, dictate what HTML looks like in WFS / STAC API. Use same link structure in both.


If you want a catalog to be crawlable you provide an html page at the top of your catalog.

Should we have catalog.json just be an HTML? No, not yet because it's not machine readable. Google may come out with some html markup to let you specify data, and at that point it'd make sense to shift.

Generating HTML pages from javascript. Change David's html browser in to something that does not 'read' files, but that turns a static json file in to html. That any static file can supply.

Root and link catalog. Root has a lot more properties. Let a root be specified. 
  - Just point at root catalog. 
  
  TODO: Root catalog should be linked to from Item, not the parent catalog. Actually put parent catalog.


