import pygame
import sys
import random
import title
import gameui
import items
import gamemap
#import chartemplate
pygame.init()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)







if __name__ == "__main__":
	screen = pygame.display.set_mode((800, 600))
	borders = gameui.Borders(screen, 800, 600)
	maze = gamemap.ShowMaze(screen, 525, 450, gamemap.s1_f1)
	clock = pygame.time.Clock()

	titlescreen = title.Title(screen, 800, 600)
	titlescreen.Display()
	display = True
	go = False
	


	while display:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				display = False
				go = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					#print charx, chary
					#print maze.map[chary][charx]
					#print maze.map[chary-1][charx]
					if maze.map[maze.chary-1][maze.charx] != gamemap.W and maze.map[maze.chary-1][maze.charx] != gamemap.Q:
						maze.chary = maze.chary - 1
					#print charx
					#print chary

				if event.key == pygame.K_DOWN:
					if maze.map[maze.chary+1][maze.charx] != gamemap.W and maze.map[maze.chary+1][maze.charx] != gamemap.Q:
						maze.chary = maze.chary + 1

				if event.key == pygame.K_LEFT:
					if maze.map[maze.chary][maze.charx-1] != gamemap.W and maze.map[maze.chary][maze.charx-1] != gamemap.Q:
						maze.charx -= 1

				if event.key == pygame.K_RIGHT:
					if maze.map[maze.chary][maze.charx+1] != gamemap.W and maze.map[maze.chary][maze.charx+1] != gamemap.Q:
						maze.charx += 1

		screen.fill(BLACK)
		maze.Display()
		borders.Display()
		
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()