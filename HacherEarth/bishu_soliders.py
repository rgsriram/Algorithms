def binary_search(a, n, k):

    i = 0
    mid = (i+n) / 2

    if a[n-1] < k:
        return n

    if a[0] > k:
        return 0

    while i < n:

        if a[mid] == k:
            return mid + 1

        if a[mid-1] <= k <= a[mid+1]:
            return mid

        if a[mid] < k:
            i = mid + 1

        else:
            n = mid
            i = 0

        mid = (i+n) // 2

    return -1

#
# a = [1, 2, 3, 4, 5, 6, 7]
# point = binary_search(a, 7, 3)
# print point
# elements = a[0:point]
#
# print elements
#
# print sum(elements), point


def main():
    n = int(raw_input().strip())
    arr = list()

    for i in range(n):
        x = int(raw_input().strip())
        print x
        arr.append(x)

    q = int(raw_input().strip())

    for q0 in range(q):
        q_s = int(raw_input().strip())
        point = binary_search(arr, n, q_s)
        elements = arr[0:point]
        print sum(elements), point


if __name__ == '__main__':
    main()