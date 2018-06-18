def minimum_distance(arr, ele1, ele2):

    n = len(arr)
    last_found = None
    result = float("inf")
    last_index = None

    if n <= 0:
        return

    for i in range(n):

        if arr[i] in [ele1, ele2]:

            if arr[i] != last_found:

                if last_index is not None:
                    result = min(result, i-last_index)

            last_index = i
            last_found = arr[i]

    return result

# arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]
arr = [3, 8, 2, 5, 4, 2, 3, 6]
print minimum_distance(arr, 3, 2)