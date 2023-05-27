import numpy as np

class Field:
    def __init__(self, grid_size: int, starting_food: int) -> None:
        self.grid_size = grid_size 
        self.food = starting_food

        # TAdd 1 to correct for zero base
        self.field = np.zeros((self.grid_size+1, self.grid_size+1), dtype=int)

        for i in range (starting_food):
            x = int(round(self.grid_size * float(np.random.rand(1)), 0))
            y = int(round(self.grid_size * float(np.random.rand(1)), 0))
            if self.field[x][y] == 0:
                self.field[x][y] = 1
            else:
                i -= 1

    def consumeFoodAt(self, x, y):
        self.field[x][y] = 0

    def printStatus(self):
        rows, cols = self.field.shape
        for row in range(rows):
            a = ''
            for col in range(cols):
                if self.field[row][col] == 0:
                    b= ' '
                else:
                    b = str(self.field[row][col]) 
                a = a + b + ' '
            print(a)
