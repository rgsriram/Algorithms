def compare(x, y):

    xy = '%s%s' % (x, y)
    yx = '%s%s' % (y, x)

    return -1 if int(xy) > int(yx) else 0


def largestNumber(a):
    return sorted(a, cmp=lambda x, y: compare(x, y))

print(largestNumber([3, 30, 34, 5, 9]))