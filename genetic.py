import pygame
from Utils.bot import Bot
from Utils.field import Field

# Main Program
# To define say a 10 x 10 grid
# Uses a zero base
grid = 9
food_density = 50
field = Field(grid, food_density)
bots = [Bot(field, (225, 225, 0)), Bot(field, (225, 0, 0))]

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    for bot in bots:        
        bot.move()
        bot.eat()
        bot.printStatus()     

        # Remove dead bots
        if not bot.isAlive:
            bots.remove(bot)
            if len(bots) == 0:
                running = False

        # Check for reproduction
        if bot.readyToReproduce:
            energy = int(bot.energy / 2)
            bot.energy = energy
            bot.readyToReproduce = False
            bots.append(Bot(field, bot.color))

        # Draw each bug        
        rect = pygame.Rect(bot.x * cell_size , bot.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, bot.color, rect, 2)


    # Add food to display
    for x in range(0, cell_count):
        for y in range(0, cell_count):
            if field.field[x][y] == 1:
                xpos = int(x * cell_size + cell_cntr_offset) 
                ypos = int(y * cell_size+ cell_cntr_offset) 
                pygame.draw.circle(window, (0, 255, 0), [xpos, ypos], 8, 0)

    pygame.display.update()
    clock.tick(2)

    #field.printStatus()

    pass

