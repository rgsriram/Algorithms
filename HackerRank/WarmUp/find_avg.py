def find_avg(arr):
	c = 0
	i = 0
	l = len(arr) - 1
	sub_arrays = []

	while c <= (l/2):

		if l % 2 == 0 and i == round(l/2.0):
			sub_arrays[0].append(arr[i])

		else:
			sub_arrays.append([arr[i], arr[l-i]])
	
		c += 1
		i += 1

	avgs = []

	for e in sub_arrays:
		avgs.append(sum(e)/len(e))

	flag = True

	for i in range(0, len(avgs)-1):
		if avgs[i] != avgs[i+1]:
			flag = False

	return (flag, sub_arrays)

print find_avg(sorted([5,2,1,3]))