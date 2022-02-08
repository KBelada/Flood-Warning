# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_within_radius(stations, centre, r):
    #Function that returns the names of the monitoring stations within a given radius of a coordinate

    within_radius = []

    for station in stations:
        if haversine(station.coord, centre) < r:
            within_radius.append(station.name)
    
    within_radius = sorted(within_radius)

    print(within_radius)

