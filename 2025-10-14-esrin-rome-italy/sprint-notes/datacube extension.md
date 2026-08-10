---
title: datacube extension

---

# datacube extension

STAC spec bands: https://github.com/radiantearth/stac-spec/blob/master/commons/common-metadata.md#bands
Datacube STAC Extension: https://github.com/stac-extensions/datacube

**champion:** Alessandro Amici

## Questions
- What from the data cube extension can we actually use bands for?
    - Going through the fields:
        - cube:dimension is required
        - cube:variable is analogous to bands

Should we use bands? 
- Cons:
    - bands typically share units whereas variables don't necessarily
    - it is not the typical word in this domain
- Pros:
    - tooling might expect bands and if you don't provide them then the tooling needs to know how to handle that.
    - if we push on with using bands more heavily (as in Emmanuel's PR) we can stay aligned.

Right now there is a 1:1 translation between the zarr and the datacube extension. 

If you can put whatever you want from whatever STAC extension within bands.


## Variable Object if we make it a band
| Existing Field Name | Proposed Field Name | Type  | Description |
| ---------------- | -------------------------| ----------- | --- |
| dimensions       | cube:dimension_refs   | \[string]                | **REQUIRED.** The dimensions of the variable. This should refer to keys in the ``cube:dimensions`` object or be an empty list if the variable has no dimensions. |
| type             | cube:type  |  string                   | **REQUIRED.** Type of the variable, either `data` or `auxiliary`. | 
| description      | description  | string                   | Same as in the band definition |
| extent           | statistics.minimum/statistics.maximum | nested object | The minimum and maximum of the values within the variable array. Same as in the band spec definition |
| values           | cube:values | \[number\|string]        | An (ordered) list of all values, especially useful for [nominal](https://en.wikipedia.org/wiki/Level_of_measurement#Nominal_level) values. |
| unit             | units | string                   | Same as in the band spec definition |
| nodata           | nodata | number\|string           | Same as in the band spec definition |
| data_type        | data_type | string                   | Same as in the band spec definition |



## Example using datacube as it is now (YAML repesentation of a STAC Item)

```yaml
stac_version: 1.1.0
type: Feature
collection: era5
id: reanalysis-era5-land
properties:
  dc:title: ERA5-Land
  dc:abstract: >-
    ERA5-Land provides land variables evolution over several decades at an
    enhanced resolution compared to ERA5. The dataset is provided in a ARCO Zarr
    format ideal for time series analysis

    Hourly, daily and monthly.
  dc:access_rights: unrestricted
  dc:subject:
    - ERA5
    - Land
    - ECMWF
    - reanalysis
    - weather
  dc:description: >
    ERA5-Land is a reanalysis dataset providing a consistent view of the
    evolution of land variables
  dc:accrual_periodicity: 'freq:monthly'
  dc:extent: 703.7 TB
  datetime: '2025-09-30T23:00:00Z'
  start_datetime: '1950-01-01T00:00:00Z'
  end_datetime: '2025-09-30T23:00:00Z'
  updated: '2025-10-12T20:55:35Z'
  cube:dimensions:
    valid_time:
      type: temporal
      extent:
      - '1950-01-01T00:00:00Z'
      - '2025-09-30T00:00:00Z'
      step: PT1D
    latitude:
      type: spatial
      axis: 'y'
      extent:
      - 90
      - -57.1
      step: 0.1
      reference_system: 4326
    longitude:
      type: spatial
      axis: x
      extent:
      - 0
      - 359.9
      step: 0.1
      reference_system: 4326
  cube:variables:
    d2m:
      type: data
      description: 2 metre dewpoint temperature
      dimensions:
        - valid_time
        - latitude
        - longitude
      unit: K
    u10:
      type: data
      description: 10 metre U wind component
      dimensions:
        - valid_time
        - latitude
        - longitude
      extent: [-70, 70]
      unit: m s**-1
    v10:
      type: data
      description: 10 metre V wind component
      dimensions:
        - valid_time
        - latitude
        - longitude
      unit: m s**-1
geometry:
  type: MultiPolygon
  coordinates:
    - - - - -180
          - -57.1
        - - -180
          - 90
        - - -0.1
          - 90
        - - -0.1
          - -57.1
        - - -180
          - -57.1
    - - - - 0
          - -57.1
        - - 0
          - 90
        - - 180
          - 90
        - - 180
          - -57.1
        - - 0
          - -57.1
bbox:
  - 0
  - -57.1
  - 359.9
  - 90
links:
  - href: 'https://doi.org/10.24381/cds.e2161bac'
    rel: derived_from
    type: text/html
    title: ERA5-Land hourly data from 1950 to present
  - href: https://earthdatahub.destine.eu/api/stac/v1/collections/era5/items/reanalysis-era5-land
    rel: self
    type: application/json
  - href: 'https://earthdatahub.destine.eu/api/stac/v1/'
    rel: root
    type: application/json
  - href: 'https://earthdatahub.destine.eu/api/stac/v1/collections/era5'
    rel: parent
    type: application/json
  - href: 'https://earthdatahub.destine.eu/api/stac/v1/collections/era5'
    rel: collection
    type: application/json
assets:
  hourly-data:
    title: ERA5-land hourly data
    href: https://data.earthdatahub.destine.eu/era5/reanalysis-era5-land-no-antartica-houly-v0.zarr
    roles:
      - data
    type: application/x-zarr
    cube:dimensions:
      valid_time:
        type: temporal
        extent:
          - '1950-01-01T00:00:00Z'
          - '2025-09-30T23:00:00Z'
        step: PT1H
      latitude:
        type: spatial
        axis: 'y'
        extent:
          - 90
          - -57.1
        step: 0.1
        reference_system: 4326
      longitude:
        type: spatial
        axis: x
        extent:
          - 0
          - 359.9
        step: 0.1
        reference_system: 4326
  thumbnail:
    href: https://s3.gra.cloud.ovh.net/v1/AUTH_954d6a1ff56543e5860809415ceebf17/edh-static/desp-edh/catalogue/era5/reanalysis-era5-land/thumbnail_5f4b32d493db27aaf83c74576bf773864934f10e0911f0b3ad6f84b3f7da52e9.png
    roles:
      - thumbnail
```

## Example using bands 

```yaml
stac_version: 1.1.0
type: Feature
collection: era5
id: reanalysis-era5-land
properties:
  dc:title: ERA5-Land
  dc:abstract: >-
    ERA5-Land provides land variables evolution over several decades at an
    enhanced resolution compared to ERA5. The dataset is provided in a ARCO Zarr
    format ideal for time series analysis

    Hourly, daily and monthly.
  dc:access_rights: unrestricted
  dc:subject:
    - ERA5
    - Land
    - ECMWF
    - reanalysis
    - weather
  dc:description: >
    ERA5-Land is a reanalysis dataset providing a consistent view of the
    evolution of land variables
  dc:accrual_periodicity: 'freq:monthly'
  dc:extent: 703.7 TB
  datetime: '2025-09-30T23:00:00Z'
  start_datetime: '1950-01-01T00:00:00Z'
  end_datetime: '2025-09-30T23:00:00Z'
  updated: '2025-10-12T20:55:35Z'
  cube:dimensions:
    valid_time:
      type: temporal
      extent:
      - '1950-01-01T00:00:00Z'
      - '2025-09-30T00:00:00Z'
      step: PT1D
    latitude:
      type: spatial
      axis: 'y'
      extent:
      - 90
      - -57.1
      step: 0.1
      reference_system: 4326
    longitude:
      type: spatial
      axis: x
      extent:
      - 0
      - 359.9
      step: 0.1
      reference_system: 4326
  bands:
    - name: d2m
      cube:type: data
      description: 2 metre dewpoint temperature
      cube:dimension_refs:
        - valid_time
        - latitude
        - longitude
      unit: K
    - name: u10
      cube:type: data
      description: 10 metre U wind component
      cube:dimension_refs:
        - valid_time
        - latitude
        - longitude
      statistics:
        minumum: 0
        maximum: 10
      unit: m s**-1
    - name: v10
      cube:type: data
      description: 10 metre V wind component
      cube:dimension_refs:
        - valid_time
        - latitude
        - longitude
      unit: m s**-1
geometry:
  type: MultiPolygon
  coordinates:
    - - - - -180
          - -57.1
        - - -180
          - 90
        - - -0.1
          - 90
        - - -0.1
          - -57.1
        - - -180
          - -57.1
    - - - - 0
          - -57.1
        - - 0
          - 90
        - - 180
          - 90
        - - 180
          - -57.1
        - - 0
          - -57.1
bbox:
  - 0
  - -57.1
  - 359.9
  - 90
links:
  - href: 'https://doi.org/10.24381/cds.e2161bac'
    rel: derived_from
    type: text/html
    title: ERA5-Land hourly data from 1950 to present
  - href: https://earthdatahub.destine.eu/api/stac/v1/collections/era5/items/reanalysis-era5-land
    rel: self
    type: application/json
  - href: 'https://earthdatahub.destine.eu/api/stac/v1/'
    rel: root
    type: application/json
  - href: 'https://earthdatahub.destine.eu/api/stac/v1/collections/era5'
    rel: parent
    type: application/json
  - href: 'https://earthdatahub.destine.eu/api/stac/v1/collections/era5'
    rel: collection
    type: application/json
assets:
  hourly-data:
    title: ERA5-land hourly data
    href: https://data.earthdatahub.destine.eu/era5/reanalysis-era5-land-no-antartica-houly-v0.zarr
    roles:
      - data
    type: application/x-zarr
  thumbnail:
    href: https://s3.gra.cloud.ovh.net/v1/AUTH_954d6a1ff56543e5860809415ceebf17/edh-static/desp-edh/catalogue/era5/reanalysis-era5-land/thumbnail_5f4b32d493db27aaf83c74576bf773864934f10e0911f0b3ad6f84b3f7da52e9.png
    roles:
      - thumbnail
```
