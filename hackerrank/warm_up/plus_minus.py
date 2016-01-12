'''
Problem from: HackerRank
Domain: Algorithms
Name: Plus Minus
'''

def fraction(arr):
	positive = sum(x > 0 for x in arr)
	negative = sum(x < 0 for x in arr)
	zero = sum(x == 0 for x in arr)
	length = float(len(arr))
	print format(positive/length, '.6f')
	print format(negative/length, '.6f')	
	print format(zero/length, '.6f')

if __name__ == '__main__':
	n = int(raw_input().strip())
	if n > 0:
		fraction(map(int, raw_input().strip().split()))