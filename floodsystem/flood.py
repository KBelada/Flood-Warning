from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    '''Returns a list of tuples of stations whos current water level is above a given relative thrashold of their typical range'''

    over_threshold = []

    for i in stations:
        if i.typical_range_stations() == False:
            pass
        elif type(i.latest_level) != float:
            pass
        else:
            if i.relative_water_level() > tol:
                over_threshold.append((i, i.relative_water_level()))
    
    over_threshold = sorted_by_key(over_threshold, 1, True)

    return over_threshold
