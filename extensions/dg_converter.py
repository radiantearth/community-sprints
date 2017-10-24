import json
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
      "links": {
        "metadata": '',
        "thumbnail": ''
      }
    }
  }
)

with open(output_file, 'w') as f:
  f.write(json.dumps({'type' : 'FeatureCollection', 'features': features}))
