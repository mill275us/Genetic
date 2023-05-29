import pygame
import copy
from operator import attrgetter
from Utils.bot import Bot
from Utils.field import Field
from Utils.botColor import PyBotColorer
from Utils.botIndexing import BotTracker
from PygameUtils.statusDisplay import StatusDisplay

# Main Program
# USER DEFINED
grid = 19   # To define say a 10 x 10 grid uses a zero base so use 9
number_of_starting_bots = 3
starting_food_pct = .5
percent_new_food_per_turn = .05
frames_per_second = 30

# Initial vars setup based on above user input
food_density = int(starting_food_pct * grid ** 2)
food_spawn_per_turn = int(percent_new_food_per_turn * grid ** 2)
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
if frames_per_second > 1:
    display_modulus = int(frames_per_second / 2)
else:
    display_modulus = 1
pygame.init()
clock = pygame.time.Clock()
cycle_coounter = 1
window = pygame.display.set_mode([screen_size + 200, screen_size])
window.fill((0, 0, 0))

# Create a status block including strings for displayyt66gty5ggggggggggggggggggggggggggggggg
statusBlock = StatusDisplay(window, screen_size + 10, 50)
disp_cycle_counter = str(cycle_coounter)
disp_num_of_bots = str(number_of_starting_bots)
disp_oldest_bug = str(cycle_coounter)

pygame.display.update()

# Simulate several evolutions of the field
running = True
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
            print("  -- Bug {} is reproducing".format(bot.id))
            energy = int(bot.energy / 2)
            bot.energy = energy
            bot.readyToReproduce = False

            new_bot = copy.deepcopy(bot)
            new_bot.id = botTracker.getId()
            new_bot.parent_id = bot.id
            new_bot.field = field
            new_bot.age = 0
            print("  -- Spawn of {} is Bug {}".format(bot.id, new_bot.id))
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
                ypos = int(y * cell_size + cell_cntr_offset) 
                pygame.draw.circle(window, (0, 255, 0), [xpos, ypos], 8, 0)

    # Display board - limit updates so there are visible at high FPS
    if (cycle_coounter % display_modulus) == 0:
        oldest_bug = max(bots, key = attrgetter("age"))
        disp_cycle_counter = str(cycle_coounter)
        disp_num_of_bots = str(len(bots))
        disp_oldest_bug = "Bug {} at Age {}".format(oldest_bug.id, oldest_bug.age)
    statusBlock.ypos = 50
    statusBlock.updateStatus((0,0,255), "Current Cycle", disp_cycle_counter)
    statusBlock.updateStatus((0,0,255), "Bug Count", disp_num_of_bots)
    statusBlock.updateStatus((0,0,255), "Oldest Bug", disp_oldest_bug)
    pygame.display.update()
    print("-> Food at end of turn {}\n".format(field.field.sum()))
    clock.tick(frames_per_second)
    cycle_coounter += 1


