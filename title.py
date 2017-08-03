import pygame
import gamemusic
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
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

		return 0



if __name__ == "__main__":
	screen = pygame.display.set_mode((500, 500))
	t = Title(screen, 500, 500)
	t.Display()