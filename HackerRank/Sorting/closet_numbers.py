def closet_number(arr):
    sorted_arr = sorted(arr)
    pairs = dict()

    for i in range(1, len(sorted_arr)):
    	diff = sorted_arr[i] - sorted_arr[i-1]

    	if diff not in pairs:
    		pairs[diff] = []

    	pairs[diff].append((sorted_arr[i-1], sorted_arr[i]))

    _min = min(pairs.keys())
    return pairs[_min]

def main():
    t = int(raw_input().strip())
    b = map(int, raw_input().strip().split(" "))

    results = []
    for pair in closet_number(b):
    	results.append(pair[0])
    	results.append(pair[1])

    print ' '.join(map(str, results))


main()