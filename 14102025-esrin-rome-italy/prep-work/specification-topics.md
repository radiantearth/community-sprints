# STAC Sprint Rome 2025 - Specification Topics

Based on participant interests and expertise, we have identified 6 focused specification topics for breakout groups. Each topic addresses critical STAC-Zarr integration challenges with clear deliverables.

## Proposed Topic 1: Zarr Store Best Practices Specification

**Objective:** Initiate a Zarr section in the [STAC best practises repo](https://github.com/radiantearth/stac-best-practices/) with recommendations on how Zarr stores are represented in STAC.

**Key Work Items:**

- layout a mapping of Zarr store concepts to STAC concepts (e.g., groups, arrays, variables to collections, items, assets)
- Identify existing or missing asset roles for Zarr stores (e.g. consolidated metadata, zarr hierarchy)
- Specify metadata fields for Zarr store properties (chunk sizes, compression, storage layout)
- Integration patterns with existing extensions (datacube, cf)
- Asset organization for multi-resolution and hierarchical Zarr stores
- Guidelines for storing STAC metadata within Zarr stores

**Potential Outputs:**

- Draft Zarr Best Practices outline
- Set of issues/PRs to be continued post-sprint
- Example STAC items and collections using the best practices

## Proposed Topic 2: STAC-Zarr Asset Discovery and Data Access Patterns

**Objective:** Establish standardized patterns for representing Zarr data as STAC assets with focus on navigation and discoverability.

**Key Work Items:**

- Collection-level vs item-level asset organization for Zarr stores
- Guidelines for representing scene-based Zarr stores (EOPF products)
- Best practices for xarray extension deprecation in favor of nd-array generic patterns
- Asset metadata requirements for pyramids/multi-resolution data groups
- Variable-specific asset handling within multidimensional stores
- Link templates for direct access to Zarr subgroups and variables

**Potential Outputs:**

- Best practices guide for STAC-Zarr asset organization
- Reference implementations for common use cases
- Asset pattern templates for different data types
- Enhancement proposals for existing STAC Extensions

> !Note: This topic is closely related to Topic 1 (Zarr Store Best Practices) and may have overlapping work items. Coordination between the two groups is encouraged to ensure consistency and avoid duplication of effort.

## Proposed Topic 3: EOPF Integration Specification

**Objective:** Define standardized STAC patterns for ESA EOPF Zarr products to ensure consistency across the ecosystem.

**Key Work Items:**

- STAC item structure for Sentinel products in Zarr format
- Metadata inheritance patterns from SAFE to Zarr to STAC
- Multi-resolution band organization and relationships
- Processing extension integration for EOPF workflows
- Collection organization for multi-temporal datasets

**Potential Outputs:**

- EOPF-STAC specification guidelines
- Reference STAC collections and items for Sentinel products
- Integration patterns with openEO and other processing frameworks

## Proposed Topic 4: Datacube Extension Enhancement for Zarr

**Objective:** Enhance the Datacube Extension to better support Zarr multidimensional data structures and CF conventions.

**Key Work Items:**

- Identify gaps in Zarr variable representation in datacube extension
- Propose solutions for identifying coordinate variables
- CF convention integration patterns (CF extension overlap)
- Datetime range handling for multidimensional datasets
- Collection-level datacube metadata for hierarchical stores

**Potential Outputs:**

- Updated Datacube Extension specification
- CF convention mapping guidelines
- Example implementations for climate and Earth observation data

## Proposed Topic 5: STAC Browser and Visualization Support

**Objective:** Define specification patterns that enable effective visualization and browsing of Zarr data through STAC interfaces.

**Key Work Items:**

- Asset metadata requirements for client-side visualization
- Thumbnail and preview generation patterns for Zarr data
- Queryable fields for multidimensional data discovery
- Performance optimization patterns for large dataset browsing
- Integration with existing STAC Browser capabilities

**Potential Outputs:**

- Visualization-friendly STAC patterns specification
- STAC Browser enhancement recommendations
- Performance guidelines for large Zarr catalog browsing

## Proposed Topic 6: Performance and Access Optimization

**Objective:** Develop specification guidelines for optimizing STAC-Zarr integration performance and remote access patterns.

**Key Work Items:**

- Chunk size and manifest optimization guidelines
- Consolidated metadata vs distributed metadata patterns
- Caching strategies for frequently accessed Zarr stores
- Asset streaming patterns for large multidimensional data
- Cloud storage optimization (S3, GCS, Azure) considerations

**Potential Outputs:**

- Performance optimization guidelines
- Reference architectures for different deployment scenarios
- Benchmarking framework for STAC-Zarr implementations

---

## Selection Process

From these 6 topics, **4 will be selected** based on:

- Participant expertise alignment
- Community priority and impact
- Technical feasibility within sprint timeframe
- Complementary nature of selected topics

Each selected topic will form a breakout group of 4-6 participants with diverse expertise to ensure comprehensive coverage and practical outcomes.
