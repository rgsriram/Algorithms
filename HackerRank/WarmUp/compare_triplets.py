def _solve(arr):
	alice = 0
	bob = 0

	mid = len(arr)/2

	for i in range(0, mid):
		if arr[i] > arr[mid+i]:
			alice += 1

		elif arr[i] < arr[mid+i]:
			bob += 1


	return alice, bob


def solve(a0, a1, a2, b0, b1, b2):
	return _solve([a0, a1, a2, b0, b1, b2])



