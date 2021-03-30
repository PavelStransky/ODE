import ode


def relaxation(y, t):
    return -y


ys, ts = ode.ode_solve(relaxation, 1)