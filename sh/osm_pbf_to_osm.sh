# This script seems redundant

while getopts r: flag
do
    case "${flag}" in
        r) REGION=${OPTARG};;
    esac
done

osmosis --read-pbf data/$REGION.osm.pbf \
        --write-xml quebec.osm
        # addr:postcode=*, addr:city=*, addr:housename=*,addr:unit=*
