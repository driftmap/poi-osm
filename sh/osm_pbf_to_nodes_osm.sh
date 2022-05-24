osmosis --read-pbf osm_extracts/quebec.osm.pbf \
        --tf accept-nodes \
        aerialway=station \
        aeroway=aerodrome,helipad,heliport \
        amenity=* building=school,university craft=* emergency=* \
        highway=bus_stop,rest_area,services \
        historic=* leisure=* office=* \
        public_transport=stop_position,stop_area railway=station \
        shop=* tourism=* \
        --write-xml outputs/quebec.nodes.osm
