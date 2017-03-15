# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))] for direction in range(len(forward))]
    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))] for direction in range(len(forward))]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for z in range(len(forward)):
                    if goal[0] == x and goal[1] == y:
                        if value[z][x][y] > 0:
                            value[z][x][y] = 0
                            policy[z][x][y] = '*'
                            change = True
                    elif grid[x][y] == 0:
                        for act_num in range(len(action)):
                            act = action[act_num]
                            new_orientation = (z + act) % len(forward)

                            x2 = x + (forward[new_orientation])[0]
                            y2 = y + (forward[new_orientation])[1]

                            if x2 > -1 and x2 < len(grid) and y2 > -1 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                # print x2, y2
                                new_cost = value[new_orientation][x2][y2] + cost[act_num]
                                if new_cost < value[z][x][y]:
                                    change = True
                                    value[z][x][y] = new_cost
                                    policy[z][x][y] = action_name[act_num]


    x = init[0]
    y = init[1]
    o = init[2]

    loop = True
    while loop:
        if x == goal[0] and y == goal[1]:
            policy2D[x][y] = '*'
            loop = False
        policy2D[x][y] = policy[o][x][y]
        if policy[o][x][y] == 'R':
            o2 = (o - 1) % len(forward)
        elif policy[o][x][y] == 'L':
            o2 = (o + 1) % len(forward)
        elif policy[o][x][y] == '#':
            o2 = o
        o = o2
        x = forward[o2][0] + x
        y = forward[o2][1] + y

    # for i in range(len(policy2D)):
    #     print policy2D[i]
    return policy2D
