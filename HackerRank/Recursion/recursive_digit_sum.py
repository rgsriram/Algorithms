def super_digit(n):
    _sum = 0

    while n > 10:
        r = n % 10
        n = n / 10
        _sum += r

    if _sum < 10:
        return n

    return super_digit(_sum)


def main():
    n, k = map(int, raw_input().strip().split(' '))
    print(super_digit(int(str(n) * k)))

if __name__ == '__main__':
    main()
