import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)


class BattleScene(object):
	def __init__(self, screen, winx, winy, party, enemies):
		self.screen = screen
		self.winx = winx
		self.winy = winy
		self.party = party
		self.enemies = enemies
		self.battleui = BattleUi(self.screen, self.winx, self.winy, self.party)


	def Display(self):
		display = True
		turn = 1
		while display:
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					display = False
					go = True

			screen.fill(BLACK)
			maze.Display()
			borders.Display()
			
			clock.tick(60)
			pygame.display.flip()
		pygame.quit()


class BattleUi(object):
	def __init__(self, screen, winx, winy, party, enemy):
		self.characters = party
		self.enemies = enemy
		self.screen = screen
		self.small = pygame.font.Font(None, 36)
		self.big = pygame.font.Font(None, 48)
		self.char1_x = winx / 16
		self.char_y = winy - 75
		self.battlequeue = []
		
	def DisplayEnemy(self):
		shift = 0
		for x in self.characters:
			name_t = self.big.render(x.name, 1, WHITE)
			hp_t = self.small.render("HP: {} / {}".format(x.hp, x.mhp), 1, WHITE)
			if x.isDead():
				hp_t = self.small.render("Dead", 1, WHITE)
			mp_t = self.small.render("MP: {} / {}".format(x.mp, x.mmp), 1, WHITE)
			self.screen.blit(name_t, (self.char1_x + (shift * 3 * self.char1_x),  20))
			self.screen.blit(hp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), 60))
			self.screen.blit(mp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), 90))
			shift += 1


	def DisplayOptions(self):
		attack = self.big.render("Attack", 1, WHITE)
		ability = self.big.render("Ability", 1, WHITE)
		item = self.big.render("Item", 1, WHITE)
		defend = self.big.render("Defend", 1, WHITE)
		# = self.small.render("Attack", 1, WHITE)
		run = self.big.render("Escape", 1, WHITE)

		self.screen.blit(attack, (self.char1_x, (self.char_y + 75)/2))
		self.screen.blit(ability, (self.char1_x, (self.char_y + 75)/2 + 30))
		self.screen.blit(item, (self.char1_x, (self.char_y + 75)/2 + 60))
		self.screen.blit(defend, (self.char1_x, (self.char_y + 75)/2 + 90))
		self.screen.blit(run, (self.char1_x, (self.char_y + 75)/2 + 120))


	def DisplayParty(self):
		shift = 0
		for x in self.characters:
			name_t = self.big.render(x.name, 1, WHITE)
			hp_t = self.small.render("HP: {} / {}".format(x.hp, x.mhp), 1, WHITE)
			if x.isDead():
				hp_t = self.small.render("Dead", 1, WHITE)
			mp_t = self.small.render("MP: {} / {}".format(x.mp, x.mmp), 1, WHITE)
			self.screen.blit(name_t, (self.char1_x + (shift * 3 * self.char1_x), self.char_y - 40))
			self.screen.blit(hp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y))
			self.screen.blit(mp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y+30))
			shift += 1


if __name__ == "__main__":
	from chartemplate import *
	base = [48, 48, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]

	party = [Character(base, 1, "Test1"), Character(base, 1, "Test2"), Character(base, 1, "Test3"), Character(base, 1, "Test4"), Character(base, 1, "Test5")] 

	screen = pygame.display.set_mode((800, 600))
	clock = pygame.time.Clock()
	b = BattleUi(screen, 800, 600, party, party)

	display = True
	turn = 1
	while display:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				display = False
				go = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z:
					party[0].hp -= 10
					party[1].hp -= 10
					party[2].hp -= 10
					party[3].hp -= 10
					party[4].hp -= 10

		screen.fill(BLACK)
		#maze.Display()
		#borders.Display()
		b.DisplayParty()	
		b.DisplayOptions()
		b.DisplayEnemy()
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()