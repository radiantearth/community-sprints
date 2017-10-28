(copy from http://board.net/p/metadata-spec)

# bare minimum raster geospatial data

| element              | type info              | name                            | description                                                                                 | 
|-----------------------|------------------------|--------------------------------|---------------------------------------------------------------------------------------------| 
| id                        | string                   | Provider ID                   | Provider ID for that item                                                                            | 
| geometry            | geojson               | Bounding Box + Footprint | in lat/long (4326)
| start_date           | date and time      | Date Start                     | First date/time in UTC (Combined date and time representation)    | 
| end_date            | date and time      | Date End                      | Last date/time in UTC (Combined date and time representation)          | 
| provider              | string                   | Provider  (optional)       | Provider name and contact. Keys: [name, url]
| license                | string                   | Data license (optional)  | Data license name based on SPDX License List | SPDX doesn't contain all
| links                    | dict                      | Resource links              | Dictionary of links to resources, could be download or other URLs (self and thumbnail required) |

need to specify some of the links as a best practice;  for example a thumbnail, ...

discussion regarding spec_version and the notion it is done at the api level.  It is not needed explicitly and has been removed.
title determined to be OBE

come back to provider. keep the field. need to determine how to use the information. 
need to write best practice for how to go beyond SPDX list 

revisit later in version 2:
| version                | semantic versioning number | Product Version | The version of the imagery metadata fields, for testing/validation  | 

Removed for now:
| product_type      | string                   | Product Type                 | Product types: [eo, sar, model, point-cloud, video] | 

Questions from Static Catalog peeps

* snake or camel casing? snake
* is links a list of dicts instead of a dict? No, this is one dict with keys such as metadata, band1, band2, ... . Values will be links.
  * great. (asking for a validation friend; well-known keys are possible to validate but not necessary)
* can provider be an "entity" (name, email, phone, contact, [address])?
* what is this unit called? (working name over here: "asset")


Questions for the group:
    name of this unit -- item, asset
    product type -- categories. Does model make sense? 
    cardinality - how should this be addressed?

  * write up some example with a document and diagram to articulate the deeper issue assocaited with cardinality mentioned above.

group discussion (Tues, midday):
product types - allowable values are the names of the standard extensions
both types and standard extensions can be extended
collapse bbox and footprint into one geojson 
provider / source


## Extensions/Schemas

scene: raster data collected with an instrument
pointcloud: 3d point cloud data
video: video data
model: raster data calculated


# Scene Specification Description 

| element             | type info                 | name                    | description                                                                                 | 
|----------------------|---------------------------|-------------------------|---------------------------------------------------------------------------------------------| 
| scene(?):crs     | reference system    | ref system             | CRS of the datasource in full WKT format. | 
| date                  | nominal date           | Date                      | The nominal date of the scene, could be center time, or a single day within a window from which data is collected |
| platform            | string                      | Unique name of platform | Specific name of the platform (e.g., landsat-8, sentinel-2A) | 
| instrument        | string                      | Instrument used     | Name of instrument or sensor (e.g., MODIS, ASTER, OLI) |
| product             | string                      | Product Name       | Name of product |
| bands               |   dict                       | Bands                    | Band names: {common_name (optional), gsd, accuracy, wv, fwhm) |
| product_version | string (optional)    | Product Version     | Version of the product |
| cloud_cover     | number (optional)   | Cloud Cover Pct    | Percent of cloud cover | 
| nadir_angle      | number (optional)   | Off nadir angle      |


# bands element example

```json
{
  "B1": {
    "common name": "blue",
    "gsd": 30.0,
    "accuracy: 5.0,
    "wavelength": 0.47,
    "fwhm": 0.04
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

Single product may have multiple band combinations (RGB, RGBIR)


Example Common Names

| Band Name | Band Range  | Landsat 5 | Landsat 7 | Landsat 8 | Sentinel 2 | MODIS |
|-----------|-------------|-----------|-----------|-----------|------------|-------|
| COASTAL   | 0.40 - 0.45 |           |           | 1         | 1          |       |
| BLUE      | 0.45 - 0.5  | 1         | 1         | 2         | 2          | 3     |
| GREEN     | 0.5 - 0.6   | 2         | 2         | 3         | 3          | 4     |
| RED       | 0.6 - 0.7   | 3         | 3         | 4         | 4          | 1     |
| PAN       | 0.5 - 0.7   |           | 8         | 8         |            |       |
| REDEDGE | 0.68 - 0.73 |
| NIR       | 0.77 - 1.00 | 4         | 4         | 5         | 8          | 2     |   lwil need to have more than one allowance, i.e. nir1 and nir2
| CIRRUS    | 1.35 - 1.40 |           |           | 9         | 10         | 26    |
| SWIR16     | 1.55 - 1.75 | 5         | 5         | 6         | 11         | 6     |   may need more than one,  DG wv03 has 8 swir bands and we cannot reuse the keys
| SWIR22     | 2.1 - 2.3   | 7         | 7         | 7         | 12         | 7     |
| Ka            | 7500 - 11000    |
| K              | 11000 - 17000     | 
| Ku            | 17000 - 25000     |
| X              | 25000 - 38000     |
| C              | 38000 - 75000     |
| S              | 75000 - 150000   |
| L              | 150000 - 300000  |
| P              | 300000 - 1000000 |            





# removed
| gsd               | number                                         | Ground Sample Distance  | Average ground sample distance (resolution) of the datasource imagery, expressed in meters. Is the distance between the centers of pixels on the ground. | 
| processing_level*        | number (optional)                        | Processing Level                  | Level of processing |
| accuracy                         | number (optional)                        | Accuracy                                   | 
| revision              | number (optional)                        | Revision                                   | Revision number of the record |

```json
{
        "sid": 
        "crs": 
        "bbox": 
        "footprint":
        "gsd": 
        "date": 
        "acquisition_start":
        "acquisition_end":
        "product_level":        {
                        "title":
                        "platform_type":
                        "platform":
                        "instrument":
                        "product":
                        "processing_level":
                        "band_map":
                        "provider":
                        "contact":
                        "license":
                        "product_version":
        },
        "cloud_cover",
        "links": {}
}
```

unique id?
title
footprint - lat/lon 4326
gsd
date - 3 dates is a lot
dg tiles

provider -- contact
