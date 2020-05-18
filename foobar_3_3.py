# find path through free pods using BFS
def find_free_path(start_x, start_y, maze):
    width = len(maze[0])
    height = len(maze)

    # matrix to store distance of each node
    board = [[None for _ in range(width)] for _ in range(height)]

    # set distance of start node as 1
    board[start_x][start_y] = 1

    # array to keep track of nodes to be explored
    path = [(start_x, start_y)]

    # adjacent nodes of current node can be found by adding current node (x, y)
    # with values in this array to get neigbhouring nodes
    adjacents = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while path:
        x, y = path.pop(0)
        for adjacent in adjacents:

            # calculate the nigbhouring node from current node
            new_x, new_y = x + adjacent[0], y + adjacent[1]

            # add the new node to the path only if its in the limit of the board
            if (0 <= new_x <= height-1) and (0 <= new_y <= width-1):

                # update the distance value of node if its not visited
                if board[new_x][new_y] is None:

                    # distance of new node is calculated by adding one to the previous nodes distance
                    board[new_x][new_y] = board[x][y] + 1

                    # add new node to the path only if its a free pod
                    if maze[new_x][new_y] != 1:
                        path.append((new_x, new_y))

    # returns board of distances of each node
    return board

def solution(maze):
    width = len(maze[0])
    height = len(maze)

    # get the distance of each node from start to end
    path_from_start_end = find_free_path(0, 0, maze)

    # get the distance of each node from end to start
    path_from_end_start = find_free_path(height-1, width-1, maze)

    # set current min_dist to a high value
    min_dist = 2 ** 32

    # loop through the board to find the total distance
    for i in range(height):
        for j in range(width):

            # get total distance if the node in the board is not None
            if path_from_start_end[i][j] and path_from_end_start[i][j]:

                # update min_dist with latest minimum total distance from start to end
                min_dist = min(path_from_start_end[i][j] + path_from_end_start[i][j] - 1, min_dist)

    return min_dist

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]]))
