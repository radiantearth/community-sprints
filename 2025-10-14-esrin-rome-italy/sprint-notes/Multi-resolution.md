---
title: Multi-resolution

---

# Multiscale discussion

Discussion on 15/10 morning

### Multi - level

Discussion on what are the impact of having multi-level in STAC or more on the Zarr side:
- Today no standard for Zarr and multi-level. Shall this be tackled inside STAC?
- Seems to be a common thoughts that this shall be done at Zarr convetion
- Question arised what are the needs at STAC level:
    - Groups of Groups seems to be a need
    - But groups of XXX is not something that is part of Zarr standard. You just have Group / Array
    - So maybe we need a Zarr convention that specifies the data model more explicitly than just group and array. This could be specified in the zarr.json or it could be a mimetype. Either could then be elevated at the STAC level as well so that we know how to open the asset.

What we need from Multi-level:

- We need to know how the data was sampled
    - We might need the crs per-overview
    
**We are clear on:**
 - It never makes sense to point from a STAC asset to a zarr array.
 - If you want to point to an array you a link template
 - Zarr group can be referenced by an asset / item / collection (?)

[] Create a ticket on writing the discussion in Best practice

Proposal based on EOPF:
- Expose the main bands  at their native resolution, and not expose all the multi-level resolution ()