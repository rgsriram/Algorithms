'''
Problem from: HackerRank
Domain: Algorithms
Name: Diagonal Difference
'''

# import numpy as np

# def diagonal_difference(matrix):
# 	return abs(matrix[::1].trace() - matrix[::-1].trace())

def diagonal_difference(a):
	length = len(a)
	d1_sum = sum(a[i][i] for i in xrange(0, length))
	d2_sum = sum(a[length-1-i][i] for i in xrange(0, length))
	return abs(d1_sum - d2_sum)

if __name__ == '__main__':
	n = int(raw_input().strip())
	a = []
	for a_i in xrange(n):
	   a_temp = map(int,raw_input().strip().split(' '))
	   a.append(a_temp)
	# matrix = np.array(a)
	print diagonal_difference(a)