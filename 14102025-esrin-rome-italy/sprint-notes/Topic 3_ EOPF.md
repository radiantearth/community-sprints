---
title: 'Topic 3: EOPF'

---

# Topic 3: EOPF

- GitHub STAC Metadata: [eopf-stac](https://github.com/EOPF-Sample-Service/eopf-stac/issues)
- GitHub .zarr/xarray Driver: [xarray-eopf](https://github.com/EOPF-Sample-Service/xarray-eopf/issues)
- GitLab python processing modules (Sentinel IPF): [eopf-cpm](https://gitlab.eopf.copernicus.eu/cpm/eopf-cpm/-/issues)

## eopf extension
- should to be kept to avoid mission specific extensions
- should be moved to official STAC extensions GitHub, Issue in CPM repository is already there

## Group level metadata
- Regarding Zarr group level metadata there is already a PR at CPM Gitlab
- STAC group level assets:
  - provide "proj:transform" and "proj:bbox"

## Group S1 GRD data by polarization
- Catherine to open a CPM issue

## Sentinel-1 SLC
- Create STAC item for each burst to enable users to select only bursts of their area of interest
  - ensure geometry is correctly representing the 'bar' 
  - property needed to store burst id e.g. `sar:burst_id`, open PR at sat extension

## Sentinel-2 
- Request to expose conditions/geometry group as array
- use same Zarr group as STAC asset approach for conditions/mask/l2a_classification/r20m or quality/atmosphere/r10m group to expose
  - Aerosol optical thickness (AOT)
  - Water vapour (WVP)
  - Scene classification map (SCL)
- Have chunk size in measurement assets?

## Have a dedicated version for mapping model in CPM
- Add it to processing:software property like
```json
"processing:software": {
  "Sentinel-1 IPF": "002.71",
  "CPM": "2.6.1",
  "CPM Mapping Model": ""
}
```

