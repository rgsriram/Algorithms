__author__ = 'sriram'


def _binary_search(a, x, s, e):
    m = (s + e)/2
    if x == a[m]:
        return m
    elif x < a[m]:
        return binary_search(a, x, 0, m-1)
    elif x > a[m]:
        return binary_search(a, x, m+1, e)
    else:
        return -1


def binary_search(a, x, i, n):
    while i < n:
        mid = (i+n)/2
        if x == a[mid]:
            return mid
        elif m < a[mid]:
            n = mid -1
        else:
            i = mid +1

if __name__ == '__main__':
    t = int(raw_input().strip())
    for a0 in xrange(t):
        m = int(raw_input().strip())
        n = int(raw_input().strip())
        a = map(int, raw_input().strip().split(" "))
        b = a
        a = sorted(a, reverse=True)
        for i in range(0, len(a)):
            if m - a[i] > 0:
                index = binary_search(a, m-a[i], 0, len(a)-1)
                if index >= 0:
                    x = b.index(a[i])
                    y = b.index(a[index])
                    if x == y:
                        print x+1, y+2
                    else:
                        print x+1, y+1
                    break
