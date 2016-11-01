__author__ = 'sriram'


def partition(a, st, end):
    pivot = a[end]
    pIndex = st
    i = st
    while i < end:
        if a[i] > pivot:
            temp = a[i]
            a[i] = a[pIndex]
            a[pIndex] = temp
            pIndex += 1
        temp = a[pIndex]
        a[pIndex] = a[end]
        a[end] = temp
        i += 1
    return pIndex


def quick_sort(a, st, end):
    if st < end:
        pIndex = partition(a, st, end)
        quick_sort(a, st, pIndex-1)
        quick_sort(a, pIndex+1, end)
    return a


def swap_number(b):
    for i in range(1, len(b)):
        value = b[i]
        hole = i
        v_ones = bin(value).count("1")
        b_ones = bin(b[hole-1]).count("1")
        while hole > 0 and (b_ones < v_ones or b[hole-1] < value):
            b[hole] = b[hole-1]
            hole -= 1
            b_ones = bin(b[hole-1]).count("1")
        b[hole] = value
    return b


def _swap_number(b):
    c = list()
    for i in range(0, len(b)-1):
        v = bin(b[i]).count("1")
        print v
        try:
            if c[v]:
                c[v].append(b[i])
                c[v].sort(reverse=True)
        except Exception:
            c[v] = []
            pass

    for r in c:
        print r

if __name__ == '__main__':
    _a_cnt = 0
    _a_cnt = int(raw_input())
    _a_i=0
    _a = []
    while _a_i < _a_cnt:
        _a_item = int(raw_input());
        _a.append(_a_item)
        _a_i +=1
    _swap_number(_a)
    # for e in _swap_number(_a):
    #     print e