

class Solution(object):

    def __init__(self):
        self.modified_indexes = [0] * 300000

    def _setZerosRow(self, mat, j, n):

        for k in range(n):

            if mat[k][j] != 0:
                self.modified_indexes[int('%s%s' % (k, j))] = 1
                mat[k][j] = 0

        return mat

    def _setZerosCol(self, mat, i, m):

        for k in range(m):

            if mat[i][k] != 0:
                self.modified_indexes[int('%s%s' % (i, k))] = 1

                mat[i][k] = 0

        return mat

    def setZeroes(self, mat, n, m):
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0 and self.modified_indexes[int("%s%s" % (i, j))] != 1:
                    mat = self._setZerosRow(mat, j, n)
                    mat = self._setZerosCol(mat, i, m)

        return mat

mat = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1]
]
n = len(mat)
m = len(mat[0])

print Solution().setZeroes(mat, n, m)
