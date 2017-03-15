# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    path = []

    opened = [[g, x, y]]
    while(path == []):
        if len(opened) == 0:
            path = "fail"
            break
        a = opened.pop(0)

        a_x = a[1]
        a_y = a[2]
        a_g = a[0]
        grid[a_x][a_y] = 1

        for i in delta:
            tmp_x = a_x + i[0]
            tmp_y = a_y + i[1]
            if (tmp_x > -1 and tmp_x < len(grid) and tmp_y >-1 and tmp_y < len(grid[0])):
                if (grid[tmp_x][tmp_y] == 0):
                    tmp_g = a_g + cost
                    opened.append([tmp_g, tmp_x, tmp_y])
                    if(tmp_x == goal[0] and tmp_y == goal[1]):
                        path = [tmp_g, tmp_x, tmp_y]

    return path

print search(grid,init,goal,cost)
