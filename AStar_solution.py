
# Got A star code from :https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
from genericpath import exists
import numpy
import random


class Node():  # Part of section 1
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (9, 9)

    path = astar(maze, start, end)
    print(path)

    def randomObs(maze, start, end, nn):  # Part of Section 2
        # This function generates a random points of obstacles in the map that is feed in
        numofrando = nn
        maze_array = numpy.array(maze)
        maze_shape = maze_array.shape
        rando_list = []
        # Find existing obstacles
        exists_cood = []
        result = numpy.where(maze_array == 1)
        listOfCoordinates = list(zip(result[0], result[1]))
        for cord in listOfCoordinates:
            exists_cood.append(cord)

        while nn > 0:

            x = maze_shape[0]
            y = maze_shape[1]

            x_random = random.randint(0, x-1)
            y_random = random.randint(0, y-1)
            random_cood = (x_random, y_random)
            # print(random_cood)

            if random_cood == start:
                pass
            elif random_cood == end:
                pass
            else:
                # print([True for x1 in rando_list if x1 == random_cood])

                val = [True for x1 in rando_list if x1 == random_cood]
                val2 = [True for x1 in rando_list if x1 == exists_cood]

                if val != [True] and val2 != [True]:
                    rando_list.append(random_cood)
                    nn = nn-1
            # print(rando_list, len(rando_list))

        # print(numofrando - len(rando_list))
        # if numofrando - len(rando_list) != 0:
        #     print("not eno")

        for i in rando_list:
            maze[i[0]][i[1]] = 1

        return maze

    inf = float('inf')

    new_maze = randomObs(maze, start, end, 20)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in new_maze]))
    # print(new_maze)

    path = astar(new_maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
