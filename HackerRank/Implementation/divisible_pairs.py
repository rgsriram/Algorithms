def divisible_sum_pairs(n, k, ar):
    nums = [0] * k
    count = 0

    for each in ar:
        m = each % k
        count += nums[(k-m) % k]
        nums[m] += 1

    return count

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisible_sum_pairs(n, k, ar)
print(result)
