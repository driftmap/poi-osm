while getopts r: flag
do
    case "${flag}" in
        r) REGION=${OPTARG};;
    esac
done

osmtogeojson outputs/$REGION/poi.osm > outputs/$REGION/poi.geojson
