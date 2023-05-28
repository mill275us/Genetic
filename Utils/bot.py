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
        self.id = -1
        self.parent_id = -1

        # Create a random probability array for movement
        a = np.random.rand(1, 8)
        a1 = a / a.sum()
        self.probability_array = a1.tolist()[0]

        # Create a random starting location
        self.x = np.random.randint(self.grid_size + 1)
        self.y = np.random.randint(self.grid_size + 1)
        self.direction = 0

    def move(self):
        from_x = self.x
        from_y = self.y
        self.direction = int(np.random.choice(np.arange(8), 1, p = self.probability_array))
        offset = self.xy_offset()
        self.x = (self.x + offset[0]) % (self.grid_size + 1)
        self.y = (self.y +  offset[1]) % (self.grid_size + 1)
        self.energy -= self.energy_decrement
        print("  {} Moving from ({}, {}) to ({}, {}) with Energy Remain={}".format(self.id, from_x, from_y, self.x, self.y, self.energy))
              
        if self.energy < 0:
            self.isAlive = False

    def xy_offset(self):
        dir = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        return dir[self.direction]
    
    def eat(self):
        if self.field.field[self.x][self.y] == 1:
            self.energy += self.food_energy
            msg = "  -- Bug {} is eating at ({}, {})".format(self.id, self.x, self.y)
            self.field.consumeFoodAt(self.x, self.y, msg)
            if self.energy >= self.mitosis_level:
                self.readyToReproduce = True

    def mutate(self):
        # Create new random weight shifts
        print("  ---- Bug {} is mutating".format(self.id))
        nw = [(np.random.rand(1) - 0.5) * self.mutation_level for i in range(8)]
        curr_p = np.array(self.probability_array)
        new_weights = np.array(nw).flatten()
        a = np.add(curr_p, new_weights)
        a[a < 0] = 0.0
        a1 = a / a.sum()
        self.probability_array = a1.tolist()
    