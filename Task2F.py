from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_level_with_fit

def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get top 5 stations
    highest_five = stations_highest_rel_level(stations, 5)

    for i in highest_five: # iterate thorugh them
        dates, levels = fetch_measure_levels(i.measure_id, datetime.timedelta(days = 2)) # Get dates and levels for the past 10 days
        plot_water_level_with_fit(i, dates, levels, 4) # plot the corresponding values


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()