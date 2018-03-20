def firstMissingInt(A):
    missing = -1
    _max = max(A) + 1

    if _max < 0:
        return 1

    else:
        a = [0] * _max

        for i in range(len(A)):
            a[A[i]] += 1

        for i in range(1, len(a)):

            if a[i] == 0:
                return i

            missing = i

        return missing + 1


A = [3,4,-1,1]
# A = [1,2,0]
# A = [-8, -7, -6]

print(firstMissingInt(A))

