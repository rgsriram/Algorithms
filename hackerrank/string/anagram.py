__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Anagrams
"""
from collections import Counter


def _anagram(string):
    if len(string) % 2 == 1:
        return -1
    _left = string[0:len(string)/2]
    _right = string[len(string)/2:len(string)]
    diff = dict(Counter(_left) - Counter(_right))
    s = 0
    for k, v in diff.iteritems():
        s += v
    return s


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        print _anagram(s)

if __name__ == '__main__':
    main()
