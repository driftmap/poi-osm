while getopts r: flag
do
    case "${flag}" in
        r) REGION=${OPTARG};;
    esac
done

node --max_old_space_size=8000 `which osmtogeojson` outputs/$REGION/poi.osm > outputs/$REGION/poi.geojson
