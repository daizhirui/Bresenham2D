import matplotlib.pyplot as plt
import numpy as np


def bresenham2Dv1(sx, sy, ex, ey):
    """ Bresenham's ray tracing algorithm in 2D.

    :param sx: x of start point of ray
    :param sy: y of start point of ray
    :param ex: x of end point of ray
    :param ey: y of end point of ray
    :return: cells along the ray
    """
    dx = abs(ex - sx)
    dy = abs(ey - sy)
    steep = abs(dy) > abs(dx)
    if steep:
        dx, dy = dy, dx  # swap

    if dy == 0:
        q = np.zeros((dx + 1, 1), dtype=int)
    else:
        q = np.append(0, np.greater_equal(
            np.diff(
                np.mod(np.arange(  # If d exceed dx, decrease d by dx
                    np.floor(dx / 2), -dy * dx + np.floor(dx / 2) - 1, -dy,
                    dtype=int), dx
                )  # offset np.floor(dx / 2) to compare d with 0.5dx
            ), 0))

    if steep:
        if sy <= ey:
            y = np.arange(sy, ey + 1)
        else:
            y = np.arange(sy, ey - 1, -1)
        if sx <= ex:
            x = sx + np.cumsum(q)
        else:
            x = sx - np.cumsum(q)
    else:
        if sx <= ex:
            x = np.arange(sx, ex + 1)
        else:
            x = np.arange(sx, ex - 1, -1)
        if sy <= ey:
            y = sy + np.cumsum(q)
        else:
            y = sy - np.cumsum(q)
    return np.vstack((x, y))


def main():
    w = 11
    h = 11
    pts = bresenham2Dv1(0, 0, 10, 9)
    im = np.zeros((h, w), dtype=int)
    im[pts[1], pts[0]] = 255
    plt.imshow(im, cmap='binary')
    plt.xticks(np.arange(0, w))
    plt.yticks(np.arange(0, h))
    plt.grid('on')
    plt.show()


if __name__ == '__main__':
    main()
