from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Calculates the total number of rivers with stations"""
    """Finds the names of stations on a specific river"""

    # Build list of stations
    stations = build_station_list()

    rivers_list = rivers_with_station(stations)
    print("Total number of rivers with at least 1 staton: ", len(rivers_list))
    rivers_sorted = sorted(rivers_list) # Sorts the list alphabetically
    print("First 10 stations: ", rivers_sorted[:10]) # Prints the first 10 rivers

    # Outputs all the stations on specific rivers
    rivers_dict = stations_by_river(stations)
    print("Stations at River Aire: ", sorted(rivers_dict["River Aire"]))
    print("Stations at River Cam: ", sorted(rivers_dict["River Cam"]))
    print("Stations at River Thames: ", sorted(rivers_dict["River Thames"]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
