from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Get sorted list by distance
    distance_list = stations_by_distance(stations, (52.2053, 0.1218))

    # Display 10 closest stations
    print("10 closest stations to Cambridge are: ", distance_list[:10])
    
    # Display 10 furthest stations
    print("10 furthest stations from Cambridge are: ", distance_list[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()