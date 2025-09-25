# Implementation Topics - Supporting Specification Development

## Overview

This STAC + Zarr community sprint at ESA/ESRIN will **primarily focus on [specification](specification-topics.md) development**, with implementation work arising organically from specification discussions. The main goal is to develop robust specifications, best practices, and guidelines for STAC-Zarr integration.

Given the 3-day sprint timeframe, implementation activities will serve to:

- **Propose immediate solutions** to specification decisions trough PRs in the corresponding repositories
- **Validate specification decisions** through proof-of-concept implementations
- **Test proposed patterns** with real-world data and use cases
- **Identify gaps** in current tooling that specifications need to address
- **Create reference examples** that demonstrate specification compliance

## Approach to Implementation Work

Implementation work during the sprint should be **secondary to specification development** and will emerge from:

1. **Specification validation needs** - Building small prototypes to test proposed patterns
2. **Participant interest** - Some participants may choose to implement concepts discussed in spec groups
3. **Reference example creation** - Developing examples that demonstrate specification compliance
4. **Gap identification** - Discovering implementation challenges that inform specification decisions

BUT any participant may propose implementation topics or areas of focus that align with the overall sprint goals and organize a group around them.

## Participant Inputs

Based on participant input, the following real-world implementation examples provide valuable context for sprint discussions:

### EOPF Sample Service Catalog

Reference implementation: [EOPF STAC Catalog](https://stac.core.eopf.eodc.eu/) | [STAC Browser](https://stac.browser.user.eopf.eodc.eu/)

**EOPF Sentinel-2 L2A Implementation Patterns:**

**Multi-Resolution Asset Organization:**

- Individual band assets at native resolutions (10m, 20m, 60m)
- Grouped assets by resolution (SR_10m, SR_20m, SR_60m)
- Full product asset pointing to complete Zarr hierarchy

**Asset Structure Patterns:**

- Media type: `application/vnd+zarr`
- Asset roles: `["data", "reflectance", "dataset"]` for grouped bands
- Asset roles: `["data", "reflectance"]` for individual bands
- Asset roles: `["data", "metadata"]` for full product

**Zarr Integration Specifications:**

- Engine-specific parameters: `"engine": "eopf-zarr"`
- Operation modes: `"op_mode": "native"` vs `"op_mode": "analysis"`
- Spatial resolution parameters: `"spatial_res": 10/20/60`
- Band selection: `"bands": ["B01"]` for individual band access
- Chunking configuration: `"chunks": {}`

**Hierarchical Data Access:**

- Full product access via `xarray:open_datatree_kwargs`
- Group-level access via `xarray:open_dataset_kwargs`
- Individual band access with band selection parameters
- Alternate access patterns for different use cases

**Metadata Patterns:**

- Consolidated metadata asset: `.zmetadata` with `application/json` type
- Projection metadata: EPSG codes, bounding boxes, transforms
- Raster metadata: scale, offset, nodata values
- Band metadata: wavelengths, common names, descriptions

**EOPF-Specific Extensions:**

- EOPF STAC extension: `cs-si.github.io/eopf-stac-extension/v1.2.0/schema.json`
- Datatake ID: `eopf:datatake_id`
- Instrument mode: `eopf:instrument_mode`

**Integration Points for Sprint Discussion:**

- Standardization of multi-resolution asset patterns
- Engine-specific parameter conventions
- Hierarchical data access patterns (DataTree vs Dataset)
- Alternate access pattern specifications
- EOPF extension integration with core STAC
- Performance optimization for different operation modes

### EOAP Zarr Cloud-Native Workflows

Based on participant input, the following real-world implementation examples provide valuable context for sprint discussions:

#### Earth Observation Application Packages (EOAP)

Reference implementation: [EOAP Zarr Cloud-Native Format](https://eoap.github.io/zarr-cloud-native-format/exploitation/)

**Key Implementation Patterns Demonstrated:**

- Collection assets with `application/vnd+zarr` media type
- Datacube extension for multidimensional metadata
- xarray:open_kwargs for Zarr-specific parameters
- Consolidated metadata usage for performance
- Spatial reference system encoding in Zarr
- Time dimension handling in STAC collections

**Technical Specifications Observed:**

- Asset roles: `["data", "zarr"]`
- Media type: `application/vnd+zarr`
- Datacube dimensions: spatial (x, y) and temporal
- Chunking strategy: `[512, 512, 1]` for time-series data
- Coordinate reference system: EPSG codes in datacube extension

**Integration Points for Sprint Discussion:**

- Standardization of Zarr asset roles and media types
- Best practices for consolidated metadata handling
- Datacube extension alignment with Zarr conventions
- Performance optimization for cloud-native access
- Workflow patterns for producer/consumer applications
