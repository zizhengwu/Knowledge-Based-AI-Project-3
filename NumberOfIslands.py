import queue

class Islands(object):
    def __init__(self):
        self.directions = list(zip([-1, -1, -1, 0, 0, 1, 1, 1], [1, -1, 0, 1, -1, 0, 1, -1]))
        self.grid = None
        self.visited = None

    def get_number_of_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # s = [[str(e) for e in row] for row in grid]
        # lens = [max(map(len, col)) for col in zip(*s)]
        # fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        # table = [fmt.format(*row) for row in s]
        # print('\n'.join(table))
        number_of_islands = 0
        self.grid = grid
        if not grid:
            return 0
        row_length = len(grid)
        column_length = len(grid[0])
        self.visited = [[False for i in range(column_length)] for j in range(row_length)]
        for row in range(row_length):
            for column in range(column_length):
                if self.visited[row][column] == False and int(grid[row][column]) == 0:
                    number_of_islands += 1
                    self.depth_first_search(row, column)
        return number_of_islands

    def depth_first_search(self, row, column):
        self.visited[row][column] = True
        q = queue.Queue()
        q.put((row, column))
        while not q.empty():
            item = q.get()
            row = item[0]
            column = item[1]
            for direction in self.directions:
                try:
                    if self.valid_index(row, column, direction[0], direction[1]) and int(self.grid[row + direction[0]][column + direction[1]]) == 0 and self.visited[row + direction[0]][column + direction[1]] == False:
                        item = (row + direction[0], column + direction[1])
                        self.visited[row + direction[0]][column + direction[1]] = True
                        q.put(item)
                except Exception as e:
                    pass

    def valid_index(self, row, column, direction_x, direction_y):
        return row + direction_x >= 0 and column + direction_y >= 0