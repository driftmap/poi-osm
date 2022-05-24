import json
import pickle
import sys

from geojson import FeatureCollection, dump

file = sys.argv[1]

data = json.load(open(file,'r'))
fc = FeatureCollection(data)
labels = []
with_labels = 0
with_coordinates = 0
with_both = 0
for idx, feat in enumerate(fc['features']):
    label_data = []
    if 'name' in feat['properties']:
        name_parts = feat['properties']['name'].split(" ")
        for part in name_parts:
            label_data.append((part, 'NAME'))
    if 'other_tags' in feat['properties']:
        tags = feat['properties']['other_tags'].split('","')
        for tag in tags:
            key, value = tag.split("=>")
            key = key.replace('"', '')
            value = value.replace('"', '')
            if 'addr' in key:
                key = key.split(":")[1]
                fc['features'][idx]['properties'][key] = value
                if len(value) > 1:
                    value_parts = value.split(" ")
                    for part in value_parts:
                        label_data.append((part, key.upper()))
                else:
                    label_data.append((value, key.upper()))
            else:
                fc['features'][idx]['properties']['other_tags'] = {}
                fc['features'][idx]['properties']['other_tags'][key] = value

    coordinates = feat['geometry']['coordinates']

    if len(label_data) > 0:
        with_labels += 1
        labels.append((label_data, coordinates))
        if len(coordinates) > 0:
            with_both += 1
    if len(coordinates) > 0:
        with_coordinates += 1

print(f"POIs with labels: {with_labels}")
print(f"POIs with coordinates: {with_coordinates}")
print(f"POIs with both: {with_both}")
pickle.dump(labels,open('outputs/quebec.osm.text.tags.coords.pkl', 'wb'))
