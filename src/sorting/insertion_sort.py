from typing import List

# Best when the list is almost sorted.
def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        key, j = arr[i + 1], i
        while j>= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr