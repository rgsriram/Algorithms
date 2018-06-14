def rain_water_trapping(arr):
    n = len(arr)
    left_max = [0] * n
    right_max = [0] * n

    max_seen_left = 0
    left_max[0] = arr[0]

    for i in range(0, n):
        if max_seen_left < arr[i]:
            max_seen_left = left_max[i] = arr[i]

        else:
            left_max[i] = max_seen_left

    max_seen_right = 0
    for i in range(n-1, 0, -1):
        if max_seen_right < arr[i]:
            max_seen_right = right_max[i] = arr[i]

        else:
            right_max[i] = max_seen_right


    rain_water = 0
    for i in range(n):
        rain_water += max(min(left_max[i], right_max[i]) - arr[i], 0)

    return rain_water


def rain_water_trapping_2(arr):
    n = len(arr)
    right_max = [0] * n

    max_seen_left = 0

    max_seen_right = 0
    for i in range(n-1, 0, -1):
        if max_seen_right < arr[i]:
            max_seen_right = right_max[i] = arr[i]

        else:
            right_max[i] = max_seen_right

    rain_water = 0
    for i in range(n):
        rain_water += max(min(max_seen_left, right_max[i]) - arr[i], 0)

        if max_seen_left < arr[i]:
            max_seen_left = arr[i]

    return rain_water

arr = [3, 0, 0, 2, 0, 4]
arr = [2, 0, 2]
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print rain_water_trapping(arr)
print rain_water_trapping_2(arr)