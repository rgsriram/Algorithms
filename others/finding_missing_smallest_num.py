'''
Q1. Find the smallest missing number
Given a sorted array of n integers where each integer is in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.

Examples
Input: {0, 1, 2, 6, 9}, n = 5, m = 10
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
Output: 0
'''

def find_missing_number(a):
	for i in range(0, len(a)):
		if a[i] != i:
			return i


if __name__ == '__main__':
	print find_missing_number()