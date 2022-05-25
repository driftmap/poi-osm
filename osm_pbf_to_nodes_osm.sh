#!/bin/bash

osmosis --read-pbf data/quebec.osm.pbf \
        --tf accept-nodes \
        aerialway=station \
        aeroway=aerodrome,helipad,heliport \
        amenity=* building=school,university craft=* \
        emergency=* \
        highway=bus_stop,rest_area,services \
        historic=* leisure=* office=* \
        public_transport=stop_position,stop_area railway=station \
        shop=* tourism=* \
        addr:housenumber=* \
        addr:street=* \
        addr:postcode=* \
        --write-xml quebec.nodes.osm
# Test if the script above success
if [ $? -eq 0 ]; then
   echo 🥳 Successful script
else
   echo "❌ Script failed"
fi
