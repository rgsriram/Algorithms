
def count_sort(arr):
    count_array = [0] * (max(arr) + 1)

    for value in arr:
        count_array[value] += 1

    for i in range(1, len(count_array)):
    	count_array[i] += count_array[i-1]

    sorted_array = [0] * (len(arr) + 1)

    for value in arr:
    	sorted_array[count_array[value]] = value
    	count_array[value] -= 1

    return sorted_array[1:]

def main():
    t = int(raw_input().strip())
    b = map(int, raw_input().strip().split(" "))
    print ' '.join(map(str, count_sort(b)))

main()

