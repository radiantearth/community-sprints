# Dataset Spec for STAC

## Introduction

One topic of interest has been the search of datasets*, instead of within a dataset, i.e. in (sub-)catalogs, items and assets. STAC is focused on search within a dataset, but it includes some simple constructs to catalog datasets. This could be an independent spec that STAC uses, and others can also independently use, to describe datasets in a lightweight way. Ideally this aligns with other efforts like DCAT, CAT 4.0 and WFS 3.0 

\* There is no standard name to use for this concept we are describing here. Others called it: dataset series (ISO 19115), collection (CNES, NASA), dataset (JAXA), dataset series (ESA), product (JAXA).

## Core

| Element      | Type                                  | Name                            | Description                                                  |
| ------------ | ------------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| id           | string                                | Dataset ID (required)           | Identifier for the dataset that is unique across the provider. MUST follow the pattern ` ^[A-Za-z0-9_\-\.~\/]+$ `. |
| title        | string                                | Title                           | A short descriptive one-line title for the dataset.          |
| description  | string                                | Description (required)          | Detailed multi-line description to fully explain the entity. [CommonMark 0.28](http://commonmark.org/) syntax MAY be used for rich text representation. |
| keywords     | [string]                              | Keywords                        | List of keywords describing the dataset. TODO: Formatting of the strings (spaces, casing, ...) |
| version      | string                                | Dataset Version                 | Version of the dataset. [Semantic Versioning (SemVer)](https://semver.org/) SHOULD be followed. |
| license_name | string                                | Dataset License Name (required) | Dataset's license name based on [SPDX License Identifier](https://spdx.org/licenses/) or `proprietary` (see `license_url`). |
| license_url  | string                                | Dataset License URL             | Dataset's license URL. MUST be specified if `license_name`  does not contain a SPDX License Identifier. |
| provider     | Provider Object                       | Provider                        | The provider that makes this data available.                 |
| geometry     | [GeoJSON Object](http://geojson.org/) | Spatial extent (required)       | The spatial extent covered by the dataset as [GeoJSON](http://geojson.org/) object. |
| datetime     | string                                | Temporal extent (required)      | Temporal extent covered by the dataset. Date/time intervals MUST be formatted according to ISO 8601. Open date ranges are not supported by ISO 8601 and MUST be encoded as proposed by [Dublin Core Collection Description: Open Date Range Format](http://www.ukoln.ac.uk/metadata/dcmi/date-dccd-odrf/2005-08-13/). |
| periodicity  | string                                | Periodicity                     | ISO8601                                                      |
| links        | [Link Object]                         | Links (required)                | A list of references to other documents, see Link Object for further documentation. |

### Provider Object

| Element | Type   | Name                  | Description |
| ------- | ------ | --------------------- | ----------- |
| name    | string | Organization name     |             |
| url     | string | Organization homepage |             |
| ...     |        |                       |             |

### Link Object

TODO: Should be compatible with STAC.

| Element | Type   | Name                                | Description |
| ------- | ------ | ----------------------------------- | ----------- |
| href    | string | Hyperlink reference (required)      |             |
| rel     | string | Relation (required)                 |             |
| type    | string | MIME-type of the referenced entity. |             |
| title   | string | Human-readable title for the link.  |             |

## Scientific extension (sci)

| Element              | Type              | Name                      | Description                                                  |
| -------------------- | ----------------- | ------------------------- | ------------------------------------------------------------ |
| doi                  | string            | Dataset DOI               | [DOI](https://www.doi.org/) of the dataset.                  |
| citiation            | string            | Proposed Dataset Citation | The proposed citation for the dataset.                       |
| publication_doi      | string            | Publication DOI           | [DOI](https://www.doi.org/) of the publication referencing this dataset. |
| publication_citation | string            | Publication Citation      | Citation of the publication referencing this dataset.        |
| providers            | [Provider Object] | Providers                 | Other providers this dataset is derived from.                |

##  EO extension (eo)

We follow the STAC EO extension, but propose additional fields:

| Element      | Type     | Name               | Description           |
| ------------ | -------- | ------------------ | --------------------- |
| unit         | ?        |                    |                       |
| asset_schema | ?        |                    |                       |
| nodata       | [number] | Nodata values      | The no data value(s). |
| pyramid      | ?        | Pyramid parameters |                       |

#### Bands

We follow the STAC EO extension for bands, but propose additional fields:

| Element   | Type     | Name          | Description                                                  |
| --------- | -------- | ------------- | ------------------------------------------------------------ |
| nodata    | [number] | Nodata values | The no data value(s).                                        |
| data_type | string   | Data Type     | Data type for band values including its bit size. Values: uint8, uint16, uint32, uint64, int8, int16, int32, int64, float16, float32, float64 |
| offset    | number   | Offset        | offset to convert band values to the actual measurement scale |
| scale     | number   | Scale         | scale to convert band values to the actual measurement scale. |

## Dimensions extension (dim)

Data can have different dimensions, e.g. in meteorology. The properties of these dimensions can be defined with several of the properties from core, EO extension etc. (TODO)

## Example

```json
{
  id: ""
}
```

