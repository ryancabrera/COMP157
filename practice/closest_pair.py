import sys
__author__ = 'Ryan Cabrera'


def main():
    p = [(0, 1), (1, 2)]
    print(brute_force_closest_points(p))


def brute_force_closest_points(p):
    d_min = sys.maxsize
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            x_i = p[i]
            d = square_root(x_i)
            print(d)

    print(d_min)


def square_root(x):
    return x**.5


if __author__:
    main()
