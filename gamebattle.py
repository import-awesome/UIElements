"""Made by Michael Chung"""
import pygame
from gameui import Turn
import math
import gamemusic
import random
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
				return 0

			if result == -1:
				return -1

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
		self.small = pygame.font.Font(None, 24)
		self.big = pygame.font.Font(None, 36)
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
			pygame.draw.rect(self.screen, WHITE, (self.char1_x  - 20 + (shift * 3 * self.char1_x), 36, 130, 100))
			pygame.draw.rect(self.screen, GREY, (self.char1_x  - 20 + (shift * 3 * self.char1_x) + 2, 38, 126, 96))
			self.screen.blit(name_t, (self.char1_x + (shift * 3 * self.char1_x) + 10,  40))
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
				#continue
			mp_t = self.small.render("MP: {} / {}".format(x.mp, x.mmp), 1, WHITE)
			pygame.draw.rect(self.screen, WHITE, (self.char1_x  - 20 + (shift * 3 * self.char1_x), self.char_y - 40, 130, 100))
			pygame.draw.rect(self.screen, GREY, (self.char1_x  - 20 + (shift * 3 * self.char1_x) + 2, self.char_y - 38, 126, 96))
			self.screen.blit(name_t, (self.char1_x +  10 + (shift * 3 * self.char1_x), self.char_y - 40))
			self.screen.blit(hp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y))
			self.screen.blit(mp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y+30))
			shift += 1

	def Win(self):
		for x in self.enemies:
			print x.name, x.hp, x.isDead()
			if x.isDead() != True:
				return False

		return True

	def gameOver(self):
		for x in self.characters:
			if x.isDead() != True:
				return False
		return True

class enemyselect(object):
	def __init__(self, screen, winx, winy, under, select, living):
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
		self.living = living

	def Display(self):

		go = False
		run = False
		display = True
		queue = []
		win = 0
		enemypos = []
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
							self.b.battlequeue.append([self.living[self.selection], enemypos[0], 2])
							#self.b.battlequeue.append(battlecalc(self.b.character[self.selection], enemypos[0]))
							print enemypos[0].name
							display = False

						if self.char1_y == self.winy / 2 - 35 and self.char2_x == self.winx/4+230:
							print "Attack"
							#party/enemy, index, 
							self.b.battlequeue.append([self.living[self.selection], enemypos[1], 2])
							#self.b.battlequeue.append(battlecalc(self.b.character[self.selection], enemypos[0]))
							print enemypos[1].name
							display = False

						if self.char1_y == self.winy / 2 and self.char2_x == self.winx/4+30:
							print "Attack"
							#party/enemy, index, 
							self.b.battlequeue.append([self.living[self.selection], enemypos[2], 2])
							#self.b.battlequeue.append(battlecalc(self.b.character[self.selection], enemypos[0]))
							print enemypos[2].name
							display = False

						if self.char1_y == self.winy / 2 and self.char2_x == self.winx/4+230:
							print "Attack"
							#party/enemy, index, 
							self.b.battlequeue.append([self.living[self.selection], enemypos[3], 2])
							#self.b.battlequeue.append(battlecalc(self.b.character[self.selection], enemypos[0]))
							print enemypos[3].name
							display = False

						if self.char1_y == self.winy / 2 + 35 and self.char2_x == self.winx/4+30:
							print "Attack"
							#party/enemy, index, 
							self.b.battlequeue.append([self.living[self.selection], enemypos[4], 2])
							#self.b.battlequeue.append(battlecalc(self.b.character[self.selection], enemypos[0]))
							print enemypos[4].name
							display = False



					if len(enemypos) > 1:
						if event.key == pygame.K_RIGHT and self.char2_x != self.winx/4 + 230:
							if len(enemypos) == 3 and self.char1_y == self.winy / 2:
								self.char2_x += 200
								self.char1_y -= 35	

							if len(enemypos) == 5 and self.char1_y == self.winy / 2 +35:
								self.char2_x += 200
								self.char1_y -= 35

							else:
								self.char2_x += 200


						if event.key == pygame.K_LEFT and self.char2_x != self.winx/4 + 30:
							self.char2_x -= 200

					if len(enemypos) >= 3:
						if event.key == pygame.K_DOWN :
							if len(enemypos) < 5 :
								if len(enemypos) == 3 and self.char1_y == self.winy/2 - 35 and self.char2_x == self.winx/4 + 230:
									self.char2_x -= 200
									self.char1_y += 35

								else:
									if self.char1_y != self.winy/2:
										self.char1_y += 35

							else:
								if self.char1_y == self.winy/2 and self.char2_x == self.winx/4 + 230:
									self.char2_x -= 200
									self.char1_y += 35

								else:
									if self.char1_y != self.winy/2 + 35:
										self.char1_y += 35

						if event.key == pygame.K_UP and self.char1_y != self.winy/2 - 35:
							self.char1_y -= 35


					if event.key == pygame.K_x:
						display = False
						self.selection -= 2
						return False
						continue
			enemypos = []	
			
		
			self.screen.fill(BLACK)
			name_t = self.big.render(self.living[self.selection].name, 1, WHITE)
			
			self.screen.blit(name_t, (self.char1_x - 4, self.winy/2 - 70))

			pygame.draw.rect(self.screen, WHITE, (self.winx/4 + 30, self.winy/2-35, 400, 120))
			pygame.draw.rect(self.screen, GREY, (self.winx/4 + 32, self.winy/2-33, 396, 116))


			pygame.draw.rect(self.screen, WHITE, (self.char2_x, self.char1_y, 200, 40))
			pygame.draw.rect(self.screen, BLACK, (self.char2_x+2, self.char1_y+2, 196, 36))
			shift_x = 0
			shift_y = 0
			for x in self.b.enemies:
				ename_t = self.small.render(x.name, 1, WHITE)
				
				#hp_t = self.small.render("HP: {} / {}".format(x.hp, x.mhp), 1, WHITE)
				if x.isDead():
					x.hp = 0
					continue
				self.screen.blit(ename_t, (self.winx/4 + (50 + (200*(shift_x%2))), self.winy / 2 - 30 + (35 * shift_y)))
				enemypos.append(x)
				shift_x+=1
				if shift_x % 2 == 0 and shift_x != 0:
					shift_y += 1

			

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

		return True

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
		living = []
		for x in self.b.characters:
			if x.isDead() == True:
				continue
			living.append(x)
		win = 0
		es = enemyselect(self.screen, self.winx, self.winy, self.b, 0, living)
		while display == True:

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
							es = enemyselect(self.screen, self.winx, self.winy, self.b, selection, living)
							if False == es.Display():
								if selection > 0:
									print self.b.battlequeue

							else:
								selection += 1
							
						if self.char_y == self.winy / 2 :
							print "Ability"
							self.b.enemies[0].hp -= 10
						if self.char_y == self.winy / 2 + 35:
							print "Item"
							self.b.enemies[0].hp -= 10
						if self.char_y == self.winy / 2 + 70:
							print "Defend"
							#living[selection].physdefence += 10
							living[selection].hp += 10
							self.b.battlequeue.append([living[selection], None, 0])
							selecion += 1
						if self.char_y == self.winy / 2 + 105:
							print "Run"
							run = True
							display = False
							return 0
						self.char_y = self.winy /2 - 35

					if event.key == pygame.K_x:
						if selection > 0:
							if self.b.battlequeue[selection-1]:
								living[selection-1].hp -= 10
								#living[selection-1].physdefence -= 10
							selection -= 1
							self.b.battlequeue.pop()
							print self.b.battlequeue
						
					if event.key == pygame.K_UP:
						if self.char_y != self.winy / 2-35:
							self.char_y -= 35

					if event.key == pygame.K_DOWN:
						if self.char_y != self.winy / 2 + 105:
							self.char_y += 35

			self.screen.fill(BLACK)
			
		
			self.b.DisplayParty()	
			self.b.DisplayEnemy()

			if selection >= len(living):
				self.b.turn += 1
				for x in self.b.enemies:
					if x.isDead() == True:
						continue
					self.b.battlequeue.append([living[random.randint(0, 1000) % len(living)], x, 1])
				for x in self.b.battlequeue:
					battlecalc(self.screen, self.winx, self.winy, x[0], x[1], x[2])
					self.screen.fill(BLACK)
					self.b.DisplayParty()
					self.b.DisplayEnemy()

					if self.b.Win() == True:
						display = False
						win = 1
						break

					if self.b.gameOver() == True:
						win = -1
						display = False
						break
					living = []
					for x in self.b.characters:
						if x.isDead():
							continue
						living.append(x)

				selection = 0
				self.b.battlequeue = []

			name_t = self.big.render(living[selection].name, 1, WHITE)
			
			self.screen.blit(name_t, (self.char1_x - 4, self.winy/2 - 70))
			pygame.draw.rect(self.screen, WHITE, (self.char1_x-4, self.winy/2-35, 170, 180))
			pygame.draw.rect(self.screen, GREY, (self.char1_x-2, self.winy/2 - 33, 166, 176))
			pygame.draw.rect(self.screen, WHITE, (self.char1_x-4, self.char_y, 170, 40))
			pygame.draw.rect(self.screen, BLACK, (self.char1_x-2, self.char_y+2, 166, 36))
			self.b.DisplayOptions()
			self.b.DisplayTurn(self.b.turn)


			clock.tick(60)
			pygame.display.flip()

		if win == -1:
			return -1

		if win == 1:
			return 1

		if run == True:
			return 0

		if go == True:
			pygame.quit()


def battlecalc(screen, winx, winy, character, enemy, direction, action = 0):
	rand = random.uniform(0.9, 1.05)
	framecounter = 0
	small = pygame.font.Font(None, 36)
	

	if rand >= 1.45:
		rand = 2
	if direction == 1:
		if action == 0:
			act = "{} is attacked by {}!".format(character.name, enemy.name)
			act2 = "{} lost {} hp!".format(character.name, int(math.floor((3*enemy.stats[0] - character.physdefence) * math.sqrt(enemy.stats[0]/character.stats[2]) * rand)))
			act3 = "{} dies!".format(character.name)
			if character.hp <= 0:
				act = "{} is already dead.".format(character.name)
				act_t = small.render(act, 1, WHITE)
				while framecounter < 45:
					screen.blit(act_t, (winx/4 -30, winy/2+85))
					framcounter += 1

					clock.tick(60)
					pygame.display.flip()
				return


			act_t = small.render(act, 1, WHITE)
			act2_t = small.render(act2, 1, WHITE)
			act3_t = small.render(act3, 1, WHITE)
			while framecounter < 90:
				pygame.draw.rect(screen, WHITE, (winx/4 - 35, winy/2+80, 450, 40))
				pygame.draw.rect(screen, GREY, (winx/4 - 33, winy/2+82, 446, 36))

				if framecounter < 45:
					screen.blit(act_t, (winx/4 -30, winy/2+85))

				else:
					if character.hp - int(math.floor((3*enemy.stats[0] - character.physdefence) * math.sqrt(enemy.stats[0]/character.stats[2]) * rand)) <= 0:
						screen.blit(act3_t, (winx/4 - 30, winy/2+85))
					else:	
						screen.blit(act2_t, (winx/4 - 30, winy/2+85))


				framecounter += 1
				clock.tick(60)
				pygame.display.flip()

			character.hp = character.hp - int(math.floor((3*enemy.stats[0] - character.physdefence) * math.sqrt(enemy.stats[0]/character.stats[2]) * rand))
			print character.hp
	if direction == 2:
		if action == 0:
			print character.name, "attacks", enemy.name
			act = "{} attacks {}!".format(character.name, enemy.name)
			act2 = "{} lost {} hp!".format(enemy.name, int(math.floor((character.physattk - enemy.stats[2]) * math.floor(math.sqrt(character.stats[0]/enemy.stats[2])) * rand)))
			act3 = "{} dies!".format(enemy.name)
			act_t = small.render(act, 1, WHITE)
			act2_t = small.render(act2, 1, WHITE)
			act3_t = small.render(act3, 1, WHITE)
			if enemy.hp <= 0:
				act = "{} is already dead.".format(enemy.name)
				act_t = small.render(act, 1, WHITE)
				while framecounter < 45:
					screen.blit(act_t, (winx/4 -30, winy/2+85))
					framcounter += 1

					clock.tick(60)
					pygame.display.flip()
				return

			while framecounter < 90:
				pygame.draw.rect(screen, WHITE, (winx/4 - 35, winy/2+80, 450, 40))
				pygame.draw.rect(screen, GREY, (winx/4 -33, winy/2+82, 446, 36))

				if framecounter < 45:
					screen.blit(act_t, (winx/4 -30, winy/2+85))

				else:
					if enemy.hp - int(math.floor((character.physattk - enemy.stats[2]) * math.floor(math.sqrt(character.stats[0]/enemy.stats[2])) * rand)) <= 0:
						screen.blit(act3_t, (winx/4 - 30, winy/2+85))
					else:
						screen.blit(act2_t, (winx/4 - 30, winy/2+85))


				framecounter += 1
				clock.tick(60)
				pygame.display.flip()
			enemy.hp = enemy.hp - int(math.floor((character.physattk - enemy.stats[2]) * math.floor(math.sqrt(character.stats[0]/enemy.stats[2])) * rand))
			print enemy.hp

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
