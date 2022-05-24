import json
import pickle
import sys

from geojson import FeatureCollection, dump

file = sys.argv[1]

data = json.load(open(file,'r'))
fc = FeatureCollection(data)
#out_words = 'quebec.osm.words.txt'
out_labels = 'quebec.osm.tags.txt'
#file_words = open(out_words, 'a')
#file_labels = open(out_labels, 'a')
labels = []
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

    if len(label_data) > 0:
        #file_words.write(f"{','.join(words)}\n")
        #file_labels.write(f"{','.join(label_data)}\n")
        print(label_data)
        labels.append(label_data)
pickle.dump(labels,open('quebec.osm.tagged_test.pkl', 'wb'))

#with open(f'{file}_cleaned.geojson', 'w') as f:
#    dump(fc, f)