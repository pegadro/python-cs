from unittest import TestCase

from typing import (
    List
)

from algorithms.sorting.BubbleSort import bubbleSort

class SortingAlgorithmsTest(TestCase):

    def test_bubble_sort(self) -> None:
        unorderedList: List[int] = [5, 1, 7, 9, 0, 8, 4, 3, 2, 6]
        orderedListManually: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        orderedList: List[int] = bubbleSort(unorderedList)

        self.assertEquals(orderedList, orderedListManually)