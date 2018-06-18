def zig_zag(arr):
    flag = False
    n = len(arr)
    i = 0

    while i < n-1:

        if (not flag and not arr[i] < arr[i+1]) or (flag and not arr[i] > arr[i+1]):
            swap = True
        else:
            swap = False

        if swap:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        flag = not flag
        i += 1

    return arr

a = [9, 6, 1, 7, 5, 2, 3]

print zig_zag(a)