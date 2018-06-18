def find_smallest_subarray(arr, n):
    l = len(arr)

    start = end = current_sum = 0
    min_len = l + 1
    _range = []

    while end < l:

        while current_sum <= n and end < l:
            current_sum += arr[end]
            end += 1

        while current_sum > n and start < l:
            current_sum -= arr[start]

            if end - start < min_len:
                min_len = end - start
                _range = [start, end]

            start += 1

    for i in range(_range[0], _range[1]):
        print(arr[i], end)

    print



def smallestSubWithSum(arr, n, x):
    # Initialize current sum and minimum length
    curr_sum = 0
    min_len = n + 1
    _range = []

    # Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < n):

        # Keep adding array elements while current
        # sum is smaller than x
        while (curr_sum <= x and end < n):
            curr_sum += arr[end]
            end += 1

        # If current sum becomes greater than x.
        while (curr_sum > x and start < n):

            curr_sum -= arr[start]
            # Update minimum length if needed
            if end - start < min_len:
                min_len = end - start
                _range = [start, end]

                # remove starting elements
            start += 1

    for i in range(_range[0], _range[1]):
        print(arr[i])

    print



def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    find_smallest_subarray(arr, n)
    # smallestSubWithSum(arr, len(arr), n)
    # print(' '.join(map(str, )))


if __name__ == '__main__':
    main()