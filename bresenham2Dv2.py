import numpy as np


def plot_line_low(x0, y0, x1, y1):
    """ Plot line of slop between (-1, 1)
    """
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    a = dy * 2  # 2 dy
    d = a - dx  # 2 dy - dx
    b = d - dx  # 2 (dy-dx)
    y = y0

    vertices = []
    for x in range(x0, x1 + 1):
        vertices.append([x, y])
        if d >= 0:
            y = y + yi
            d = d + b
        else:
            d = d + a

    return np.array(vertices).T


def plot_line_high(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    a = dx * 2  # 2dx
    d = a - dy  # 2 dx - dy
    b = d - dy  # 2 (dx - dy)
    x = x0

    vertices = []
    for y in range(y0, y1 + 1):
        vertices.append([x, y])
        if d >= 0:
            x = x + xi
            d = d + b
        else:
            d = d + a

    return np.array(vertices).T


def bresenham2Dv2(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dy) == 0:
        x = list(range(x0, x1 + 1))
        return np.array([x, [y0] * len(x)])
    if abs(dx) == 0:
        y = list(range(y0, y1 + 1))
        return np.array([[x0] * len(y), y])

    if abs(dy) < abs(dx):
        if dx < 0:
            return plot_line_low(x1, y1, x0, y0)
        else:
            return plot_line_low(x0, y0, x1, y1)
    else:
        if dy < 0:
            return plot_line_high(x1, y1, x0, y0)
        else:
            return plot_line_high(x0, y0, x1, y1)
