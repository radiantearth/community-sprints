## EOPF Zarr Stores

This document gives on overview about the EOPF Zarr store structure of the different Sentinel missions, as currently created during SAFE to EOPF conversion with [CPM](https://cpm.pages.eopf.copernicus.eu/eopf-cpm/main/index.html) by the EOPF Sample Service.

### Top-level structure

```
/
├── conditions      # variables that describe measurement conditions
├── measurements    # variables for the sensed data
├── quality         # variables with flags and quality information that help to filter measurements
├── .zattrs         # metadata: stac item, processing history and other metadata
├── .zgroup
└── .zmetadata      # content of .zattrs and consolidated metadata of whole Zarr store
```


### Sentinel-2

- Measurements grouped by resolution
- Bands as variables
- Example: https://stac.browser.user.eopf.eodc.eu/collections/sentinel-2-l2a/items/S2B_MSIL2A_20251006T123309_N0511_R052_T28WFT_20251006T131746


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

### Sentinel-3

- One dataset for all measurements 
- Bands as variables
- Example: https://stac.browser.user.eopf.eodc.eu/collections/sentinel-3-olci-l1-efr/items/S3A_OL_1_EFR____20251006T121942_20251006T122242_20251006T141353_0179_131_166_2340_PS1_O_NR_004

```
/
├── conditions
├── measurements
│   ├── latitude (4090, 4865) float64
│   ├── longitude (4090, 4865) float64
│   ├── oa01_radiance (4090, 4865) float32
│   ├── oa02_radiance (4090, 4865) float32
│   ├── oa03_radiance (4090, 4865) float32
│   ├── ...
│   ├── oa21_radiance (4090, 4865) float32
│   ├── orphans
│   └── time_stamp (4090,) int64
└── quality
```

### Sentinel-1 GRD

- Data is grouped by polarization
- Example: https://stac.browser.user.eopf.eodc.eu/collections/sentinel-1-l1-grd/items/S1A_IW_GRDH_1SDV_20251006T125832_20251006T125857_061305_07A5EF_9D82

```
/
├── S01SIWGRD_20251006T125832_0025_A350_9D82_07A5EF_VH
│   ├── conditions
│   ├── measurements
│   └── quality
└── S01SIWGRD_20251006T125832_0025_A350_9D82_07A5EF_VV
    ├── conditions
    ├── measurements
    └── quality
```

### Sentinel-1 SLC

-  Data is grouped by 
   - polarization (VH, VV)
   - sub-swath (IW1 .. IW3)
   - and burst (60458 .. 60465)
- Example: converted from S1A_IW_SLC__1SDV_20250130T161959_20250130T162026_057676_071BB7_3B7C.SAFE

```
/
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60457 
│   ├── conditions
│   ├── measurements                                              
│   └── quality
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60458
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60459
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60460
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60461
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60462
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60463
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60464
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW1_60465
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60457
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60458
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60459
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60460
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60461
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60462
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60463
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60464
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW2_60465
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60457
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60458
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60459
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60460
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60461
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60462
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60463
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60464
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VH_IW3_60465
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60457
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60458
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60459
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60460
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60461
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60462
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60463
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60464
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW1_60465
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60457
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60458
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60459
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60460
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60461
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60462
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60463
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60464
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW2_60465
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60457
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60458
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60459
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60460
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60461
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60462
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60463
├── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60464
└── S01SIWSLC_20250130T161959_0027_A330_3B7C_071BB7_VV_IW3_60465
```

### Sentinel-1 OCN

- Data is grouped by geophysical component
  - Ocean Swell spectra (osw)
  - Ocean Wind field (owi)
  - Surface Radial Velocity (rvl)
- Example: https://stac.browser.user.eopf.eodc.eu/collections/sentinel-1-l2-ocn/items/S1A_EW_OCN__2SDH_20251006T120345_20251006T120450_061304_07A5E9_6344

```
/
├── osw
│   └── S01SEWOCN_20251006T120345_0065_A350_6344_07A5E9_HH
│       ├── conditions
│       ├── measurements
│       └── quality
├── owi
│   └── S01SEWOCN_20251006T120345_0065_A350_6344_07A5E9_HH
│       ├── conditions
│       ├── measurements
│       │   ├── latitude (434, 417) float32
│       │   ├── longitude (434, 417) float32
│       │   ├── wind_direction (434, 417) float32
│       │   └── wind_speed (434, 417) float32
│       └── quality
└── rvl
    └── S01SEWOCN_20251006T120345_0065_A350_6344_07A5E9_HH
        ├── conditions
        ├── measurements
        └── quality
```

## Related information

- EOPF Product Specifications
  - Sentinel 1: https://s1.pages.eopf.copernicus.eu/s1-l12-rp/main/pfs/index.html
  - Sentinel 2: https://s2.pages.eopf.copernicus.eu/pdfs-adfs
  - Sentinel 3 
    - OLCI: https://s3.pages.eopf.copernicus.eu/OLCI/s3olci/main/pdfs/index.html
    - SLSTR: https://s3.pages.eopf.copernicus.eu/SLSTR/s3slstr/main/pdfs/index.html
- [EOPF Naming Scheme](https://cpm.pages.eopf.copernicus.eu/eopf-cpm/main/PSFD/3-product-types-naming-rules.html)
- [EOPF Core Python Modules](https://cpm.pages.eopf.copernicus.eu/eopf-cpm/main/index.html)