"""
    Based off of solution here:
        https://programmingpraxis.com/2012/07/31/send-more-money-part-1/
"""

import itertools
__author__ = 'Ryan Cabrera'


def main():
    word_1 = list("send")
    word_2 = list("more")
    word_3 = list("money")

    letters = list(set(word_1 + word_2 + word_3))
    digits = range(10)

    send, more, money = solve_cabrera(letters, digits)

    print("send =", send, "\nmore =", more, "\nmoney =", money)


def solve_cabrera(letters, digits):
    char_num_permutations = itertools.permutations(digits, len(letters))

    for individual_char_num_permutation in char_num_permutations:
        sol = dict(zip(letters, individual_char_num_permutation))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        send = 1000 * sol['s'] + 100 * sol['e'] + 10 * sol['n'] + sol['d']
        more = 1000 * sol['m'] + 100 * sol['o'] + 10 * sol['r'] + sol['e']
        money = 10000 * sol['m'] + 1000 * sol['o'] + 100 * sol['n'] + 10 * sol['e'] + sol['y']

        if send + more == money:
            for letters in sol:
                print(letters, "=", sol.get(letters))
            return send, more, money


if __author__:
    main()
