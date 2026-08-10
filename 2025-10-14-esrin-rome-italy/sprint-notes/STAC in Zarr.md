---
title: STAC in Zarr

---

# STAC in Zarr

The idea is to create a new Zarr convention similar to the [experimental geo convention](https://github.com/zarr-experimental/geo-proj). This convention would specify how to include STAC metadata in a group node of a Zarr store. The discussion is around where / what format to put the data for object.

## Name

stac

### Example

```json
{
    "f17cb550-5864-4468-aeb7-f3180cfb622f": {
        "version": "0.1.0",
        "schema": "https://raw.githubusercontent.com/zarr-experimental/stac/refs/tags/v0.1.0/schema.json",
        "name": "stac",
        "description": "Convention for including STAC within Zarr metadata",
        "spec": "https://github.com/zarr-experimental/stac/blob/v0.1.0/README.md",
        "configuration": {
            "metadata": {...quasi-stac object...},
            "link": "https://canonical-stac-object-link",
        }
    }
}
```

**REQUIRED** either `"metadata"` or `"link"`



## Options

For all these options: nested under a special field within the zarr.json there is one of the following:

1. **quasi-full stac object**
2.  missing fields that are not already defined in other Zarr conventions
3. **link out to where the canonical STAC object can be found**
4. don't do it

### Option 1: Quasi-full embeded stac object
| Perspective | Pros | Cons |
| -- | ---- | ---- |
| Producer | Proscribe how STAC items should be presented | Both Zarr and STAC/extension versions need to be tracked |
| Provider/Curator | Not necessary to generate stac items | Need to retool stac item manually from producers versions, conventions |
| Consumer | Zarr includes recognizable (browser renderable) stac item in metadata| duplicated metadata |

### Option 2: Missing fields that are not already defined in other Zarr conventions 
| Perspective | Pros | Cons |
| -- | ---- | ---- |
| Producer | Dont need to track updates as closely | producer needs to do deduplication  |
| Provider/Curator | more customizable for item generation | needs more tooling and reference |
| Consumer | less metadata | consumer needs to understand mapping |

### Option 3: External Link to STAC item
| Perspective | Pros | Cons |
| -- | ---- | ---- |
| Producer | Dont need to track updates as closely | producer needs to do deduplication  |
| Provider/Curator | more customizable for item generation | needs more tooling and reference |
| Consumer | less metadata | consumer needs to understand mapping |

What is the point of putting STAC in Zarr?
 - EOPF: the point is to have a self-describing dataset that contains all the metadata you need. In SAFE they used to have to map the fields from SAFE to STAC, but with this way they can just grab the STAC item.
 - Michele: Makes sense to have STAC inside
 - The goal is to minimize the effort that people need to do to create a STAC item. So even if the embedded STAC isn't exactly the STAC that you would want. Because there wouldn't be references to the asset itself for instance.
 - It's very rare to update the metadata without updating the data. So it isn't a big problem to keep the embedded stac object uptodate.
 
What if there were just a link to the STAC metadata instead?
- maybe this could be part of the specification that you should be able to reference a STAC elsewhere.

Where should you put overlapping fields?
 - Do you put cf fields within the embedded stac object?
 - Do you put proj fields within the enbedded stac object?
 - How does this relate to the geo Zarr convention?
 - Idea: If a particular field is already covered within another zarr convention then it is recommended to not include.

Should there be reference from within the embedded stac object to where to the other information can be found. Or does the tooling just have the mapping?

The `stac_extensions` should always be included in the embedded stac object. Then when you process the embedded stac object to create your STAC object you can do a mapping to a new version if you want.

What should the top-level field be?

How does it affect performance:
- There is the idea of perhaps storing the metadata as an array of bytes instead of putting it in the json.

### EOPF example - encoded metadata as arrays

![image](https://hackmd.io/_uploads/S1ohNX0Tle.png)


## Serverless STAC
The idea of serving a STAC directly from Zarr. There is an idea that this would be cool because there is a single source of truth, but it might not be very performant.

### Example
- Consuming a Zarr directly as if it were a STAC json by pointing directly to the `.zgroup` file. But the STAC metadata are all at the top level of the `.zgroup` file. There would be need to be an understanding within stac browser of how to find the nested field.