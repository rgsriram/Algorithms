__author__ = 'sriram'


def insertion_sort(b):
    for i in range(1, len(b)):
        value = b[i]
        hole = i
        while hole > 0 and b[hole-1] > value:
            b[hole] = b[hole-1]
            hole -= 1
        b[hole] = value
        print ' '.join(str(x) for x in b)


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        b = map(int, raw_input().strip().split(" "))
        insertion_sort(b)

if __name__ == '__main__':
    main()
