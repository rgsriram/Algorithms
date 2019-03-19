def partition(arr, st, end):
    j = 0

    for i in range(st, end):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return j


def positive_and_negative(arr):
    n = len(arr)

    if not n:
        return

    pivot = partition(arr, 0, n)

    if pivot < 0:
        return

    pos = pivot
    neg = 0

    while neg < pos < n and arr[neg] < 0:
        arr[pos], arr[neg] = arr[neg], arr[pos]
        pos += 1
        neg += 2

    return arr

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
print positive_and_negative(arr)