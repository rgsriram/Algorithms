"""
Insertion Sort

B: O(n); A: O(n2), W: O(n2)
"""

# 9 6 3 4
# 6 9 3 4


def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        value = a[i]
        hole = i

        while hole and a[hole - 1] > value:
            a[hole] = a[hole -1]
            hole -= 1
        a[hole] = value

    print a

if __name__ == '__main__':
    a = [9,0,100,817,1]
    insertion_sort(a)