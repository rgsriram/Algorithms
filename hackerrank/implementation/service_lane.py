__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Service Lane
"""


def get_smallest_element(arr, x, y):
    iMin = x
    for i in range(x+1, y+1, 1):
        if arr[i] < arr[iMin]:
            iMin = i
    return arr[iMin]


def main():
    n,t = raw_input().strip().split(' ')
    n,t = [int(n),int(t)]
    width = map(int,raw_input().strip().split(' '))
    for a0 in xrange(t):
        i,j = raw_input().strip().split(' ')
        i,j = [int(i),int(j)]
        print get_smallest_element(width, i, j)

if __name__ == '__main__':
    main()