def count_path_mat(m, n):

    res = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        res[i][0] = 1

    for j in range(m):
        res[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            res[i][j] = (res[i-1][j] + res[i][j-1]) % 10

    return res[n-1][m-1]


print count_path_mat(32, 32) ** 9 + 7