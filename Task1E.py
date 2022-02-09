from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Output top N rivers with the most stations"""
    # Build list of stations
    stations = build_station_list()

    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
