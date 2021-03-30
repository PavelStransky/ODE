import ode


def relaxation(y, t):
    """ Derivatives for the relaxation system """
    return -y


ys, ts = ode.ode_solve(relaxation, 1)