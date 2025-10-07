## About

One major use case to be considered during this sprint is the [EO Processing Framework (EOPF)](https://eopf.copernicus.eu/), which evolves the data format of the Copernicus Sentinel missions towards a format based on Zarr. The [EOPF Sample Service]() provides a rolling archive of products converted from SAFE to EOPF Zarr and makes them discoverable in a [STAC catalog](). Together with the [EOPF Toolkit]() and the [EOPF Explorer]() projects, the creation, distribution, tooling support and user uptake of the new format is fostered.

This folder contains some preparative material to be considered as background information for the work on the specification topics during the sprint.

- [EOPF STAC item assets](eopf-assets-info.md) - The current approach to STAC Zarr assets in the EOPF Sample Service project.
- [EOPF Zarr store structure](eopf-zarr-structure-info.md) - Details on the Zarr store layout of the different Sentinel product types.
