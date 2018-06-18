def minimumTotal(A):
    n = len(A)
    minimums = A[n - 1]
    print minimums

    for row in reversed(xrange(n - 1)):
        for col, value in enumerate(A[row]):
            print row, col, col + 1, min(minimums[col], minimums[col + 1]) + value
            minimums[col] = min(minimums[col], minimums[col + 1]) + value
            print minimums[col]

    return minimums[0]


print minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])