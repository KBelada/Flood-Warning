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
    distance_list=[] # empty 
    for station in stations:
        distance = haversine(station.coord, p)
        distance_list.append((station.name, station.town, distance))
    return sorted_by_key(distance_list, 2)