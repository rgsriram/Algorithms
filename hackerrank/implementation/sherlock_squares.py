__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Sherlock and Squares
"""

from math import *


def perfect_square(x, y):
    return int(floor(sqrt(y)) - ceil(sqrt(x))) + 1


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        (x, y) = raw_input().strip().split(' ')
        print perfect_square(int(x), int(y))

if __name__ == '__main__':
    main()
