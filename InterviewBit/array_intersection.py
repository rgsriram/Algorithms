def intersect(A, B):
    n = len(A)
    m = len(B)

    iA = 0
    iB = 0
    common = []

    while iA < n and iB < m:

        if A[iA] < B[iB]:
            iA += 1

        elif B[iB] < A[iA]:
            iB += 1

        elif A[iA] == B[iB]:
            common.append(A[iA])
            iA += 1
            iB += 1

    return common


print intersect([1,2, 3, 3, 4, 5, 6], [3, 3, 5])