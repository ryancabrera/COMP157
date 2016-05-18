import math

__author__ = 'Ryan Cabrera'


def main():

    m = 60
    n = 12
    #middle_school(m, n)

    #print(middle_school(m, n))
    #middle_school(m, n)
    #print(sieve(12))

    loc = sieve(7)

    for x in loc:
        if x != 0:
            print(x)

    print(sieve(7))
    print(list(rosetta_sieve(7)))

    templist = [1, 2, 3]



def middle_school(m, n):
    m_values = sieve(m)
    n_values = sieve(n)

    print(m_values)
    print(n_values)

    greatest_cvalue= list()

    for common_value in m_values:
        if common_value in n_values:
            greatest_cvalue.append(common_value)
    return greatest_cvalue


def sieve(n):
    a = [0]*n**2
    i = 0
    l = [0] * len(a)
    print(math.floor(n**.5))
    for p in range(2, n):
        a[p] = p

    for p in range(2, math.floor(n**.5)):
        if a[p] != 0:
            j = p*p
            while j <= n:
                a[j] = 0
                j += p

    for p in range(2, n):
        if a[p] != 0:
            l.append(a[p])
            i += 1

    l = set(l)
    l.remove(0)
    l = list(l)

    return l


#This snippet was taken from rosteta code
def rosetta_sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))


if __author__:
    main()
