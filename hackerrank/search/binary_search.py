__author__ = 'sriram'


from collections import OrderedDict

def binary_search(a, x, s, e):
    m = (s + e)/2
    if m < 0 or m >= len(a):
        return -1
    if x == a[m]:
        return m
    elif x < a[m]:
        return binary_search(a, x, 0, m-1)
    elif x > a[m]:
        return binary_search(a, x, m+1, e)


def main():
    x = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))

    print binary_search(a, x, 0, n)

if __name__ == '__main__':
    main()

