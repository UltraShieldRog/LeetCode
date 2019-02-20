import copy
class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        time = 0
        while True:
            grid_prev = copy.deepcopy(grid)
            for line_index in range(len(grid)):
                for box_index in range(len(grid[line_index])):
                    if grid_prev[line_index][box_index] == 2:
                        if box_index+1 < len(grid[line_index]):
                            if grid_prev[line_index][box_index+1] == 1: 
                                grid[line_index][box_index+1] = 2 
                        if box_index-1 >= 0:
                            if grid_prev[line_index][box_index-1] == 1: 
                                grid[line_index][box_index-1] = 2 
                        if line_index+1 < len(grid):
                            if grid_prev[line_index+1][box_index] == 1: 
                                grid[line_index+1][box_index] = 2 
                        if line_index-1 >= 0:
                            if grid_prev[line_index-1][box_index] == 1: 
                                grid[line_index-1][box_index] = 2 
            if grid_prev == grid:
                break
            time += 1
        for lines in grid:
            if 1 in lines:
                return -1
        else:
            return time
