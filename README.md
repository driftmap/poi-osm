# Parsing points-of-interest from OSM extracts

Following the general blueprint from [this Medium article](https://medium.com/codait/easy-access-to-all-points-of-interest-data-acc6569e45b2).

## Steps

### 1. Download OSM extract

WRITE SCRIPT

### 2. Select points of interest
```console

bash osm_pbf_to_nodes_osm.sh

```

|Input|Output|
|---|---|
|quebec.osm.pbf|quebec.nodes.osm|

### 3. Drop ways, keep nodes

```console

bash nodes_osm_to_poi_osm.sh

```
|Input|Output|
|---|---|
|quebec.nodes.pbf|quebec.poi.osm|


### 4. Convert to (Geo)JSON

```console

bash poi_osm_to_poi_geojson.sh

|Input|Output|
|---|---|
|quebec.poi.osm|quebec.poi.geojson|

```

### 5. Clean (Geo)JSOn and extract names, labels and coordinates

THIS NEEDS TO BE REWRITTEN TO *ALSO* GET COORS

```python

bash nodes_osm_to_poi_osm.sh

```