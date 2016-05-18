__author__ = 'Ryan Cabrera'


def main():
    print(eucalid(60, 12))


def eucalid(m, n):
    while n != 0:
        r = n % m
        m = n
        n = r
    return m

if __author__:
    main()
