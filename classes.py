import pygame

win = pygame.display.set_mode((500, 500))

class button(object, x, y):
    def __init__(self):
    	self.x = x
    	self.y = y
    	self.width = 64
    	self.height = 64
    	self.clicked = False
    	pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

    