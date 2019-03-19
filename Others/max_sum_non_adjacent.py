def max_sum(arr):
    n = len(arr)

    prev = arr[0]
    current = max(prev, arr[1])
    res = 0

    for i in range(2, n):
        res = max(arr[i]+prev, current)
        prev = current
        current = res

    return res

arr = [5, 5, 10, 100, 10, 5]
arr = [3, 2, 5, 10, 7]
arr = [3, 2, 7, 10]
arr = [1, 20, 3]
print max_sum(arr)