__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Alternating Characters
"""



def get_no_of_deletions(string):
    count = 0

    for index in range(0, len(string)-1):
        if string[index] == string[index+1]:
            count += 1
    return count


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        print get_no_of_deletions(s)

if __name__ == '__main__':
    main()
