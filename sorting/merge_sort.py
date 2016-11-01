
def merge(l, r, a):
    i = j = k = 0

    nl = len(l)
    nr = len(r)

    while i < nl and j < nr:
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1

        k += 1

    while i < nl:
        a[k] = l[i]
        i += 1
        k += 1

    while j < nr:
        a[k] = r[j]
        j += 1
        k += 1

    return a


def merge_sort(a):
    mid = len(a)/2

    if mid > 0:
        l = a[0:mid]
        r = a[mid:len(a)]

        l = merge_sort(l)
        r = merge_sort(r)
        a = merge(l, r, a)

    return a

if __name__ == '__main__':
    a = [9, 0, 100, 817, 1]
    print merge_sort(a)