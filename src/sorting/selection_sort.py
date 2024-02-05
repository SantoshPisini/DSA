from typing import List

# Pick the small element and place at first.
def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        for j in range(i, len(arr) - 1):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr