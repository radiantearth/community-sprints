import json
import sys


def convert_records(fname):
    with open(fname) as fp:
        records = json.loads(fp.read())['features']
        return [convert_record(r) for r in records]


def bbox_from_poly(poly):
    mx, my = -180, -90
    nx, ny = 180, 90
    for c in poly['coordinates'][0]:
        mx = max(mx, c[0])
        my = max(my, c[1])
        nx = min(nx, c[0])
        ny = min(ny, c[1])
    return [nx, ny, mx, my]


def convert_record(rec):
    props = rec['properties']
    rec.pop('_permissions')
    rec.pop('_links')
    rec['bbox'] = bbox_from_poly(rec['geometry'])
    tmpl = 'https://tiles.planet.com/data/v1/item-types/%s/items/%s/thumb'
    thumblink = tmpl % (
        props['item_type'],
        rec['id'],
    ) + "?api_key="
    rec['properties'] = {
        'start_date': props['acquired'],
        'end_date': props['acquired'],
        'provider': 'https://planet.com',
        'license': 'WTFPL-4.20',
        'links': {
            'thumbnail': thumblink
        }
    }
    return rec


if __name__ == '__main__':
    converted = convert_records(sys.argv[1])
    print(json.dumps({'items': converted}))
