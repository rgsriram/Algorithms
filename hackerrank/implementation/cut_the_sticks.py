__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Cut the sticks
"""


def get_smallest_element(arr, x, y):
    iMin = x
    for i in range(x, y, 1):
        if arr[i] < arr[iMin]:
            iMin = i
    return arr[iMin]


def get_sticks_count(arr):
    x = get_smallest_element(arr, 0, len(arr))
    arr = [element - x for element in arr]
    arr = [arr[i] for i, e in enumerate(arr) if e > 0]

    if len(arr) > 0:
        print len(arr)
        get_sticks_count(arr)


def main():
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print n
    get_sticks_count(arr)

if __name__ == '__main__':
    main()
