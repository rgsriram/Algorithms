'''
Problem from: HackerRank
Domain: Algorithms
Name: Angry Professor
'''

import sys


def get_plus_minus_zero_from_arr(arr):
    positive = sum(x > 0 for x in arr)
    negative = sum(x < 0 for x in arr)
    zero = sum(x == 0 for x in arr)

    return positive, negative, zero


def check_attendence(k, a):
    (positive, negative, zero) = get_plus_minus_zero_from_arr(a)
    if (negative + zero) >= k:
        return True
    return False


def check_inputs(input, _from, _to):
    if (_from <= input <= _to):
        return True
    return False


def main():
    t = int(raw_input().strip())

    if check_inputs(t, 1, 10):
        for a0 in xrange(t):
            n, k = raw_input().strip().split(' ')
            n, k = [int(n), int(k)]
            a = map(int, raw_input().strip().split(' '))

            if check_inputs(n, 1, 1000) and check_inputs(k, 1, n) and check_inputs(len(a), 1, n):
                if check_attendence(k, a):
                    print "NO"
                else:
                    print "YES"

if __name__ == '__main__':
    main()
