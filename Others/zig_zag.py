def zig_zag(arr):
    flag = True

    for i in range(len(arr)-1):

        if flag:

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        else:

            if arr[i] < arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        flag = not flag

    return arr

arr = [4, 3, 7, 8, 6, 2, 1]
print zig_zag(arr)