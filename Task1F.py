from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    '''Delivers a list of all the stations with inconsistent typical range data, sorted alphabetically'''
    #Build list of stations
    stations = build_station_list()

    #Print list of stations with inconsistent typical range data
    print(inconsistent_typical_range_stations(stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
