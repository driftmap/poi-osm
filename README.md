# Parsing points-of-interest from OSM extracts

Following the general blueprint from [this Medium article](https://medium.com/codait/easy-access-to-all-points-of-interest-data-acc6569e45b2).

## Steps

### 1. Download OSM extract

For the latest OSM extract in the beta testing regions run one of the following scripts:

**California**
```console
wget https://download.geofabrik.de/north-america/us/california-latest.osm.pbf
```

**Georgia**
```console
wget https://download.geofabrik.de/north-america/us/georgia-latest.osm.pbf -P osm_extracts
```

**New York**
```console
wget https://download.geofabrik.de/north-america/us/new-york-latest.osm.pbf -P osm_extracts
```

**Quebec**
```console
wget https://download.geofabrik.de/north-america/canada/quebec-latest.osm.pbf -P osm_extracts
```

### 2. Select points of interest
```console

bash sh/osm_pbf_to_nodes_osm.sh

```

|Input|Output|
|---|---|
|\*.osm.pbf|\*.nodes.osm|

### 3. Drop ways, keep nodes

```console

bash sh/nodes_osm_to_poi_osm.sh

```
|Input|Output|
|---|---|
|\*.nodes.pbf|\*.poi.osm|


### 4. Convert to (Geo)JSON

```console

bash sh/poi_osm_to_poi_geojson.sh

```

|Input|Output|
|---|---|
|\*.poi.osm|\*.poi.geojson|

### 5. Clean (Geo)JSOn and extract names, labels and coordinates

```python

python py/clean_poi.py quebec.poi.geojson

```

|Input|Output|
|---|---|
|\*.poi.geojson|\*.osm.text.tags.coords.pkl|