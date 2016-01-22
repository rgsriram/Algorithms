__author__ = 'sriram'

"""
Problem from: HackerRank
Domain: Algorithms
Name: Caesar Cipher
"""


def encrypt(word, k):
    encrypt_word = ''

    for c in word:
        ascii_val = ord(c)
        if 65 <= ascii_val <= 90:
            encrypt_c = ascii_val + k
            encrypt_c = encrypt_c if encrypt_c <= 90 else 65 + (encrypt_c % 90) - 1
            encrypt_word += chr(encrypt_c)
        elif 97 <= ascii_val <= 122:
            encrypt_c = ascii_val + k
            encrypt_c = encrypt_c if encrypt_c <= 122 else 97 + (encrypt_c % 122) - 1
            encrypt_word += chr(encrypt_c)
        else:
            encrypt_word += c

    return encrypt_word


def get_key(k):
    while k >= 26:
        k = (26 + k) % 26
    return k


def main():
    n = int(raw_input().strip())
    s = raw_input().strip()
    k = int(raw_input().strip())
    k = get_key(k)
    print encrypt(s, k)

if __name__ == '__main__':
    main()
