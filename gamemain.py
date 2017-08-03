import pygame
import sys
import random
import title
import gameui
import items
import gamemap
import random
import gamebattle
import gamemusic
import maps2
import gametown
#import chartemplate
pygame.init()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (30, 30, 30)
RED = (255, 0, 0)
GOLD = (255, 255, 0)







if __name__ == "__main__":
	from chartemplate import Character
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Atlus Mashup")
	borders = gameui.Borders(screen, 800, 600)
	strat = 0
	floor = 0
	maze = gamemap.ShowMaze(screen, 595, 510, maps2.allmaps[strat][floor][0])
	clock = pygame.time.Clock()
	inMaze = False
	titlescreen = title.Title(screen, 800, 600)
	music = gamemusic.MusicPlayer()
	#index 0 is gold, index 1 is inventory, max 20 items
	inventory = [0, []]
	toggle = 1
	display = True
	go = False
	base = [30, 60, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]
	
	enemy = [Character(base, 1, "En1"), Character(base, 1, "En2"), Character(base, 1, "En3"), Character(base, 1, "En4"), Character(base, 1, "En5")] 
	party = [Character(base, 1, "Char1"), Character(base, 1, "Char2"), Character(base, 1, "Char3"), Character(base, 1, "Char4"), Character(base, 1, "Char5")] 
	town = gametown.Town(screen, 800, 600, party)
	save_hp = []
	save_mp = []
	revert = 0

	music.title()
	if -1 == titlescreen.Display():
		display = False
		pygame.quit()

	music.Stop2()
	battlecheck = random.randint(0, 200)
	screen.fill(BLACK)
	stepcount = 0
	while display:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				display = False
				go = True
				continue

			if inMaze == True:

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_z and maze.map[maze.chary][maze.charx] == gamemap.B:
						
						small = pygame.font.Font(None, 26)
						yes = "Yes"
						no = "No"
						selectorx = 300
						selectory = 300

						yesno = "Do you want to return to the town?"
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
											inMaze = False
											if revert == 1:
												#for x, y, z in party, save_hp, save_mp:
												#	x.mhp = y
												#	x.mmp = z
												revert = 0
												save_mp = []
												save_hp = []
									if event2.key == pygame.K_LEFT:
										if selectorx != 300:
											selectorx -= 120

									if event2.key == pygame.K_RIGHT:
										if selectorx != 420:
											selectorx += 120


							pygame.draw.rect(screen, GREEN, (248, 248, 304, 104))
							pygame.draw.rect(screen, GREY, (250, 250, 300, 100))
							pygame.draw.rect(screen, WHITE, (300, 300, 70, 35))
							pygame.draw.rect(screen, WHITE, (420, 300, 70, 35))
							pygame.draw.rect(screen, GREEN, (selectorx, selectory, 70, 35))
							pygame.draw.rect(screen, GREY, (302, 302, 66, 31))
							pygame.draw.rect(screen, GREY, (422, 302, 66, 31))

							screen.blit(yesno_t, (260, 270))
							screen.blit(yes_t, (317, 308))
							screen.blit(no_t, (442, 308))
							clock.tick(60)
							pygame.display.flip()

						

						screen.fill(BLACK)
						continue

					if event.key == pygame.K_z and maze.map[maze.chary][maze.charx] == gamemap.SD:
						maps2.allmaps[strat][floor][1] = 1
						floor+=1
						maze = gamemap.ShowMaze(screen, 595, 510, maps2.allmaps[strat][floor][0], gamemap.SU)
						continue

					if event.key == pygame.K_z and maze.map[maze.chary][maze.charx] == gamemap.SU:
						floor-=1
						maze = gamemap.ShowMaze(screen, 595, 510, maps2.allmaps[strat][floor][0], gamemap.SD)
						continue

					if event.key == pygame.K_t:
						if maps2.allmaps[strat][floor][1] == 1:
							maps2.allmaps[strat][floor][1] = 0

						else:
							maps2.allmaps[strat][floor][1] = 1
						
						continue

					if event.key == pygame.K_UP:
						if maze.map[maze.chary-1][maze.charx] != gamemap.W and maze.map[maze.chary-1][maze.charx] != gamemap.Q:
							maze.chary = maze.chary - 1
							stepcount += 1


					if event.key == pygame.K_DOWN:
						if maze.map[maze.chary+1][maze.charx] != gamemap.W and maze.map[maze.chary+1][maze.charx] != gamemap.Q:
							maze.chary = maze.chary + 1
							stepcount += 1


					if event.key == pygame.K_LEFT:
						if maze.map[maze.chary][maze.charx-1] != gamemap.W and maze.map[maze.chary][maze.charx-1] != gamemap.Q:
							maze.charx -= 1
							stepcount += 1


					if event.key == pygame.K_RIGHT:
						if maze.map[maze.chary][maze.charx+1] != gamemap.W and maze.map[maze.chary][maze.charx+1] != gamemap.Q:
							maze.charx += 1
							stepcount += 1


					
					if (battlecheck * 35) % 80 + stepcount >= 65 and toggle == 2:
						stepcount = 0

						if battlecheck <= 79:
							enemy = [Character(base, 1, "En1"), Character(base, 1, "En2")] 

						if battlecheck <= 159 and battlecheck >= 80 :
							enemy = [Character(base, 1, "En1"), Character(base, 1, "En2"), Character(base, 1, "En3")] 

						if battlecheck >= 160 and battlecheck <= 174:
							enemy = [Character(base, 1, "En1"), Character(base, 1, "En2"), Character(base, 1, "En3"), Character(base, 1, "En4")] 

						if battlecheck >= 175 and battlecheck <= 189:
							enemy = [Character(base, 1, "En1"), Character(base, 1, "En2"), Character(base, 1, "En3"), Character(base, 1, "En4"), Character(base, 1, "En5")] 

						if battlecheck >= 190:
							enemy = [Character(base, 1, "En1")] 
							
						battlecheck = random.randint(0, 200)

						music.Stop2()
						bs = gamebattle.BattleScene(screen, 800, 600, party, enemy)
						music.battleStart()
						result = bs.Display() 
						
						music.Stop2()
						music.mazeStart()

						if result == 0:
							display = True
							go = True

						if result == -1:
							display = False
							go = True

		if inMaze == True:
			screen.fill(BLACK)
			if maps2.allmaps[strat][floor][1] == 1:
				maze.Display()
			else:
				maze.fog(maze.charx, maze.chary)
			borders.Display()

		else:
			music.Stop()
			for x in party:
				save_hp.append(x.mhp)
				save_mp.append(x.mmp)

			music.townStart()
			if 1 == town.Display():
				inMaze = True
				#for x, y, z in party, save_hp, save_mp:
				#	if x.mmp != z or x.mhp != y:
				#		revert = 1
				#		break


			else:
				display = False
			music.Stop2()
			music.mazeStart()
			
			#music.mazeStart()
		clock.tick(60)
		pygame.display.flip()

	pygame.quit()