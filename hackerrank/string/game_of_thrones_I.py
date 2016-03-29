__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Alternating Characters
"""


def is_palindrome(_dict, is_odd):
    values = [v for k, v in _dict.iteritems()]
    if is_odd:
        if values.count(1) > 1:
            return False
        else:

    else:
        if values.count(1) >= 1:
            return False
    return True


def is_found(string):
    is_odd = False if len(string) % 2 == 0 else True
    str_dict = {}
    for c in string:
        if c not in str_dict:
            str_dict[c] = 0
        str_dict[c] += 1
    print str_dict
    return is_palindrome(str_dict, is_odd)


def main():
    s = raw_input().strip()
    if is_found(s):
        print 'YES'
    else:
        print 'NO'

if __name__ == '__main__':
    main()
