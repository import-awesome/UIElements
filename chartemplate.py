"""Made by Michael Chung"""

import pygame
import math
import items

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()

class Character(object):
	def __init__(self, base, level, name):
		self.name = name #raw_input("Enter Character Name: ")
		self.level = level
		self.hp = base[0]
		self.mhp = base[1]
		self.mp = base[2]
		self.mmp = base[3]
		self.stats = base[4]
		self.exp = 0
		self.nexp = 100
		self.equip = base[5]
		self.physattk = base[6]
		self.physdefence = base[7]

	def isDead(self):
		if self.hp <= 0:
			self.hp = 0
			return True

		return False

	def lvlup(self, gain):
		if gain + self.exp >= self.nexp:
			temp = self.exp + gain - self.nexp
			self.nexp = self.nexp + (self.level * self.nexp)
			self.exp = temp
			return True

		return False

class Land(Character):
	def __init__(self):
		base = [48, 48, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]
		Character.__init__(self, base, 1)


class Night(Character):
	def __init__(self):
		base = [37, 37, 29, 29, [8, 7, 4, 10, 8], ["", "", "", ""], 24, 12]
		Character.__init__(self, base, 1)


class Fort(Character):
	def __init__(self):
		base = [52, 52, 21, 21, [5, 6, 11, 13, 6], ["", "", "", ""], 22, 20]
		Character.__init__(self, base, 1)


class Medic(Character):
	def __init__(self):
		base = [40, 40, 39, 39, [5, 10, 6, 6, 5], ["", "", "", ""], 22, 14]
		Character.__init__(self, base, 1)


class Rune(Character):
	def __init__(self):
		base = [31, 31, 42, 42, [4, 11, 4, 5, 6], ["", "", "", ""], 22, 12]
		Character.__init__(self, base, 1)

class Party(object):
	def __init__(self):
		#General party, max is 5 members
		self.party = []

		#Positions are 0-6. 0-3 are front row, 4-6 are back row
		#self.positions = []

	def createParty(self):
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

			self.screen.fill(BLACK)

			
			clock.tick(60)
			pygame.display.flip()

		if go == True:
			pygame.quit()

	def addMember(self, char):
		if len(self.party) < 5:
			self.party.append(char)

		else:
			print "Cant add more party members"
			#cant add party memebers


if __name__ == "__main__":
	c = Rune()
	print c.name