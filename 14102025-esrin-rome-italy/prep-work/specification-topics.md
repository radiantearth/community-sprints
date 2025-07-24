# Overview

Specification specific discussions to be had and work to be done, with a focus on STAC + Zarr integration challenges and improvements needed to better support multidimensional geospatial data.

## STAC Specification

**GitHub Page:** [https://github.com/radiantearth/stac-spec](https://github.com/radiantearth/stac-spec)

### Collection Assets for Zarr Stores

* **Collection-level Assets Implementation**
  * Finalize support for assets at the collection level to reference large Zarr stores
  * Define asset roles and types specific to Zarr stores (e.g., "zarr-store", "zarr-metadata")
  * Establish patterns for consolidated metadata references

### Datetime Handling for Multidimensional Data

* **Datetime Range vs Single Datetime**
  * Address challenges with single datetime requirement for multidimensional datasets (datacube extension)
  * Extension patterns for datetime ranges in datacube scenarios
  * Balance between core spec simplicity and extension flexibility

### Zarr-Specific Metadata Patterns

* **Metadata Duplication vs Reference**
  * Guidelines for when to duplicate Zarr metadata in STAC vs when to reference
  * Strategies for keeping STAC metadata synchronized with Zarr stores
  * Performance implications of different approaches

### Search and Discovery Optimization

* **Nested Structure Navigation**
  * Improve browsability of hierarchical Zarr structures. Guidelines for identifying the collections, items and assets levels in a Zarr store
  * Link templates for direct access to Zarr subgroups
  * Collection search patterns for large multidimensional datasets

## STAC API

**GitHub Page:** [https://github.com/radiantearth/stac-api-spec](https://github.com/radiantearth/stac-api-spec)

__The sprint will focus on the core spec and extensions that are relevant to Zarr integration but if a group forms to work on the API spec, it will be welcome to do so.__

### Collection Search Enhancement

* **Collection-level Search Optimization**
  * Enhance collection search for Zarr catalog discovery
  * Federated search across multiple STAC catalogs
  * Performance optimization for large collection catalogs

### Query Capabilities for Multidimensional Data

* **Advanced Queryables**
  * Custom queryables for nested Zarr metadata structures
  * Variable-based search within datacube collections
  * Temporal and spatial subsetting query patterns

### Asset Streaming and Access

* **Large Asset Handling**
  * Streaming patterns for large Zarr metadata files
  * Partial asset access for consolidated metadata
  * Caching strategies for frequently accessed Zarr stores

## STAC Extensions

**GitHub Page:** [github.com/stac-extensions](https://github.com/stac-extensions)

### Datacube Extension Enhancements

* **Zarr Integration Improvements**
  * Better support for Zarr variable representation
  * Dimension and coordinate handling alignment with Zarr spec
  * CF convention integration patterns
  * Discussion: [Datacube Extension Issues](https://github.com/stac-extensions/datacube)

### CF Extension Development

* **Climate and Forecast Metadata**
  * Alignment with CF conventions for atmospheric and oceanic data
  * Standard name and units handling
  * Cell methods representation for temporal aggregations
  * Discussion: [CF Extension PR #8](https://github.com/stac-extensions/cf/pull/8)

### Link Templates Extension

* **Dynamic Link Generation**
  * Zarr subgroup access patterns
  * Template-based navigation for nested structures
  * Qubed integration and formalization
  * Support for hierarchical data browsing

### Zarr Extension (Proposed)

* **Dedicated Zarr Extension**
  * Zarr-specific metadata fields and patterns
  * Asset roles and types for Zarr stores
  * Integration with existing extensions (datacube, cf)
  * Discussion: [Zarr Extension Discussion #1222](https://github.com/radiantearth/stac-spec/discussions/1222)

### Virtual Assets Extension

* **Virtual Zarr Support**
  * Reference file cataloging patterns
  * Kerchunk and VirtualiZarr integration
  * Asset organization for virtual stores
  * Cloud-optimized access without data duplication

## Cross-Specification Alignment

### GeoZarr Specification Integration

* **Coordinate Reference System Handling**
  * Alignment between STAC spatial properties and GeoZarr CRS encoding
  * Multi-resolution data representation
  * Chunking strategy recommendations

### OGC Standards Alignment

* **OGC API Compatibility**
  * Coverage API integration for Zarr data access
  * Processes API for Zarr data processing workflows
  * Records API alignment for metadata discovery

### CF Conventions Integration

* **Climate Data Standards**
  * CF convention compliance in STAC metadata
  * Attribute mapping between CF and STAC
  * Temporal dimension handling for climate datasets

## EOPF-Specific Specification Needs

### ESA Data Model Integration

* **EOPF Product Structure**
  * STAC patterns for ESA processing levels
  * Multi-resolution band organization
  * Metadata inheritance from SAFE to Zarr to STAC

### Sentinel Data Representation

* **Standardized Patterns**
  * Consistent STAC item structure for Sentinel products in Zarr
  * Multi-temporal collection organization
  * Band asset organization and relationships
  * Coordinate system handling across different Sentinel missions
