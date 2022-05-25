import json
import pickle
import re
import sys

from geojson import FeatureCollection

file = sys.argv[1]

address_tags = [
    'name','city','street','postcode','housenumber','suburb','unit','housename'
]

def if_attribute_in_properties(properties):
    attr_labels = []
    other = {}
    for attr in properties:
        if attr in ['name']:
            attr_parts = properties[attr].split(" ")
            for part in attr_parts:
                attr_labels.append((part, attr.upper()))
        elif 'addr' in attr:
            attr_split = attr.split(":")[1]
            if attr_split in address_tags:
                attr_parts = properties[attr].split(" ")
                for part in attr_parts:
                    attr_labels.append((part, attr_split.upper()))
        else:
            if attr != 'id':
                other[attr] = properties[attr]
    return attr_labels, other

data = json.load(open(file,'r'))
fc = FeatureCollection(data)
labels = []
with_labels = 0
with_coordinates = 0
with_both = 0
for idx, feat in enumerate(fc['features']):
    label_data, other = if_attribute_in_properties(feat['properties'])
    coordinates = feat['geometry']['coordinates']
    id = re.findall('\d+', feat['id'])
    if len(label_data) > 0:
        with_labels += 1
        labels.append((label_data, coordinates, id, other))
        if len(coordinates) > 0:
            with_both += 1
    if len(coordinates) > 0:
        with_coordinates += 1

print(f"POIs with labels: {with_labels}")
print(f"POIs with coordinates: {with_coordinates}")
print(f"POIs with both: {with_both}")
pickle.dump(labels,open('outputs/can.quebec.osm.tagged.pkl', 'wb'))
