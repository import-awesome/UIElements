import pygame
pygame.init()





BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (30, 30, 30)
RED = (255, 0, 0)
SAPH = (15, 82, 186)
TOWNBLUE = (0, 142, 204)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()



class Town(object):
	def __init__(self, screen, winx, winy, party):
		self.screen = screen
		self.winx = winx
		self.winy = winy
		self.party = party
		#self.inventory = inventory
		self.townimage = pygame.image.load("etria.jpg")
		self.towndisp = self.townimage.get_rect()
		self.big = pygame.font.Font(None, 72)
		self.small = pygame.font.Font(None, 48)
		

	def Display(self):
		inn = "Etrian Inn"
		shop = "Mike's Merch"
		bar = "Cheap Drinks"
		guild = "Explorer Guild"
		entermaze = "Enter Maze"
		inn_t = self.small.render(inn, 1, TOWNBLUE)
		shop_t = self.small.render(shop, 1, TOWNBLUE)
		bar_t = self.small.render(bar, 1, TOWNBLUE)
		guild_t = self.small.render(guild, 1, TOWNBLUE)
		enter_t = self.small.render(entermaze, 1, TOWNBLUE)
		display = True
		option = 0
		townselecty = int((self.winy*9)/20)
		towninn = Inn(self.screen, self.winx, self.winy, self.party)
		townbar = Bar(self.screen, self.winx, self.winy, self.party)
		townshop = Shop(self.screen, self.winx, self.winy, self.party)
		while display:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					option = 0
					display = False
					continue

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:
						townselecty = int((self.winy*9)/20) + 200

					if event.key == pygame.K_z:
						if townselecty == int((self.winy*9)/20):
							print "Inn"
							towninn.Display()
						if townselecty == int((self.winy*9)/20) + 50:
							print "Shop"
							townshop.Display()

						if townselecty == int((self.winy*9)/20) + 100:
							print "Bar"
							townbar.Display()
						if townselecty == int((self.winy*9)/20) + 150:
							print "Guild"

						if townselecty == int((self.winy*9)/20) + 200:

							small = pygame.font.Font(None, 26)
							yes = "Yes"
							no = "No"
							selectorx = 300
							selectory = 300

							yesno = "Do you want to go to the Maze?"
							yesno_t = small.render(yesno, 1, WHITE)
							yes_t = small.render(yes, 1, WHITE)
							no_t = small.render(no, 1, WHITE)
							check = True
							while check:

								for event2 in pygame.event.get():
									if event2.type == pygame.KEYDOWN:
										if event2.key == pygame.K_z:
											check = False
											if selectorx == 300:
												option = 1
												display = False
										if event2.key == pygame.K_LEFT:
											if selectorx != 300:
												selectorx -= 120

										if event2.key == pygame.K_RIGHT:
											if selectorx != 420:
												selectorx += 120


								pygame.draw.rect(self.screen, GREEN, (248, 248, 304, 104))
								pygame.draw.rect(self.screen, GREY, (250, 250, 300, 100))
								pygame.draw.rect(self.screen, WHITE, (300, 300, 70, 35))
								pygame.draw.rect(self.screen, WHITE, (420, 300, 70, 35))
								pygame.draw.rect(self.screen, GREEN, (selectorx, selectory, 70, 35))
								pygame.draw.rect(self.screen, GREY, (302, 302, 66, 31))
								pygame.draw.rect(self.screen, GREY, (422, 302, 66, 31))

								self.screen.blit(yesno_t, (260, 270))
								self.screen.blit(yes_t, (317, 308))
								self.screen.blit(no_t, (442, 308))
								clock.tick(60)
								pygame.display.flip()

							self.screen.fill(BLACK)
							continue

					if event.key == pygame.K_UP:
						if townselecty != int((self.winy*9)/20):
							townselecty -= 50

					if event.key == pygame.K_DOWN:
						if townselecty != int((self.winy*9)/20) + 200:
							townselecty += 50




			self.screen.fill(BLACK)
			self.screen.blit(self.townimage, self.towndisp)
			pygame.draw.rect(self.screen, WHITE, (38, 268, 254, 254))
			pygame.draw.rect(self.screen, GREY, (40, 270, 250, 250))
			pygame.draw.rect(self.screen, TOWNBLUE, (38, townselecty-2, 254, 54))
			pygame.draw.rect(self.screen, GREY, (40, townselecty, 250, 50))

			self.screen.blit(inn_t, (42, 275))
			self.screen.blit(shop_t, (42, 325))
			self.screen.blit(bar_t, (42, 375))
			self.screen.blit(guild_t, (42, 425))
			self.screen.blit(enter_t, (42, 475))



			clock.tick(60)
			pygame.display.flip()

		return option

class Inn(object):
	def __init__(self, screen, winx, winy, party):
		self.screen = screen
		self.winx = winx
		self.winy = winy
		self.party = party
		#self.party = party
		#self.inventory = inventory
		self.townimage = pygame.image.load("inn2.jpg")
		self.towndisp = self.townimage.get_rect()
		self.big = pygame.font.Font(None, 72)
		self.small = pygame.font.Font(None, 48)
		

	def Display(self):
		inn = "Sleep"
		shop = "Save"
		bar = "Item Storage"
		talk = "Talk"
		entermaze = "Back to Town"
		inn_t = self.small.render(inn, 1, TOWNBLUE)
		shop_t = self.small.render(shop, 1, TOWNBLUE)
		bar_t = self.small.render(bar, 1, TOWNBLUE)
		talk_t = self.small.render(talk, 1, TOWNBLUE)
		enter_t = self.small.render(entermaze, 1, TOWNBLUE)
		display = True
		option = 0
		townselecty = int((self.winy*9)/20)
		while display:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					option = 0
					display = False
					continue

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:
						townselecty = int((self.winy*9)/20) + 200

					if event.key == pygame.K_z:
						if townselecty == int((self.winy*9)/20):
							print "Inn"		
							small = pygame.font.Font(None, 26)

							framecount = 0
							for x in self.party:
								x.hp = x.mhp
								rest = "Party Memebers revived, hp and mp refilled."
								rest_t = small.render(rest, 1, WHITE)
								while framecount < 120:
									pygame.draw.rect(self.screen, WHITE, (198, 208, 454, 54))
									pygame.draw.rect(self.screen, GREY, (200, 210, 450, 50))
									self.screen.blit(rest_t, (242, 225))
									clock.tick(60)
									framecount += 1
									pygame.display.flip()


						if townselecty == int((self.winy*9)/20) + 50:
							print "Shop"
						if townselecty == int((self.winy*9)/20) + 100:
							print "Bar"
						if townselecty == int((self.winy*9)/20) + 150:
							print "Guild"

						if townselecty == int((self.winy*9)/20) + 200:
							print "Back"
							display = False
							continue
							

					if event.key == pygame.K_UP:
						if townselecty != int((self.winy*9)/20):
							townselecty -= 50

					if event.key == pygame.K_DOWN:
						if townselecty != int((self.winy*9)/20) + 200:
							townselecty += 50




			self.screen.fill(BLACK)
			self.screen.blit(self.townimage, self.towndisp)
			pygame.draw.rect(self.screen, WHITE, (38, 268, 254, 254))
			pygame.draw.rect(self.screen, GREY, (40, 270, 250, 250))
			pygame.draw.rect(self.screen, TOWNBLUE, (38, townselecty-2, 254, 54))
			pygame.draw.rect(self.screen, GREY, (40, townselecty, 250, 50))

			self.screen.blit(inn_t, (42, 275))
			self.screen.blit(shop_t, (42, 325))
			self.screen.blit(bar_t, (42, 375))
			self.screen.blit(talk_t, (42, 425))
			self.screen.blit(enter_t, (42, 475))



			clock.tick(60)
			pygame.display.flip()

		return option

class Bar(object):
	def __init__(self, screen, winx, winy, party):
		self.screen = screen
		self.winx = winx
		self.winy = winy
		self.party = party
		#self.party = party
		#self.inventory = inventory
		self.townimage = pygame.image.load("bar.jpg")
		self.towndisp = self.townimage.get_rect()
		self.big = pygame.font.Font(None, 72)
		self.small = pygame.font.Font(None, 48)
		

	def Display(self):
		inn = "Talk"
		shop = "Drink"
		bar = "Food"
		talk = "Drink More"
		entermaze = "Back to Town"
		inn_t = self.small.render(inn, 1, TOWNBLUE)
		shop_t = self.small.render(shop, 1, TOWNBLUE)
		bar_t = self.small.render(bar, 1, TOWNBLUE)
		talk_t = self.small.render(talk, 1, TOWNBLUE)
		enter_t = self.small.render(entermaze, 1, TOWNBLUE)
		display = True
		option = 0
		townselecty = int((self.winy*9)/20)
		while display:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					option = 0
					display = False
					continue

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:
						townselecty = int((self.winy*9)/20) + 200

					if event.key == pygame.K_z:
						if townselecty == int((self.winy*9)/20):
							print "Inn"		
							small = pygame.font.Font(None, 26)

							framecount = 0
							for x in self.party:
								x.hp = x.mhp
								rest = "Party Memebers revived, hp and mp refilled."
								rest_t = small.render(rest, 1, WHITE)
								while framecount < 120:
									pygame.draw.rect(self.screen, WHITE, (198, 208, 454, 54))
									pygame.draw.rect(self.screen, GREY, (200, 210, 450, 50))
									self.screen.blit(rest_t, (242, 225))
									clock.tick(60)
									framecount += 1
									pygame.display.flip()


						if townselecty == int((self.winy*9)/20) + 50:
							print "Shop"
						if townselecty == int((self.winy*9)/20) + 100:
							print "Bar"
						if townselecty == int((self.winy*9)/20) + 150:
							print "Guild"

						if townselecty == int((self.winy*9)/20) + 200:
							print "Back"
							display = False
							continue
							

					if event.key == pygame.K_UP:
						if townselecty != int((self.winy*9)/20):
							townselecty -= 50

					if event.key == pygame.K_DOWN:
						if townselecty != int((self.winy*9)/20) + 200:
							townselecty += 50




			self.screen.fill(BLACK)
			self.screen.blit(self.townimage, self.towndisp)
			pygame.draw.rect(self.screen, WHITE, (38, 268, 254, 254))
			pygame.draw.rect(self.screen, GREY, (40, 270, 250, 250))
			pygame.draw.rect(self.screen, TOWNBLUE, (38, townselecty-2, 254, 54))
			pygame.draw.rect(self.screen, GREY, (40, townselecty, 250, 50))

			self.screen.blit(inn_t, (42, 275))
			self.screen.blit(shop_t, (42, 325))
			self.screen.blit(bar_t, (42, 375))
			self.screen.blit(talk_t, (42, 425))
			self.screen.blit(enter_t, (42, 475))



			clock.tick(60)
			pygame.display.flip()

		return option

class Shop(object):
	def __init__(self, screen, winx, winy, party):
		self.screen = screen
		self.winx = winx
		self.winy = winy
		self.party = party
		#self.party = party
		#self.inventory = inventory
		self.townimage = pygame.image.load("shop2.jpg")
		self.towndisp = self.townimage.get_rect()
		self.big = pygame.font.Font(None, 72)
		self.small = pygame.font.Font(None, 48)
		

	def Display(self):
		inn = "Buy"
		shop = "Sell"
		bar = "Talk"
		talk = "Trade"
		entermaze = "Back to Town"
		inn_t = self.small.render(inn, 1, TOWNBLUE)
		shop_t = self.small.render(shop, 1, TOWNBLUE)
		bar_t = self.small.render(bar, 1, TOWNBLUE)
		talk_t = self.small.render(talk, 1, TOWNBLUE)
		enter_t = self.small.render(entermaze, 1, TOWNBLUE)
		display = True
		option = 0
		townselecty = int((self.winy*9)/20)
		while display:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					option = 0
					display = False
					continue

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:
						townselecty = int((self.winy*9)/20) + 200

					if event.key == pygame.K_z:
						if townselecty == int((self.winy*9)/20):
							print "Inn"		
							small = pygame.font.Font(None, 26)

							framecount = 0
							for x in self.party:
								x.hp = x.mhp
								rest = "Party Memebers revived, hp and mp refilled."
								rest_t = small.render(rest, 1, WHITE)
								while framecount < 120:
									pygame.draw.rect(self.screen, WHITE, (198, 208, 454, 54))
									pygame.draw.rect(self.screen, GREY, (200, 210, 450, 50))
									self.screen.blit(rest_t, (242, 225))
									clock.tick(60)
									framecount += 1
									pygame.display.flip()


						if townselecty == int((self.winy*9)/20) + 50:
							print "Shop"
						if townselecty == int((self.winy*9)/20) + 100:
							print "Bar"
						if townselecty == int((self.winy*9)/20) + 150:
							print "Guild"

						if townselecty == int((self.winy*9)/20) + 200:
							print "Back"
							display = False
							continue
							

					if event.key == pygame.K_UP:
						if townselecty != int((self.winy*9)/20):
							townselecty -= 50

					if event.key == pygame.K_DOWN:
						if townselecty != int((self.winy*9)/20) + 200:
							townselecty += 50




			self.screen.fill(BLACK)
			self.screen.blit(self.townimage, self.towndisp)
			pygame.draw.rect(self.screen, WHITE, (38, 268, 254, 254))
			pygame.draw.rect(self.screen, GREY, (40, 270, 250, 250))
			pygame.draw.rect(self.screen, TOWNBLUE, (38, townselecty-2, 254, 54))
			pygame.draw.rect(self.screen, GREY, (40, townselecty, 250, 50))

			self.screen.blit(inn_t, (42, 275))
			self.screen.blit(shop_t, (42, 325))
			self.screen.blit(bar_t, (42, 375))
			self.screen.blit(talk_t, (42, 425))
			self.screen.blit(enter_t, (42, 475))



			clock.tick(60)
			pygame.display.flip()

		return option