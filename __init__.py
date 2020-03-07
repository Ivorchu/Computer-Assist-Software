import pygame
from classes import button
#from runautohotkey import 
#from webcrawler import 
#from magnifier import 
#from stock import 
#from lottery import 
#from reminder import 
#from youtube import 
#from news import 
#from texting import 
#from autoscheduleplanner import

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Computer Assist Software")

def redrawAppWindow():
	win.fill((255, 255, 255))
	pygame.display.update()

start = classes.button()

#mainloop
run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	redrawAppWindow()

pygame.quit()