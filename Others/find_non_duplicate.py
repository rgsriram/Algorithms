# def nonDuplicate(arr):
#
#     for i in range(len(arr)):
#
#         if arr[abs(arr[i])] >= 0:
#             arr[abs(arr[i])] = -arr[abs(arr[i])]
#
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             print arr[i]
#
#
# nonDuplicate([12, 1, 12, 3, 12, 1, 1, 2, 3, 3])


def printRepeating(arr, n):
    # First check all the
    # values that are
    # present in an array
    # then go to that
    # values as indexes
    # and increment by
    # the size of array
    for i in range(0, n):
        index = arr[i] % n
        arr[index] += n

        # Now check which value
        # exists more
        # than once by dividing
        # with the size
    # of array
    for i in range(0, n):
        if (arr[i] / n) > 1:
            print i

# Driver's code
arr = [1, 6, 3, 150, 3, 100, 100]
arr_size = len(arr)

print ("The repeating elements are:")

printRepeating(arr, arr_size)