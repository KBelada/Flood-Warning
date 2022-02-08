# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_within_radius(stations, centre, r):
    #Function that returns the names of the monitoring stations within a given radius of a coordinate, sorted alphabetically.

    within_radius = []

    for station in stations:
        if haversine(station.coord, centre) < r:
            within_radius.append(station.name)
    
    within_radius = sorted(within_radius)

    print(within_radius)


def rivers_by_station_number(stations, N):
    #Function that returns the N rivers with the greatest number of stations, sorted by number of stations.
    
    station_number = [('River Cam', 0)]   #Random river to start for loop

    for station in stations:
        for i in range(len(station_number)):
            if station.river == station_number[i][0]:
                station_number[i][1] += 1

            else:
                station_number.append((station.river, 1))
            
    station_number = sorted_by_key(station_number, 1)

    n = N - 1
    return station_number[n:]

