import json
import pickle
import re
import sys

from geojson import FeatureCollection
from typing import List, Dict

class POIParser():
    def __init__(self, region:str, query_tags:list) -> None:
        self.region = region
        self.query_tags = query_tags

    def load_data(self):
        self.data = json.load(open(f"outputs/{self.region}/poi.geojson",'r'))
        self.fc = FeatureCollection(self.data)
        self.labels = []
        self.with_labels = 0
        self.with_coordinates = 0
        self.with_both = 0

    def parse_POI(self):
        for idx, feat in enumerate(self.fc['features']):
            label_data, other = self._if_attribute_in_properties(feat['properties'])
            coordinates = feat['geometry']['coordinates']
            id = re.findall('\d+', feat['id'])
            if len(label_data) > 0:
                self.with_labels += 1
                self.labels.append((label_data, coordinates, id, other))
                if len(coordinates) > 0:
                    self.with_both += 1
            if len(coordinates) > 0:
                self.with_coordinates += 1
        self._print_summaries()
        pickle.dump(self.labels,open(f'outputs/{self.region}/{self.region}.osm.tagged.pkl', 'wb'))

    def _print_summaries(self):
        print(f"POIs with labels: {self.with_labels}")
        print(f"POIs with coordinates: {self.with_coordinates}")
        print(f"POIs with both: {self.with_both}")

    def _if_attribute_in_properties(self, properties:List[Dict]):
        attr_labels = []
        other = {}
        for attr in properties:
            if attr in ['name']:
                attr_parts = properties[attr].split(" ")
                for part in attr_parts:
                    attr_labels.append((part, attr.upper()))
            elif 'addr' in attr:
                attr_split = attr.split(":")[1]
                if attr_split in self.query_tags:
                    attr_parts = properties[attr].split(" ")
                    for part in attr_parts:
                        attr_labels.append((part, attr_split.upper()))
            else:
                if attr != 'id':
                    other[attr] = properties[attr]
        return attr_labels, other

