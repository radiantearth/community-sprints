---
title: Examples

---

Multiresolution brainstorming Concept examples s2-L2A

# Example SR (Brainstorming only - i think this could be removed - see #1)

```json
"SR_10m": {
            "gsd": 10,
            "href": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/14/products/cpm_v256/S2C_MSIL2A_20251014T142151_N0511_R096_T25WET_20251014T161521.zarr/measurements/reflectance/r10m",
            "type": "application/vnd+zarr",
            "multiscale": {
              "template": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/14/products/cpm_v256/S2C_MSIL2A_20251014T142151_N0511_R096_T25WET_20251014T161521.zarr/measurements/reflectance/{{resolution}}"
              "r20m": {
                  origingroupname: "r10m"
                  gsd: ...,
                  projection: ...,
                  tilegird: ...,
                  ...
              }  
            },
            "bands": [
                {"name": "B02", "common_name": "blue", "description": "Blue (band 2)", "center_wavelength": 0.49, "full_width_half_max": 0.098},
                {"name": "B03", "common_name": "green", "description": "Green (band 3)", "center_wavelength": 0.56, "full_width_half_max": 0.045},
                {"name": "B04", "common_name": "red", "description": "Red (band 4)", "center_wavelength": 0.665, "full_width_half_max": 0.038},
                {"name": "B08", "common_name": "nir", "description": "NIR 1 (band 8)", "center_wavelength": 0.842, "full_width_half_max": 0.145}
            ],
            "roles": ["data", "reflectance", "dataset"],
            "title": "Surface Reflectance - 10m",
            "xarray:open_dataset_kwargs": {"chunks": {}, "engine": "eopf-zarr", "op_mode": "native"}
        },
``` 

# B08 example (no overviews) (Brainstorming only - i think this could be removed - see #1)

```json
"B08_10m": {
            "gsd": 10,
            "href": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/14/products/cpm_v256/S2C_MSIL2A_20251014T142151_N0511_R096_T25WET_20251014T161521.zarr/measurements/reflectance/r10m/b08",
            "type": "application/vnd+zarr",
            "bands": [{"name": "B08", "common_name": "nir", "description": "NIR 1 (band 8)", "center_wavelength": 0.842, "full_width_half_max": 0.145}],
            "roles": ["data", "reflectance"],
            "title": "NIR 1 (band 8) - 10m",
            "nodata": 0,
            "alternate": {
                "xarray": {
                    "href": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/14/products/cpm_v256/S2C_MSIL2A_20251014T142151_N0511_R096_T25WET_20251014T161521.zarr/measurements/reflectance/r10m",
                    "xarray:open_dataset_kwargs": {"bands": ["B08"], "chunks": {}, "engine": "eopf-zarr", "op_mode": "analysis", "spatial_res": 10}
                }
            },
            "data_type": "uint16",
            "proj:bbox": [499980, 7690200, 609780, 7800000],
            "proj:code": "EPSG:32625",
            "proj:shape": [10980, 10980],
            "description": "BOA reflectance from MSI acquisition at spectral band b08 834.6 nm",
            "raster:scale": 0.0001,
            "raster:offset": -0.1,
            "proj:transform": [10, 0, 499980, 0, -10, 7800000, 0, 0, 1]
        },
```



Some other alternative: If we only have the highest resolution exposed (no overviews described)

Asset href link templates ("zarr-store" template solution?) ?

`self.item.assets[0].href = self.item.href/{group1}/{group2}/.../{asset/band_name}`

```python
self.item.href = "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/14/products/cpm_v256/S2C_MSIL2A_20251014T142151_N0511_R096_T25WET_20251014T161521.zarr"
```

# 1 Reflectance Asset:

```json
"assets": {
   "reflectance": {
            "gsd": 10,
            "href": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/14/products/cpm_v256/S2C_MSIL2A_20251014T142151_N0511_R096_T25WET_20251014T161521.zarr/measurements/reflectance/",
            "type": "application/vnd+zarr",
            "bands": [       
                {"name": "r20m/B01", "common_name": "coastal", "description": "Coastal aerosol (band 1)", "center_wavelength": 0.443, "full_width_half_max": 0.027,   },
                {"name": "r10m/B02", "common_name": "blue", "description": "Blue (band 2)", "center_wavelength": 0.49, "full_width_half_max": 0.098},
                {"name": "r10m/B03", "common_name": "green", "description": "Green (band 3)", "center_wavelength": 0.56, "full_width_half_max": 0.045},
                {"name": "r10m/B04", "common_name": "red", "description": "Red (band 4)", "center_wavelength": 0.665, "full_width_half_max": 0.038},
                {"name": "r20m/B05", "common_name": "rededge", "description": "Red edge 1 (band 5)", "center_wavelength": 0.704, "full_width_half_max": 0.019},
                {"name": "r20m/B06", "common_name": "rededge", "description": "Red edge 2 (band 6)", "center_wavelength": 0.74, "full_width_half_max": 0.018},
                {"name": "r20m/B07", "common_name": "rededge", "description": "Red edge 3 (band 7)", "center_wavelength": 0.783, "full_width_half_max": 0.028},
                {"name": "r20m/B8A", "common_name": "nir08", "description": "NIR 2 (band 8A)",  "center_wavelength": 0.865, "full_width_half_max": 0.033 },
                {"name": "r10m/B08", "common_name": "nir", "description": "NIR 1 (band 8)", "center_wavelength": 0.842, "full_width_half_max": 0.145},        
                {"name": "r60m/B09", "common_name": "nir09", "description": "NIR 3 (band 9)", "center_wavelength": 0.945, "full_width_half_max": 0.026},
                {"name": "r20m/B11", "common_name": "swir16", "description": "SWIR 1 (band 11)", "center_wavelength": 1.61, "full_width_half_max": 0.143},
                {"name": "r20m/B12", "common_name": "swir22", "description": "SWIR 2 (band 12)", "center_wavelength": 2.19, "full_width_half_max": 0.242}
            ],
            "roles": ["data", "reflectance", "dataset"],
            "title": "Surface Reflectance"
        }
  }
  "linkTemplates": [
    {
      "rel": "data-variable",
      "title": "store",
      "uriTemplate": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/14/products/cpm_v256/S2C_MSIL2A_20251014T142151_N0511_R096_T25WET_20251014T161521.zarr/measurements/reflectance/{resolution}/{band}",
      "variables": {
        "resolution": {
            "description": "resolution"
        },
        "band": {
          "description": "...",
         "type": "string",
          "enum": [
            "b02",
            "b03",
            "b04",
          ]
        }
      }
    ]
}
``` 

# Measurement asset for each resolution

```json
{
  "assets": {
    "measurements_10m": {
      "title": "Reflectance measurements in 10m resolution",
      "gsd": 10,
      "href": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/06/products/cpm_v256/S2B_MSIL2A_20251006T123309_N0511_R052_T28WFT_20251006T131746.zarr/measurements/reflectance/r10m",
      "type": "application/vnd+zarr; version=2",
      "roles": [ "data", "reflectance" ],
      "bands": [
        { "name": "b02", "eo:common_name": "blue", "description": "Blue (band 2)", "eo:center_wavelength": 0.49, "eo:full_width_half_max": 0.098 },
        { "name": "b03", "eo:common_name": "green", "description": "Green (band 3)",          "eo:center_wavelength": 0.56,          "eo:full_width_half_max": 0.045        },
        { "name": "b04", "eo:common_name": "red", "description": "Red (band 4)", "eo:center_wavelength": 0.665, "eo:full_width_half_max": 0.038 },
        { "name": "b08", "eo:common_name": "nir", "description": "NIR 1 (band 8)", "eo:center_wavelength": 0.842, "eo:full_width_half_max": 0.145 }
      ],
      "proj:code": "EPSG:32634",
      "proj:shape": [10980,10980],
      "proj:transform": [],
      "proj:bbox": [],
      "nodata": 0,
      "data_type": "uint16",
      "raster:scale": 0.0001,
      "raster:offset": -0.1,
      "raster:spatial_resolution": 10
    },
    "measurements_20m": {
      "title": "Reflectance measurements in 20m resolution",
      "gsd": 20,
      "href": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/06/products/cpm_v256/S2B_MSIL2A_20251006T123309_N0511_R052_T28WFT_20251006T131746.zarr/measurements/reflectance/r20m",
      "type": "application/vnd+zarr; version=2",
      "bands": [
        { "name": "b01", "eo:common_name": "coastal", "description": "Coastal aerosol (band 1)", "eo:center_wavelength": 0.443, "eo:full_width_half_max": 0.027 },
        { "name": "b02", "eo:common_name": "blue", "description": "Blue (band 2)", "eo:center_wavelength": 0.49, "eo:full_width_half_max": 0.098 },
        { "name": "b03", "eo:common_name": "green", "description": "Green (band 3)",          "eo:center_wavelength": 0.56,          "eo:full_width_half_max": 0.045        },
        { "name": "b04", "eo:common_name": "red", "description": "Red (band 4)", "eo:center_wavelength": 0.665, "eo:full_width_half_max": 0.038 },
        { "name": "b05", "eo:common_name": "rededge071", "description": "Red edge 1 (band 5)", "eo:center_wavelength": 0.704, "eo:full_width_half_max": 0.019 },
        { "name": "b06", "eo:common_name": "rededge075", "description": "Red edge 2 (band 6)", "eo:center_wavelength": 0.74, "eo:full_width_half_max": 0.018 },
        { "name": "b07", "eo:common_name": "rededge078", "description": "Red edge 3 (band 7)", "eo:center_wavelength": 0.783, "eo:full_width_half_max": 0.028 },
        { "name": "b8a", "eo:common_name": "nir08", "description": "NIR 2 (band 8A)", "eo:center_wavelength": 0.865, "eo:full_width_half_max": 0.033 },
        { "name": "b11", "eo:common_name": "swir16", "description": "SWIR 1 (band 11)", "eo:center_wavelength": 1.61, "eo:full_width_half_max": 0.143 },
        { "name": "b12", "eo:common_name": "swir22", "description": "SWIR 2 (band 12)", "eo:center_wavelength": 2.19, "eo:full_width_half_max": 0.242 }
      ],
      "roles": [ "data", "reflectance" ],
      "proj:code": "EPSG:32634",
      "proj:shape": [5490,5490],
      "proj:transform": [],
      "proj:bbox": [],
      "nodata": 0,
      "data_type": "uint16",
      "raster:scale": 0.0001,
      "raster:offset": -0.1,
      "raster:spatial_resolution": 20
    },
    "measurements_60m": {
      "title": "Reflectance measurements in 60m resolution",
      "gsd": 60,
      "href": "https://objects.eodc.eu:443/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/06/products/cpm_v256/S2B_MSIL2A_20251006T123309_N0511_R052_T28WFT_20251006T131746.zarr/measurements/reflectance/r60m",
      "type": "application/vnd+zarr; version=2",
      "bands": [
        { "name": "b01", "eo:common_name": "coastal", "description": "Coastal aerosol (band 1)", "eo:center_wavelength": 0.443, "eo:full_width_half_max": 0.027 },
        { "name": "b02", "eo:common_name": "blue", "description": "Blue (band 2)", "eo:center_wavelength": 0.49, "eo:full_width_half_max": 0.098 },
        { "name": "b03", "eo:common_name": "green", "description": "Green (band 3)",          "eo:center_wavelength": 0.56,          "eo:full_width_half_max": 0.045        },
        { "name": "b04", "eo:common_name": "red", "description": "Red (band 4)", "eo:center_wavelength": 0.665, "eo:full_width_half_max": 0.038 },
        { "name": "b05", "eo:common_name": "rededge071", "description": "Red edge 1 (band 5)", "eo:center_wavelength": 0.704, "eo:full_width_half_max": 0.019 },
        { "name": "b06", "eo:common_name": "rededge075", "description": "Red edge 2 (band 6)", "eo:center_wavelength": 0.74, "eo:full_width_half_max": 0.018 },
        { "name": "b07", "eo:common_name": "rededge078", "description": "Red edge 3 (band 7)", "eo:center_wavelength": 0.783, "eo:full_width_half_max": 0.028 },
        { "name": "b8a", "eo:common_name": "nir08", "description": "NIR 2 (band 8A)", "eo:center_wavelength": 0.865, "eo:full_width_half_max": 0.033 },
        { "name": "b09", "eo:common_name": "nir09", "description": "NIR 3 (band 9)", "eo:center_wavelength": 0.945, "eo:full_width_half_max": 0.026 },
        { "name": "b11", "eo:common_name": "swir16", "description": "SWIR 1 (band 11)", "eo:center_wavelength": 1.61, "eo:full_width_half_max": 0.143 },
        { "name": "b12", "eo:common_name": "swir22", "description": "SWIR 2 (band 12)", "eo:center_wavelength": 2.19, "eo:full_width_half_max": 0.242 }
      ],
      "roles": [ "data", "reflectance" ],
      "proj:code": "EPSG:32634",
      "proj:shape": [1830,1830],
      "proj:transform": [],
      "proj:bbox": [],
      "nodata": 0,
      "data_type": "uint16",
      "raster:scale": 0.0001,
      "raster:offset": -0.1,
      "raster:spatial_resolution": 60
    }
  }
}
```
