import numpy as np

class Field:
    def __init__(self, grid_size: int, starting_food: int) -> None:
        self.grid_size = grid_size 
        self.food = starting_food
        self.cell_count = (grid_size + 1) ** 2

        # TAdd 1 to correct for zero base
        self.field = np.zeros((self.grid_size+1, self.grid_size+1), dtype=int)
        self.addFood(starting_food)

    def consumeFoodAt(self, x, y, message=""):
        self.field[x][y] = 0
        print(message + "     >> Food at {}, {} eaten".format(x, y))

    def addFood(self, amount_to_add):
        if (self.field.sum() + amount_to_add) > self.cell_count:
            amount_to_add = 0
        i = 0
        while i < amount_to_add:
            x = np.random.randint(self.grid_size + 1)
            y = np.random.randint(self.grid_size + 1)
            if self.field[x][y] == 0:
                self.field[x][y] = 1
                i += 1

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
