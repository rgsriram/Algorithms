'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here

import sys

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

global intervals

def func(e):
    p = 0
    pos = 1
    lst = 0

    while p < len(intervals):
        st = intervals[p].start
        end = intervals[p].end

        st = max(lst, st)

        if (st+e) > end:
            pos = 0
            break

        lst = st+e
        p += 1

    return pos == 1


def binary_search(i, j):
    ans = 0
    low = i
    high = j

    while low <= high:
        mid = (high + low)/2

        if not func(mid):
            high = mid -1

        else:
            ans = mid
            low = mid + 1

    return ans

def gcd(a, b):
    if (a==0) or (b==0):
        return 0

    if a==b:
        return  a

    if a >b:
        return gcd(a-b, b)

    return gcd(a, b-a)


def main():
    t = int(raw_input().strip())

    for a0 in xrange(t):
        n = int(raw_input().strip())
        local_min = sys.maxint
        intervals = []

        for b0 in xrange(n):
            s, e = map(int, raw_input().strip().split(' '))
            intervals.append(Interval(s, e))
            local_min = min(local_min, e-s)

        intervals.sort(key=lambda x: x.s)
        val = binary_search(1, local_min)

        if func(val+0.5):
            val += 0.5

        g = gcd(val*10, 10)

        print("%s/%s" % ((val*10)/g, (10/g)))

main()