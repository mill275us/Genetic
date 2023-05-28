import numpy as np

class Field:
    def __init__(self, grid_size: int, starting_food: int, verbose=False) -> None:
        self.grid_size = grid_size 
        self.food = starting_food
        self.verbose = verbose

        # TAdd 1 to correct for zero base
        self.field = np.zeros((self.grid_size+1, self.grid_size+1), dtype=int)
        self.addFood(starting_food)

    def consumeFoodAt(self, x, y):
        self.field[x][y] = 0
        print("  >> Food at {}, {} eaten".format(x, y))
        print("  >> Food remaining is {} for {}".format(self.field.sum(), self))

    def addFood(self, amount_to_add):
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
