

# 1 1 1 2 3

# 3 4 8 8 89


def removeDuplicatesII(a):

    i = 0
    n = len(a)

    while i < n-1:

        if a[i] == a[i+1]:
            a = a[0:i] + a[i+2:n]
            n = len(a)
        else:
            i += 1

    return a


def removeDuplicatesI(a):

    i = 0
    n = len(a)

    while i < n-1:

        if a[i] == a[i+1]:
            a.pop(i)
            n = len(a)

        i += 1

    return a

print removeDuplicatesI([1000, 1000, 1001, 1002, 1002, 1003, 1003, 1004, 1010, 1010])