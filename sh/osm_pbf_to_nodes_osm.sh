#!/bin/bash
while getopts r: flag
do
    case "${flag}" in
        r) REGION=${OPTARG};;
    esac
done

osmosis --read-pbf osm_extracts/$REGION-latest.osm.pbf \
        --tf accept-nodes \
         building=* \
         aerialway=station \
         aeroway=aerodrome,helipad,heliport \
         amenity=* \
         building=school,university craft=* \
         highway=bus_stop,rest_area,services \
         historic=* leisure=* office=* \
         public_transport=stop_position,stop_area railway=station \
         shop=* tourism=* \
         addr:housenumber=* \
         addr:street=* \
         addr:postcode=* \
         addr:city=* \
        --tf reject-nodes \
          amenity=drinking_water,watering_point,shower,telephone,toilets,bench,parcel_locker,bbq,dog_toilet,give_box,post_box,fountain,waste_basket,parking_entrance,parking,fire_station \
        --tf reject-ways \
        --tf reject-relations \
        --write-xml outputs/$REGION/nodes.osm

#        --write-xml quebec.nodes.osm

# Test if the script above success
if [ $? -eq 0 ]; then
   echo 🥳 Successful script: $REGION
else
   echo "❌ Script failed: "$REGION
fi
