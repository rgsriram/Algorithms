def pythogorean_triplet(arr):

    n = len(arr)

    if not n:
        return

    arr.sort()
    square_item_map = dict((item ** 2, item) for item in arr)
    res = []

    for i in range(n-1, 1, -1):
        found = False
        x = arr[i] ** 2

        for j in range(i-1, 0, -1):
            y = arr[j] ** 2

            if x-y in square_item_map:
                found = True
                res.append((arr[i], arr[j], square_item_map[x-y]))
                break

        if found:
            continue

    return res

print pythogorean_triplet([1, 4, 5, 3, 6])