'''
Problem from: HackerRank
Domain: Algorithms
Name: Simple Array Sum
'''

def array_sum(arr):
	return sum(arr)

if __name__ == '__main__':
	n = int(raw_input().strip())
	print array_sum(map(int, raw_input().strip().split()))