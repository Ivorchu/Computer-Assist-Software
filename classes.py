import pygame

class button(object):
    def __init__(self):
    	self.x = 50
    	self.y = 425
    	self.width = 64
    	self.height = 64
    	self.clicked = False
    	pygame.draw.rect(win, (255,0,0), (x, y, width, height))

    