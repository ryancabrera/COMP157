from unittest import TestCase
from practice.cabrera_class_exercise3_1 import SortingExamples

__author__ = 'Ryan Cabrera'


class TestSortingExamples(TestCase):
    def test_bubble_sort(self):
        s = SortingExamples()
        bubble_list = s.random_sample_size_100
        self.assertListEqual(SortingExamples.bubble_sort(bubble_list), sorted(bubble_list))

    def test_selection_sort(self):
        self.fail()
