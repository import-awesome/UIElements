import pygame
import random

musictracks = ["storm.ogg"]


class MusicPlayer(object):
	def __init__(self):
		self.musictracks = ["storm.ogg", "onetruth.ogg", "suprise.ogg", "winds.ogg", "fire.ogg", "foe.ogg"]
		self.mapmusic = ["woods.ogg", "joy.oggs"]
		self.titlescreen = "thread.ogg"
		pygame.mixer.music.set_volume(50)

	def battleStart(self):
		pygame.mixer.music.load(self.musictracks[random.randint(0, len(self.musictracks) - 1)])
		pygame.mixer.music.play(-1)

	def Stop(self):
		pygame.mixer.music.fadeout(3000)

	def title(self):
		pygame.mixer.music.load(self.titlescreen)
		pygame.mixer.music.play(-1)

	def Rewind(self):
		pygame.mixer.music.rewind()
