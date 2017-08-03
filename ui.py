import pygame
import sys
import random
import title

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((750, 550))
work = title.Title(screen, 750, 550)
pygame.display.set_caption("Testing")

x = 50
y = 50

yp = 50
xp = 50

vxp = 700
vyp = 450



playing = True
font = pygame.font.Font(None, 48)
player = "@"
tile = "."
enemy = "X"
gold = "G"
health = 10
health_max = 10
player_health = "Health: {}/{}".format(health, health_max)
player_font = pygame.font.Font(None, 72)
player_text = player_font.render(player, 1, WHITE)
health_text = font.render(player_health, 1, WHITE)
enemy_text = player_font.render(enemy, 1, RED)
gold_text = player_font.render(gold, 1, GOLD)
tile_text = player_font.render(tile, 1, GREEN)

overlay_x = 750 / 3
overlay_y = 550 - 40
over_px = 20
over_py = 20

action = ""
text = font.render(action, 1, WHITE)
action_pos = (50, 510)
sco = 0
score_pos = (400, 510)
score = "Score:     {}".format(sco)
scoretext = font.render(score, 1, GREEN)

enemy_move = 0
gold_life = 0
gx = random.randint(1, 15)*50
gy = random.randint(1, 10)*50
while gx == xp and gy == yp:
	gx = random.randint(1, 15)*50
	gy = random.randint(1, 9)*50

while gx == vxp and gy == vyp:
	gx = random.randint(1, 15)*50
	gy = random.randint(1, 9)*50

hit = 0
hit_timer = 0
title = True
title_t = 0


while playing:

	if title:
		work.Display()
		title = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				menu = True
				while menu:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								menu = False
					pygame.draw.rect(screen, GREY, [over_px, over_py, overlay_x, overlay_y])
					clock.tick(60)
					pygame.display.flip()

			if event.key == pygame.K_DOWN:
				yp += 50
				if yp >= 450:
					yp = 450
				else:
					action = "You moved down."
					text = font.render(action, 1, WHITE)

			if event.key == pygame.K_UP:
				yp += -50
				if yp <= 50:
					yp = 50

				else:
					action = "You moved up."
					text = font.render(action, 1, WHITE)

			if event.key == pygame.K_LEFT:
				xp += -50
				if xp <= 0:
					xp = 0

				else:
					action = "You moved left."
					text = font.render(action, 1, WHITE)

			if event.key == pygame.K_RIGHT:
				xp += 50
				if xp >= 700:
					xp = 700
				else:
					action = "You moved right."
					text = font.render(action, 1, WHITE)

			if random.randint(0, 150) <= 50:

				i = random.randint(0, 3)
				if i == 0:
					vyp += 50
					if vyp >= 450:
						vyp = 450

				if i == 1:
					vyp += -50
					if vyp <= 50:
						vyp = 50

				if i == 2:
					vxp += -50
					if vxp <= 0:
						vxp = 0

				if i == 3:
					vxp += 50
					if vxp >= 700:
						vxp = 700
			if vxp == xp and vyp == yp:
				if hit == 0:
					health += -5
					hit = 1
					player_health = "Health: {}/{}".format(health, health_max)

				health_text = font.render(player_health, 1, WHITE)
				if health == 0:
					playing = False;
			

	enemy_move += 1
	gold_life += 1

	if enemy_move >= 30:
		enemy_move = 0

		if random.randint(0, 150) <= 85:

			i = random.randint(0, 3)
			if i == 0:
				vyp += 50
				if vyp >= 450:
					vyp = 450

			if i == 1:
				vyp += -50
				if vyp <= 50:
					vyp = 50

			if i == 2:
				vxp += -50
				if vxp <= 0:
					vxp = 0

			if i == 3:
				vxp += 50
				if vxp >= 700:
					vxp = 700
		if vxp == xp and vyp == yp:
			
			while gx == vxp and gy == vyp:
				gx = random.randint(1, 15)*50
				gy = random.randint(1, 9)*50

			if hit == 0:
				health += -5
				hit = 1
				player_health = "Health: {}/{}".format(health, health_max)

			health_text = font.render(player_health, 1, WHITE)
			if health == 0:
				playing = False;

	screen.fill(BLACK)

	if hit == 1:
		hit_timer += 1
		if hit_timer >= 360:
			hit = 0
			hit_timer = 0
	
	pygame.draw.rect(screen, GREY, [0, 505, 750, 5])
	pygame.draw.rect(screen, GREY, [0, 45, 750, 5])
	for i in range(25, 750, 50):
		for j in range(50, 500, 50):
			screen.blit(tile_text, (i, j))

	if gold_life == 240:
		gx = random.randint(1, 15)*50
		gy = random.randint(1, 9)*50
		while gx == xp and gy == yp:
			gx = random.randint(1, 15)*50
			gy = random.randint(1, 9)*50

		while gx == vxp and gy == vyp:
			gx = random.randint(1, 15)*50
			gy = random.randint(1, 9)*50

		gold_life = 0

	if xp == gx and yp == gy:
		sco += 100
		score = "Score:     {}".format(sco)
		scoretext = font.render(score, 1, GREEN)
		gx = random.randint(1, 15)*50
		gy = random.randint(1, 9)*50
		while gx == xp and gy == yp:
			gx = random.randint(1, 15)*50
			gy = random.randint(1, 9)*50

		while gx == vxp and gy == vyp:
			gx = random.randint(1, 15)*50
			gy = random.randint(1, 9)*50
		gold_life = 0

	pygame.draw.rect(screen, BLACK, [xp, yp, x, y])
	pygame.draw.rect(screen, BLACK, [vxp, vyp, x, y])
	pygame.draw.rect(screen, BLACK, [gx, gy, x, y])
	screen.blit(gold_text, (gx, gy))
	screen.blit(player_text, (xp, yp))
	screen.blit(health_text, (10, 10))
	screen.blit(enemy_text, (vxp, vyp))

	screen.blit(text, action_pos)
	screen.blit(scoretext, score_pos)

	clock.tick(60)
	pygame.display.flip()

go = "GAME OVER"
go_text = font.render(go, 1, WHITE)

while not playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = True

	screen.fill(BLACK)
	screen.blit(go_text, (250, 255))
	screen.blit(scoretext, (270, 325))
	clock.tick(60)
	pygame.display.flip()	


pygame.quit()