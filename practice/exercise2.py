__author__ = 'Ryan Cabrera'


def main():
    n = 4
    ps = [None] * n
    print(q(n, ps))


def q(n, ps):
    p = n - 1
    if n == 1:
        ps[p] = "(1)"
        print(ps)
        return 1
    else:
        ps[p] = "q(" + str(p) + ") + 2 * " + str(p) + " - 1"
        print(ps)
        return q(n - 1, ps) + 2 * n - 1


if __author__:
    main()
