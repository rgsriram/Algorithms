def element_appear_once(arr):
    new_arr = [None] * (max(arr) + 1)

    for i in range(len(arr)):
        if not new_arr[arr[i]]:
            new_arr[arr[i]] = -1

        else:
            new_arr[arr[i]] *= -1

    for i in range(len(new_arr)):

        if new_arr[i] == -1:
            print i


element_appear_once([1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8])
