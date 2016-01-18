__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Find digits
"""

get_digits = lambda x, y, count: count+1 if y != 0 and x % y == 0 else count


def find_digits(arr, num):
    count = 0
    for each in arr:
        count = get_digits(num, int(each), count)
    return count


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = raw_input().strip()
        number = int(n)
        print find_digits(list(n), number)

if __name__ == '__main__':
    main()
