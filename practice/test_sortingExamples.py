from unittest import TestCase
from practice.cabrera_class_exercise3_1 import SortingExamples

__author__ = 'Ryan Cabrera'


class TestSortingExamples(TestCase):
    def test_bubble_sort(self):
        s = SortingExamples()
        bubble_list = s.random_sample_size_100
        self.assertListEqual(s.bubble_sort(bubble_list), sorted(bubble_list))

    def test_selection_sort(self):
        s = SortingExamples()
        selection_list = s.random_sample_size_100
        self.assertListEqual(s.selection_sort(selection_list), sorted(selection_list))

    def test_insertion_sort(self):
        s = SortingExamples()
        insertion_list = s.random_sample_size_10
        self.assertListEqual(s.insertion_sort(insertion_list), sorted(insertion_list))
