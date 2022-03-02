from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import risk_level_towns
# 2G takes a long time to run, demonstration of outputs can be viewed quickly
# on Github

def run():
    stations = build_station_list()
    update_water_levels(stations)

    severe, high, moderate, low, no = risk_level_towns(stations)
    print("Severe: ", severe)
    print("High: ", high)
    print("Moderate: ", moderate)
    print("Low: ", low)
    print("No data: ", no)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
