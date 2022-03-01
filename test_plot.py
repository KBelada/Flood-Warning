from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation

def test_plot_water_levels():
    # Create a generic station
    s_id1 = "s_id1"
    m_id1 = "test-m-id1"
    label1 = "label1"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "river1"
    town1 = "town1"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    #Should be invalid if either dates or levels are empty
    assert plot_water_levels(s1, [], []) == None
    #Should be invlaid if dates and levels are not of the same lenght
    assert plot_water_levels(s1, [], [1]) == None
