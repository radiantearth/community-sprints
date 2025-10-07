## EOPF Assets

This documents describes the current EOPF Sample Service approach to EOPF assets as they are available in the [STAC catalog](https://stac.browser.user.eopf.eodc.eu/). 

### Generic assets

For every EOPF product, independent of mission and product type, the following applies:
- All Zarr groups which are in the `measurements` group and contain arrays are provided as assets. 
- There is an asset with the key `product` which references the full Zarr store (top-level of Zarr hierarchy).
- There is an asset with the key `product_metadata` which references the consolidated metadata file (.zmetadata) at the top-level of the Zarr hierarchy
- Assets representing a Zarr group have the role `dataset` and use the xarray extension to provide parameters for the [xarray-eopf](https://github.com/EOPF-Sample-Service/xarray-eopf) backend.
- Assets representing a Zarr array have the role `data`

### Mission-specific assets

For some product types additional assets are provided. Most of them reference Zarr arrays. The intention behind this was to provide a similar Item/Asset structure to the users as in CDSE to be less disruptive and to facilitate the user uptake. The following list represents the current selection:

- Sentinel-2 L1C
  - Reflectance data of the indiviual bands, but only in their finest resolution
  - True color image data (TCI)
- Sentinel-2 L2A
  - Reflectance data of the indiviual bands, but only in their finest resolution
  - Aerosol optical thickness (AOT)
  - Water vapour (WVP)
  - Scene classification map (SCL)
  - True color image data (TCI)
- Sentinel-3 OLCI L1 EFR/ERR
  - Radiance for the individual bands Oa01 to Oa21
- Sentinel-3 OLCI L2 LFR/LRR
  - Integrated Water Vapour Column
  - Land Quality and Science Flags
  - Terrestrial Chlorophyll Index
  - Green Instantaneous FAPAR (GIFAPAR)
  - GIFAPAR - Rectified Reflectance - red and NIR channel
- Sentinel-1 GRD
  - Calibration and noise metadata per polarisation

### See also

- [Implementation Topics](../implementation-topics.md), section EOPF Sample Service Catalog
- https://github.com/EOPF-Sample-Service/eopf-stac/issues/27
- https://github.com/EOPF-Sample-Service/eopf-stac/issues/38