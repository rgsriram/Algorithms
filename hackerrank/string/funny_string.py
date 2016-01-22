__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Funny String
"""


def is_funny(string):
    reverse = string[::-1]
    for index in range(0, len(string)-1):
        if not abs(ord(string[index]) - ord(string[index+1])) == abs(ord(reverse[index]) - ord(reverse[index+1])):
            return False
    return True


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        output = 'Funny'
        output = output if is_funny(s) else 'Not Funny'
        print output

if __name__ == '__main__':
    main()
