import pygame
import sys
import random
import title
import gameui
import items
import gamemap
import random
import gamebattle
#import chartemplate
pygame.init()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)







if __name__ == "__main__":
	from chartemplate import Character
	screen = pygame.display.set_mode((800, 600))
	borders = gameui.Borders(screen, 800, 600)
	maze = gamemap.ShowMaze(screen, 525, 450, gamemap.s1_f1)
	clock = pygame.time.Clock()
	inMaze = True
	titlescreen = title.Title(screen, 800, 600)
	
	
	display = True
	go = False
	base = [60, 60, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]
	
	party = [Character(base, 1, "Test1"), Character(base, 1, "Test2"), Character(base, 1, "Test3"), Character(base, 1, "Test4"), Character(base, 1, "Test5")] 
	enemy = [Character(base, 1, "Test1"), Character(base, 1, "Test2")] 



	if -1 == titlescreen.Display():
		display = False
		pygame.quit()

	stepcount = 0
	while display:
		battlecheck = random.randint(0, 200)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				display = False
				go = True

			if inMaze == True:

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_z and maze.map[maze.chary][maze.charx] == gamemap.B:
						inMaze = False
						screen.fill(BLACK)
						continue

					if event.key == pygame.K_UP:
						if maze.map[maze.chary-1][maze.charx] != gamemap.W and maze.map[maze.chary-1][maze.charx] != gamemap.Q:
							maze.chary = maze.chary - 1

					if event.key == pygame.K_DOWN:
						if maze.map[maze.chary+1][maze.charx] != gamemap.W and maze.map[maze.chary+1][maze.charx] != gamemap.Q:
							maze.chary = maze.chary + 1

					if event.key == pygame.K_LEFT:
						if maze.map[maze.chary][maze.charx-1] != gamemap.W and maze.map[maze.chary][maze.charx-1] != gamemap.Q:
							maze.charx -= 1

					if event.key == pygame.K_RIGHT:
						if maze.map[maze.chary][maze.charx+1] != gamemap.W and maze.map[maze.chary][maze.charx+1] != gamemap.Q:
							maze.charx += 1

					stepcount += 1

					if (battlecheck * 35) % 20 + stepcount > 18:
						stepcount = 0
						bs = gamebattle.BattleScene(screen, 800, 600, party, enemy)

						result = bs.Display()
						enemy = [Character(base, 1, "Test1")] 

						if result == 0:
							display = True
							go = True

						if result == -1:
							display = False
							go = True

						

				


		#Battle Check before the maze is redrawn
		#Town is also drawn here and exits its own display when going back to maze
		#Town has internal displays for different areas
		#
		#
		#
		#

		if inMaze == True:
			screen.fill(BLACK)
			maze.fog(maze.charx, maze.chary)
			borders.Display()

		else:
			print "In Town"
			inMaze = True
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()