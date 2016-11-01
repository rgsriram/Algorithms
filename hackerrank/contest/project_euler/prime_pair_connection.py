__author__ = 'sriram'


def get_prime_numbers(p1, p2):
    primes = []
    for num in range(p1, p2):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def find_next_prime(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p


def find_prime_connection(primes):
    sum = 0
    for i in range(1, len(primes)):
        primes[i-1], primes[i]


def prime_pair_connection(p1, p2):
    primes = get_prime_numbers(p1, p2)
    primes.append(find_next_prime(primes[len(primes)-1]+1, 2*(primes[len(primes)-1]+1)))
    find_prime_connection(primes)


if __name__ == '__main__':
    n = int(raw_input().strip())
    (p1, p2) = map(int, raw_input().strip().split())
    prime_pair_connection(p1, p2)