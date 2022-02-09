# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_data():

    # Create stations with inconsistent typical range data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    b_id = "test-b-id"
    m_id = "test-mb-id"
    label = "that station"
    coord = (-2.0, 5.0)
    trange = (2.3, -3.4445)
    river = "River B"
    town = "Your Town"
    b = MonitoringStation(b_id, m_id, label, coord, trange, river, town)

    a_id = "test-a-id"
    m_id = "test-ma-id"
    label = "a station"
    coord = (-2.0, 6.0)
    trange = None
    river = "River A"
    town = "Their Town"
    a = MonitoringStation(a_id, m_id, label, coord, trange, river, town)

    c = [s, b, a]

    assert inconsistent_typical_range_stations(c) == ["a station", "that station"]
