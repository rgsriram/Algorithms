
def max_sum(arr):
    max_so_far = 0
    max_ending_here = 0

    for each in arr:
        max_ending_here += each
        max_so_far = max(max_ending_here, max_so_far)
        max_ending_here = max(max_ending_here, 0)

    return max_so_far

print max_sum([-2, -3, 4, -1, -2, 1, 5, -3])