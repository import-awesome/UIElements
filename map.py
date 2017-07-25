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

cols = "0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4"
s1_f1 = [
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],			
			[Q, Q, Q, Q, Q, Q, WD, WD, WD, WD, WD, Q, WD, WD, WD, Q, WD, WD, WD, Q, WD, WD, WD, WD, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, F, F, F, WRL, F, F, F, D, F, F, F, D, F, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, F, WLRU, F, WRL, F, WLRU, F, WL, WRU, F, F, WRL, F, F, WLRUD, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, D, WU, WUD, Q, D, WLD, F, WRL, F, F, WRL, F, F, WL, WRU, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q], 
			[Q, Q, Q, Q, Q, WR, F, WRL, F, WRL, F, F, F, WRL, F, WUDL, Q, WUDR, F, WL, WD, WUD, WUDR, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR , F, WRL, F, WLRD, F, WLU, WUD, WR, F, F, D, F, F, D, F, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, WRL, F, F, F, WRL, F, WRL, F, WUDL, Q, WUD, WUD, WR, F, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, WLD, WUD, WUD, WU, WR, F, WRL, F, F, WRL, F, F, WL, WUD, WUD, E, WUD, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, F, F, WL, WRD, F, WL, WUD, WUD, WRD, F, F, D, F, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, WUD, WUD, WUDR, F, WRL, F, F, D, F, F, F, F, F, WRL, WUD, WU, WRU, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, F, F, WRL, F, WU, WD, WUD, WUD, WU, WUR, SD, WRL, F, WLD, WRD, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, WUDL, WUDR, F, WRL, F, WRL, F, F, F, WLD, WD, WU, WRD, F, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, F, F, WRL, F, WRL, F, F, F, F, F, WRL, F, F, WUDL, WUD, E, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, WUDL, WU, WUD, WR, F, WL, WUD, E, WUD, WUR, F, WRL, F, WLRUD, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, D, F, WRL, F, WRL, F, F, F, WRL, F, WRL, F, F, F, WLRU, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, WUD, WUD, WR, F, WRL, F, WLD, WUR, F, WLU, WRD, F, WLD, WUD, WU, WUD, WUD, E, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, D, F, WRL, F, F, WRL, F, WRL, F, F, F, F, WRL, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, WRL, F, WRL, F, F, WRL, F, WRL, F, WUDL, WUDR, F, WRL, F, WLRUD, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, WR, F, F, WRL, F, F, F, F, WRL, B, WRL, F, F, F, F, D, F, F, F, WL, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, WU, WU, Q, WU, WU, WU, WU, Q, WU, Q, WU, WU, WU, WU, Q, WU, WU, WU, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q],
			[Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, F, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q]
			




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
		maze.Display()
		pygame.draw.rect(screen, BLACK, (math.floor(2 + charx * 525 / 35), math.floor(3 + chary * 450 / 30), 10, 10))
		gui.Display()
		
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()