while getopts r: flag
do
    case "${flag}" in
        r) REGION=${OPTARG};;
    esac
done

osmconvert outputs/$REGION/nodes.osm \
           --drop-ways \
           --drop-author \
           --drop-relations \
           --drop-version \
           -o=outputs/$REGION/poi.osm