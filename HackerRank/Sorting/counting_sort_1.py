
def count_sort(arr):
    count_array = [0] * (max(arr) + 1)

    for value in arr:
        count_array[value] += 1

    return count_array


def main():
    t = int(raw_input().strip())
    b = map(int, raw_input().strip().split(" "))
    print ' '.join(map(str, count_sort(b)))

main()