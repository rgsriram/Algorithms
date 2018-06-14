import sys


def find_median_two_sorted_arr(arr1, arr2):

    x = len(arr1)
    y = len(arr2)

    if x > y:
        find_median_two_sorted_arr(arr2, arr1)

    low = 0
    high = x

    while low <= high:

        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        max_left_x = sys.maxint * -1 if partition_x == 0 else arr1[partition_x-1]
        min_right_x = sys.maxint if partition_x == x else arr1[partition_x]

        max_left_y = sys.maxint * -1 if partition_y == 0 else arr2[partition_y - 1]
        min_right_y = sys.maxint if partition_y == y else arr2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:

            if (x + y) % 2 == 0:
                return max(max_left_x, max_left_y) + min(min_right_x, min_right_y)

            else:
                return max(max_left_x, max_left_y)

        elif max_left_x > min_right_y:
            high = partition_x - 1

        else:
            low = partition_x + 1


a = [1, 4, 7, 11]
b = [3, 5, 8, 10, 12, 13]

print find_median_two_sorted_arr(a, b) / 2.0