import json
import pickle
import sys

from geojson import FeatureCollection

file = sys.argv[1]

def if_attribute_in_properties(properties):
    attr_labels = []
    for attr in properties:
        if attr == 'name':
            attr_parts = properties[attr].split(" ")
            for part in attr_parts:
                attr_labels.append((part, attr.upper()))
        if 'addr' in attr:
            attr_split = attr.split(":")[1]
            attr_parts = properties[attr].split(" ")
            for part in attr_parts:
                attr_labels.append((part, attr_split.upper()))
    return attr_labels

data = json.load(open(file,'r'))
fc = FeatureCollection(data)
labels = []
with_labels = 0
with_coordinates = 0
with_both = 0
for idx, feat in enumerate(fc['features']):
    label_data = if_attribute_in_properties(feat['properties'])
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
pickle.dump(labels,open('outputs/can.quebec.osm.tagged.pkl', 'wb'))
