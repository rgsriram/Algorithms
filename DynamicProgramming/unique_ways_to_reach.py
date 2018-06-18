def ways_to_reach_cell(mat):
    count = 0
    i = 0
    j = 0

    while i < len(mat):

        while j < len(mat[i]):

            if mat[i+1][j] == 1:
                j = 1

            j += 1
