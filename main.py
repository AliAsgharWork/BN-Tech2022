import numpy as np


class PathFinder:

    key = {
        "Empty": 0,
        "Start": 1,
        "End": 2,
        "Obstacles": 3
    }

    def __init__(self, grid_n):
        self.grid_n = grid_n
        # self.key = {
        #     "Empty": 0,
        #     "Start": 1,
        #     "End": 2,
        #     "Obstacles": 3
        # }

    def create_map(self):

        n = self.grid_n
        surface = np.zeros((n, n))
        print(surface, '\n')

        surface[0][0] = self.key["Start"]
        surface[9][9] = self.key["End"]
        surface[7][9] = self.key["Obstacles"]
        surface[7][8] = self.key["Obstacles"]
        surface[7][7] = self.key["Obstacles"]
        surface[8][7] = self.key["Obstacles"]

        print(surface)


# Execution
pf = PathFinder(10)
pf.create_map()
