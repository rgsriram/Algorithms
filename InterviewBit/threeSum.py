def threeSum(a, b):

    a.sort()
    min_diff = 9223372036854775807
    target = None

    i = 0

    while i < len(a) - 2:
        l = i+1
        r = len(a) - 1

        _sum = a[i] + a[l] + a[r]
        _ab_sum = abs(_sum-b)

        if _ab_sum == 0:
            return _sum

        elif _ab_sum < min_diff:
            target = _sum
            min_diff = _ab_sum

        if _sum < b:
            l += 1

        else:
            r -= 1

    return target

print threeSum([ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ], -1)