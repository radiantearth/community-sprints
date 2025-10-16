---
title: Sample of Xarray DataTree of EOPF

---

# Sample of Sentinle-2 L2A Xarray DataTree by EOPF as of 2025-10

`S2A_MSIL2A_20251013T091041_N0511_R050_T37WDM_20251013T105319`

Path: [https://objects.eodc.eu/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/13/products/cpm_v256/S2A_MSIL2A_20251013T091041_N0511_R050_T37WDM_20251013T105319.zarr](https://objects.eodc.eu/e05ab01a9d56408d82ac32d69a5aae2a:202510-s02msil2a-eu/13/products/cpm_v256/S2A_MSIL2A_20251013T091041_N0511_R050_T37WDM_20251013T105319.zarr)


```python
s2_l2a_dataset = xr.open_dataset(
    s2_l2a_url,
    engine="zarr",
    group="/measurements/reflectance/r10m",
    chunks={"x": 512, "y": 512}
    # chunks="auto"
)
```

```
<xarray.DataTree>
Group: /
│   Attributes:
│       other_metadata:  {'AOT_retrieval_model': 'CAMS', 'L0_ancillary_data_quali...
│       stac_discovery:  {'assets': {'analytic': {'eo:bands': [{'center_wavelengt...
├── Group: /conditions
│   ├── Group: /conditions/geometry
│   │       Dimensions:                        (angle: 2, band: 13, y: 23, x: 23,
│   │                                           detector: 7)
│   │       Coordinates:
│   │         * angle                          (angle) <U7 56B 'zenith' 'azimuth'
│   │         * band                           (band) <U3 156B 'b01' 'b02' ... 'b11' 'b12'
│   │         * y                              (y) int64 184B 7200000 7195000 ... 7090000
│   │         * x                              (x) int64 184B 399960 404960 ... 509960
│   │         * detector                       (detector) int64 56B 4 5 6 7 8 9 10
│   │       Data variables:
│   │           mean_sun_angles                (angle) float64 16B dask.array<chunksize=(2,), meta=np.ndarray>
│   │           mean_viewing_incidence_angles  (band, angle) float64 208B dask.array<chunksize=(13, 2), meta=np.ndarray>
│   │           sun_angles                     (angle, y, x) float64 8kB dask.array<chunksize=(2, 23, 23), meta=np.ndarray>
│   │           viewing_incidence_angles       (band, detector, angle, y, x) float64 770kB dask.array<chunksize=(7, 4, 2, 23, 23), meta=np.ndarray>
│   ├── Group: /conditions/mask
│   │   ├── Group: /conditions/mask/detector_footprint
│   │   │   ├── Group: /conditions/mask/detector_footprint/r10m
│   │   │   │       Dimensions:  (y: 10980, x: 10980)
│   │   │   │       Coordinates:
│   │   │   │         * y        (y) int64 88kB 7199995 7199985 7199975 ... 7090225 7090215 7090205
│   │   │   │         * x        (x) int64 88kB 399965 399975 399985 399995 ... 509735 509745 509755
│   │   │   │       Data variables:
│   │   │   │           b02      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b03      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b04      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b08      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   ├── Group: /conditions/mask/detector_footprint/r20m
│   │   │   │       Dimensions:  (y: 5490, x: 5490)
│   │   │   │       Coordinates:
│   │   │   │         * y        (y) int64 44kB 7199990 7199970 7199950 ... 7090250 7090230 7090210
│   │   │   │         * x        (x) int64 44kB 399970 399990 400010 400030 ... 509710 509730 509750
│   │   │   │       Data variables:
│   │   │   │           b05      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b06      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b07      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b11      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b12      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   │           b8a      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │   └── Group: /conditions/mask/detector_footprint/r60m
│   │   │           Dimensions:  (y: 1830, x: 1830)
│   │   │           Coordinates:
│   │   │             * y        (y) int64 15kB 7199970 7199910 7199850 ... 7090350 7090290 7090230
│   │   │             * x        (x) int64 15kB 399990 400050 400110 400170 ... 509610 509670 509730
│   │   │           Data variables:
│   │   │               b01      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │               b09      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   │               b10      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   ├── Group: /conditions/mask/l1c_classification
│   │   │   └── Group: /conditions/mask/l1c_classification/r60m
│   │   │           Dimensions:  (y: 1830, x: 1830)
│   │   │           Coordinates:
│   │   │             * y        (y) int64 15kB 7199970 7199910 7199850 ... 7090350 7090290 7090230
│   │   │             * x        (x) int64 15kB 399990 400050 400110 400170 ... 509610 509670 509730
│   │   │           Data variables:
│   │   │               b00      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │   └── Group: /conditions/mask/l2a_classification
│   │       ├── Group: /conditions/mask/l2a_classification/r20m
│   │       │       Dimensions:  (y: 5490, x: 5490)
│   │       │       Coordinates:
│   │       │         * y        (y) int64 44kB 7199990 7199970 7199950 ... 7090250 7090230 7090210
│   │       │         * x        (x) int64 44kB 399970 399990 400010 400030 ... 509710 509730 509750
│   │       │       Data variables:
│   │       │           scl      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   │       └── Group: /conditions/mask/l2a_classification/r60m
│   │               Dimensions:  (y: 1830, x: 1830)
│   │               Coordinates:
│   │                 * y        (y) int64 15kB 7199970 7199910 7199850 ... 7090350 7090290 7090230
│   │                 * x        (x) int64 15kB 399990 400050 400110 400170 ... 509610 509670 509730
│   │               Data variables:
│   │                   scl      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│   └── Group: /conditions/meteorology
│       ├── Group: /conditions/meteorology/cams
│       │       Dimensions:        (latitude: 9, longitude: 9)
│       │       Coordinates:
│       │         * latitude       (latitude) float64 72B 64.91 64.79 64.67 ... 64.06 63.94
│       │         * longitude      (longitude) float64 72B 36.88 37.17 37.46 ... 38.91 39.2
│       │           isobaricInhPa  float64 8B ...
│       │           number         int64 8B ...
│       │           step           int64 8B ...
│       │           surface        float64 8B ...
│       │           time           datetime64[ns] 8B ...
│       │           valid_time     datetime64[ns] 8B ...
│       │       Data variables:
│       │           aod1240        (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           aod469         (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           aod550         (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           aod670         (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           aod865         (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           bcaod550       (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           duaod550       (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           omaod550       (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           ssaod550       (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           suaod550       (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │           z              (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│       │       Attributes:
│       │           Conventions:             CF-1.7
│       │           GRIB_centre:             ecmf
│       │           GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
│       │           GRIB_edition:            1
│       │           GRIB_subCentre:          0
│       │           history:                 2025-10-13T13:10 GRIB to CDM+CF via cfgrib-0.9.1...
│       │           institution:             European Centre for Medium-Range Weather Forecasts
│       └── Group: /conditions/meteorology/ecmwf
│               Dimensions:        (latitude: 9, longitude: 9)
│               Coordinates:
│                 * latitude       (latitude) float64 72B 64.91 64.79 64.67 ... 64.06 63.94
│                 * longitude      (longitude) float64 72B 36.88 37.17 37.46 ... 38.91 39.2
│                   isobaricInhPa  float64 8B ...
│                   number         int64 8B ...
│                   step           int64 8B ...
│                   surface        float64 8B ...
│                   time           datetime64[ns] 8B ...
│                   valid_time     datetime64[ns] 8B ...
│               Data variables:
│                   msl            (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│                   r              (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│                   tco3           (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│                   tcwv           (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│                   u10            (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│                   v10            (latitude, longitude) float32 324B dask.array<chunksize=(9, 9), meta=np.ndarray>
│               Attributes:
│                   Conventions:             CF-1.7
│                   GRIB_centre:             ecmf
│                   GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
│                   GRIB_edition:            1
│                   GRIB_subCentre:          0
│                   history:                 2025-10-13T13:10 GRIB to CDM+CF via cfgrib-0.9.1...
│                   institution:             European Centre for Medium-Range Weather Forecasts
├── Group: /measurements
│   └── Group: /measurements/reflectance
│       ├── Group: /measurements/reflectance/r10m
│       │       Dimensions:  (y: 10980, x: 10980)
│       │       Coordinates:
│       │         * y        (y) int64 88kB 7199995 7199985 7199975 ... 7090225 7090215 7090205
│       │         * x        (x) int64 88kB 399965 399975 399985 399995 ... 509735 509745 509755
│       │       Data variables:
│       │           b02      (y, x) float64 964MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b03      (y, x) float64 964MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b04      (y, x) float64 964MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b08      (y, x) float64 964MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       ├── Group: /measurements/reflectance/r20m
│       │       Dimensions:  (y: 5490, x: 5490)
│       │       Coordinates:
│       │         * y        (y) int64 44kB 7199990 7199970 7199950 ... 7090250 7090230 7090210
│       │         * x        (x) int64 44kB 399970 399990 400010 400030 ... 509710 509730 509750
│       │       Data variables:
│       │           b01      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b02      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b03      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b04      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b05      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b06      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b07      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b11      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b12      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       │           b8a      (y, x) float64 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│       └── Group: /measurements/reflectance/r60m
│               Dimensions:  (y: 1830, x: 1830)
│               Coordinates:
│                 * y        (y) int64 15kB 7199970 7199910 7199850 ... 7090350 7090290 7090230
│                 * x        (x) int64 15kB 399990 400050 400110 400170 ... 509610 509670 509730
│               Data variables:
│                   b01      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b02      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b03      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b04      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b05      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b06      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b07      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b09      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b11      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b12      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
│                   b8a      (y, x) float64 27MB dask.array<chunksize=(512, 512), meta=np.ndarray>
└── Group: /quality
    ├── Group: /quality/atmosphere
    │   ├── Group: /quality/atmosphere/r10m
    │   │       Dimensions:  (y: 10980, x: 10980)
    │   │       Coordinates:
    │   │         * y        (y) int64 88kB 7199995 7199985 7199975 ... 7090225 7090215 7090205
    │   │         * x        (x) int64 88kB 399965 399975 399985 399995 ... 509735 509745 509755
    │   │       Data variables:
    │   │           aot      (y, x) uint16 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           wvp      (y, x) uint16 241MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   ├── Group: /quality/atmosphere/r20m
    │   │       Dimensions:  (y: 5490, x: 5490)
    │   │       Coordinates:
    │   │         * y        (y) int64 44kB 7199990 7199970 7199950 ... 7090250 7090230 7090210
    │   │         * x        (x) int64 44kB 399970 399990 400010 400030 ... 509710 509730 509750
    │   │       Data variables:
    │   │           aot      (y, x) uint16 60MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           wvp      (y, x) uint16 60MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   └── Group: /quality/atmosphere/r60m
    │           Dimensions:  (y: 1830, x: 1830)
    │           Coordinates:
    │             * y        (y) int64 15kB 7199970 7199910 7199850 ... 7090350 7090290 7090230
    │             * x        (x) int64 15kB 399990 400050 400110 400170 ... 509610 509670 509730
    │           Data variables:
    │               aot      (y, x) uint16 7MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │               wvp      (y, x) uint16 7MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    ├── Group: /quality/l2a_quicklook
    │   ├── Group: /quality/l2a_quicklook/r10m
    │   │       Dimensions:  (band: 3, y: 10980, x: 10980)
    │   │       Coordinates:
    │   │         * band     (band) int64 24B 1 2 3
    │   │         * y        (y) int64 88kB 7199995 7199985 7199975 ... 7090225 7090215 7090205
    │   │         * x        (x) int64 88kB 399965 399975 399985 399995 ... 509735 509745 509755
    │   │       Data variables:
    │   │           tci      (band, y, x) uint8 362MB dask.array<chunksize=(3, 512, 512), meta=np.ndarray>
    │   ├── Group: /quality/l2a_quicklook/r20m
    │   │       Dimensions:  (band: 3, y: 5490, x: 5490)
    │   │       Coordinates:
    │   │         * band     (band) int64 24B 1 2 3
    │   │         * y        (y) int64 44kB 7199990 7199970 7199950 ... 7090250 7090230 7090210
    │   │         * x        (x) int64 44kB 399970 399990 400010 400030 ... 509710 509730 509750
    │   │       Data variables:
    │   │           tci      (band, y, x) uint8 90MB dask.array<chunksize=(3, 512, 512), meta=np.ndarray>
    │   └── Group: /quality/l2a_quicklook/r60m
    │           Dimensions:  (band: 3, y: 1830, x: 1830)
    │           Coordinates:
    │             * band     (band) int64 24B 1 2 3
    │             * y        (y) int64 15kB 7199970 7199910 7199850 ... 7090350 7090290 7090230
    │             * x        (x) int64 15kB 399990 400050 400110 400170 ... 509610 509670 509730
    │           Data variables:
    │               tci      (band, y, x) uint8 10MB dask.array<chunksize=(3, 512, 512), meta=np.ndarray>
    ├── Group: /quality/mask
    │   ├── Group: /quality/mask/r10m
    │   │       Dimensions:  (y: 10980, x: 10980)
    │   │       Coordinates:
    │   │         * y        (y) int64 88kB 7199995 7199985 7199975 ... 7090225 7090215 7090205
    │   │         * x        (x) int64 88kB 399965 399975 399985 399995 ... 509735 509745 509755
    │   │       Data variables:
    │   │           b02      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b03      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b04      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b08      (y, x) uint8 121MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   ├── Group: /quality/mask/r20m
    │   │       Dimensions:  (y: 5490, x: 5490)
    │   │       Coordinates:
    │   │         * y        (y) int64 44kB 7199990 7199970 7199950 ... 7090250 7090230 7090210
    │   │         * x        (x) int64 44kB 399970 399990 400010 400030 ... 509710 509730 509750
    │   │       Data variables:
    │   │           b05      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b06      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b07      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b11      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b12      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   │           b8a      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │   └── Group: /quality/mask/r60m
    │           Dimensions:  (y: 1830, x: 1830)
    │           Coordinates:
    │             * y        (y) int64 15kB 7199970 7199910 7199850 ... 7090350 7090290 7090230
    │             * x        (x) int64 15kB 399990 400050 400110 400170 ... 509610 509670 509730
    │           Data variables:
    │               b01      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │               b09      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    │               b10      (y, x) uint8 3MB dask.array<chunksize=(512, 512), meta=np.ndarray>
    └── Group: /quality/probability
        └── Group: /quality/probability/r20m
                Dimensions:  (y: 5490, x: 5490)
                Coordinates:
                  * y        (y) int64 44kB 7199990 7199970 7199950 ... 7090250 7090230 7090210
                  * x        (x) int64 44kB 399970 399990 400010 400030 ... 509710 509730 509750
                    band     int64 8B ...
                Data variables:
                    cld      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
                    snw      (y, x) uint8 30MB dask.array<chunksize=(512, 512), meta=np.ndarray>
```