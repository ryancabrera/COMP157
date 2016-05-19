__author__ = 'Ryan Cabrera'


def main():
    print(q(4))


def q(n):
    if n == 1:
        print(1)
        return 1
    else:
        p = n-1
        ps = "q(", p, ") + 2 *", p, "- 1"
        print(ps)
        return q(n - 1) + 2 * n - 1


if __author__:
    main()
