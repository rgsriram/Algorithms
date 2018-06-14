import sys


def next_permutation(arr):
    """
    1. Find the number which is greater than the number on left. Store it as 'X'
    2. Find the number which is greater than 'X' and smaller than the all other numbers. Store it as 'Y'
    3. Swap 'X' and 'Y'
    4. Reverse the numbers from 'X' index.
    :param arr:
    :return:
    """
    x_index = -1
    n = len(arr)

    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            x_index = i-1
            break

    if x_index == -1:
        return

    y_index = -1
    y = sys.maxint

    for j in range(x_index+1, n):
        if arr[x_index] < arr[j] < y:
            y = arr[j]
            y_index = j

    arr[x_index], arr[y_index] = arr[y_index], arr[x_index]

    i = x_index + 1
    j = n-1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]

        i += 1
        j -= 1

    return arr


arr = [4,8,3,2,1]
arr = [2,1,8,7,6,5]
arr = [1,2, 3, 4]
# arr = [5,3, 4, 9, 7, 6]
arr = [6, 9, 5, 4, 3]
print next_permutation(arr)
