global _sum

_sum = 0


def combinational_helper(nums, res, end, index, group, i):

    if index == group:
        zxor = reduce(lambda a, b: a ^ b, res[0:group], 0)

        global _sum
        _sum += zxor

        return

    if i >= end:
        return

    res[index] = nums[i]

    combinational_helper(nums, res, end, index+1, group, i+1)
    combinational_helper(nums, res, end, index, group, i+1)


def combinational_sum(nums, group=3):
    res = [0] * len(nums)
    nums.sort()
    combinational_helper(nums, res, len(nums), 0, group, 0)

    return _sum % (10 ** 9 + 7)


def main():
    N = int(raw_input().strip())
    nums = map(int, raw_input().strip().split(' '))
    L, R = map(int, raw_input().strip().split(' '))
    L, R = map(int, raw_input().strip().split(' '))

    print(combinational_sum(nums))


main()