#List the names of the rivers with the 9 greatest numbers of stations on them.

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

rivers_by_station_number(build_station_list(), 9)
