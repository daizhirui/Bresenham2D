import time

import numpy as np
from matplotlib import pyplot as plt

from bresenham2Dv1 import bresenham2Dv1
from bresenham2Dv2 import bresenham2Dv2
from bresenham2Dv3 import bresenham2Dv3
from skimage.draw import line


def draw_result(w, h, pts):
    im = np.zeros((h, w), dtype=int)
    im[pts[1], pts[0]] = 255
    plt.imshow(im, cmap='binary')
    plt.plot(pts[0, [0, -1]], pts[1, [0, -1]], color='red')
    plt.grid('on')
    plt.show()


def main():
    x0 = 0
    y0 = 0
    x1 = 3
    y1 = 5
    w = x1 + 1
    h = y1 + 1

    ts1 = []
    ts2 = []
    ts3 = []
    ts4 = []

    base = 2
    max_i = 7
    for i in range(max_i, -1, -1):
        x1p = x1 * (base ** i)
        y1p = y1 * (base ** i)

        t0 = time.time()
        pts1 = bresenham2Dv1(x0, y0, x1p, y1p)
        t1 = time.time()

        pts2 = bresenham2Dv2(x0, y0, x1p, y1p)
        t2 = time.time()

        pts3 = bresenham2Dv3(x0, y0, x1p, y1p)
        t3 = time.time()

        # http://members.chello.at/easyfilter/Bresenham.pdf
        # https://scikit-image.org/docs/dev/api/skimage.draw.html#skimage.draw.line
        pts4 = np.array(line(x0, y0, x1p, y1p))
        t4 = time.time()

        ts1.append(t1 - t0)
        ts2.append(t2 - t1)
        ts3.append(t3 - t2)
        ts4.append(t4 - t3)

    print(f'v1: {t1 - t0}\n'
          f'v2: {t2 - t1}\n'
          f'v3: {t3 - t2}\n'
          f'scikit: {t4 - t3}')
    draw_result(w, h, pts1)
    draw_result(w, h, pts2)
    draw_result(w, h, pts3)
    draw_result(w, h, pts4)

    x = base ** np.array(range(max_i, -1, -1)) * max(x1, y1) + 1
    plt.plot(x, ts1, label='v1')
    plt.plot(x, ts2, label='v2')
    plt.plot(x, ts3, label='v3')
    plt.plot(x, ts4, label='scikit')
    plt.ticklabel_format(axis='y', style='sci', scilimits=(1, -1))
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    """
    The result shows that v1 and v2 are equivalent. v3 gives slightly 
    different output sometimes. v1 has shorter runtime when the number of 
    vertices is greater than 50. However, scikit-image provides an 
    implementation faster than all my implementations.
    """


if __name__ == '__main__':
    main()
