from py.parse_poi import POIParser

import subprocess
import sys

region = sys.argv[1]
query_tags = [
    'name','city','street','postcode','housenumber','suburb','unit','housename'
]

# subprocess.call(f"bash sh/osm_pbf_to_nodes_osm.sh -r {region}", shell=True)
# subprocess.call(f"bash sh/nodes_osm_to_poi_osm.sh -r {region}", shell=True)
# subprocess.call(f"bash sh/poi_osm_to_poi_geojson.sh -r {region}", shell=True)

PP = POIParser(region, query_tags)
PP.load_data()
PP.parse_POI()