__author__ = 'sriram'


def str_to_int(s):
    ctr = i = 0
    negative = False

    if s[0] == "-":
        negative = True
        s = s.replace("-", "")

    for c in reversed(s):
        i += (ord(c) - 48) * (10 ** ctr)
        ctr += 1

    val = -1 * i if negative else i

    return val


if __name__ == '__main__':
    num = raw_input("Enter the string to convert into number: ")
    print str_to_int(num)