def segregate_zero(arr):
    z = 0
    i = 0
    n = len(arr)

    while i < n:
        if arr[i] == 0:
            arr[i], arr[z] = arr[z], arr[i]
            z += 1

        i += 1

    print(arr)

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
segregate_zero(arr)