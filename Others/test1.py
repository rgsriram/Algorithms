# def getLongestBalancedChromosome(c):
#     m = dict()
#     m[0] = -1
#
#     count_0 = 0
#     count_1 = 1
#
#     res = 0
#     for i in range(len(c)):
#         if c[0] == '0':
#             count_0 += 1
#         else:
#             count_1 += 1
#
#         if m.get(count_1 - count_0):
#             res = max(res, i - m[count_1 - count_0])
#
#         else:
#             m[count_1 - count_0] = i
#
#     return res
#
# def max_equal_sub(s):
#     '''
#     I get the substrings by iterating over the starts and the ends for each start. For each
#     of these, check if the counts are equal.
#     '''
#     return max((s[b:e] for b in range(len(s)) for e in range(b, len(s)) if s[b:e].count('1') == s[b:e].count('0')), key=len)
#
#
#
# def stringLen(str):
#     # Create a python dictionary to store
#     # differences between counts of 1s and 0s.
#     m = dict()
#
#     # Initially difference is 0.
#     m[0] = -1
#
#     count_0 = 0
#     count_1 = 0
#     res = 0
#     for i in range(len(str)):
#
#         # Keeping track of counts of
#         # 0s and 1s.
#         if str[i] == '0':
#             count_0 += 1
#         else:
#             count_1 += 1
#
#         # If difference between current
#         # counts already exists, then
#         # substring between previous and
#         # current index has same no. of
#         # 0s and 1s. Update result if
#         # this substring is more than
#         # current result.
#         if m.get(count_1 - count_0):
#             res = max(res, i - m[count_1 - count_0])
#
#         # If current difference is
#         # seen first time.
#         else:
#             m[count_1 - count_0] = i
#     return res
#
#
# print getLongestBalancedChromosome("11010111")
# print stringLen("00001")
# print len(max_equal_sub("00001"))


def binarySearchCount(arr, n, key):
    left = 0
    right = n

    mid = 0
    while (left < right):

        mid = left + (right - left) // 2

        if (arr[mid] == key):

            while (arr[mid + 1] == key and mid + 1 < n):
                mid += 1
            break

        elif (arr[mid] > key):
            right = mid

        else:
            left = mid + 1

    while (arr[mid] > key):
        mid -= 1

    return mid + 1

arr = [1,1,1,1, 2,2, 3,2, 2, 1, 1, 1]

print binarySearchCount(arr, len(arr), 5)


