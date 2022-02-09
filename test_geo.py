from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

"""Unit test for the geo module"""

def test_stations_by_distance():
    # Create 3 random stations
    s1 = MonitoringStation("s_id1", "m_id1", "label1", (-2.0, 4.0), (-2.3, 3.4445), "river1", "town1")
    s2 = MonitoringStation("s_id2", "m_id2", "label2", (-1.0, 3.0), (-2.3, 3.4445), "river2", "town2")
    s3 = MonitoringStation("s_id3", "m_id3", "label3", (-3.0, 5.0), (-2.3, 3.4445), "river3", "town3")
    s_list = [s1, s2, s3]
    sorted_s_by_dis = stations_by_distance(s_list, (2.0, 1.0))
    assert len(sorted_s_by_dis) == 3
    for i in range(3):
        assert len(sorted_s_by_dis[i]) == 3
    assert sorted_s_by_dis[0][0] == "s_id2" #3.6
    assert sorted_s_by_dis[0][1] == "town2"
    assert round(sorted_s_by_dis[0][2], 1) == 3.6
    assert sorted_s_by_dis[1][0] == "s_id1" #5
    assert sorted_s_by_dis[1][1] == "town1"
    assert round(sorted_s_by_dis[1][2], 1) == 5.0
    assert sorted_s_by_dis[2][0] == "s_id3" #6.4
    assert sorted_s_by_dis[2][1] == "town3"
    assert round(sorted_s_by_dis[2][2], 1) == 6.4


def test_rivers_with_stations():
    s1 = MonitoringStation("s_id1", "m_id1", "label1", (-2.0, 4.0), (-2.3, 3.4445), "river1", "town1")
    s2 = MonitoringStation(None, "m_id2", "label2", (-1.0, 3.0), (-2.3, 3.4445), "river2", "town2")
    s3 = MonitoringStation("s_id3", "m_id3", "label3", (-3.0, 5.0), (-2.3, 3.4445), "river3", "town3")
    s4 = MonitoringStation("s_id4", "m_id4", "label4", (-3.0, 2.5), (-2.3, 3.4445), "river3", "town3")
    s_list = [s1, s2, s3, s4]
    rivers_test = rivers_with_station(s_list)
    assert len(rivers_test) == 2
    assert rivers_test[0] == "river1"
    assert rivers_test[1] == "river3"

def test_stations_by_river():
    s1 = MonitoringStation("s_id1", "m_id1", "label1", (-2.0, 4.0), (-2.3, 3.4445), "river1", "town1")
    s2 = MonitoringStation(None, "m_id2", "label2", (-1.0, 3.0), (-2.3, 3.4445), "river2", "town2")
    s3 = MonitoringStation("s_id3", "m_id3", "label3", (-3.0, 5.0), (-2.3, 3.4445), "river3", "town3")
    s4 = MonitoringStation("s_id4", "m_id4", "label4", (-3.0, 2.5), (-2.3, 3.4445), "river3", "town4")
    s_list = [s1, s2, s3, s4]
    rivers_dict_test = stations_by_river(s_list)
    assert len(rivers_dict_test) == 2
    assert len(rivers_dict_test["river1"]) == 1
    assert rivers_dict_test["river1"][0] == "s_id1"
    assert len(rivers_dict_test["river3"]) == 2
    assert "s_id3" in rivers_dict_test["river3"]
    assert "s_id4" in rivers_dict_test["river3"]
    