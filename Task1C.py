#Calculate stations within 10km of Cambridge City center

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

# Build list of stations
stations = build_station_list()

stations_within_radius(stations, (52.2053, 0.1218), 10)
