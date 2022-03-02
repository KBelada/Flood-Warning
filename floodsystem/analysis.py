import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
from .stationdata import build_station_list, update_water_levels
from .datafetcher import fetch_measure_levels
import datetime
from .flood import stations_level_over_threshold


def polyfit(dates, levels, p):
    """Returns a least-square fit of polynomial degree p"""

    # Convert dates into floats
    float_dates = matplotlib.dates.date2num(dates)

    # Date shift
    d0 = float_dates[0]

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(float_dates - d0, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, d0

def rel_risk(stations):
    '''Assign risk level to each station based on current level relative to typical range'''

    pos = 0
    severe_risk = []
    high_risk = []
    moderate_risk = []
    low_risk = []

    rel_level = stations_level_over_threshold(stations, -11111)

    for i in rel_level:
        for n in stations_level_over_threshold(stations, 2.5):
            if i[0] == n[0]:
                severe_risk.append(i[0])
                pos += 1
    
    for i in range(pos, len(rel_level)):
        for n in stations_level_over_threshold(stations, 1.2):
            if rel_level[i][0] == n[0]:
                high_risk.append(rel_level[i][0])
                pos += 1

    for i in range(pos, len(rel_level)):
        for n in stations_level_over_threshold(stations, 0.7):
            if rel_level[i][0] == n[0]:
                moderate_risk.append(rel_level[i][0])
                pos += 1
    
    for i in range(pos, len(rel_level)):
        for n in stations_level_over_threshold(stations, -11111):
            if rel_level[i][0] == n[0]:
                low_risk.append(rel_level[i][0])
                pos += 1
    
    data_stations = []
    for i in rel_level:
        data_stations.append(i[0])
    
    no_data_stations = []
    for i in stations:
        if i not in data_stations:
            no_data_stations.append(i)

    return severe_risk, high_risk, moderate_risk, low_risk, no_data_stations

def changing_level(stations):
    '''Updates risk level based on if the water level has risen or fallen over the past day'''
    
    severe, high, moderate, low, no = rel_risk(stations)
    valid_data = severe, high, moderate, low

    for i in valid_data:
        for n in i:
            try:
                dates, levels = fetch_measure_levels(n.measure_id, datetime.timedelta(days=1))
            except Exception:
                continue
            else:
                if len(levels) > 1:
                    for k in levels:
                        if type(k) == float:
                            level_diff = levels[0] - levels[-1]
                            typical_range_diff = n.typical_range[1] - n.typical_range[0]
                            if level_diff > 0.5*typical_range_diff:
                                if n in high:
                                    high.remove(n)
                                    severe.append(n)
                                elif n in moderate:
                                    moderate.remove(n)
                                    high.append(n)
                                elif n in low:
                                    low.remove(n)
                                    moderate.append(n)
                            if level_diff < 0 and abs(level_diff) > typical_range_diff:
                                if n in severe:
                                    severe.remove(n)
                                    high.append(n)
                                elif n in high:
                                    high.remove(n)
                                    moderate.append(n)
                                elif n in moderate:
                                    moderate.remove(n)
                                    low.append(n)
    
    return severe, high, moderate, low, no

def risk_towns(stations):
    '''Assigns risk level to towns based on recent river level data'''

    severe, high, moderate, low, no = changing_level(stations)

    severe_towns = []
    high_towns = []
    moderate_towns = []
    low_towns = []
    no_towns = []

    for i in severe:
        severe_towns.append(i.town)
    
    for i in high:
        if i.town not in severe_towns:
            high_towns.append(i.town)
    
    for i in moderate:
        if i.town not in severe_towns and i.town not in high_towns:
            moderate_towns.append(i.town)
    
    for i in low:
        if i.town not in severe_towns and i.town not in high_towns and i.town not in moderate_towns:
            low_towns.append(i.town)

    for i in no:
        no_towns.append(i.town)

    for i in stations:
        if i.town not in severe_towns and i.town not in high_towns and i.town not in moderate_towns and i.town not in low_towns and i.town not in no_towns:
            no_towns.append(i.town)
    
    return severe_towns, high_towns, moderate_towns, low_towns, no_towns
