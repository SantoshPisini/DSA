def merge(arr, start, mid, end):
    i, j, temp = start, mid + 1, []
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= end:
        temp.append(arr[j])
        j += 1
    k = 0
    for i in range(start, end + 1):
        arr[i] = temp[k]
        k += 1

def merge_sort(arr, start, end):
    if (start < end):
        mid = start + (end - start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)
    return arr
