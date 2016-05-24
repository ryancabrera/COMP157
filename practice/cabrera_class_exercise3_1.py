import random
import time
import copy

__author__ = 'Ryan Cabrera'


class SortingExamples(object):
    def __init__(self):
        self.random_sample_size_10 = random.sample(range(1, 10000), 10)
        self.random_sample_size_100 = random.sample(range(1, 10000), 100)
        self.random_sample_size_1000 = random.sample(range(1, 10000), 1000)

    @classmethod
    def bubble_sort(cls, random_sample):
        start_time = time.clock()
        n = len(random_sample)

        for i in range(1, n):
            for j in range(n-1):
                if random_sample[j] > random_sample[j + 1]:
                    random_sample[j], random_sample[j + 1] = random_sample[j + 1], random_sample[j]

        end_time = time.clock()
        print("\tBubble Sort Time:", end_time - start_time)

        return random_sample

    @classmethod
    def selection_sort(cls, random_sample):
        start_time = time.clock()
        n = len(random_sample)

        for i in range(n):
            minimum_j = i

            for j in range(i + 1, n):
                if random_sample[j] < random_sample[minimum_j]:
                    minimum_j = j

            random_sample[i], random_sample[minimum_j] = random_sample[minimum_j], random_sample[i]

        end_time = time.clock()
        print("\tSelection Sort Time:", end_time - start_time)

        return random_sample


def main():
    sort_examples = SortingExamples()
    random_number_list = list()

    random_number_list.append(sort_examples.random_sample_size_10)
    random_number_list.append(sort_examples.random_sample_size_100)
    random_number_list.append(sort_examples.random_sample_size_1000)

    for item in random_number_list:
        print("Random List:\n\t", item)
        print("Random List Size:", len(item))

        bubble_list = copy.copy(item)
        bubble_list = sort_examples.bubble_sort(bubble_list)
        print("\t", bubble_list, "\n")

        selection_list = copy.copy(item)
        selection_list = sort_examples.selection_sort(selection_list)
        print("\t", selection_list, "\n")

if __author__:
    main()