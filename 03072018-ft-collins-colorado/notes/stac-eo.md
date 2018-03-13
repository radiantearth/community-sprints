## Overview

This was a dedicated discussion about an Earth Observation 'profile' of STAC (though there is still some debate on whether
'profile' is the best name). Raw notes were recorded at http://board.net/p/stac-eo-profile

Matt took the group through what the [core metadata group](https://github.com/radiantearth/community-sprints/tree/master/10252017-boulder-co/workstreams/core-metadata) did
in the previous sprint. They created many additional fields that are only relevant for earth observation.

It became clear though that most of the fields belong at a higher level, as they'd be repeated a ton if listed in every
single item. So most of the discussion went to how to define a 'product' / 'asset'.

One smaller improvement that helped many things was to make the 'assets' field in an Item a 'dict' instead of an array. This
makes it easier to access a particular asset programmatically, so is a win just for that. But the group also decided to 
use the same keys in the assets in an item to match the keys in an 'asset definition' file. The asset definition would be
linked to from an Item level, but any particular asset could be looked up in the dict, using the same key as in the item. 

The other decision was to make less fields be 'required', but to add in more optional fields. Like we don't force everyone
to include Sun Elevation and Sun Azimuth. But we do define the names and value ranges for them, so that if someone does
want to use it then they are using a common name.

The other thing discussed was to align with the [OpenSearch Extension for Earth Observation](http://docs.opengeospatial.org/is/13-026r8/13-026r8.html)
specification. They have put lots of thinking in the naming of things, so we should make our definitions compatible. But
likely define a subset, as they really define a ton. Perhaps could make an EO optional extension with all the extra fields
that might be used.

Matt H will run with writing up the new spec improvements, as well as writing up the EO profile.

## Raw notes



Lots of talk between scene specific metadata and product metadata. 

What do we do for crs that aren't projected?
 null.
 
 Date / nominal date - more applies to mosaics. MODIS example, applies to 9th day, not the 16 day range. 
 When talking about one scene it makes less sense.
 
 Adopt iso 8601 for dates - lets us define periods, instantenous dates, etc. So flexible it will cover everything, but then implementation is a pain. 
 Way to claim that only mandatory implementation is a small subset of it? 
 
 Start and time seem sufficient


OpenSearch for EO: http://docs.opengeospatial.org/is/13-026r8/13-026r8.html

Core idea: leverage the naming conventions from the OpenSearch for EO, but subset to the EO fields important for us.

Product - landsat TOA vs landsat SR

Do you search for area and time and see what products are available? Or they know they want surface reflectance.

If records represent collection / acquisition - those are not backed by any time of image. Those are what you pass in to produce a product. We catalog what images are directly accessible.

In earth engine, we have virtual, produce on the fly.

Overrides? May have to.

Bands - complicated enough that you want to give lots of information.
  - key. Goes back to how assets are stored. Right now stored as a list. Think it needs to be a dictionary, that can be referenced from the bands.
      - problem is if you are after one specific asset you have to parse all of it if it's after. 

New way: Have a dictionary for assets. Have a name as the key (up to the provider to decide it). 

How do you know which one is the image? 

Perhaps get to common key names, like 'visual'.

Name is human readable name.

Boundless added 'type' and 'fileType'.
 They key off of geotiff file type.
 
 Band order - move to common names. 
 
 order key next to href?
 
TODO change Asset = {
         "B1": { "href": "http://...."} more
         
Bands - could be complete standalone item, drone put all the stuff in it. 

Product has asset definition table. Can use it merge with assets.
  - Can have a product definition field, or a link to a product definition.
  - If product definition is not defined on the asset.
  
GSD - use meters. 

Meant to describe a metadata or asset, not an algorithm.

How to do single geotiff with many bands. 
  - it would have index. 

Records have 


How do you search / filter for stuff?
  one asset

From Boulder Sprint:
    
    

# Scene Specification Description 

| element             | type info                 | name                    | description                                                                                 | 
|----------------------|---------------------------|-------------------------|---------------------------------------------------------------------------------------------| 
| scene(?):crs     | reference system    | ref system             | CRS of the datasource in full WKT format. (null if no crs / rpcs)
| platform            | string                      | Unique name of platform | Specific name of the platform (e.g., landsat-8, sentinel-2A) | 
| instrument        | string                      | Instrument used     | Name of instrument or sensor (e.g., MODIS, ASTER, OLI) |
| product             | string                      | Product Name       | Name of product (optional) (revisit - need to figure out product) |
| bands               |   dict                       | Bands                    | Band names: {common_name (optional), gsd, accuracy, wv, fwhm) |
| product_version | string (optional)    | Product Version     | Version of the product |
| cloud_cover     | number (optional)   | Cloud Cover Pct    | Percent of cloud cover | 
| nadir_angle      | number (optional)   | Off nadir angle      |
| sun_azimuth    | number (optional)   | Sun Azimuth |
| sun_elevation  | number (optional)   | Sun Elevation |
| supported_assets | array of asset names | Supported Assets | A list of the key names for the asset types that are available now.



# Asset Definition 

```
{
   "name" : "landsat SR"
   "platform" : "cool sat"
   "instrument" : "olii"
   "bands": {

    "1":  {

    "common name": "blue",

    "gsd": 30.0,

    "accuracy: 5.0,

    "wavelength": 0.47,

    "fwhm": 0.04

    }

   }
   "assets" = { "analytic": {  // key must match the asset key

           "name" : "4-band analytic image"

      "description" : "A 4-band analytic PlanetScope Image"

      "type" : "Geotiff"

      "required" : "true" (or false)

      "bands" : [ "1", "2", "4", "3" ]

    }

}
```

# Item example
```
{
   "links": [

        {"rel": "asset-definition", "href": link/to/assetdefinitionfile" }

    ]
    "assets": {
        "analytic" {
            "href": urltofile
        }
    }   
}

# Inline Item example (idea)
{
   "links": [

        {"rel": "asset-definition", "href": link/to/assetdefinitionfile" }

    ],
    "asset_definition": {

       "name" : "landsat SR"

       "platform" : "cool sat"

       "instrument" : "olii"

       "bands": {

    "1":  {

    "common name": "blue",

    "gsd": 30.0,

    "accuracy: 5.0,

    "wavelength": 0.47,

    "fwhm": 0.04

    }

       }

       "assets" = { "analytic": {  // key must match the asset key

           "name" : "4-band analytic image"

      "description" : "A 4-band analytic PlanetScope Image"

      "type" : "Geotiff"

      "required" : "true" (or false)

      "bands" : [ "1", "2", "4", "3" ]

    }

    },

    "assets": {
        "analytic" {
            "href": urltofile
        }
    },
    "properties": {

    "available_assets": ["analytic"]

    }

}

```

Questions for group:
    - federation: self-contained?
    - cloud_cover: % or floating point?
    - how many geometry parameters (azimuth, sun angles)
    - geometry as an entity (dictionary)?

# Product Specification Description

| element             | type info                                   | name                    | description                                                                                 | 
|----------------------|---------------------------|-------------------------|---------------------------------------------------------------------------------------------| 
| platform            | string                       | Unique name of platform | Specific name of the platform (e.g., landsat-8, sentinel-2A)      | 
| instrument        | string                       | Instrument used               | Name of instrument or sensor (e.g., MODIS, ASTER, OLI)      |
| product             | string                       | Product Name                 | Name of product                                                                         |
| bands               |   dict                        | Bands                               | Band names: {common_name (optional), gsd, accuracy, wv, fwhm) |
| product_version | string (optional)     | Product Version                | Version of the product                                                               |


--
Collaborate seamlessly on documents! This pad text is synchronized as you type, so that everyone viewing this page sees the same text. 
Create your own board and a (secret) name for it here: http://board.net This service is provided on fair-use with open source technology by fairkom. 
Consider a donation in Euro or FairCoin https://www.fairkom.eu/en/sponsoring#Donations for disk space and new features. Virtual hug guaranteed! 


