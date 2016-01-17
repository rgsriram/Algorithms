"""
Problem from: HackerRank
Domain: Algorithms
Name: Sherlock and Beast
"""


# def get_multiples(number):
#     for mul in xrange(number / 3, -1, -1):
#         diff = number - mul * 3
#         if not diff % 5:
#             return "%s%s" % (mul * 3, diff)

#     return -1

def get_multiples(number):
    ans = ''
    for num in xrange(number, -1, -1):
        if (num % 3 == 0) and ((number - num) % 5 == 0):
            for i in xrange(0, num):
                ans = "%s%s" % (ans, str(5))
            for j in xrange(0, (number - num)):
                ans = "%s%s" % (ans, str(3))
            break
    if ans is '':
        return -1
    return ans


def get_decent_number(number):
    three = str(3)
    if number < 3:
        return -1
    elif number == 5:
        return three * 5

    return get_multiples(number)


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print get_decent_number(n)

if __name__ == '__main__':
    main()
