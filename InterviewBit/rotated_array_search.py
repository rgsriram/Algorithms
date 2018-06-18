def binarySearch(a, low, high, k):
    if high < low:
        return -1

    mid = (low + high) / 2

    if a[mid] == k:
        return a[mid]

    elif k > a[mid]:
        return binarySearch(a, mid+1, high, k)

    return binarySearch(a, 0, mid-1, k)

