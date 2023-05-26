from Utils.bot import Bot
from Utils.field import Field

# Main Program
# To define say a 10 x 10 grid
# Uses a zero base
grid = 9
food_density = 50
field = Field(grid, food_density)
bot = Bot(field)

# Simulate several evolutions of the field
for i in range(10):
    bot.move()
    bot.eat()
    bot.printStatus()
    field.printStatus()
