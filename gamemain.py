import pygame
import sys
import random
import title
import gameui
import items
import gamemap
import random
import gamebattle
import gamemusic
import maps2
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
	floor = 0
	maze = gamemap.ShowMaze(screen, 595, 510, maps2.allmaps[floor])
	clock = pygame.time.Clock()
	inMaze = False
	titlescreen = title.Title(screen, 800, 600)
	music = gamemusic.MusicPlayer()
	
	toggle = 1
	display = True
	go = False
	base = [60, 60, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]
	
	enemy = [Character(base, 1, "En1"), Character(base, 1, "En2"), Character(base, 1, "En3"), Character(base, 1, "En4"), Character(base, 1, "En5")] 
	party = [Character(base, 1, "Char1"), Character(base, 1, "Char2"), Character(base, 1, "Char3"), Character(base, 1, "Char4"), Character(base, 1, "Char5")] 


	music.title()
	if -1 == titlescreen.Display():
		display = False
		pygame.quit()

	music.Stop()
	battlecheck = random.randint(0, 200)

	stepcount = 0
	while display:
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

					if event.key == pygame.K_z and maze.map[maze.chary][maze.charx] == gamemap.SD:
						floor+=1
						maze = gamemap.ShowMaze(screen, 595, 510, maps2.allmaps[floor])
						continue

					if event.key == pygame.K_z and maze.map[maze.chary][maze.charx] == gamemap.SU:
						floor-=1
						maze = gamemap.ShowMaze(screen, 595, 510, maps2.allmaps[floor])
						continue

					if event.key == pygame.K_x:
						if toggle == 1:
							toggle = 0

						else:
							toggle = 1
						
						continue

					if event.key == pygame.K_UP:
						if maze.map[maze.chary-1][maze.charx] != gamemap.W and maze.map[maze.chary-1][maze.charx] != gamemap.Q:
							maze.chary = maze.chary - 1
							stepcount += 1


					if event.key == pygame.K_DOWN:
						if maze.map[maze.chary+1][maze.charx] != gamemap.W and maze.map[maze.chary+1][maze.charx] != gamemap.Q:
							maze.chary = maze.chary + 1
							stepcount += 1


					if event.key == pygame.K_LEFT:
						if maze.map[maze.chary][maze.charx-1] != gamemap.W and maze.map[maze.chary][maze.charx-1] != gamemap.Q:
							maze.charx -= 1
							stepcount += 1


					if event.key == pygame.K_RIGHT:
						if maze.map[maze.chary][maze.charx+1] != gamemap.W and maze.map[maze.chary][maze.charx+1] != gamemap.Q:
							maze.charx += 1
							stepcount += 1


					
					if (battlecheck * 35) % 80 + stepcount >= 65:
						stepcount = 0
						battlecheck = random.randint(0, 200)

						
						bs = gamebattle.BattleScene(screen, 800, 600, party, enemy)
						music.battleStart()
						result = bs.Display() 
						
						music.Stop()

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
			if toggle == 1:
				maze.Display()
			else:
				maze.fog(maze.charx, maze.chary)
			borders.Display()

		else:
			print "In Town"
			inMaze = True
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()