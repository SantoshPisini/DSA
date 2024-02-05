def partition(arr, start, end):
    pivot = arr[start + (end - start) // 2]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return start

def quick_sort(arr, start, end):
    if start < end:
        mid = partition(arr, start, end)
        quick_sort(arr, start, mid - 1)
        quick_sort(arr, mid, end)
    return arr
