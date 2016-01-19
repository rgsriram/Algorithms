__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Chocolate Feast
"""


def find_chocolates(n, c, m, s):
    (t_w, r_w) = divmod(n, c)
    s = t_w
    while t_w >= m:
        (t_w, r_w) = divmod(t_w, m)
        s += t_w
        t_w += r_w
    return s


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n, c, m = raw_input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        print find_chocolates(n, c, m, 0)


if __name__ == '__main__':
    main()
