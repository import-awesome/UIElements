"""Made by Michael Chung"""


import pygame
import math
import gameui
Q = "Q"
F = "."
D = "D"
E = "E"
B = "B"
W = "W"
WD = "W"
WL = "W"
WR = "W"
WU = "W"
WD = "W"
WRL = "W"
WRU = "W"
WUR = "W"
WRD = "W"
WLU = "W"
WLD = "W"
WLRU = "W"
WLRD = "W"
WLRUD = "W"
WUDL = "W"
WUDR = "W"
WUD = "W"
SU = "S"
SD = "S"

s1_f1 = [
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],			
			[Q, Q, Q, Q, Q, Q, W, W, W, W, W, Q, W, W, W, Q, W, W, W, Q, W, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, F, F, F, W, F, F, F, D, F, F, F, D, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, F, W, F, W, F, W, F, W, W, F, F, W, F, F, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, D, W, W, Q, D, W, F, W, F, F, W, F, F, W, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q], 
			[Q, Q, Q, Q, Q, W, F, W, F, W, F, F, F, W, F, W, Q, W, F, W, W, W, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, W, F, W, F, W, W, W, F, F, D, F, F, D, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, W, F, F, F, W, F, W, F, W, Q, W, W, W, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, W, W, W, W, W, F, W, F, F, W, F, F, W, W, W, E, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, F, F, W, W, F, W, W, W, W, F, F, D, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, W, W, W, F, W, F, F, D, F, F, F, F, F, W, W, W, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, F, F, W, F, W, W, W, W, W, W, SD, W, F, W, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, W, W, F, W, F, W, F, F, F, W, W, W, W, F, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, F, F, W, F, W, F, F, F, F, F, W, F, F, W, W, E, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, W, W, W, W, F, W, W, E, W, W, F, W, F, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, D, F, W, F, W, F, F, F, W, F, W, F, F, F, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, W, W, W, F, W, F, W, W, F, W, W, F, W, W, W, W, W, E, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, D, F, W, F, F, W, F, W, F, F, F, F, W, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, W, F, W, F, F, W, F, W, F, W, W, F, W, F, W, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, W, F, F, W, F, F, F, F, W, B, W, F, F, F, F, D, F, F, F, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, W, W, Q, W, W, W, W, Q, W, Q, W, W, W, W, Q, W, W, W, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q]
		
		]



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)

class Floor(object):
	def __init__(self, screen, p_x, p_y, x, y):
		self.screen = screen
		self.x = x
		self.y = y
		pygame.draw.rect(self.screen, GREY, (p_x, p_y, x, y))

class Door(object):
	def __init__(self, screen, p_x, p_y, x, y):
		self.screen = screen
		self.x = x
		self.y = y
		pygame.draw.rect(self.screen, GOLD, (p_x, p_y, x, y))

class Wall(object):
	def __init__(self, screen, p_x, p_y, x, y):
		self.screen = screen
		self.x = x
		self.y = y
		pygame.draw.rect(self.screen, BLACK, (p_x, p_y, x, y))

class Base(object):
	def __init__(self, screen, p_x, p_y, x, y):
		self.screen = screen
		self.x = x
		self.y = y
		pygame.draw.rect(self.screen, RED, (p_x, p_y, x, y))


class Stairs(object):
	def __init__(self, screen, p_x, p_y, x, y):
		self.screen = screen
		self.x = x
		self.y = y
		pygame.draw.rect(self.screen, BLUE, (p_x, p_y, x, y))


class ShowMaze(object):
	def __init__(self, screen, win_x, win_y, maps):
		self.screen = screen
		self.winx = win_x
		self.winy = win_y
		self.map = maps
		self.clear = False
		self.start = self.find(B)
		self.charx = self.start[0]
		self.chary = self.start[1]

	def find(self, q):
		c = 0
		r = 0
		print q
		for x in self.map:
			for y in x:
				if y == B:
					return [r, c]
				r += 1
			c += 1
			r = 0
		return [0, 0]


	def fog(self, curx, cury):

		#print "cur: ", curx, cury

		self.fogshow(curx, cury, 0)
		self.fogshow(curx, cury, 1)
		self.fogshow(curx, cury, 2)
		self.fogshow(curx, cury, 3)
		pygame.draw.rect(self.screen, BLACK, (math.floor(2 + self.charx * 525 / 35), math.floor(3 + self.chary * 450 / 30), 10, 10))

		
		return

	def fogshow(self, curx, cury, dir):

		if self.map[cury][curx] == SD or self.map[cury][curx] == SU:
			Stairs(self.screen, math.floor(curx * self.winx / 35), math.floor(cury * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))
			return

		if self.map[cury][curx] == E or self.map[cury][curx] == D:
			Door(self.screen, math.floor(curx * self.winx / 35), math.floor(cury * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))
			return

		if self.map[cury][curx] == B:
			Base(self.screen, math.floor(curx * self.winx / 35), math.floor(cury * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))
			if dir == 0:
				self.fogshow(curx, cury-1, dir)
				self.fogshow(curx-1, cury, dir)

			if dir == 1:
				self.fogshow(curx, cury-1, dir)
				self.fogshow(curx+1, cury, dir)

			if dir == 2:
				self.fogshow(curx, cury+1, dir)
				self.fogshow(curx+1, cury, dir)

			if dir == 3:
				self.fogshow(curx, cury+1, dir)
				self.fogshow(curx-1, cury, dir)



			#self.fog(curx+1, cury)

		if self.map[cury][curx] == W:
			Wall(self.screen, math.floor(curx * self.winx / 35), math.floor(cury * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))
			return

		if self.map[cury][curx] == F:
			Floor(self.screen, math.floor(curx * self.winx / 35), math.floor(cury * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))
			if dir == 0:
				self.fogshow(curx, cury-1, dir)
				self.fogshow(curx-1, cury, dir)

			if dir == 1:
				self.fogshow(curx, cury-1, dir)
				self.fogshow(curx+1, cury, dir)

			if dir == 2:
				self.fogshow(curx, cury+1, dir)
				self.fogshow(curx+1, cury, dir)

			if dir == 3:
				self.fogshow(curx, cury+1, dir)
				self.fogshow(curx-1, cury, dir)


		
		else:
			return

		return

	



	def Display(self):
		c = 0
		r = 0
		for x in self.map:
			for y in x:
				if y == B:
					Base(self.screen, math.floor(r * self.winx / 35), math.floor(c * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))
				
				if y == SD or y == SU:
					Stairs(self.screen, math.floor(r * self.winx / 35), math.floor(c * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))

				if y == F:
					Floor(self.screen, math.floor(r * self.winx / 35), math.floor(c * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))

				if y == D or y == E:
					Door(self.screen, math.floor(r * self.winx / 35), math.floor(c * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))

				if y == W:
					Wall(self.screen, math.floor(r * self.winx / 35), math.floor(c * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))
				r += 1
			c += 1
			r = 0
		pygame.draw.rect(self.screen, BLACK, (math.floor(2 + self.charx * 525 / 35), math.floor(3 + self.chary * 450 / 30), 10, 10))

	def printmap(self):
		print cols
		row = 0
		for x in self.map:
			for y in x:
				print y,
				#if y == F:
					#Floor(self.screen, math.floor(x * self.winx / 35), math.floor(y * self.winy / 30), math.floor(self.winx/35), math.floor(self.winy/30))

			print row
			row += 1

if __name__ == "__main__":
	pygame.init()
	chary = 0
	charx = 0
	screen = pygame.display.set_mode((800, 600))
	maze = ShowMaze(screen, 525, 450, s1_f1)
	start = maze.find(B)
	print start
	charx = start[0]
	chary = start[1]
	gui = gameui.Borders(screen, 800, 600)

	clock = pygame.time.Clock()

	#titlescreen = title.Title(screen, 800, 600)
	#titlescreen.Display()
	display = True
	#go = False
	maze.printmap()	
	while display:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				display = False
				go = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					print charx, chary
					print maze.map[chary][charx]
					print maze.map[chary-1][charx]
					if maze.map[chary-1][charx] != W and maze.map[chary-1][charx] != Q:
						chary = chary - 1
					#print charx
					#print chary

				if event.key == pygame.K_DOWN:
					if maze.map[chary+1][charx] != W and maze.map[chary+1][charx] != Q:
						chary = chary + 1

				if event.key == pygame.K_LEFT:
					if maze.map[chary][charx-1] != W and maze.map[chary][charx-1] != Q:
						charx -= 1

				if event.key == pygame.K_RIGHT:
					if maze.map[chary][charx+1] != W and maze.map[chary][charx+1] != Q:
						charx += 1

		
		screen.fill(BLACK)
		#maze.Display()
		maze.fog(charx, chary)
		pygame.draw.rect(screen, BLACK, (math.floor(2 + charx * 525 / 35), math.floor(3 + chary * 450 / 30), 10, 10))
		gui.Display()
		
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()

#class Maze(object):
#	def __init__(self, screen, win_x, win_y, map):