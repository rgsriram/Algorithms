class Element(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j


def is_valid(i, j):
    return 0 <= i < R and 0 <= j < C


def find_no_of_islands(mat, n, m):
    visited = [[0 for j in range(m)] for i in range(n)]
    queue = []
    size = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                queue.append(Element(i, j))

    postions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1)
    ]

    while len(queue) > 0:
        element = queue.pop(0)

        if visited[element.i][element.j] == 0:
            size += 1

        for position in postions:
            next_i = position[0]
            next_j = position[1]

            if is_valid(element.i + next_i, element.j + next_j) and mat[element.i + next_i][element.j + next_j] == 1 and visited[element.i + next_i][element.j + next_j] == 0:
                queue.append(Element(element.i + next_i, element.j + next_j))
                visited[element.i + next_i][element.j + next_j] = 1

    return size

mat = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
R = 5
C = 5
visited = [[0 for j in range(R)] for i in range(C)]
print find_no_of_islands(mat, R, C)