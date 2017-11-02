__author__ = 'sriram'

import ctypes


def flipping_bits(b):
    return ctypes.c_uint32(~b).value


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        b = int(raw_input().strip())
        print flipping_bits(b)

if __name__ == '__main__':
    main()