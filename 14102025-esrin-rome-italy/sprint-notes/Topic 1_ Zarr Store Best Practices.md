---
title: 'Topic 1: Zarr Store Best Practices'

---

# Topic 1: Zarr Store Best Practices

**Key questions/priorities for this topic:**
1) Layout a mapping of Zarr store concepts to STAC concepts (e.g., groups, arrays, variables to collections, items, assets, bands)
2) Identify existing or missing asset roles for Zarr stores (e.g. consolidated metadata, zarr hierarchy, virtual Zarr?)
3) Specify metadata fields for Zarr store properties (chunk sizes, compression, storage layout)
4) Integration patterns with existing extensions (datacube, cf)
5) Asset organization for multi-resolution and hierarchical Zarr stores
6) Guidelines for storing STAC metadata within Zarr stores 
7) Naming conventions for Zarr/Virual Zarr assets 
8) Datetime range handling for multidimensional datasets

## 1) Layout a mapping of Zarr store concepts to STAC concepts

Firstly, we collect what options by participants regarding the mapping of nomenclature are being used.

---

| STAC | ZARR |
| -------- | -------- |
| Catalog  | Group    |
| Collections  | Group of Arrays |
| Item  | Array |
| Asset  | Variable |
| Band  | Coordinates |

---

### Earth Data Hub: https://earthdatahub.destine.eu/ by Alessandro

|STAC|Zarr|[ERA 5 example](https://earthdatahub.destine.eu/collections/era5) |
|---|---|--|
|Catalog|-|-|
|Collections|-|ERA5|
|Item|Group (could be, but not yet used )| |
|Asset|Group of arrays (that have a set of common coordinates) = Group in NetCFD / Read as a dataset in Xarray -> mapped to an asset| |
||Variable| mapped to a band in the Asset (or the Item)|
||Coordinates| |

---

### DKRZ: https://wwestac.cloud.dkrz.de/collections/ngc3028

|STAC|Zarr| DKRZ |
|---|---|--|
|Catalog|-| |
|Collections| Group||
|Item| Group of arrays | |
|Asset|| |
||Variable| |
||Coordinates| |

---

## Notes from discussion

*14/10/2025*

Tangible ERA5 example: 
- high level collection: concepts (on website, high level image squares)
    - ex
    - ex 
    - ex
- datasets: actually contain the data
- STAC Items under era5 
    - ERA5 hourly data on single levels 
        - every item has just one asset at the moment
        - considering adding more assets for each asset (different views)
        - every asset is a piece of code 
    - ERA5 montly data on single levels
    - Pressure levels
    - Land hourly data  


Same issue as EOPF? EOPF resolutions vs -- different temporal extents 

Question on this mapping is what prevents to move the Group to the Item level

|STAC|Zarr| EOPF example |
|---|---|--|
|Catalog|-| |
|Collections|Outside of the Zarr |Product Type (S1 SLC / S2 L2A / ...)|
|Item| A general Group  | EO Product|
|Asset | The general Group, Group of arrays | EO Product + r10m or slc or ... |
||Variable| |
||Coordinates| |

Reason of exposing the group of arrays to facilitate access. dont need to know the path to get to data

We need to define the two basic object:
- Group of groups
- Group of arrays

As a group, we want to determine which mapping from Zarr --> STAC is best. Do pro/con list of each mapping 

Content of STAC vs Zarr: try to avoid repition of metadata could be something usefull for some people:
- it is mostly linked to how the data are exposed (expose through STAC, filter through Zarr )

Comment on how to align a mapping with potential people that would like to present their STAC collectiomn of COG through a virtualization.

Need to be able to differenciate between Zarr Groups and Group of Arrays since they seem to represent different "objects"

A need on the definition of oveview for Zarr in STAC:
- Today Zarr does not contain reprenset them (geotiff like)
- Should we do something in stac (potential role extension  or separate asset)

**Things to clarify:**
- mapping of the hierarchy - specifically how to tell groups of arrays (xr.Dataset) and groups of groups (xr.DataTree) apart at the STAC level
- n-dimensional overview representation
- metadata representation in Zarr

Need of someone to represent the chunk in the STAC for data cube.
- comment on is it really need
- Yes to provide by example two assets that represents same data with different chunking strategies
- Better could be to specify a way to represent the data 
- Perhaps it could be role like 


Compression needs:
- Zarr supports specific compression
- So it could be beneficial to have the info, so that people knows if the driver is supported
- The consensus is that is not needed in search, it would be an access issue

---
Specific topic that could be adressed in the other group but kept as a possible exploration:
- How to capture what Xarray extension was doing but as a generic / agnostic extension (not a specific language one)
- Open a ticket on STAC browser for misalignement on Collection of collection/ Catalog of Catalog

Can be adressed in the next days.


If there is a typical way people express overviews (multiscale, levels of aggregation, resampling method, etc)

---
- Good practices learned from CDSE STAC:
https://github.com/eu-cdse/eometadatatool

- EOPF Sentinel Zarr Samples Service STAC API
https://stac.browser.user.eopf.eodc.eu
---

