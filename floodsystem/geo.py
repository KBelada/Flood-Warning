# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from ensurepip import version
from os import stat
from .utils import sorted_by_key  # noqa

from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    """Make a list of stations and their distanced from a fixed point p, then sort it in ascending order"""
    distance_list=[]
    for station in stations:
        distance = haversine(station.coord, p)
        distance_list.append((station.name, station.town, distance))
    return sorted_by_key(distance_list, 2)


def stations_within_radius(stations, centre, r):
    #Function that returns the names of the monitoring stations within a given radius of a coordinate

    within_radius = []

    for station in stations:
        if haversine(station.coord, centre) < r:
            within_radius.append(station.name)
    
    within_radius = sorted(within_radius)

    print(within_radius)


def rivers_with_station(stations):
    """Creates a list of rivers which have at least one station, with no duplicates"""
    rivers_list = []
    for station in stations:
        if station.name == None:
            pass
        else:
            rivers_list.append(station.river)
    return set(rivers_list) # Removes any duplicates


def stations_by_river(stations):
    """Creates a dictionary which uses rivers as keys and maps them to their station(s)"""
    river_set = rivers_with_station(stations) # Get rivers with stations from previous function
    river_dict = {} # Create an empty dictionary
    for river in river_set:
        river_dict[river] = [] # Add an empty list to every key
    for station in stations:
        river_dict[station.river].append(station.name) # Append new elements to lists with appropriate key
    return river_dict