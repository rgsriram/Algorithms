def min_cost(arr):

    n = len(arr)
    m = len(arr[0])

    temp = [[0 for _ in range(m)] for _ in range(n)]
    sum = 0

    for i in range(m):
        temp[0][i] = sum + arr[0][i]
        sum = temp[0][i]

    sum = 0

    for i in range(n):
        temp[i][0] = sum + arr[i][0]
        sum = temp[i][0]

    for i in range(1, n):
        for j in range(1, m):
            temp[i][j] = arr[i][j] + min(arr[i][j-1], arr[i-1][j])

    print a
    print temp
    return temp[n-1][m-1]

# a = [
#     [1, 2, 1],
#     [2, 3, 4],
#     [1, 4, 3],
#     [4, 3, 2],
#     [1, 3, 10]
# ]

a  = [
  [1, 2, 1],
  [2, 3, 2],
  [3, 4, 4],
  [1, 4, 3]
]

print min_cost(a)