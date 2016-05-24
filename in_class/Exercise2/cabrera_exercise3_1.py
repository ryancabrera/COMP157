import random
import time

__author__ = 'Ryan Cabrera'


def main():
    random_sample_size_10 = random.sample(range(1, 10000), 10)
    random_sample_size_100 = random.sample(range(1, 10000), 100)
    random_sample_size_1000 = random.sample(range(1, 10000), 1000)

    print("Random Sample Size: 10")
    print("  Selection Sort:")
    selection_sort(random_sample_size_10)
    print("  Bubble Sort:")
    bubble_sort(random_sample_size_10)

    print()

    print("Random Sample Size: 100")
    print("  Selection Sort:")
    selection_sort(random_sample_size_100)
    print("  Bubble Sort:")
    bubble_sort(random_sample_size_100)

    print()

    print("Random Sample Size: 1000")
    print("  Selection Sort:")
    selection_sort(random_sample_size_1000)
    print("  Bubble Sort:")
    bubble_sort(random_sample_size_1000)


def bubble_sort(random_sample):
    start_time = time.clock()
    n = len(random_sample)

    for i in range(1, n):
        for j in range(n-1):
            if random_sample[j] > random_sample[j + 1]:
                random_sample[j], random_sample[j + 1] = random_sample[j + 1], random_sample[j]

    end_time = time.clock()
    print("\tTime:", end_time - start_time)

    return random_sample


def selection_sort(random_sample):
    start_time = time.clock()
    n = len(random_sample)

    for i in range(n):
        minimum_j = i

        for j in range(i + 1, n):
            if random_sample[j] < random_sample[minimum_j]:
                minimum_j = j

        random_sample[i], random_sample[minimum_j] = random_sample[minimum_j], random_sample[i]

    end_time = time.clock()
    print("\tTime:", end_time - start_time)

    return random_sample


if __author__:
    main()
