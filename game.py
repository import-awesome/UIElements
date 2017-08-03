import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Rectangle")
done = False
clock = pygame.time.Clock()

score1 = 0
score2 = 0



class Paddle(object):
	def __init__(self):
		self.x = 10
		self.y = 100
		self.pos_x = 0
		self.pos_y = 0
		
		self.color = WHITE

	def draw(self, position, org = 0):
		pygame.draw.rect(screen, self.color, (position[0], position[1], self.x, self.y))
		self.pos_y = position[1]
		self.pos_x = position[0]
		if org == 0:
			self.start_y = position[1]
			self.start_x = position[0]

	def move(self, dir):

		if(dir == 1):
			self.pos_y += -50

		if(dir == 0):
			self.pos_y += 50

		if self.pos_y >= 300:
			self.pos_y = 300
		if self.pos_y <= 100:
			self.pos_y = 100

		self.draw([self.pos_x, self.pos_y], 1)
			

class Ball(object):
	def __init__(self):
		self.x = 10
		self.y = 10
		self.v_x = 5
		self.v_y = 5
		self.pos_x = 0
		self.pos_y = 0
		self.start_x = 0
		self.start_y = 0
		self.color = WHITE

	def draw(self, position, org = 0):
		pygame.draw.rect(screen, self.color, (position[0], position[1], self.x, self.y))
		self.pos_y = position[1]
		self.pos_x = position[0]
		if org == 0:
			self.start_y = position[1]
			self.start_x = position[0]

	def move(self, left, right):
		self.pos_x += self.v_x
		self.pos_y += self.v_y
		if self.pos_x > size[0]:
			self.pos_y = self.start_y
			self.pos_x = self.start_x
			global score1
			score1 += 1
		if self.pos_x < 0:
			self.pos_y = self.start_y
			self.pos_x = self.start_x
			global score2
			score2 += 1

		if self.pos_y > 390 or self.pos_y < 100:
			self.v_y = self.v_y * -1

		if self.pos_x == left.pos_x + left.x and (self.pos_y >= left.pos_y and self.pos_y <= left.pos_y + left.y):
			self.v_x = self.v_x * -1

		if self.pos_x == right.pos_x and (self.pos_y >= right.pos_y and self.pos_y <= right.pos_y + right.y):
			self.v_x = self.v_x * -1

		self.draw([self.pos_x, self.pos_y], 1)





left = Paddle()
right = Paddle()
ball = Ball()

left.draw([10, (size[1]/2) - 50])
right.draw([680, (size[1]/2) - 50])
ball.draw([size[0]/2, size[1]/2])
font = pygame.font.Font(None, 72)
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				left.move(1)

			if event.key == pygame.K_s:
				left.move(0)

			if event.key == pygame.K_UP:
				right.move(1)

			if event.key == pygame.K_DOWN:
				right.move(0)



	screen.fill(BLACK)
	left.move(2)
	right.move(2)
	ball.move(left, right)
	score = "{}                  {}".format(score1, score2)
	text = font.render(score, 1, WHITE)
	textpos = (size[0] / 2 - 150, 25)
	screen.blit(text, textpos)

	clock.tick(60)
	pygame.display.flip()
pygame.quit()
