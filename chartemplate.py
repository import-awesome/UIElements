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

class Template(object):
	def __init__(self, level, name, health, MP):
		self.level = level
		self.hp = health
		self.hp_max = health
		self.name = name
		self.mp = MP
		self.mp_max = MP

	def isDead(self):
		return self.health <= 0


class Character(Template):
	def __init__(self, level, name, health, MP, stats):
		self.level = level
		self.hp = health
		self.hp_max = health
		self.name = name
		self.mp = MP
		self.mp_max = MP
		self.str = stats[0]
		self.agi = stats[1]
		self.end = stats[2]
		self.mnd = stats[3]
		self.spd = stats[4]
		self.luc = stats[5]
		self.points = 3
		self.exp = 0
		"""Gear will be Weapon - 0, Offhand - 1, Extra - 2, Extra - 3"""
		self.gear = ["", "", "", ""]
		self.exp_next = 50

	def lvlup(self, gain):
		self.exp = self.exp + gain
		if self.exp >= self.exp_next:
			self.level = self.level + 1
			self.exp = self.exp - self.exp_next
			self.exp_next = math.ciel(self.exp_next * self.level)



class Fighter(Character):
	def __init__(self):
		self.gear[0] = items.weapons["Training Sword"]
