from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():
    a = MonitoringStation('a1', 'a2', 'a_name', (1.0,1.0), (1.0, 2.0), 'a4', 'a5')
    a.latest_level = 1.0
    b = MonitoringStation('a1', 'a2', 'a_name', (1.0,1.0), (1.0, 2.0), 'a4', 'a5')
    b.latest_level = 2.0
    c = MonitoringStation('a1', 'a2', 'a_name', (1.0,1.0), (1.0, 2.0), 'a4', 'a5')
    c.latest_level = 3.0
    d = MonitoringStation('a1', 'a2', 'a_name', (1.0,1.0), (1.0, 2.0), 'a4', 'a5')
    d.latest_level = None
    e = MonitoringStation('a1', 'a2', 'a_name', (1.0,1.0), (1.0, 2.0), 'a4', 'a5')
    e.latest_level = 1.5

    s = [a, b, c, d, e]

    assert stations_highest_rel_level(s, 3) == [c, b, e]
