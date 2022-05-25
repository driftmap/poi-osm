# Install

Install [Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis): `brew install osmosis`

Install [OSMConvert](https://wiki.openstreetmap.org/wiki/Osmconvert): `brew install osmconvert`



# Parsing points-of-interest from OSM extracts

Following the general blueprint from [this Medium article](https://medium.com/codait/easy-access-to-all-points-of-interest-data-acc6569e45b2).

## Steps

### 1. Download OSM extract

For the latest OSM extract in the beta testing regions run one of the following scripts:

Download a pbf extract of OSM data, e.g. [this extract of Quebec from GeoFabrick](https://download.geofabrik.de/north-america/canada/quebec.html), which we are using for Montreal. 

**California**
```console
wget https://download.geofabrik.de/north-america/us/california-latest.osm.pbf -P osm_extracts
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

### 2a. Run OSM to (Geo)JSON parsing pipeline

```python
python osm_to_json.py parseosm --region {REGION} --osm {BOOLEAN}
```

Alternatively you can run through steps 2b to 5 one by one:

### 2b. Select points of interest
```console

bash sh/osm_pbf_to_nodes_osm.sh -r $REGION

```

|Input|Output|
|---|---|
|\*.osm.pbf|\*.nodes.osm|

### 3. Drop ways, keep nodes

```console

bash sh/nodes_osm_to_poi_osm.sh -r $REGION

```
|Input|Output|
|---|---|
|\*.nodes.pbf|\*.poi.osm|


### 4. Convert to (Geo)JSON

```console

bash sh/poi_osm_to_poi_geojson.sh -r $REGION

```

|Input|Output|
|---|---|
|\*.poi.osm|\*.poi.geojson|

### 5. Clean (Geo)JSOn and extract names, labels and coordinates

```python
python osm_to_json.py parseosm --region {REGION} --osm False
```


|Input|Output|
|---|---|
|\*.poi.geojson|\*.osm.text.tags.coords.pkl|