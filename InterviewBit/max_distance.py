def max_distance(a):
    n = len(a)
    l_min = [0] * n
    r_max = [0] * n

    l_min[0] = a[0]
    r_max[n - 1] = a[n -1]

    for i in range(1, len(a)):
        l_min[i] = min(a[i], a[i-1])

    for j in range(len(a)-2, -1, -1):
        r_max[j] = max(a[j], a[j+1])

    i = 0
    j = 0
    _max = -1

    while i < n and j < n:

        if l_min[i] <= r_max[j]:
            _max = max(_max, (j - i))
            j += 1

        else:
            i += 1

    return _max

print max_distance([3, 5, 4, 2])
print max_distance([3, 4, 2, 5])
print max_distance([1])
print max_distance([-1, -1, 2])