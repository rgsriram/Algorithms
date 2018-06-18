
def edit_distance(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    T = [0] * n

    for row in range(n):
        T[row] = [0] * m

    for j in range(0, m):
        T[0][j] = j

    for i in range(0, n):
        T[i][0] = i

    for i in range(1, n):
        for j in range(1, m):

            if str1[i-1] == str2[j-1]:
                T[i][j] = T[i-1][j-1]

            else:
                T[i][j] = min(T[i][j-1], T[i-1][j-1], T[i-1][j]) + 1

    return T[n-1][m-1]

# print edit_distance(list('sunday'), list('saturday'))
print edit_distance(list('geek'), list('gesek'))
# edit_distance(list('1234'), list('12345'))