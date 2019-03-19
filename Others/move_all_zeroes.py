def move_zeroes(arr):
    n = len(arr)
    zp = n-1

    pointer = 0

    while pointer < zp:

        if arr[pointer] == 0:
            is_zero = arr[zp] == 0
            arr[pointer], arr[zp] = arr[zp], arr[pointer]

            if not is_zero:
                pointer += 1

            zp -= 1
        else:
            pointer += 1

    return arr

arr = [1, 3, 0, 5, 6, 7]
# arr = [1, 2, 0, 4, 3, 0, 5, 0]
print move_zeroes(arr)