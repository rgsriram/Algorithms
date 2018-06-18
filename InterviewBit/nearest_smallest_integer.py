def nearest_smallest_integer(A):
    n = len(A)
    res = [-1] * n
    st = [A[0]]

    for i in range(1, n):
        temp = []
        found = False

        while len(st) > 0:
            x = st.pop()

            if x < A[i]:
                temp.extend([A[i], x])
                found = True
                break

            temp.append(x)

        if found:
            res[i] = A[i]
        temp = [A[i]] + temp

    return res


A = [4, 5, 2, 10, 8]
A = [3, 2, 1]
A = [34, 35, 27, 42, 5, 28, 39, 20, 28 ]
print nearest_smallest_integer(A)