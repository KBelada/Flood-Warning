from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy

import datetime

def test_polyfit():
    
    # Build stations and update water levels
    stations = build_station_list()
    update_water_levels(stations)

    # Checks the data types of the outputs
    for i in range(1, 1500, 100):
        stat = stations[i]
        dates, levels = fetch_measure_levels(stat.measure_id, datetime.timedelta(days=10))
    for n in range(2, 4):
        assert type(polyfit(dates, levels, n)[0]) == numpy.poly1d
        assert type(polyfit(dates, levels, n)[1]) == numpy.float64