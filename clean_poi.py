import json
import sys

from geojson import FeatureCollection, dump

file = sys.argv[1]

data = json.load(open(file,'r'))
fc = FeatureCollection(data)
for idx, feat in enumerate(fc['features']):
    if 'other_tags' in feat['properties']:
        tags = feat['properties']['other_tags'].split('","')
        for tag in tags:
            key, value = tag.split("=>")
            key = key.replace('"', '')
            value = value.replace('"', '')
            fc['features'][idx]['properties']['other_tags'] = {}
            fc['features'][idx]['properties']['other_tags'][key] = value

with open(f'{file.replace(".json", "")}.geojson', 'w') as f:
   dump(fc, f)
