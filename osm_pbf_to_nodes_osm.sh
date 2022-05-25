#!/bin/bash

osmosis --read-pbf data/quebec.osm.pbf \
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
          amenity=drinking_water,watering_point,shower,telephone,toilets,bench,parcel_locker,bbq,dog_toilet,give_box,post_box,fountain \
        --tf reject-ways \
        --tf reject-relations \
        --write-xml quebec.nodes.osm
# Test if the script above success
if [ $? -eq 0 ]; then
   echo 🥳 Successful script
else
   echo "❌ Script failed"
fi
