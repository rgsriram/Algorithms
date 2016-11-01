__author__ = 'sriram'


def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


def find_trialing_zeroes(n):
    sum = factorial(n)
    count = 0
    while sum/10 > 0:
        if sum % 10 == 0:
            count += 1
        else:
            break
        sum /= 10
    return count

if __name__ == '__main__':
    n = int(raw_input())
    print find_trialing_zeroes(n)