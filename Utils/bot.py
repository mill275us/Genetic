import numpy as np

class Bot:
    def __init__(self, field: object, color) -> None:
        # Grid size is zero indexed square field
        self.field = field
        self.grid_size = field.grid_size
        self.energy = 250
        self.energy_decrement = 50
        self.food_energy = 100
        self.isAlive = True
        self.color = color

        # Create a random probability array
        # For movement
        a = np.random.rand(1, 7)
        self.probability_array  = a / a.sum()

        # Create a random starting location
        self.x = int(round(self.grid_size * float(np.random.rand(1)), 0))
        self.y = int(round(self.grid_size * float(np.random.rand(1)), 0))
        self.direction = 0
        self.field.field[self.x][self.y] = 9

    def move(self):
        self.field.field[self.x][self.y] = 0
        self.direction = int(round(7 * float(np.random.rand(1)), 0))
        offset = self.xy_offset()
        self.x = (self.x + offset[0]) % (self.grid_size + 1)
        self.y = (self.y +  offset[1]) % (self.grid_size + 1)
        self.energy -= self.energy_decrement
        
        if self.energy < 0:
            self.isAlive = False

    def xy_offset(self):
        dir = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        return dir[self.direction]
    
    def eat(self):
        if self.field.field[self.x][self.y] == 1:
            self.energy += self.food_energy
            self.field.consumeFoodAt(self.x, self.y)
    
    def printStatus(self):
        print("Moving direction {} into cell ({}, {}) --> Energy = {}".format(self.direction, self.x, self.y, self.energy))
