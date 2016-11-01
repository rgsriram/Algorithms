__author__ = 'sriram'


def is_rotatable(i):
    return bool(i % 2)


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print 'Yes' if not is_rotatable(n) else 'No'

if __name__ == '__main__':
    main()