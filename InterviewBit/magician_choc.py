import math
import heapq


# def magician_chocalate(A, B):
#
#     i = 0
#     n = 0
#     j = 0
#
#     while i < B:
#
#         n += A[j]
#
#         A[j] /= 2
#
#         if j == len(A) - 1:
#             j = 0
#         else:
#             j += 1
#
#         print n, j, A[j]
#         i += 1
#
#     return int(n % ((10 ** 9) + 7))


def heap_store(q, element):
    q.pop(0)
    q.append(element)
    heapq._heapify_max(q)
    return q


def magician_chocalate(A, B):
    i = 0
    n = 0
    j = 0

    q = A
    heapq._heapify_max(q)

    while i < B:

        n += q[0]

        q = heap_store(q, q[0]/2)

        if j == len(A) - 1:
            j = 0
        else:
            j += 1

        i += 1

    return int(n % ((10 ** 9) + 7))


A = [78, 46, 53, 43, 79, 46, 79, 80, 65, 81, 39, 84, 63, 24, 54, 42, 99, 15, 86, 45, 51, 47, 94, 35, 15, 30, 23]
B = 45

print magician_chocalate(A, B)