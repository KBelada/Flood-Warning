from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import  rivers_by_station_number
from haversine import haversine, Unit

"""Unit test for the geo module"""

def test_stations_by_distance():
    # Create 3 generic stations
    s_id1 = "s_id1"
    m_id1 = "test-m-id1"
    label1 = "label1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "river1"
    town1 = "town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    s_id2 = "s_id2"
    m_id2 = "test-m-id2"
    label2 = "label2"
    coord2 = (-1.0, 3.0)
    trange2 = (-2.3, 3.4445)
    river2 = "river2"
    town2 = "town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    s_id3 = "s_id3"
    m_id3 = "test-m-id3"
    label3 = "label3"
    coord3 = (-3.0, 5.0)
    trange3 = (-2.3, 3.4445)
    river3 = "river3"
    town3 = "town3"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    s_list = [s1, s2, s3]

    sorted_s_by_dis = stations_by_distance(s_list, (2.0, 1.0))
    assert len(sorted_s_by_dis) == 3
    for i in range(3):
        assert len(sorted_s_by_dis[i]) == 3
    assert sorted_s_by_dis[0][0] == "label2" #3.6
    assert sorted_s_by_dis[0][1] == "town2"
    assert round(sorted_s_by_dis[0][2], 1) == 400.9
    assert sorted_s_by_dis[1][0] == "label1" #5
    assert sorted_s_by_dis[1][1] == "town1"
    assert round(sorted_s_by_dis[1][2], 1) == 555.9
    assert sorted_s_by_dis[2][0] == "label3" #6.4
    assert sorted_s_by_dis[2][1] == "town3"
    assert round(sorted_s_by_dis[2][2], 1) == 711.9


def test_rivers_with_stations():
    # Create 4 generic station objects, one with no station at a river, 2 on the same river
    s_id1 = "s_id1"
    m_id1 = "test-m-id1"
    label1 = "label1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "river1"
    town1 = "town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    s_id2 = None
    m_id2 = "test-m-id2"
    label2 = "label2"
    coord2 = (-1.0, 3.0)
    trange2 = (-2.3, 3.4445)
    river2 = "river2"
    town2 = "town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    s_id3 = "s_id3"
    m_id3 = "test-m-id3"
    label3 = "label3"
    coord3 = (-3.0, 5.0)
    trange3 = (-2.3, 3.4445)
    river3 = "river3"
    town3 = "town3"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    s_id4 = "s_id4"
    m_id4 = "test-m-id4"
    label4 = "label4"
    coord4 = (-3.0, 5.0)
    trange4 = (-2.3, 3.4445)
    river4 = "river3"
    town4 = "town4"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    s_list = [s1, s2, s3, s4]

    rivers_test = rivers_with_station(s_list)
    assert len(rivers_test) == 3
    assert rivers_test == {"river1", "river2", "river3"}


def test_stations_by_river():
    # Create 4 generic station objects, one with no station at a river, 2 on the same river
    s_id1 = "s_id1"
    m_id1 = "test-m-id1"
    label1 = "label1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "river1"
    town1 = "town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    s_id2 = None
    m_id2 = "test-m-id2"
    label2 = "label2"
    coord2 = (-1.0, 3.0)
    trange2 = (-2.3, 3.4445)
    river2 = "river2"
    town2 = "town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    s_id3 = "s_id3"
    m_id3 = "test-m-id3"
    label3 = "label3"
    coord3 = (-3.0, 5.0)
    trange3 = (-2.3, 3.4445)
    river3 = "river3"
    town3 = "town3"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    s_id4 = "s_id4"
    m_id4 = "test-m-id4"
    label4 = "label4"
    coord4 = (-3.0, 5.0)
    trange4 = (-2.3, 3.4445)
    river4 = "river3"
    town4 = "town4"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    s_list = [s1, s2, s3, s4]

    rivers_dict_test = stations_by_river(s_list)
    assert len(rivers_dict_test) == 3
    assert len(rivers_dict_test["river1"]) == 1
    assert rivers_dict_test["river1"][0] == "label1"
    assert len(rivers_dict_test["river3"]) == 2
    assert "label3" in rivers_dict_test["river3"]
    assert "label4" in rivers_dict_test["river3"]


def test_rivers_by_station_number():
    # Create 7 generic station objects, 2 rivers with 2 stations on them, 1 river with 3 stations on it
    s_id1 = "s_id1"
    m_id1 = "test-m-id1"
    label1 = "label1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "river1"
    town1 = "town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    s_id2 = "s_id2"
    m_id2 = "test-m-id2"
    label2 = "label2"
    coord2 = (-1.0, 3.0)
    trange2 = (-2.3, 3.4445)
    river2 = "river2"
    town2 = "town2"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    s_id3 = "s_id3"
    m_id3 = "test-m-id3"
    label3 = "label3"
    coord3 = (-3.0, 5.0)
    trange3 = (-2.3, 3.4445)
    river3 = "river3"
    town3 = "town3"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    s_id4 = "s_id4"
    m_id4 = "test-m-id4"
    label4 = "label4"
    coord4 = (-3.0, 5.0)
    trange4 = (-2.3, 3.4445)
    river4 = "river3"
    town4 = "town4"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    s_id5 = "s_id5"
    m_id5 = "test-m-id5"
    label5 = "label5"
    coord5 = (-3.0, 5.0)
    trange5 = (-2.3, 3.4445)
    river5 = "river3"
    town5 = "town5"
    s5 = MonitoringStation(s_id5, m_id5, label5, coord5, trange5, river5, town5)

    s_id6 = "s_id6"
    m_id6 = "test-m-id6"
    label6 = "label4"
    coord6 = (-3.0, 5.0)
    trange6 = (-2.3, 3.4445)
    river6 = "river1"
    town6 = "town6"
    s6 = MonitoringStation(s_id6, m_id6, label6, coord6, trange6, river6, town6)

    s_id7 = "s_id7"
    m_id7 = "test-m-id7"
    label7 = "label7"
    coord7 = (-3.0, 5.0)
    trange7 = (-2.3, 3.4445)
    river7 = "river2"
    town7 = "town7"
    s7 = MonitoringStation(s_id7, m_id7, label7, coord7, trange7, river7, town7)

    s_list = [s1, s2, s3, s4, s5, s6, s7]
    
    top_1_test = rivers_by_station_number(s_list, 1)
    assert len(top_1_test) == 1
    assert ("river3", 3) in top_1_test
    top_2_test = rivers_by_station_number(s_list, 2)
    assert len(top_2_test) == 3 #Because 2 rivers with 2 stations
    assert top_2_test[0] == ("river3", 3)
    assert top_2_test[1] == ("river1", 2)
    assert top_2_test[2] == ("river2", 2)
    top_3_test = rivers_by_station_number(s_list, 3)
    assert top_3_test == top_2_test


def test_stations_within_radius():

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.197227, 0.087527)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    b_id = "test-b-id"
    m_id = "test-mb-id"
    label = "that station"
    coord = (-2.0, 5.0)
    trange = (2.3, 3.4445)
    river = "River B"
    town = "Your Town"
    b = MonitoringStation(b_id, m_id, label, coord, trange, river, town)

    c = [s, b]

    assert stations_within_radius(c, (52.2053, 0.1218), 10) == ["some station"]
