__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Utopian Tree
"""


def get_height(seasons, initial_height=1):
    for i in xrange(1, (seasons+1), 1):
        if i % 2 == 0:
            initial_height += 1
        else:
            initial_height *= 2
    return initial_height


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print get_height(seasons=n)

if __name__ == '__main__':
    main()
