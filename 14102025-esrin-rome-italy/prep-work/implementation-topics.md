# Overview

The STAC ecosystem's software tooling provides implementation of the specification, enabling its use in products and services.
Implementations and tools also uncover issues with the specification, evolve extensions, and inform improvements to the spec.

This STAC + Zarr community sprint at ESA/ESRIN focuses on addressing key challenges in the intersection of STAC and Zarr technologies, particularly in the context of ESA's Earth Observation Processing Framework (EOPF) and large-scale geospatial data distribution.

The majority, but not all, of STAC software is housed in the [stac-utils Github organization](https://github.com/stac-utils).
This document will collect topics for the STAC sprint that relate to those softwares and their integration with Zarr.
These topics might include:

- STAC + Zarr integration patterns
- GeoZarr implementation challenges
- Virtual Zarr and STAC interoperability
- Collection-level assets for Zarr stores
- Link Templates Extension applications
- Bug fixes and new features
- Documentation improvements
- FAQs and explainers
- New repositories

Please add your topic suggestions to the sections below, using Github pull requests.
If you see a software repository of interest, please add bullet points under that software.
If you don't see the software repository you're interested, please add it to the appropriate section (or start a new one).

During the sprint itself, we will coordinate work using appropriate project management tools.

## STAC + Zarr Core Integration

Core implementations and patterns for integrating STAC with Zarr data stores, addressing the fundamental question of how to best catalog and discover Zarr data using STAC.

### Data Organization Patterns

- **One Big Zarr (Aligned Data)**
  - Collection-level assets pointing to consolidated Zarr stores
  - Metadata extraction and duplication strategies
  - Search and discovery patterns for large multidimensional datasets
  - Examples: ERA5, CMIP6 datasets

- **Many Smaller Zarrs (Unaligned Data)**
  - Item-level assets for scene-based Zarr stores
  - Spatial and temporal extent handling
  - Coordinate reference system variations
  - Examples: Sentinel-2 L2A scenes in Zarr format

### Metadata Challenges

- **Collection Assets Implementation**
  - Zarr store references at collection level
  - Consolidated metadata (.zmetadata) handling
  - Asset roles and types for Zarr stores

- **Zarr Group Metadata**
  - Missing group-level metadata files
  - Relationship between STAC assets and Zarr groups
  - Consolidated metadata parsing and representation

## GeoZarr Integration

Work related to the GeoZarr specification and its integration with STAC catalogs.

- **GeoZarr Specification Alignment**
  - Coordinate reference system encoding
  - Spatial metadata representation
  - Integration with STAC spatial properties

- **Implementation Challenges**
  - Multi-resolution data handling
  - Chunking strategies for geospatial data
  - Performance optimization for cloud access

## Virtual Zarr and STAC

Integration of Virtual Zarr technologies (VirtualiZarr, Icechunk) with STAC catalogs.

- **VirtualiZarr Integration**
  - Reference file generation from legacy formats
  - STAC catalog generation from virtual stores
  - Cloud-optimized workflows without data duplication

- **Kerchunk and STAC**
  - Reference file cataloging patterns
  - Asset organization for kerchunk references
  - Search and discovery optimization

## EOPF-Specific Use Cases

Implementation topics specific to ESA's Earth Observation Processing Framework.

- **EOPF Sample Service Integration**
  - STAC catalog structure for EOPF products
  - Zarr asset organization and metadata
  - Multi-resolution band handling

- **Sentinel Data in Zarr**
  - Conversion patterns from SAFE to Zarr
  - STAC item structure for Sentinel products
  - Band organization and asset relationships

## Core Implementations

Core implementations provide the base data structures and functionality for STAC + Zarr integration.

- **[pystac](https://github.com/stac-utils/pystac)**
  - Zarr asset handling improvements
  - Collection assets support for Zarr stores
  - Extension support for Zarr-specific metadata

- **[xarray integration](https://github.com/stac-utils/xpystac)**
  - STAC to xarray.Dataset conversion
  - Zarr store opening from STAC items
  - DataTree support for hierarchical Zarr stores

## Extensions and Specifications

Work on STAC extensions relevant to Zarr integration.

- **[Datacube Extension](https://github.com/stac-extensions/datacube)**
  - Zarr variable representation
  - Dimension and coordinate handling
  - CF convention integration

- **[CF Extension](https://github.com/stac-extensions/cf)**
  - Climate and Forecast metadata alignment
  - Standard name and units handling
  - Cell methods representation

- **[Link Templates Extension](https://github.com/stac-extensions/link-templates)**
  - Zarr subgroup access patterns
  - Dynamic link generation for nested structures
  - Qubed integration patterns

## Client Software

Software for accessing and working with STAC + Zarr data.

- **[stackstac](https://github.com/gjoseph92/stackstac)**
  - Zarr backend support
  - Multi-dimensional array construction from STAC

- **[odc-stac](https://github.com/opendatacube/odc-stac)**
  - Zarr data loading optimization
  - Chunking strategy alignment

- **[intake-stac](https://github.com/intake/intake-stac)**
  - Zarr driver integration
  - Catalog browsing for Zarr stores

## Server Software

STAC API implementations with Zarr-specific optimizations.

- **[stac-fastapi](https://github.com/stac-utils/stac-fastapi)**
  - Collection search for Zarr catalogs
  - Large collection handling optimization
  - Asset streaming for Zarr metadata

- **[pgstac](https://github.com/stac-utils/pgstac)**
  - Zarr metadata indexing strategies
  - Collection-level asset support
  - Search optimization for multidimensional data

## Testing and Validation

- **[stac-validator](https://github.com/stac-utils/stac-validator)**
  - Zarr asset validation rules
  - Collection assets validation
  - Extension-specific validation

- **Zarr Integration Testing**
  - End-to-end workflow testing
  - Performance benchmarking
  - Interoperability testing across tools

## Documentation and Examples

- **Best Practices Documentation**
  - STAC + Zarr integration patterns
  - Performance optimization guides
  - Use case examples and tutorials

- **Reference Implementations**
  - Example catalogs for different Zarr patterns
  - Code samples for common workflows
  - Integration examples with popular tools

## Research and Development

Experimental work and proof-of-concepts for advanced STAC + Zarr integration.

- **Federated Search**
  - Cross-catalog Zarr discovery
  - Distributed metadata aggregation
  - Performance optimization strategies

- **Advanced Chunking Strategies**
  - Optimal chunk sizes for different access patterns
  - Dynamic rechunking based on usage
  - Cloud storage optimization

- **Metadata Optimization**
  - Consolidated metadata strategies
  - Lazy loading patterns
  - Caching and performance improvements
