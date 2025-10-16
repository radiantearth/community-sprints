---
title: 'Topic 2: Asset Discovery and Data Access Patterns'

---

# Topic 2: Asset Discovery and Data Access Patterns

**Key questions/priorities for this topic:**
- Asset href resolution
- Collection-level vs item-level asset organization for Zarr stores
- Guidelines for representing scene-based Zarr stores (EOPF products)
- Best practices for xarray extension deprecation in favor of nd-array generic patterns
- Asset metadata requirements for pyramids/multi-resolution data groups
- Variable-specific asset handling within multidimensional stores
- Link templates for direct access to Zarr subgroups and variables 
- Identify gaps in Zarr variable representation in datacube extension
- Propose solutions for identifying coordinate variables
- CF convention integration patterns (CF extension overlap)
- Collection-level datacube metadata for hierarchical stores
- Alignment with CF conventions for atmospheric and oceanic data
- Standard name and units handling
- Cell methods representation for temporal aggregations 

## Glossary

- Zarr Terminology: https://zarr-specs.readthedocs.io/en/latest/v3/core/#concepts-and-terminology

## Assets hierarchy (DEAD END)

- Should we have a mechanism describing asset hierarchy (store -> zarr groups -> variables)?
- If previous is yes, should we have a inheritance mechanism?


## Asset resolution

- Should it be resolvable? No, it might
- Mime-Type
- How to represent 

Where is my Data? Get to the band directly. 

Whatever is referenced as an asset should be accessible 

## Global rules

- A zarr asset SHALL be a group with array(s) (equivalent to an xarray dataset)
- The group variables and dimensions SHALL be described with the datacube extension
- the Zarr store should be a link in the collection or item with the "store" relationship (or "asset"?) and with the type to "application/vnd+zarr"
- band should contain a key per data variable and should be the relative path to the array from the asset href.
- If needed for the use case, the data cube extension should be used to provide more information about the data variables and dimensions and their relationships
    - No need identified for EOPF
    - Important for CF datasets 
- Consolidated metadata 

## Best Practises

## Required extensions

- New link relationship to define a "store" (rel)
    - Zarr mime type. parameter in the content type parameters indicating the zarr version 
    - example from COG: "type": "image/tiff; application=geotiff; profile=cloud-optimized"

```jsonld
"links": [
    {
        "rel" : "store",
        "href": "s3://somebucket/key/datastore.zarr",
        "title": "Zarr Store",
        "type": "application/vnd+zarr; version=2"
    }
]

- gsd as array?
- 


### Band as variable example (STAC v1.0)

```jsonld=
"properties": {
  "start_datetime": "2025-09-12T12:33:22Z",
},
"assets": {
    "store": {
        "href": "s3://somebucket/key/datastore.zarr",
        "roles": ["store"]
    },
    "group": {
        "href": "s3://somebucket/key/datastore.zarr/measurements",
        "roles": ["group"]
    },
    "b04": {
        "href": "s3://somebucket/key/datastore.zarr/measurements/b02",
        "cube:dimensions":{
            
        },
        "roles": ["variable"],
        
    }
}
```

[EOPF STAC item example for Sentinel-2 L2A](https://stac.core.eopf.eodc.eu/collections/sentinel-2-l2a/items/S2B_MSIL2A_20251006T123309_N0511_R052_T28WFT_20251006T131746)

EOPF Sentinel-2 Zarr store:
```
/
├── conditions
├── measurements
│   └── reflectance     
│       ├── r10m
│       │   ├── b02 (10980, 10980) uint16
│       │   ├── b03 (10980, 10980) uint16
│       │   ├── b04 (10980, 10980) uint16
│       │   ├── b08 (10980, 10980) uint16
│       │   ├── x (10980,) int64
│       │   └── y (10980,) int64
│       ├── r20m
│       └── r60m   
└── quality
```

### Sentinel2 Item example (STAC v1.1)

```jsonld=
"properties": {
  "start_datetime": "2025-09-12T12:33:22Z",
},
"assets": {
    //Will be moved to links?
    "store": {
        "href": "s3://somebucket/key/datastore.zarr",
        "roles": ["store"]
    },
    "measurements/r10m": {
        "href": "s3://somebucket/key/datastore.zarr/measurements/r10m",
        "roles": ["group"],
        "cube:dimensions":{
            "x": {
                
            },
            "y": {
                
            }
        },
        "cube:variables": {
            "b02": {
                "dimensions": ["x", "y"]
                "type": "data",
                "unit": null
            }
            "b03",
            "b04",
            "b08"
        },
        "proj:shape": [10980, 10980],
        band: {
            "b02":
            {
                "gsd": 10
                "name": "red",
                "description": "red (??? um)",
                "eo:common_name": "red",
                "raster:*"
            }
        }
    },
    "measurements_r10m": {
        "href": "s3://somebucket/key/datastore.zarr/measurements/r10m",
        "roles": ["group"],
        "gsd": 10,  //  raster:spatial_resolution
        "data_type": "uint16",
        "raster:scale": 0.0001,
        "raster:offset": 0.0,
        "nodata": 0,
        // not sure datacube extension is necessary here
        "cube:dimensions":{
            "x": {
                
            },
            "y": {
                
            }
        },
        "cube:variables": {
            "b02": {
                "dimensions": ["x", "y"]
                "type": "data",
                "unit": null
                ""
            }
            "b03": {
                "dimensions": ["x", "y"]
                "type": "data",
                "unit": null
                ""
            }
            "b04": {
                "dimensions": ["x", "y"]
                "type": "data",
                "unit": null
                ""
            }
            "b08": {
                "dimensions": ["x", "y"]
                "type": "data",
                "unit": null
                ""
            }
        },
        //
        band: {
            "b02":
            {
                "name": "red",
                "description": "red (??? um)",
                "eo:common_name": "red",
                
                "cf:standard_name": ...
            }
        }
    },
    "measurements_r10m": {
        "href": "s3://somebucket/key/datastore.zarr/measurements/r10m",
        "roles": ["group"],
    },
    "b02": {
        "href": "s3://somebucket/key/datastore.zarr/measurements/b02",
        "cube:dimensions":{
            "x": {
                
            },
            "y": {
                
            }
        },
        "cube:variables": {
            ""
        },
        "roles": ["variable"],
        "band": {
            "name": "red",
            "description": "Red band (???um)"
        }
    },
    "array": {
        "href": "s3://somebucket/key/datastore.zarr/measurements/b02#",
        "roles": ["data"]
    }    
}
```

### One big Zarr (CF Simulation data)

Zarr with one group (xarray dataset)
![image](https://hackmd.io/_uploads/SyuMNnoaxe.png)

[Interactive viewer](https://gridlook.pages.dev/#https://s3.eu-dkrz-1.dkrz.cloud/wrcp-hackathon/data/ICON/d3hp003.zarr/P1D_mean_z7_atm)


```python
import xarray as xr
import json

defs = {
    "uri": "https://s3.eu-dkrz-1.dkrz.cloud/wrcp-hackathon/data/ICON/d3hp003.zarr/P1D_mean_z5_atm"
}

ds = xr.open_dataset(defs["uri"], engine="zarr", chunks={})

asset = {}
asset["href"] = defs["uri"]
asset["links"] = [
    dict(
        href=defs["store"],
        rel="store",
        type="application/vnd+zarr; version=2",
        title="Zarr store",
    )
]
asset["roles"] = ["group"]
asset["cube:dimensions"] = dict(
    time=dict(
        type="temporal",
        description="time",
        extent=[str(ds["time"].min().values), str(ds["time"].max().values)],
        step="P1D",
        unit="seconds since 2020-01-01T00:00:00",
,
    ),
    cell=dict(
        type="spatial",
        axis="cell",
        description="cell index in HEALPix grid",
        bbox = [-180.0, -90.0, 180.0, 90.0],
        reference_system="HEALPix",
    ),
    pressure=dict(
        type="vertical",
        axis="z",
        description="pressure level",
        extent=[float(ds["pressure"].min().values), float(ds["pressure"].max().values)],
        unit="Pa",
    ),
    soil_level=dict(
        type="vertical",
        axis="z",
        description="soil level",
        extent=[
            float(ds["soil_level"].min().values),
            float(ds["soil_level"].max().values),
        ],
        unit=ds["soil_level"].attrs.get("units", "unknown"),
    ),
    pressure_rva=dict(
        type="vertical",
        axis="z",
        description="pressure level for relative vorticity",
        extent=[
            float(ds["pressure_rva"].min().values),
            float(ds["pressure_rva"].max().values),
        ],
        unit=ds["pressure_rva"].attrs.get("units", "unknown"),
    ), # no idea what this is. Contents are bogus.
)

asset["cube:variables"] = {
    k: {
        "dimensions": list(ds[k].dims),
        "type": "data",
        "unit": str(ds[k].attrs.get("units", None)),
    }
    for k in ds.data_vars
}
asset["proj:shape"] = [ds.dims[k] for k in ds.dims]
asset["band"] = [
    {
        "name": k,
        "description": ds[k].attrs.get("long_name", ""),
        "standard_name": ds[k].attrs.get("standard_name", ""),
        "unit": str(ds[k].attrs.get("units", None)),
    }
    for k in ds.data_vars
]

print(json.dumps(asset, indent=2))

```
generates the json for an asset.

```jsonld
{
  "href": "https://s3.eu-dkrz-1.dkrz.cloud/wrcp-hackathon/data/ICON/d3hp003.zarr/P1D_mean_z5_atm",
  "roles": [
    "group"
  ],
  "links": [
    {
      "href": "https://s3.eu-dkrz-1.dkrz.cloud/wrcp-hackathon/data/ICON/d3hp003.zarr",
      "rel": "store",
      "type": "application/vnd+zarr; version=2",
      "title": "Zarr store"
    }
  ],
  "cube:dimensions": {
    "time": {
      "type": "temporal",
      "description": "time",
      "extent": [
        "2020-01-02T00:00:00.000000000",
        "2021-03-01T00:00:00.000000000"
      ],
      "step": "P1D",
      "unit": "seconds since 2020-01-01T00:00:00"
    },
    "cell": {
      "type": "spatial",
      "axis": "cell",
      "description": "cell index in HEALPix grid",
      "bbox": [
        -180.0,
        -90.0,
        180.0,
        90.0
      ],
      "reference_system": "HEALPix"
    },
    "pressure": {
      "type": "vertical",
      "axis": "z",
      "description": "pressure level",
      "extent": [
        5.0,
        100000.0
      ],
      "unit": "Pa"
    },
    "soil_level": {
      "type": "vertical",
      "axis": "z",
      "description": "soil level",
      "extent": [
        0.0,
        6.0
      ],
      "unit": "unknown"
    },
    "pressure_rva": {
      "type": "vertical",
      "axis": "z",
      "description": "pressure level for relative vorticity",
      "extent": [
        16.0,
        23.0
      ],
      "unit": "unknown"
    }
  },
  "cube:variables": {
    "clivi": {
      "dimensions": [
        "time",
        "cell"
      ],
      "type": "data",
      "unit": "kg m-2"
    },
    "clt": {
      "dimensions": [
        "time",
        "cell"
      ],
      "type": "data",
      "unit": "m2 m-2"
    },
```
...
```jsonld
  },
 },
  "proj:shape": [
    425,
    12288,
    1,
    30,
    5,
    3
  ],
  "band": [
    {
      "name": "clivi",
      "description": "cloud ice path",
      "standard_name": "atmosphere_mass_content_of_cloud_ice",
      "unit": "kg m-2"
    },
    {
      "name": "clt",
      "description": "total cloud cover",
      "standard_name": "clt",
      "unit": "m2 m-2"
    },
```
...
```jsonld
  ]
}
```



```jsonld=
"assets": {
    "store":{
        "href": "s3://somebucket/key/datastore.zarr"
        roles: ["store"]
    },
    "P1D_mean_z5_atm": {
        "href": "s3://somebucket/key/datastore.zarr/P1D_mean_z5_atm",
        "cube:dimensions":{
            "time": ...,
            "cell": ...,
            "pressure": ...,
            "pressure_rva": ...,
            "crs": ...
        },
        "cube:variables":{
            "clivi" : {
              "description" : "Cloud Ice Vertically Integrated"
            },
            "clwvi" : {
              "description" : "Cloud Water Vertically Integrated"
            }
        },
        "roles": ["variable"],
        "band" : [
            { 
                "name": "clvi",
                "description": "Cloud Ice Vertically Integrated"
            },
            { 
                "name":"clwvi",
                "description" : "Cloud Water Vertically Integrated"
            }
            
        ]
    }
}
```

Item with a VirtualiZarr file and netCDF files
 
```jsonld=
"assets": {
    "data": {
        "href": "https://some.path/data/CMIP6/ScenarioMIP/rlus_day_CESM2-WACCM_ssp585_r1i1p1f1_gn_20150101-20241231.nc",
      "type": "application/netcdf",
      "title": "NetCDF file",
      "roles": [
        "data"
      ]
    }
},
"links": [
    {
        "rel": "store",
        "href":  "https://some.path/kerchunk/CMIP6_ScenarioMIP_NCAR_CESM2-WACCM_ssp585_r1i1p1f1_day_rlus_gn_v20200702_kr1.0.json",
        "title": "VirtualiZarr Store",
        "type": "application/vnd+zarr; version=2; profile=virtualizarr"
    }
]
```

Zarr with datatree as groups
 
```jsonld=
"assets": {
    "data": {
        "href": "s3://somebucket/key/datastore.zarr",
        "cube:dimensions":{
            
        }
    }
}
```