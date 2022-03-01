import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib
from .analysis import polyfit


def plot_water_levels(station, dates, levels):
    """Plots water level data against time for a station"""

    # Make sure there are valid points to plot
    if len(dates)==0 or len(dates)!=len(levels):
        print("Invalid data")
    else:
        # Plot
        plt.plot(dates, levels)
        plt.plot(dates, [station.typical_range[0]]*len(dates), label = 'typical low')
        plt.plot(dates, [station.typical_range[1]]*len(dates), label = 'typical high')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    
    # Convert dates into floats
    float_dates = matplotlib.dates.date2num(dates)

    # Get best-fit polynomial and time shift
    poly, d0 = polyfit(dates, levels, p)

    #Plot
    plt.plot(dates, poly(float_dates - d0), '.')

    # Plot water level data (with typical range shown)
    plot_water_levels(station, dates, levels)
    plt.show()
