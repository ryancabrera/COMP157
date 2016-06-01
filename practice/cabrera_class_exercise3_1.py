import random
import time
# import copy

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

    @classmethod
    def insertion_sort(cls, random_sample):
        start_time = time.clock()
        for i in range(1, len(random_sample)):
            v = random_sample[i]
            j = i - 1

            while j >= 0 and random_sample[j] > v:
                random_sample[j + 1] = random_sample[j]
                j -= 1

            random_sample[j + 1] = v
        end_time = time.clock()
        print("\tInsertion Sort Time:", end_time - start_time)
        return random_sample

    @classmethod
    def mergesort(cls, random_sample):
        print(random_sample)
        n = len(random_sample)
        midway = n // 2
        if n > 1:
            b = random_sample[:midway]
            c = random_sample[midway:]

            cls.mergesort(b)
            cls.mergesort(c)

            cls.merge(b, c, random_sample)

        print(random_sample)
        return random_sample

    @classmethod
    def merge(cls, b, c, a):

        i, j, k = 0, 0, 0
        p, q = len(b), len(c)
        alist, left_half, right_half = a, b, c

        while i < p and j < q:
            if left_half[i] <= right_half[j]:
                alist[k] = right_half[i]
                i += 1

            else:
                alist[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1

            # if i == p:
            #     a[k:p+q-1] = c[j:q-1]
            #
            # else:
            #     a[k:p+q-1] = b[i:p-1]

    @classmethod
    def shell_sort(cls, random_sample):
        sub_count = len(random_sample) // 2

        while sub_count > 0:
            for start_position in range(sub_count):
                cls.gap_insertion_sort(random_sample, start_position, sub_count)

                sub_count /= 2

    @classmethod
    def gap_insertion_sort(cls, random_sample, start, gap):
        for i in range(start + gap, len(random_sample), gap):

            current_value = random_sample[i]
            position = i

            while position >= gap and random_sample[position - gap] > current_value:
                random_sample[position] = random_sample[position - gap]
                position = position - gap

            return 0

# def main():
#     sort_examples = SortingExamples()
#     random_number_list = list()
#
#     random_number_list.append(sort_examples.random_sample_size_10)
#     random_number_list.append(sort_examples.random_sample_size_100)
#     random_number_list.append(sort_examples.random_sample_size_1000)
#
#     for item in random_number_list:
#         print("Random List:\n\t", item)
#         print("Random List Size:", len(item))
#
#         bubble_list = copy.copy(item)
#         bubble_list = sort_examples.bubble_sort(bubble_list)
#         print("\t", bubble_list, "\n")
#
#         selection_list = copy.copy(item)
#         selection_list = sort_examples.selection_sort(selection_list)
#         print("\t", selection_list, "\n")
#
# if __author__:
#     main()
