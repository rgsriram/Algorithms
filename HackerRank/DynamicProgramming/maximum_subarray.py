def find_contigouous_sum(a):
	_sum = a[0]
	current_max_sum = a[0]

	for i in range(1, len(a)):
		_sum = max(a[i], _sum + a[i])
		current_max_sum = max(_sum, current_max_sum)

	return current_max_sum

def find_non_contigouous_sum(a):
	sum_ = 0
	pos_arr = filter(lambda x: x>0, a)

	if len(pos_arr):
		sum_ = sum(pos_arr)
	else:
		sum_ = max(a)

	return sum_

def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
    	l = raw_input().strip().split(" ")
        b = map(int, raw_input().strip().split(" "))
        print "%s %s" % (find_contigouous_sum(b), find_non_contigouous_sum(b))

if __name__ == '__main__':
    main()
