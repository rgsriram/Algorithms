
# 9 6 3 4


def partition(a, s, e):
    pivot = a[e]
    pIndex = s

    for i in range(s, e-1):
        if a[i] <= pivot:
            a[pIndex], a[i] = a[i], a[pIndex]
            pIndex += 1
        a[pIndex], a[e] = a[e], a[pIndex]
    return pIndex


def quick_sort(a, s, e):
    if s < e:
        p = partition(a, s, e)
        a = quick_sort(a, 0, p)
        a = quick_sort(a, p, e)
    print a
    return a

if __name__ == '__main__':
    a = [9, 0, 100, 817, 1]
    print quick_sort(a, 0, len(a)-1)