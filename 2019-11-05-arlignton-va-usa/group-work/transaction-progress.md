# Notes from Discussions

## Bulk Transactions
- Scott from L3/Harris proposed a CRUD interface that is non transactional
- How does this align with OGC WFS?
- Bulk transactions are not a problem unique to STAC, should probably not lock ourselves into a single solution
- Why is there a need for bulk transactions? 
- - Convenience
- - Performance 
- What are the semantics of a transaction? 
- Commit/Rollback? Is this an implementation detail or something that belongs in the spec?
- Is there a need to support anything besides bulk insert and delete?

## Transactions
- What are the semantics of a transaction? Do we really mean CRUD? (yes!) 

## Versioning
- Should STAC maintain older versions of items? Do we need more than timeline transaction-log type versioning (aka branches) — No
- Are timestamps enough?
- Do e-tags provide enough granularity?
- If we don’t advertise versions then how do we refer to them?
- Scott was using e-tags for providing bulk safe concurrent updates
- E-tags only let you know the current version

# Consensus 
## Transaction Endpoints (based on Staccato)
- `POST /stac/{collection_id}/items` - creates a new item
- `PUT /stac/{collection_id}/items/{item_id}` - creates updates a new item
- - Optional If-Match header must match E-tag
- `PATCH /stac/{collection_id}/items/{item_id}` - updates an item item
- - Optional If-Match header must match E-tag
- `DELETE /stac/{collection_id}/items/{item_id}` - deletes an item
- - Optional If-Match header must match E-tag

## Bulk Transaction Endpoints
- `POST /stac/{collection_id}/items` - creates n items by posting a feature collection (?) or array of features or feature stream
- `DELETE /stac/{collection_id}/items` - truncates an item collection
