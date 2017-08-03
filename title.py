import pygame
import gamemusic
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (30, 30, 30)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()

class Title(object):
	def __init__(self, s, win_x, win_y):
		self.title1 = "Atlus"
		self.title2 = "MashUp"		
		self.big = pygame.font.Font(None, 72)
		self.small = pygame.font.Font(None, 48)
		self.title1_t = self.big.render(self.title1, 1, BLUE)
		self.title2_t = self.big.render(self.title2, 1, RED)
		self.start = "Start"
		self.start_t = self.small.render(self.start, 1, WHITE)
		self.quit = "Quit"
		self.quit_t = self.small.render(self.quit, 1, WHITE)
		self.options = "Load Game"
		self.option_t = self.small.render(self.options, 1, WHITE)
		self.size_x = win_x
		self.size_y = win_y
		self.selector_x = 190
		self.selector_y = 40
		self.sel_x = self.size_x/2 - 115
		self.sel_y = self.size_y/2
		self.screen = s

	def Display(self):
		display = True
		go = False
		while display:
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					display = False
					go = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						if self.sel_y != self.size_y/2:
							self.sel_y += -40
					if event.key == pygame.K_DOWN:
						if self.sel_y != self.size_y/2 + 80:
							self.sel_y += 40
					if event.key == pygame.K_z:
						if self.sel_y == self.size_y/2:
							display = False
							
							continue


						if self.sel_y == self.size_y/2 + 80:
							display = False
							go = True
							continue

			self.screen.fill(BLACK)
			pygame.draw.rect(self.screen, WHITE, [self.sel_x, self.sel_y, self.selector_x, self.selector_y])
			pygame.draw.rect(self.screen, BLACK, [self.sel_x+2, self.sel_y+2, self.selector_x-4, self.selector_y-4])

			self.screen.blit(self.title1_t, (self.size_x/2 - 130, self.size_y/2 - 100))
			self.screen.blit(self.title2_t, (self.size_x/2 - 90, self.size_y/2 - 60))
			self.screen.blit(self.start_t, (self.size_x/2 - 110, self.size_y/2))
			self.screen.blit(self.option_t, (self.size_x/2 - 110, (self.size_y/2)+40))
			self.screen.blit(self.quit_t, (self.size_x/2 - 110, (self.size_y/2)+80))
			clock.tick(60)
			pygame.display.flip()

		

		if go == True:
			pygame.quit()
			return -1

		self.newDisplay()

		return 0

	def newDisplay(self):
		framecounter = 0
		go = False
		text1 = "This is a game inspired by Etrian Odyssey, made by Atlus."
		text2 = "All of the ideas are recreations from those games."
		text3 = "The maps are also pulled from those games."
		text4 = "We hope you find it interesting."
		text5 = "You are given 5 premade characters to navigate a maze."
		text6 = "The goal is to get to the end of the maze,"
		text7 = "and defeat the boss."

		small = pygame.font.Font(None, 36)
		t1 = small.render(text1, 1, WHITE)
		t2 = small.render(text2, 1, WHITE)
		t3 = small.render(text3, 1, WHITE)
		t4 = small.render(text4, 1, WHITE)
		t5 = small.render(text5, 1, WHITE)
		t6 = small.render(text6, 1, WHITE)
		t7 = small.render(text7, 1, WHITE)

		while framecounter <= 500:

			self.screen.fill(BLACK)
			pygame.draw.rect(self.screen, WHITE, [self.size_x/16, self.size_y/16, self.size_x*7/8, self.size_y*7/8])
			pygame.draw.rect(self.screen, GREY, [self.size_x/16+2, self.size_y/16+2, self.size_x*7/8-4, self.size_y*7/8-4])

			if framecounter > 60:
				self.screen.blit(t1, (self.size_x/16+10, self.size_y/16+20))
			if framecounter > 120:
				self.screen.blit(t2, (self.size_x/16+10, self.size_y/16+90))

			if framecounter > 180:
				self.screen.blit(t3, (self.size_x/16+10, self.size_y/16+170))

			if framecounter > 240:
				self.screen.blit(t5, (self.size_x/16+10, self.size_y/16+250))

			if framecounter > 300:
				self.screen.blit(t6, (self.size_x/16+10, self.size_y/16+330))

			if framecounter > 360:
				self.screen.blit(t7, (self.size_x/16+10, self.size_y/16+410))

			if framecounter > 420:
				self.screen.blit(t4, (self.size_x/16+10, self.size_y/16+490))

			#if framecounter > 180:

			#if framecounter > 240:

			framecounter += 1
			clock.tick(60)
			pygame.display.flip()


if __name__ == "__main__":
	screen = pygame.display.set_mode((500, 500))
	t = Title(screen, 500, 500)
	t.Display()