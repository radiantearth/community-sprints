# Flat File Catalog

## Purpose

Flat file catalogs, or Asset Networks, define a network of linked
assets for the purpose of automated crawling. It is defined
by a network of linked metadata in a standardized format.

## Description

An Asset Network defines a tree graph structure, with a single global entry point from which
the entire network can be crawled. The nodes in this network are defined by Node metadata,
which can point downstream to other Nodes as well as directly describe Assets.

### Nodes

A Node in the network contains top level metadata to describe the node, a list of assets,
and a list of links to other nodes. The node metadata may only have assets, or only have links,
or both. There are both required and optional fields for metadata.

One important component of the nodes is that they may embed asset or link data to any degree.
There may be no embedded data, a partial set of data for an asset or linked node, or fully
embed all information of the network. If the full asset or linked node is embedded into the
upstream node, the upstream node may or may not contain the URI to the downstream node or asset.

Nodes can contain optional data that has semantic meaning according to the context of the node.
Examples:
- Specification of semantic meaning of URI pattern (e.g. z/x/y) that the crawler can recognize and take advantage of.
- SEO tags
- Generic "user data"

### Assets

Assets contain the metadata that is specific to the format of the asset. The asset must state it's format.
The Asset network does not have specific requirements for participation in the network; the spec of
the formats is a downstream concern of the definition of the Asset Network.

_The formats (e.g. "scenes", "cogs") can be written against the ideal information to be determined by the core metadata team_

### What this is not

- A network that focuses on being up to date - no guarantees around when new data will be made available.

## Resources

- Workstream description: https://github.com/radiantearth/boulder-sprint/blob/master/workstreams/flat-file-catalog.md
- Notes: https://board.net/p/flat-catalog


## TODO:

- figure out time - we have to argue with other groups. 8601-and-done
