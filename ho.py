import numpy as np

import ode
import graphs

def ho(y, t):
    """ Derivatives for the harmonic osciilator """
    x, v = y
    return np.array([v, -x])

def analytical_solution(t):
    return np.sin(t)

ys, ts = ode.ode_solve(ho, (0, 1))
print(ys)