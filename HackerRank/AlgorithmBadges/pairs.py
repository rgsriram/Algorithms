__author__ = 'sriram'


def find_pairs(k, a):
    dict_pair = {e : a.count(e) for e in a}
    pairs = 0
    for el in a:
        x = el + k
        y = el - k
        # if dict_pair.get(x, -1) > 0 or dict_pair.get(y, -1) > 0:
        pairs += dict_pair.get(x, 0) + dict_pair.get(y, 0)
    return pairs/2


def main():
    (n, k) = map(int, raw_input().strip().split(" "))
    a = map(int, raw_input().strip().split(" "))
    print find_pairs(k, a)

if __name__ == '__main__':
    main()