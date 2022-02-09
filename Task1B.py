from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """List of stations in ascending order of distance from a chosen point"""

    # Build list of stations
    stations = build_station_list()

    # Get sorted list by distance
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    # Display 10 closest stations
    if len(distance_list) >= 10: #first check if there are at least 10 stations in the list
        print("10 closest stations to Cambridge are: ", distance_list[:10])
    
    # Display 10 furthest stations
    if len(distance_list) >= 10: #first check if there are at least 10 stations in the list
        print("10 furthest stations from Cambridge are: ", distance_list[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()