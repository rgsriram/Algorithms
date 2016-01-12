'''
Problem from: HackerRank
Domain: Algorithms
Name: Staircase
'''

import sys

def stair_case(n):
	for iindex in range(1, n):
		for jindex in range(1, n-iindex):
			sys.stdout.write(' ')
		for kindex in range(0, iindex):
			sys.stdout.write('#')
		sys.stdout.write('\n')

if __name__ == '__main__':
	num = int(raw_input().strip()) + 1
	stair_case(num)

