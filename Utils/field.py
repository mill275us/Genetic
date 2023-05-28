import numpy as np

class Field:
    def __init__(self, grid_size: int, starting_food: int) -> None:
        self.grid_size = grid_size 
        self.food = starting_food

        # TAdd 1 to correct for zero base
        self.field = np.zeros((self.grid_size+1, self.grid_size+1), dtype=int)
        self.addFood(starting_food)

    def consumeFoodAt(self, x, y):
        self.field[x][y] = 0

    def addFood(self, amount_to_add):
        for i in range (amount_to_add):
            x = np.random.randint(self.grid_size + 1)
            y = np.random.randint(self.grid_size + 1)
            if self.field[x][y] == 0:
                self.field[x][y] = 1
            else:
                i -= 1

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
