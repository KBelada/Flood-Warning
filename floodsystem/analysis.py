import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Returns a least-square fit of polynomial degree p"""

    # Convert dates into floats
    float_dates = matplotlib.dates.date2num(dates)

    # Date shift
    d0 = float_dates[0]

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(float_dates - d0, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, d0