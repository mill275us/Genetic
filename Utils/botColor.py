class PyBotColorer:
    def __init__(self, num_of_bots) -> None:
        self.number_of_bots = num_of_bots
        self.current_color = 0
        self.increment = int(255 / self.number_of_bots)

    def pyColorForBot(self):
        self.current_color += self.increment
        r = 255
        g = 0
        b = self.current_color
        return (r, g, b)
