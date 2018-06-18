import sys

S = "AAAAAAA"
T = "AA"


def window(s, t):

    i = 0
    chars = []
    _index = []
    _min_index = sys.maxint
    _window = []
    temp = list(t)

    while i < len(s):

        if s[i] in temp and s[i] not in chars:
            chars.append(s[i])
            _index.append(i)
            temp.remove(s[i])

        if len(chars) == len(t):
            temp = list(t)
            chars = []
            window_size = min((_index[-1] - _index[0]), _min_index)

            if _min_index > window_size:
                _window = _index
                _min_index = window_size

            _index = []

        i += 1

    ans = ''

    print _window

    if _window:
        for i in range(_window[0], _window[-1]+1):
            ans += s[i]

        return ans

print window(S, T)
