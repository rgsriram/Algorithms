
def zero_one_subarray(arr):
    count_index_map = dict()
    count = 0
    max_len = 0

    n = len(arr)

    for i in range(n):

        count += -1 if arr[i] == 0 else 1

        if count in count_index_map:
            max_len = max(max_len, i - count_index_map[count])

        else:
            count_index_map[count] = i

        print count_index_map

    print max_len


arr = [0, 1, 0, 1, 1, 1]

# arr = [1, 0, 1, 0, 1, 1, 1, 0]
zero_one_subarray(arr)
