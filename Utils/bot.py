import numpy as np

class Bot:
    def __init__(self, field: object, color) -> None:
        # Grid size is zero indexed square field
        self.field = field
        self.grid_size = field.grid_size
        self.energy = 250
        self.energy_decrement = 50
        self.food_energy = 150
        self.mitosis_level = 500
        self.mutation_level = 0.05
        self.isAlive = True
        self.readyToReproduce = False
        self.color = color

        # Create a random probability array
        # For movement
        a = np.random.rand(1, 8)
        self.probability_array  = a / a.sum()

        # Create a random starting location
        self.x = int(round(self.grid_size * float(np.random.rand(1)), 0))
        self.y = int(round(self.grid_size * float(np.random.rand(1)), 0))
        self.direction = 0
        self.field.field[self.x][self.y] = 9

    def move(self):
        self.field.field[self.x][self.y] = 0

        #### Note this is just moving in a random direction!
        ### It is not using the probability that I created above
        self.direction = int(round(7 * float(np.random.rand(1)), 0))
        offset = self.xy_offset()
        
        ### Ok to remove this
        if self.direction == 7:
            print("7", offset)

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
            if self.energy >= self.mitosis_level:
                self.readyToReproduce = True

    def mutate(self):
        # Create new random weight shifts
        nw = [round(float((np.random.rand(1) - 0.5) * self.mutation_level), 3) for i in range(7)]
    
    def printStatus(self):
        print("Moving direction {} into cell ({}, {}) --> Energy = {}".format(self.direction, self.x, self.y, self.energy))
