# def findPivot(arr, element):
#
#

def profitSort(arr, l, r):
    count = 0

    for each in arr:
        if l <= each <= r:
            count += 1

    return count


def main():
    n = int(raw_input().strip())
    arr = list()

    for i in range(n):
        x = int(raw_input().strip())
        print x
        arr.append(x)

    q = int(raw_input().strip())

    for q0 in range(q):
        q_s = int(raw_input().strip())


if __name__ == '__main__':
    main()