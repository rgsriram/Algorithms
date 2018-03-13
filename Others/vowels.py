"""
Reverse vowles
a e i o u
"""


def is_vowel(c):
    return c in ('a', 'e', 'i', 'o', 'u')


def reverse_vowles(str):

    str = list(str)
    i = 0
    j = len(str) - 1

    # apple -> eppla

    while i < j:

        i_is_vowel = is_vowel(str[i])
        j_is_vowel = is_vowel(str[j])

        if i_is_vowel and j_is_vowel:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1

        elif i_is_vowel:
            j -= 1

        elif j_is_vowel:
            i += 1

        else:
            i += 1
            j -= 1

    return ''.join(str)

print reverse_vowles('sriram')
print reverse_vowles('apple')
print reverse_vowles('sriramganesh')
print reverse_vowles('chandersekar')
print reverse_vowles('peeruiavi')