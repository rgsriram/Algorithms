__author__ = 'sriram'


def find_n(a, b, n):
    c = n - 2
    sum = 0

    while c > 0:
        sum = a + b ** 2
        a = b
        b = sum
        c -= 1
    return sum


def main():
    (a, b, n) = map(int, raw_input().strip().split(" "))
    print find_n(a, b, n)

if __name__ == '__main__':
    main()