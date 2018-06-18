import sys


def max_consecutive_gap(arr):
    _max = sys.maxint * -1

    if len(arr) < 2:
        return 0

    for i in range(len(arr)-1):
        _max = max(abs(arr[i] - arr[i+1]), _max)

    return abs(_max)


print max_consecutive_gap([ 1, 1, 2 ])