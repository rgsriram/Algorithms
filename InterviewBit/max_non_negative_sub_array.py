def max_positive_sub_array(arr):
    n = len(arr)

    if n <= 0:
        return 0

    tmp_total = -1
    tmp_size = 0

    total = 0
    size = 0
    results = []
    start = None

    for i in range(n):

        if arr[i] > 0:

            if start is None:
                start = i
            
            tmp_total += arr[i]
            tmp_size += 1

        else:
            if total > tmp_total or tmp_total == 0:
                continue

            elif total == tmp_total:
                if size < tmp_size:
                    total = tmp_total
                    size = tmp_size

                results = arr[start:i]

            elif total < tmp_total:
                total = tmp_total
                results = arr[start:i]
                size = start + i + 1

            start = None
            tmp_total = 0
            tmp_size = 0

    if tmp_total > total:
        results = arr[start:n]

    return results

arr = [2, 3, -7, 1, 2, 5]
arr = [0, 0, -1, -1]
# arr = [1, 2, 5, -7, 2, 3, -7]
print max_positive_sub_array(arr)