import sys

R = 12
C = 10

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

min_dist = sys.maxsize


def isSafe(mat, visited, x, y):

    if (mat[x][y] == 0 or visited[x][y]):
        return False

    return True


def isValid(x, y):

    if (x < R and y < C and x >= 0 and y >= 0):
        return True

    return False


def markUnsafeCells(mat):

    for i in range(R):
        for j in range(C):
            if (mat[i][j] == 0):
                for k in range(4):
                    if (isValid(i + rowNum[k], j + colNum[k])):
                        mat[i + rowNum[k]][j + colNum[k]] = -1

    for i in range(R):
        for j in range(C):
            if (mat[i][j] == -1):
                mat[i][j] = 0


def findShortestPathUtil(mat, visited, i, j, dist):

    global min_dist

    if (j == C - 1):
        min_dist = min(dist, min_dist)
        return

    if (dist > min_dist):
        return

    visited[i][j] = True

    for k in range(4):
        if (isValid(i + rowNum[k], j + colNum[k]) and isSafe(mat, visited, i + rowNum[k], j + colNum[k])):
            findShortestPathUtil(
                mat, visited, i + rowNum[k], j + colNum[k], dist + 1)

    visited[i][j] = False


def findShortestPath(mat):

    global min_dist

    min_dist = sys.maxsize

    visited = [[False for i in range(C)] for j in range(R)]

    markUnsafeCells(mat)

    for i in range(R):
        if (mat[i][0] == 1):

            findShortestPathUtil(mat, visited, i, 0, 0)

            if (min_dist == C - 1):
                break

    if (min_dist != sys.maxsize):
        print("Length of shortest safe route is", min_dist)
    else:
        print("Destination not reachable from given source")


mat = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

findShortestPath(mat)
