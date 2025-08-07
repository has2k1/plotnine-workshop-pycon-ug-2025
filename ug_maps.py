import pickle
import hashlib
from pathlib import Path
from geopandas import GeoDataFrame


__all__ = (
    "ug",
    "ug_regions",
    "ug_subregions",
    "ug_districts",
    "ug_subcounties",
    "ug_towns",
    "ug_lakes",
    "ug_rivers",
)
CACHE_DIR = Path("cache/")

def load_file(filepath, verbose=False):
    filepath = Path(filepath)
    # load from cached file and/or
    # create one after loading
    checksum = hashlib.md5(filepath.read_bytes()).hexdigest()
    cache_filename = CACHE_DIR / f"{checksum}.pkl"
    CACHE_DIR.mkdir(exist_ok=True)
    try:
        df = pickle.load(cache_filename.open("rb"))
    except OSError:
        df = GeoDataFrame.from_file(filepath)
        pickle.dump(df, cache_filename.open("wb"))
        if verbose:
            print(f"Read and cached: {filepath}")
    else:
        if verbose:
            print(f"Read from the cache: {filepath}")


    return df


ug = load_file("./data/maps/2014/ug.gpkg")
ug_districts = load_file("./data/maps/2014/ug_districts.gpkg")
ug_regions = load_file("./data/maps/2014/ug_regions.gpkg")
ug_subregions = load_file("./data/maps/2014/ug_subregions.gpkg")
ug_subcounties = load_file("./data/maps/2014/ug_subcounties.gpkg")
ug_towns = load_file("./data/maps/2014/ug_towns.gpkg")
ug_lakes = load_file("./data/maps/2014/ug_lakes.gpkg")
ug_rivers = load_file("./data/maps/2014/ug_rivers.gpkg")
