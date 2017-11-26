__author__ = 'sriram'


def insertion_sort(b):
    swap = 0

    for i in range(1, len(b)):
        value = b[i]
        hole = i
        while hole > 0 and b[hole-1] > value:
            b[hole] = b[hole-1]
            hole -= 1
            swap += 1
        b[hole] = value
    
    return swap


def main():
    t = int(raw_input().strip())
    b = map(int, raw_input().strip().split(" "))
    print insertion_sort(b)

if __name__ == '__main__':
    main()
