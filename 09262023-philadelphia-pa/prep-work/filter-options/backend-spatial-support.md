## Overview

This document lists the spatial operations various backends support, to help determine what geometry operations should be core
and which extensions. (apologies for formatting - just pasting stuff in while I'm working on another doc)

### Elastic
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-geo-shape-query.html

The following is a complete list of spatial relation operators available:

INTERSECTS - (default) Return all documents whose geo_shape field intersects the query geometry.
DISJOINT - Return all documents whose geo_shape field has nothing in common with the query geometry.
WITHIN - Return all documents whose geo_shape field is within the query geometry.
CONTAINS - Return all documents whose geo_shape field contains the query geometry. Note: this is only supported using the recursive Prefix Tree Strategy [6.6]

### BigQuery
https://cloud.google.com/bigquery/docs/gis-data#using_joins_with_spatial_data

BigQuery implements optimized spatial JOINs for INNER JOIN and CROSS JOIN operators with the following standard SQL predicate functions:

ST_DWithin
ST_Intersects
ST_Contains
ST_Within
ST_Covers
ST_CoveredBy
ST_Equals
ST_Touches

### MongoDB
https://docs.mongodb.com/manual/reference/operator/query-geospatial/

Operators
Query Selectors
Name	Description
$geoIntersects	Selects geometries that intersect with a GeoJSON geometry. The 2dsphere index supports $geoIntersects.
$geoWithin	Selects geometries within a bounding GeoJSON geometry. The 2dsphere and 2d indexes support $geoWithin.
$near	Returns geospatial objects in proximity to a point. Requires a geospatial index. The 2dsphere and 2d indexes support $near.
$nearSphere	Returns geospatial objects in proximity to a point on a sphere. Requires a geospatial index. The 2dsphere and 2d indexes support $nearSphere.

### Solr
https://lucene.apache.org/solr/guide/6_6/spatial-search.html

