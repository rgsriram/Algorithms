class Element(object):
    def __init__(self, i, j, current_time=0):
        self.i = i
        self.j = j
        self.current_time = current_time


def is_valid(i, j):
    return 0 <= i < R and 0 <= j < C


def minimum_rotten_time(mat):
    queue = []

    for i in range(R):
        for j in range(C):
            if mat[i][j] == 2:
                queue.append(Element(i, j))

    current_time = 0
    while len(queue) > 0:
        element = queue.pop(0)
        current_time = element.current_time

        if is_valid(element.i+1, element.j) and mat[element.i+1][element.j] == FRESH:
            mat[element.i + 1][element.j] = ROTTEN
            queue.append(Element(element.i+1, element.j, current_time+1))

        if is_valid(element.i-1, element.j) and mat[element.i-1][element.j] == FRESH:
            mat[element.i - 1][element.j] = ROTTEN
            queue.append(Element(element.i-1, element.j, current_time+1))

        if is_valid(element.i, element.j+1) and mat[element.i][element.j+1] == FRESH:
            mat[element.i][element.j + 1] = ROTTEN
            queue.append(Element(element.i, element.j+1, current_time+1))

        if is_valid(element.i, element.j-1) and mat[element.i][element.j-1] == FRESH:
            mat[element.i][element.j - 1] = ROTTEN
            queue.append(Element(element.i, element.j-1, current_time+1))

    for i in range(R):
        for j in range(C):
            if mat[i][j] == 1:
                return -1

    return current_time

R = 3
C = 5

ROTTEN = 2
FRESH = 1
EMPTY = 0

mat = [
    [2, 1, 0, 2, 1],
    [1, 0, 1, 2, 1],
    [1, 0, 0, 2, 1],
]

print minimum_rotten_time(mat)