import pygame
import copy
from Utils.bot import Bot
from Utils.field import Field
from Utils.botColor import PyBotColorer

class BotTracker:
    def __init__(self) -> None:
        self.next_id = 0

    def getId(self):
        self.next_id += 1
        return self.next_id

# Main Program
# To define say a 10 x 10 grid
# Uses a zero base
grid = 19
number_of_starting_bots = 3
food_density = int(.5 * grid ** 2)
food_spawn_per_turn = int(.10 * grid ** 2)
field = Field(grid, food_density)
bots = []

# Create starting field of bots
botTracker = BotTracker()
botColorer = PyBotColorer(number_of_starting_bots)
for i in range(number_of_starting_bots):
    ###bots.append(Bot(field, botColorer.pyColorForBot()))
    newBot = Bot(field, (255,0,0))
    newBot.id = botTracker.getId()
    bots.append(newBot)

# Setup Pygame for display
screen_size = 500
cell_size = int(screen_size / (grid + 1))
cell_count = int(screen_size / cell_size)
cell_cntr_offset = int(cell_size / 2)

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode([screen_size, screen_size])
window.fill((0, 0, 0))
pygame.display.update()

# Simulate several evolutions of the field
running = True
cycle_coounter = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen`
    window.fill((0, 0, 0))
    print("Cycle {} ---> Number of bugs: {}".format(cycle_coounter, len(bots)))

    # Add new food
    field.addFood(food_spawn_per_turn)

    for bot in bots:        
        bot.move()
        bot.eat()

        # Remove dead bots
        if not bot.isAlive:
            bots.remove(bot)
            if len(bots) == 0:
                running = False

        # Check for reproduction
        if bot.readyToReproduce:         
            print("-- Bug {} is reproducing".format(bot.id))
            energy = int(bot.energy / 2)
            bot.energy = energy
            bot.readyToReproduce = False

            new_bot = copy.deepcopy(bot)
            new_bot.id = botTracker.getId()
            new_bot.parent_id = bot.id
            print("-- Spawn of {} is Bug {}".format(bot.id, new_bot.id))
            new_bot.mutate()
            bots.append(new_bot)        
        
        # Draw each bug        
        rect = pygame.Rect(bot.x * cell_size , bot.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, bot.color, rect, 2)

    # Disply Food on field
    for x in range(0, cell_count):
        for y in range(0, cell_count):
            if field.field[x][y] == 1:
                xpos = int(x * cell_size + cell_cntr_offset) 
                ypos = int(y * cell_size+ cell_cntr_offset) 
                pygame.draw.circle(window, (0, 255, 0), [xpos, ypos], 8, 0)

    # Display board
    pygame.display.update()
    clock.tick(1)
    cycle_coounter += 1


