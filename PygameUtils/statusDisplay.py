import pygame

class StatusDisplay:
    def __init__(self, py_surface, x_starting_pos, y_starting_pos) -> None:
        self.window = py_surface
        self.xpos = x_starting_pos
        self.ypos = y_starting_pos
        self.font = font = pygame.font.SysFont('timesnewroman', 20)

    def updateStatus(self, color, label_text, value_text):
        self.window.blit(self.font.render(label_text, False, color), (self.xpos, self.ypos ))
        self.ypos += 50
        self.window.blit(self.font.render(value_text, False, color), (self.xpos, self.ypos ))
        self.ypos += 50
