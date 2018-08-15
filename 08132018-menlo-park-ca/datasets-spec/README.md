# Dataset Spec for STAC

## Core

| Element     | Type                                  | Name                       | Description                                                  |
| ----------- | ------------------------------------- | -------------------------- | ------------------------------------------------------------ |
| id          | string                                | Dataset ID (required)      | Identifier for the dataset that is unique across the provider. MIUST follow the pattern ` ^[A-Za-z0-9_\-\.~\/]+$ `. |
| title       | string                                | Title                      | A short descriptive one-line title for the dataset.          |
| description | string                                | Description (required)     | Detailed multi-line description to fully explain the entity. [CommonMark 0.28](http://commonmark.org/) syntax MAY be used for rich text representation. |
| keywords    | [string]                              | Keywords                   | List of keywords describing the dataset. TODO: Formatting of the strings (spaces, casing, ...) |
| version     | string                                | Dataset Version            | Version of the dataset. [Semantic Versioning (SemVer)](https://semver.org/) SHOULD be followed. |
| license     | string                                | Dataset License (required) | Dataset's license name based on [SPDX License Identifier](https://spdx.org/licenses/) or following guidelines for non-SPDX licenses. |
| provider    | Provider Object                       | Provider                   | The provider that makes this data available.                 |
| geometry    | [GeoJSON Object](http://geojson.org/) | Spatial extent (required)  | The spatial extent covered by the dataset as [GeoJSON](http://geojson.org/) object. |
| datetime    | string                                | Temporal extent (required) | Temporal extent covered by the dataset. Date/time intervals MUST be formatted according to ISO 8601. Open date ranges are not supported by ISO 8601 and MUST be encoded as proposed by [Dublin Core Collection Description: Open Date Range Format](http://www.ukoln.ac.uk/metadata/dcmi/date-dccd-odrf/2005-08-13/). |
| periodicity | string                                | Periodicity                | ISO8601                                                      |
| links       | [Link Object]                         | Links (required)           | A list of references to other documents, see Link Object for further documentation. |

### Provider Object

| Element | Type   | Name                  | Description |
| ------- | ------ | --------------------- | ----------- |
| name    | string | Organization name     |             |
| url     | string | Organization homepage |             |

### Link Object

| Element | Type   | Name                           | Description |
| ------- | ------ | ------------------------------ | ----------- |
| href    | string | Hyperlink reference (required) |             |
| rel     | string | Relation (required)            |             |
| type    | string |                                |             |
| title   | string |                                |             |

## Scientific extension (sci)

| Element              | Type   | Name                      | Description                                                  |
| -------------------- | ------ | ------------------------- | ------------------------------------------------------------ |
| doi                  | string | Dataset DOI               | [DOI](https://www.doi.org/) of the dataset.                  |
| citiation            | string | Proposed Dataset Citation | The proposed citation for the dataset.                       |
| publication_doi      | string | Publication DOI           | [DOI](https://www.doi.org/) of the publication referencing this dataset. |
| publication_citation | string | Publication Citation      | Citation of the publication referencing this dataset.        |


