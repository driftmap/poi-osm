from py.parse_poi import POIParser

import click
import subprocess

query_tags = [
    'name','city','street','postcode','housenumber','suburb','unit','housename'
]

@click.group()
def main() -> None:
    pass

@click.command()
@click.option("--region", default="georgia", required=True, help="OSM region to parse.")
@click.option("--osm", default=False, required=True, help="Parse all OSM files or just last file.")
def parseosm(region:str, osm:bool) -> None:
    if osm == True:
        subprocess.call(f"bash sh/osm_pbf_to_nodes_osm.sh -r {region}", shell=True)
        subprocess.call(f"bash sh/nodes_osm_to_poi_osm.sh -r {region}", shell=True)
        subprocess.call(f"bash sh/poi_osm_to_poi_geojson.sh -r {region}", shell=True)

    PP = POIParser(region, query_tags)
    PP.load_data()
    PP.parse_POI()

main.add_command(parseosm)

if __name__ == '__main__':
    main()
