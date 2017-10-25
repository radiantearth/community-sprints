import json
import mercantile
from shapely.geometry import shape

output_file = 'digital_globe-search-results-minimal.geojson'
dg_file = 'dg_boulder_available.json'

def tms_template_url(rec):
    url = u"https://idaho.geobigdata.io/v1/tile/idaho-images/{idaho_id}/".format(idaho_id=rec["properties"]["attributes"]["idahoImageId"]) + \
    u"{z}/{x}/{y}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2RpZ2l0YWxnbG9iZS1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8Z2JkeHwxMDQ2IiwiYXVkIjoidmhhTkVKeW1MNG0xVUNvNFRxWG11S3RrbjlKQ1lEa1QiLCJleHAiOjE1MDg5NTg5NTYsImlhdCI6MTUwODM1NDE1NiwiYXpwIjoidmhhTkVKeW1MNG0xVUNvNFRxWG11S3RrbjlKQ1lEa1QifQ.s4tqr0rGqF7UXBlBty0oHK-W24X7EVv_wKi3xyTkRRY"
    return url

def thumbnail_url(rec):
    bounds = shape(rec['geometry']).bounds
    tile = mercantile.bounding_tile(*bounds)
    return tms_template_url(rec).format(z=tile.z, x=tile.x, y=tile.y)

dg = {
  'geometry': 'geometry',
  'id': 'idahoImageId',
  'start_date': 'acquisitionDate',
  'end_date': 'acquisitionDate',
  'provider': 'vendorName'
}

features = []
with open(dg_file) as f:
  dg_data = json.loads(f.read())

for feature in dg_data:
  attr = feature['properties']['attributes']
  features.append(
  {
    "type": "Feature",
    "bbox": shape(feature['geometry']).bounds,
    "geometry": feature[dg['geometry']],
    "properties": {
      "id" : attr[dg['id']],
      "start_date": attr[dg['start_date']],
      "end_date": attr[dg['end_date']],
      "provider": attr[dg['provider']],
      "license": '',
      "osgeo:tms": tms_template_url(feature),
      "links": {
        "metadata": '',
          "thumbnail": thumbnail_url(feature)
      },
      "capabilities": ["osgeo:tms"]
    }
  }
)

with open(output_file, 'w') as f:
  f.write(json.dumps(
    {
      'type': 'FeatureCollection', 
      'features': features
    }
  ))
