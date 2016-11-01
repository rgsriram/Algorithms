"""
Bubble Sort:

Compare element with adjacent element if it greater then swap
B: O(n); A: O(n2), W: O(n2)
"""


def bubble_sort(a):
    n = len(a)

    for k in range(1, n):
        flag = 0
        for i in range(0, n-k):
            print n-k-1
            j = i+1
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                flag = 1
        if flag == 0:
            break
    print a

if __name__ == '__main__':
    a = [9,0,100,817,1]
    bubble_sort(a)