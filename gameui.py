"""Made by Michael Chung"""

import pygame
# chartemplate

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()

class SubMenu(object):
	def __init__(self, screen, win_x, win_y):
		self.screen = screen
		self.size_x = win_x
		self.size_y = win_y
		self.menu_x = win_x / 3 - 10
		self.menu_y = win_y - (win_y/8)
		self.menu_pos_x = win_y - self.menu_x - 10
		self.menu_pos_y = win_y/16


	def Display(self):
		display = True
		go = False
		while display:
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					display = False
					go = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:
						display = False

			#self.screen.fill(BLACK)

			pygame.draw.rect(self.screen, GREY, [self.menu_pos_x, self.menu_pos_y, self.menu_x, self.menu_y])
			

			
			clock.tick(60)
			pygame.display.flip()

		if go == True:
			pygame.quit()

class Turn(object):
	def __init__(self, screen, win_x, win_y, turn):
		self.screen = screen
		self.pos_x = win_x - (win_x/4)
		self.pos_y = 10
		self.big = pygame.font.Font(None, 72)
		self.small = pygame.font.Font(None, 36)
		self.turn = turn
		self.turn_dis = "Turn: {}".format(self.turn)
		self.turn_t = self.small.render(self.turn_dis, 1, GOLD)

	def Display(self, turn):
		self.turn = self.turn + turn
		self.turn_dis = "Turn: {}".format(self.turn)
		self.turn_t = self.small.render(self.turn_dis, 1, GOLD)
		self.screen.blit(self.turn_t, (self.pos_x, self.pos_y))

class Borders(object):
	def __init__(self, screen, win_x, win_y):
		self.screen = screen
		self.topline_x = 5
		self.topline_y = 40
		self.line_x = win_x - 10
		self.line_y = 5
		self.bottom_x = 5
		self.bottom_y = win_y - 80

	def Display(self):
		pygame.draw.rect(self.screen, GREY, [self.topline_x, self.topline_y, self.line_x, self.line_y])
		pygame.draw.rect(self.screen, GREY, [self.bottom_x, self.bottom_y, self.line_x, self.line_y])


class UI(object):
	def __init__(self, screen, win_x, win_y, characters):
		self.screen = screen
		self.character_count = len(characters)
		self.characters = characters
		self.char1_x = win_x / 16
		self.char_y = win_y - 75
		self.small = pygame.font.Font(None, 24)

	def Display(self):
		shift = 0
		for x in self.characters:
			name_t = self.small.render(x.name, 1, WHITE)
			hp_t = self.small.render("HP: {} / {}".format(x.hp, x.mhp), 1, WHITE)
			mp_t = self.small.render("MP: {} / {}".format(x.mp, x.mmp), 1, WHITE)
			en_t = self.small.render("EN: {} / {}".format(x.energy, x.energy_max), 1, WHITE)
			self.screen.blit(name_t, (self.char1_x + (shift * 4 * self.char1_x), self.char_y))
			self.screen.blit(hp_t, (self.char1_x - 25 + (shift * 4 * self.char1_x), self.char_y+15))
			self.screen.blit(mp_t, (self.char1_x - 25 + (shift * 4 * self.char1_x), self.char_y+35))
			self.screen.blit(en_t, (self.char1_x - 25 + (shift * 4 * self.char1_x), self.char_y+55))
			shift += 1





if __name__ == "__main__":
	screen = pygame.display.set_mode((500, 500))
	m = SubMenu(screen, 500, 500)
	t = Turn(screen, 500, 500, 1)
	u = Borders(screen, 500, 500)

	display = True
	go = False
	c = chartemplate.Character(1, "TEST", 100, 10, 100, [1, 1, 1, 1, 1, 1])
	c1 = chartemplate.Character(1, "TEST1", 100, 10, 100, [1, 1, 1, 1, 1, 1])
	c2 = chartemplate.Character(1, "TEST2", 100, 10, 100, [1, 1, 1, 1, 1, 1])
	c3 = chartemplate.Character(1, "TEST3", 100, 10, 100, [1, 1, 1, 1, 1, 1])
	chars = [c, c1, c2, c3]
	ui = UI(screen, 500, 500, chars)
	while display:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				display = False
				go = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					t.Display(1)

				if event.key == pygame.K_x:
					m.Display()

		screen.fill(BLACK)
		t.Display(0)
		u.Display()
		ui.Display()
		#pygame.draw.rect(self.screen, GREY, [self.menu_pos_x, self.menu_pos_y, self.menu_x, self.menu_y])
		

		
		clock.tick(60)
		pygame.display.flip()

	if go == True:
		pygame.quit()

