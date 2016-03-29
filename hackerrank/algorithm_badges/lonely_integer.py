__author__ = 'sriram'


def lonely_integer(b):
    res = {i: b.count(i) for i in set(b) if b.count(i) < 2}
    return ' '.join(str(x) for x in res.keys())


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        b = map(int, raw_input().strip().split(" "))
        print lonely_integer(b)

if __name__ == '__main__':
    main()
