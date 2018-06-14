def partition(arr, s, e):
    pivot = a[e]
    p_index = s

    for i in range(s, e):
        if arr[i] >= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1

    arr[p_index], arr[e] = arr[e], arr[p_index]

    return p_index, arr

a = [ 1, 9, 3, 2, 4]

a = [ 1090, 8, 1901, 7, 6, 4, 17, 29, 78]


def quick_select(arr, l, r, k):

    if l > r:
        return -1

    pivot, arr = partition(arr, l, r)

    if pivot == k:
        print arr
        return arr[pivot]

    elif pivot > k:
        return quick_select(arr, l, pivot-1, k)

    return quick_select(arr, pivot+1, r, k)


k = 2
print quick_select(a, 0, len(a) -1, k-1)