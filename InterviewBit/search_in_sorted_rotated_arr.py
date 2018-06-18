def find_pivot(arr, start, end):

    if arr[start] < arr[end]:
        # Array is not sorted
        return start

    mid = (start + end) / 2

    if arr[mid] < arr[mid+1]:
        return mid + 1

    if arr[start] < arr[mid]:
        return find_pivot(arr, mid + 1, end)

    return find_pivot(arr, start, mid - 1)


def binary_search(arr, start, end, element):

    if start > end:
        return -1

    mid = (start + end) / 2

    if arr[mid] == element:
        return mid

    if arr[mid] < element:
        return binary_search(arr, mid+1, end, element)

    return binary_search(arr, start, mid+1, element)


def pivoted_binary_search(arr, element):
    start = 0
    end = len(arr) - 1

    pivot = find_pivot(arr, start, end)

    if pivot == -1:
        return binary_search(arr, start, end, element)

    if arr[pivot] == element:
        return pivot

    if arr[0] < element:
        return binary_search(arr, start, pivot-1, element)

    return binary_search(arr, pivot, end, element)


a = [4, 5, 6, 7, 1, 2, 3]
print pivoted_binary_search(a, 6)