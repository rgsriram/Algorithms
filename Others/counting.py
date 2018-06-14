def counting_sort(arr):
    _max = max(arr)

    op = [0] * (len(arr) + 1)

    count_arr = [0] * (_max+1)

    for each in arr:
        count_arr[each] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(arr)):
        op[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1

    for i in range(len(arr)):
        arr[i] = op[i]

    print arr


arr = [1,4,5,3,100, 98]

counting_sort(arr)