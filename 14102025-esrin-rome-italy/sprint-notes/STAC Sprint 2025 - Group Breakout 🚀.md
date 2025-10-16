---
title: "STAC Sprint 2025 - Group Breakout \U0001F680"

---

# STAC Sprint 2025 - Group Formation 🚀
**ESA ESRIN, Frascati | October 14-16, 2025**

:::info
**📋 Instructions:**
1. **Add your name** to topics you're interested in
2. **Volunteer as Champion** if you want to facilitate a topic
3. We'll select **topics** based on interest and expertise balance
:::

---

## Topic 1: Zarr Store Best Practices - Room A
**Focus:** Foundational concept mapping - how Zarr stores are represented in STAC

### Interest Level
**Interested participants** (add your name + expertise area):
- Christoph Reimer
- Julia Signell
- Michelle Roby
- Marcin Niemyjski
- Vincent Dumoulin
- Alessandro Amici (multi-scale arrays, harmonisation with CF-Conventions)
- Fabian Wachsmann
- Kameswar Rao Modali
- Brian Terry
- Petr Sevcik

**Champion volunteers** (facilitator role):
- Julia Signell

**Key questions/priorities for this topic:**
- Layout a mapping of Zarr store concepts to STAC concepts (e.g., groups, arrays, variables to collections, items, assets, bands)
- Identify existing or missing asset roles for Zarr stores (e.g. consolidated metadata, zarr hierarchy, virtual Zarr?)
- Specify metadata fields for Zarr store properties (chunk sizes, compression, storage layout)
- Integration patterns with existing extensions (datacube, cf)
- Asset organization for multi-resolution and hierarchical Zarr stores
- Guidelines for storing STAC metadata within Zarr stores 
- Naming conventions for Zarr/Virtual Zarr assets
- Datetime range handling for multidimensional datasets

**Notes:** https://hackmd.io/ZogL7o93TQ2_PtOfv9bfLw

## Topic 2: Asset Discovery and Data Access Patterns - Room E
**Focus:** Standardized patterns for asset organization, navigation, and templating

### Interest Level
**Interested participants** (add your name + expertise area):
- Lukas Bindreiter
- Fabrice Brito (common band name -> Zarr?)
- Florian Ziemen (multi-resolution model output)
- Daniel Santillan (STAC + extensions + client visualization)
- Rhys Evans (nd-array extension)
- Catherine Bouzinac
- Mario Winkler
- Michele Claus (Data Access libraries)
- Francesco Bartoli (Data Access libraries)
- Emmanuel Mathot (Asset resolution)
- Jolyon Martin
- Vincent Sarago

**Champion volunteers** (facilitator role):
- Emmanuel Mathot

**Key questions/priorities for this topic:**
- Collection-level vs item-level asset organization for Zarr stores https://hackmd.io/56N_jfv_SPmJbd61UEnauQ#
- Guidelines for representing scene-based Zarr stores (EOPF products)
- Best practices for xarray extension deprecation in favor of nd-array generic patterns
- Asset metadata requirements for pyramids/multi-resolution data groups
- Variable-specific asset handling within multidimensional stores
- Link templates for direct access to Zarr subgroups and variables 
- Identify gaps in Zarr variable representation in datacube extension
- Propose solutions for identifying coordinate variables
- CF convention integration patterns (CF extension overlap)
- Collection-level datacube metadata for hierarchical stores
- Alignment with CF conventions for atmospheric and oceanic data
- Standard name and units handling
- Cell methods representation for temporal aggregations 

**Notes:** https://hackmd.io/_jRR2sHGRNenRIzq93589g

---

## Topic 3: EOPF Integration Specification - Room P
**Focus:** ESA-specific STAC patterns for Sentinel products in Zarr format

### Interest Level
**Interested participants** (add your name + expertise area):
- Christoph Reimer
- Michele Claus (Sentinel-1 specific fields/metadata)
- Jan Musiał 
- Catherine Bouzinac
- Petr Sevcik (Sentinel-1, Sentinel-2 effective data search and chunked usage on large scale)
- Mario Winkler

**Champion volunteers** (facilitator role):
- 
- 

**Key questions/priorities for this topic:**
- STAC item structure for Sentinel products in Zarr format
- EOContainer: Zarr store organisation and STAC representation
- Shall all Zarr groups be described (and exposed as assets) at STAC level?
- Metadata inheritance patterns from SAFE to Zarr to STAC
- Multi-resolution band organization and relationships
- Processing extension integration for EOPF workflows
- Collection organization for multi-temporal datasets
- **EOPF Extension Deprecation:** Replace EOPF-specific fields with existing STAC extensions (timestamps, product:acquisition_type, s1/s2 specific fields)
- Avoid duplication of STAC elements 

**Notes:** https://hackmd.io/@stac-sprint-2025/HJPRMVppeg

---


## Topic 5: STAC Browser and Visualization Support
**Focus:** Specification patterns for effective visualization and browsing

### Interest Level
**Interested participants** (add your name + expertise area):
- Kameswar Rao Modali (else Topic 2)
- 
- 

**Champion volunteers** (facilitator role):
- 
- 

**Key questions/priorities for this topic:**
- Asset metadata requirements for client-side visualization
- Thumbnail and preview generation patterns for Zarr data
- Queryable fields for multidimensional data discovery
- Performance optimization patterns for large dataset browsing
- Integration with existing STAC Browser capabilities
- Improve browsability of hierarchical Zarr structures
- Guidelines for identifying the collections, items and assets levels in a Zarr store 

---

## Topic 6: Performance and Access Optimization
**Focus:** Guidelines for optimizing STAC-Zarr integration performance

### Interest Level
**Interested participants** (add your name + expertise area):

- Marcin Niemyjski (CloudFerro) - One of the core developers of the new CDSE STAC, with expertise in the two most popular implementations: pgstac and SFEOS. One of the developers behind [CDSE STAC indexing tool](https://github.com/eu-cdse/eometadatatool).
- Fabian Wachsmann (German Climate Computing Center) - Implementing and maintaining [DKRZ Zarr catalog](https://discover.dkrz.de/external/stac2.cloud.dkrz.de/fastapi/?.language=en)

**Champion volunteers** (facilitator role):
- 
- 

**Key questions/priorities for this topic:**
- Chunk size and manifest optimization guidelines
- Consolidated metadata vs distributed metadata patterns
- Caching strategies for frequently accessed Zarr stores
- Asset streaming patterns for large multidimensional data
- Cloud storage optimization (S3, GCS, Azure) considerations
- **Sequential HTTP request reduction:** Optimize Zarr access to limit the number of HTTP requests
- **Remote rendering performance:** Strategies for large Zarr arrays at different zoom levels
- **Download vs streaming behavior:** Guidelines for when to stream vs download Zarr data
- Virtual Zarr support: Reference file cataloging patterns, Kerchunk and VirtualiZarr integration 

---

## Topic 7: STAC Contributions to Zarr Ecosystem
**Focus:** How STAC metadata and conventions can enhance Zarr stores

### Interest Level
**Interested participants** (add your name + expertise area):
- 
- 
- 

**Champion volunteers** (facilitator role):
- 
- 

**Key questions/priorities for this topic:**
- **Embedded STAC Metadata Patterns:** Storage location evaluation (.zattrs vs .zstac files vs Zarr arrays)
- Self-describing Zarr stores with STAC Collection/Item metadata
- EOPF implementation reference (stac_discovery field pattern)
- Scalability: JSON vs chunked tabular format for large collections
- **Zarr Extensions for STAC Use Cases:** Geospatial metadata extensions (CRS, spatial reference)
- Temporal dimension handling conventions
- Multi-resolution/pyramid encoding patterns
- **STAC Encoding in Zarr Attributes:** Asset roles and types for Zarr groups/arrays
- STAC extension metadata encoding (eo, sat, processing)
- Collection-level vs item-level metadata placement
- **Cross-Domain Patterns:** Domain-agnostic catalog patterns (beyond geospatial) 

---

## 📊 Selection Summary

:::warning
**Organizers will fill this section after the formation phase**
:::

### Selected Topics (4 total):
1. **Topic X:** [Topic Name] - Champion: [Name] - Group size: X people
2. **Topic X:** [Topic Name] - Champion: [Name] - Group size: X people
3. **Topic X:** [Topic Name] - Champion: [Name] - Group size: X people
4. **Topic X:** [Topic Name] - Champion: [Name] - Group size: X people

### Room Assignments:
- **Breakout Room 1:** [Topic Name]
- **Breakout Room 2:** [Topic Name]
- **Breakout Room 3:** [Topic Name]
- **Breakout Room 4:** [Topic Name]

---

## 💡 Alternative Topics

**Do you have a different topic idea?** Add it here with a brief description:

### Proposed Alternative Topics:
- **Topic Name:** [Description] - Proposed by: [Name]
  - Interested: 
  - 

---

## ℹ️ Reference Information

### Topic Details
Full specification topics document: https://github.com/radiantearth/community-sprints/blob/main/14102025-esrin-rome-italy/prep-work/specification-topics.md

### Champion Role
Champions are **facilitators**, not necessarily technical experts:
- ✅ Keep discussions on track and inclusive
- ✅ Ensure decisions are captured (GitHub issues/docs)
- ✅ Prepare 5-min daily wrap-up presentation
- ✅ Track action items and coordinate with other groups

### Success Metrics (per group)
- At least **2 GitHub issues** opened
- At least **1 PR** or detailed specification draft
- Clear **action plan** for post-sprint continuation
- Cross-pollination with other groups

---

## 📝 Notes & Comments

Use this section for general comments, questions, or suggestions:

- 
- 

---

**Last updated:** [Time] | **Document URL:** [Share this with all participants]