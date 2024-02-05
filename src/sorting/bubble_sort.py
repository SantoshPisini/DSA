from typing import List

# Pick the large element and place at last
def bubble_sort(arr: List[int]) -> List[int]:
    for _ in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr