import json
import mercantile
from shapely.geometry import shape

output_file = 'digital_globe-search-results-minimal.geojson'
dg_file = 'dg_boulder_available.json'

def bbox_from_poly(poly):
    mx, my = -180, -90
    nx, ny = 180, 90
    for c in poly['coordinates'][0][0]:
        mx = max(mx, c[0])
        my = max(my, c[1])
        nx = min(nx, c[0])
        ny = min(ny, c[1])
    return [nx, ny, mx, my]

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
  'attributes': {
    'id': 'idahoImageId',
    'start_date': 'acquisitionDate',
    'end_date': 'acquisitionDate',
    'provider': 'vendorName'
  }
}

features = []
with open(dg_file) as f:
  dg_data = json.loads(f.read())

for feature in dg_data:
  features.append(
  {
    "type": "Feature",
    "bbox": bbox_from_poly(feature[dg['geometry']]),
    "geometry": feature[dg['geometry']],
    "properties": {
      "id" : feature['properties']['attributes'][dg['attributes']['id']],
      "start_date": feature['properties']['attributes'][dg['attributes']['start_date']],
      "end_date": feature['properties']['attributes'][dg['attributes']['end_date']],
      "provider": feature['properties']['attributes'][dg['attributes']['provider']],
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
  f.write(json.dumps({'type' : 'FeatureCollection', 'features': features}))
