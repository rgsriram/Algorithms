def replace_zero(number, num='5'):
    return int(str(number).replace('0', num))


def main():
    n = int(input().strip())
    print(replace_zero(n))

if __name__ == '__main__':
    main()