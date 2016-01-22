__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Pangrams
"""

import string


def is_pangram(line):
    if all(x in line for x in list(string.ascii_lowercase)):
        return True
    return False


def main():
    line = raw_input().strip()
    if is_pangram(line.lower()):
        print 'pangram'
    else:
        print 'not pangram'

if __name__ == '__main__':
    main()
