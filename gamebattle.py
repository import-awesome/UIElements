import pygame
from gameui import Turn
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (30, 30, 30)
RED = (255, 0, 0)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()



class BattleScene(object):
	def __init__(self, screen, winx, winy, party, enemies):
		self.screen = screen
		self.winx = winx
		self.winy = winy
		self.party = party
		self.enemies = enemies
		self.battleui = BattleUi(self.screen, self.winx, self.winy, self.party, self.enemies)


	def Display(self):
		display = True
		turn = 1
		result = 0
		menu = menuselect(self.screen, self.winx, self.winy, self.battleui)
		while display:
			result = menu.Display()
			if result == 0 or result == 1:
				break



			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					display = False
					go = True


			self.battleui.turn += 1
						#b.turn += 1

			self.screen.fill(BLACK)
			#maze.Display()
			#borders.Display()
			self.battleui.DisplayParty()	
			#b.DisplayOptions()
			self.battleui.DisplayEnemy()
			self.battleui.DisplayTurn(turn)
			clock.tick(60)
			pygame.display.flip()
		#pygame.quit()


class BattleUi(object):
	def __init__(self, screen, winx, winy, party, enemy):
		self.characters = party
		self.enemies = enemy
		self.screen = screen
		self.winx = winx
		self.winy = winy
		self.small = pygame.font.Font(None, 36)
		self.big = pygame.font.Font(None, 48)
		self.char1_x = winx / 16
		self.char_y = winy - 75
		self.battlequeue = []
		self.turn = 0

	def DisplayTurn(self, turn):
		disturn = Turn(self.screen, self.winx, self.winy, turn)
		disturn.Display(self.turn)
		#self.turn += 1
		
	def DisplayEnemy(self):
		shift = 0
		for x in self.enemies:
			name_t = self.big.render(x.name, 1, WHITE)
			hp_t = self.small.render("HP: {} / {}".format(x.hp, x.mhp), 1, WHITE)
			if x.isDead():
				x.hp = 0
				hp_t = self.small.render("Dead", 1, WHITE)
				shift += 1
				continue
			mp_t = self.small.render("MP: {} / {}".format(x.mp, x.mmp), 1, WHITE)
			self.screen.blit(name_t, (self.char1_x + (shift * 3 * self.char1_x),  40))
			self.screen.blit(hp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), 80))
			self.screen.blit(mp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), 110))
			shift += 1


	def DisplayOptions(self):
		attack = self.big.render("Attack", 1, WHITE)
		ability = self.big.render("Ability", 1, WHITE)
		item = self.big.render("Item", 1, WHITE)
		defend = self.big.render("Defend", 1, WHITE)
		# = self.small.render("Attack", 1, WHITE)
		run = self.big.render("Escape", 1, WHITE)

		self.screen.blit(attack, (self.char1_x, (self.char_y + 75)/2-35))
		self.screen.blit(ability, (self.char1_x, (self.char_y + 75)/2))
		self.screen.blit(item, (self.char1_x, (self.char_y + 75)/2 + 35))
		self.screen.blit(defend, (self.char1_x, (self.char_y + 75)/2 + 70))
		self.screen.blit(run, (self.char1_x, (self.char_y + 75)/2 +105))


	def DisplayParty(self):
		shift = 0
		for x in self.characters:
			name_t = self.big.render(x.name, 1, WHITE)
			hp_t = self.small.render("HP: {} / {}".format(x.hp, x.mhp), 1, WHITE)
			if x.isDead():
				hp_t = self.small.render("Dead", 1, WHITE)
				continue
			mp_t = self.small.render("MP: {} / {}".format(x.mp, x.mmp), 1, WHITE)
			self.screen.blit(name_t, (self.char1_x + (shift * 3 * self.char1_x), self.char_y - 40))
			self.screen.blit(hp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y))
			self.screen.blit(mp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y+30))
			shift += 1

	def Win(self):
		for x in self.enemies:
			print x.hp
			print x.isDead()
			if x.isDead() != True:
				return False

		return True

class enemyselect(object):
	def __init__(self, screen, winx, winy, under, select):
		self.screen = screen
		self.b = under
		self.winx = winx
		self.winy = winy
		self.small = pygame.font.Font(None, 36)
		self.big = pygame.font.Font(None, 48)
		self.char2_x = winx / 4 + 30
		self.char1_y = winy / 2 - 35
		self.char1_x = winx / 16
		self.char_y = winy /2 - 35
		self.selection = select

	def Display(self):

		go = False
		run = False
		display = True
		queue = []
		win = 0
		while display == True:

		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					display = False
					go = True
					#selection = 5

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_z:
						if self.char1_y == self.winy / 2 - 35 and self.char2_x == self.winx/4+30:
							print "Attack"
							#party/enemy, index, 
							self.b.battlequeue.append([0, -10])
							display  = False

					if event.key == pygame.K_x:
						display = False
						continue
							
			
		
			self.screen.fill(BLACK)
			name_t = self.big.render(self.b.characters[self.selection].name, 1, WHITE)
			
			self.screen.blit(name_t, (self.char1_x - 4, self.winy/2 - 70))

			pygame.draw.rect(self.screen, WHITE, (self.winx/4 + 30, self.winy/2-35, 400, 140))
			pygame.draw.rect(self.screen, GREY, (self.winx/4 + 32, self.winy/2-33, 396, 136))
			pygame.draw.rect(self.screen, WHITE, (self.char2_x, self.char1_y, 200, 40))
			pygame.draw.rect(self.screen, BLACK, (self.char2_x+2, self.char1_y+2, 196, 36))
			pygame.draw.rect(self.screen, WHITE, (self.char1_x-4, self.winy/2-35, 170, 180))
			pygame.draw.rect(self.screen, GREY, (self.char1_x-2, self.winy/2 - 33, 166, 176))
			pygame.draw.rect(self.screen, WHITE, (self.char1_x-4, self.char_y, 170, 40))
			pygame.draw.rect(self.screen, BLACK, (self.char1_x-2, self.char_y+2, 166, 36))
			self.b.DisplayParty()	
			self.b.DisplayOptions()
			self.b.DisplayEnemy()
			self.b.DisplayTurn(self.b.turn)
			
			clock.tick(60)
			pygame.display.flip()


class menuselect(object):
	def __init__(self, screen, winx, winy, under):
		self.screen = screen
		self.b = under
		self.winx = winx
		self.winy = winy
		self.small = pygame.font.Font(None, 36)
		self.big = pygame.font.Font(None, 48)
		self.char1_x = winx / 16
		self.char_y = winy /2 - 35

	def Display(self):
		selection = 0	
		go = False
		run = False
		display = True
		#queue = []
		win = 0
		es = enemyselect(self.screen, self.winx, self.winy, self.b, 0)
		while selection < len(self.b.characters) and display == True:

			self.screen.fill(BLACK)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					display = False
					go = True
					#selection = 5

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_z:
						if self.char_y == self.winy / 2 - 35:
							print "Attack"
							es = enemyselect(self.screen, self.winx, self.winy, self.b, selection)
							es.Display()
							
						if self.char_y == self.winy / 2 :
							print "Ability"
							self.b.enemies[0].hp -= 10
						if self.char_y == self.winy / 2 + 35:
							print "Item"
							self.b.enemies[0].hp -= 10
						if self.char_y == self.winy / 2 + 70:
							print "Defend"
							self.b.enemies[0].hp -= 10
						if self.char_y == self.winy / 2 + 105:
							print "Run"
							run = True
							display = False
							return 0
						self.char_y = self.winy /2 - 35
						selection += 1

					if event.key == pygame.K_x:
						if selection > 0:
							selection -= 1
							self.b.battlequeue.pop()
							print self.b.battlequeue
						
					if event.key == pygame.K_UP:
						if self.char_y != self.winy / 2-35:
							self.char_y -= 35

					if event.key == pygame.K_DOWN:
						if self.char_y != self.winy / 2 + 105:
							self.char_y += 35
			
			if selection >= 5:
				selection = 0
				self.b.turn += 1
				for x in self.b.battlequeue:
					self.b.enemies[0].hp += x

				if self.b.Win() == True:
					display = False
					win = 1

				self.b.battlequeue = []

			self.screen.fill(BLACK)
			
			name_t = self.big.render(self.b.characters[selection].name, 1, WHITE)
			
			self.screen.blit(name_t, (self.char1_x - 4, self.winy/2 - 70))

			pygame.draw.rect(self.screen, WHITE, (self.char1_x-4, self.winy/2-35, 170, 180))
			pygame.draw.rect(self.screen, GREY, (self.char1_x-2, self.winy/2 - 33, 166, 176))
			pygame.draw.rect(self.screen, WHITE, (self.char1_x-4, self.char_y, 170, 40))
			pygame.draw.rect(self.screen, BLACK, (self.char1_x-2, self.char_y+2, 166, 36))
			self.b.DisplayParty()	
			self.b.DisplayOptions()
			self.b.DisplayEnemy()
			self.b.DisplayTurn(self.b.turn)
			clock.tick(60)
			pygame.display.flip()

		if win == 1:
			return 1

		if run == True:
			return 0

		if go == True:
			pygame.quit()


if __name__ == "__main__":
	from chartemplate import *
	base = [48, 48, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]

	party = [Character(base, 1, "Test1"), Character(base, 1, "Test2"), Character(base, 1, "Test3"), Character(base, 1, "Test4"), Character(base, 1, "Test5")] 

	screen = pygame.display.set_mode((800, 600))
	#b = BattleUi(screen, 800, 600, party, party)
	bs = BattleScene(screen, 800, 600, party, party)
	bs.Display()
	"""
	display = True
	turn = 1
	#b.DisplayTurn(b.turn)

	menu = menuselect(screen, 800, 600, b)

	while display:

		if 0 == menu.Display():
			break

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				display = False
				go = True


		b.turn += 1
					#b.turn += 1

		screen.fill(BLACK)
		#maze.Display()
		#borders.Display()
		b.DisplayParty()	
		#b.DisplayOptions()
		b.DisplayEnemy()
		b.DisplayTurn(b.turn)
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()
	"""