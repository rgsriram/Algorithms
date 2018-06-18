"""
def partition(a, s, e):

    pivot = s
    i = s + 1
    j = e

    while i < j:

        while a[i] < a[j] and i < e:
            i += 1

        while a[i] > a[j] and j >= s:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    a[pivot], a[j] = a[j], a[pivot]

    return pivot
"""


def partition(a, s, e):

    pivot = s
    i = s + 1
    j = e

    while i < j:

        while a[i] < a[pivot] and i < e:
            i += 1

        while a[j] > a[pivot] and j >= s:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    a[pivot], a[j] = a[j], a[pivot]

    return pivot


def quick_select(a, s, e, k):

    pivot = partition(a, s, e)

    if pivot == k:
        return a[pivot]

    elif pivot < k:
        return quick_select(a, pivot+1, e, k)

    else:
        return quick_select(a, s, pivot, k)


def kth_smallest(a, k):
    return quick_select(a, 0, len(a)-1, k)

# a = [ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ]
# print kth_smallest(a, 1)

a = [1]


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def partition(self, a, s, e):

        pivot = s
        i = s + 1
        j = e

        while i < j:

            while a[i] < a[pivot] and i < e:
                i += 1

            while a[j] > a[pivot] and j >= s:
                j -= 1

            if i < j:
                a[i], a[j] = a[j], a[i]

        print pivot, j
        a[pivot], a[j] = a[j], a[pivot]

        return pivot

    def quick_select(self, a, s, e, k):
        pivot = self.partition(a, s, e)

        if pivot == k:
            return a[pivot]

        elif pivot < k:
            return self.quick_select(a, pivot + 1, e, k)

        else:
            return self.quick_select(a, s, pivot, k)

    def kthsmallest(self, A, B):

        if len(A) == 0:
            return -1

        if len(A) == 1:
            return A[0]

        return self.quick_select(A, 0, len(A)-1, B)


print Solution().kthsmallest(a, 1)

