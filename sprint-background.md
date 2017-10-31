## Introduction

This document serves as a summary of the background goals and work of the boulder sprint. It was a 3 day event, bringing together
24 people from 14 different organizations, aimed at collaboration around specifications that increase the interoperability of
finding imagery and other captured geospatial information. See [sprint-overview](sprint-overview.md) for more information
on what happened at the sprint.

## Background and goals

Many different software and data providers in the last few years have created RESTful JSON-based API's that enable
searching of imagery and other geospatial assets - video, SAR, LiDAR, DEM's, etc. All enable searching by geography, time
and at least a few other fields. And though they all do roughly the same thing each looks a bit different. And thus each
requires specific code to be written to search its holdings - be it a javascript based GUI, a command line tool, or an 
integration in desktop software. 

None of the providers saw the actual API as their core value proposition, but there was no good open standard that handled
the search well. The OGC CS-W specification is built for online catalogs, but it does not handle tens of millions of records
of imagery that well - it is more geared towards searching vector data layers in an SDI. The ebRIM profile of CS-W could
handle more, but it's outdated and not accessible to modern web developers. The goal of most providers is to enable non-geo
developers to sensible search the catalog.

Though the Open Geospatial Consortium is a logical place to collaborate on geospatial standards it has had a fairly 
out-dated way of collaborating - relying on word document editing and telecons, instead of github, markdown and OpenAPI specs
(thankfully that has started to shift in a fairly major way, and the goal is to bring the work together). So it felt
like the time was right to gather the developers who actually built the variety of services so they could share 
experiences and get to some solid specifications that everyone could implement. [Radiant Earth](http://radiant.earth) 
emerged as a great neutral convener who was willing to sponsor an in-person meeting. Their goal is to help
bring satellite imagery to NGO's and the developer world, and enabling all imagery holdings to be much more accessible
through open standards is directly in line with their mission.

Having at least the initial meeting in person was essential, to enable high bandwidth exchange of information, and to 
also connect people to a community of others grappling with the same issues. The primary goal was to walk out of the
meeting with a draft specification for searching imagery that every organization could implement over the next couple months.
And to use that to attract more implementations, aiming to have a majority of the earth imagery assets in the world available 
through standardized search API's. But the goal is to not only develop one or two specifications, but to help build 
collaborative technological environment in the geospatial domain.

## Prep

The first set of work for the sprint was to try to get everyone on the same page by sharing their implementations and 
experiences before meeting, so we could hit the ground running as much as possible. 
A number of organizations were already using [Open API](https://www.openapis.org/) 2.0 as an internal tool to help document and
design their API's for imagery search. So a repository was created for organizations to contribute their API specs
(as OpenAPI 2.0) and an overview of their experience. See the [implementations folder](https://github.com/radiantearth/catalog-api-spec/tree/7159634c0873683042b758ed05e91097e83477ac/implementations)
 (from the state right before the sprint) to see the prep work done. 
 
Early contributors included [OpenAerialMap](http://openaerialmap), [RasterFoundry](http://rasterfoundry.com), [Planet](http://planet.com), 
[Pixia](http://pixia.com) and [DigitalGlobe](http://digitalglobe.com). There was also work to gather the various metadata
that was in use by [various providers](https://github.com/radiantearth/imagery-metadata-spec/tree/c7e8a12e07c061640790d2f642090222aaa9b967/non-standard-implementations). 
And a small group from Boundless andH exagon Geospatial also 
made a [proposed draft](https://github.com/radiantearth/catalog-api-spec/blob/178c817220f9ca113cd380271b2649623ac7ac39/proposed/spec-draft-1.yaml) based on 
[WFS 3.0](https://github.com/opengeospatial/WFS_FES), as well as a functioning [Java API](https://github.com/joshfix/open-catalog) for it
from Boundless, and Hexagon got their internal system all ready to create a new API and connect to the same backend. There
was also good discussion in Github issues for the metadata, with Matt Hanson [raising](https://github.com/radiantearth/imagery-metadata-spec/issues/18) a 
number of good points and spurring discussion.

Everyone participating was also divided in to [workstreams](https://github.com/radiantearth/boulder-sprint/tree/master/workstreams), which
each had a set of background reading and work to do. The other prep work that organizations did was to prepare a lightning talk, so that everyone could easily get a sense of
what everyone else was working on and where they were coming from.

## Organizations

There were 14 total organizations, representing a number of diverse perspectives:

* [Amazon](http://amazon.com) hosts a number of [Public Datasets](https://aws.amazon.com/public-datasets/) of interest to
the community including Landsat and Sentinel, that are ideal candidates for static catalog standards.
* [Azavea](http://azavea.com) builds [GeoTrellis](http://geotrellis.io), a high performancs scale-out raster processing engine, 
as well as [RasterFoundry](http://rasterfoundry.com) which builds UI and raster data storage on top of GeoTrellis.
* [BITS](http://www.caci.com/bit-systems/) came, representing the NGA [GEOINT Services](https://home.geointservices.io/) 
perspective, particularly as a consumer of imagery catalogs, with a special emphasis on offline usage.
* [Boundless](http://boundlessgeo.com) creates a full stack of open source geospatial software, and is interesting in both
consuming imagery catalogs as well as adding the interface to their suite of tools.
* [DevSeed](http://devseed.com/) has been working on [Sat-API](https://github.com/sat-utils/sat-api) to expose Landsat and
Sentinel as a single API, leveraging Amazon technologies. Their [Sat-search](https://github.com/sat-utils/sat-search) python
client also consumes satellite imagery API's
* [DigitalGlobe](http://digitalglobe.com) is the largest company providing satellite imagery, and have built a number of 
imagery API's over the years. Their [GBDX platform](https://gbdx.geobigdata.io/) platform has the most modern API, and they
also have teams consuming satellite imagery.
* [Element84](http://www.element84.com/) have built a bunch of NASA's imagery search API's, including a lot of work on 
[CMR Search](https://cmr.earthdata.nasa.gov).
* [Google](http://google.com) builds [Earth Engine](https://earthengine.google.com/) which has the largest repository of 
public earth observation data, and is exploring how to make it available to more than just Earth Engine users.
* [Harris](https://www.harris.com/)'s [ENVI](https://www.harris.com/solution/envi) started life as a desktop imagery analysis
tool, but now is a powerful set of cloud processing components. They build connectors to all the major imagery providers, bringing 
a great client-side perspective.
* [Hexagon Geospatial](http://www.hexagongeospatial.com/) has a huge array of geospatial products. Their 
[Erdas Apollo](http://www.hexagongeospatial.com/products/power-portfolio/erdas-apollo) team was represented, which provides 
an imagery catalog API on top of any set of geospatial data holdings.
* [Humanitarian OpenStreetMap Team](https://www.hotosm.org/) (HOT) builds [Open Aerial Map](http://openaerialmap.org) which lets
anyone host open imagery for disaster response and tracing in OSM, primarily from drones and satellites. They have a catalog API
that powers their browser.
* [Planet](http://planet.com) has the most earth imagining satellites in space, and makes the data available through its
[Data API](https://www.planet.com/docs/reference/data-api/).
* [Pixia](http://pixia.com) provides high performance video and imagery serving software, and has a catalog API for their users
to search the holdings in the software.
* [Radiant Earth](http://radiant.earth) provides a geospatial and imagery technology platform built on RasterFoundry and other
tools that aims to positively impact the developing world’s greatest social, economic and environmental challenges.









