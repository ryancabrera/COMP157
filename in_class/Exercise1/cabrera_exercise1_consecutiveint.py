__author__ = 'Ryan Cabrera'


def main():
    print(step_one(60, 24))


def step_one(m, n):
    t = min(m, n)
    return step_two(m, n, t)


def step_two(m, n, t):

    if m % t == 0:
        return step_three(m, n, t)

    else:
        return step_four(m, n, t)


def step_three(m, n, t):
    if n % t == 0:
        return t

    else:
        return step_four(m, n, t)


def step_four(m, n, t):
    t -= 1
    return step_two(m, n, t)


if __author__:
    main()
