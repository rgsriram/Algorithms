__author__ = 'sriram'

import sys


def amount(b, w, x, y, z):
    if x > (y+z):
        sum = b * (y+z)
    else:
        sum = b * x

    if y > (x+z):
        sum += w * (x+z)
    else:
        sum += w * y

    return sum


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        b, w = raw_input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        print amount(b, w, x, y, z)

if __name__ == '__main__':
    main()

