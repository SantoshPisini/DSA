
from cgitb import reset
from typing import List
from data_structures.heap import heap_driver
from data_structures.linked_list import LinkedList


print("Hey Santosh!")

# Sorting
# array = [1, 23, 15, 3, -6, 20, 0, 147, 69, -99]
# result = quick_sort(array, 0, len(array) - 1)
# result1 = merge_sort(array, 0, len(array) - 1)
# heap_sort(array)
# print(array)


# heap_driver()


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         result = []
#         for interval in intervals:
#             if interval[1] < newInterval[0]:
#                 result.append(interval)
#             elif newInterval[1] < interval[0]:
#                 result.append(newInterval)
#                 newInterval = interval
#             elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
#                 newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
#         result.append(newInterval)
#         return result

# s = Solution()
# print(s.insert([[1,3],[6,9]], [2,5]))



ll = LinkedList()
ll.insert_at_last(1)
ll.insert_at_last(2)
ll.insert_at_last(3)
ll.insert_at_last(4)
ll.insert_at_last(5)
ll.print()
# ll.oddEvenList(ll)
ll.print()
ll.remove_at_end()
ll.print()