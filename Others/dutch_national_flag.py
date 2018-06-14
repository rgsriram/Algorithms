def dutch_national_flag(arr):
    low = 0
    high = len(arr) - 1

    pointer = 0

    while pointer <= high:

        if arr[pointer] == 0:
            arr[pointer], arr[low] = arr[low], arr[pointer]
            low += 1
            pointer += 1

        elif arr[pointer] == 1:
            pointer += 1

        else:
            arr[high], arr[pointer] = arr[pointer], arr[high]
            high -= 1

    print arr


dutch_national_flag([0,0,1,0,1,2,0,2,1])
