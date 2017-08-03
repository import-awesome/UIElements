import pygame

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GOLD = (255, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()


class Pause_Menu(object):
    def __init__(self, screen, winx, winy, party):
        self.characters = party
        self.screen = screen
        self.winx = winx
        self.winy = winy
        self.small = pygame.font.Font(None, 30)
        self.big = pygame.font.Font(None, 115)
        self.char1_x = winx / 16
        self.char_y = winy - 75
        self.pause = True


    # The text that appears on the screen surface and its color
    def pause_menu_text(self, text, font):
        surface_text = self.small.render(text, True, BLACK)
        return surface_text, surface_text.get_rect()

    ''' Continue, quit, load, and save buttons
        X and Y corresponds to the positon of the mouse cursor 
        Action refers to unpausing, quitting, loading and saving '''
    def pause_menu_button(self, button_msg, x, y, width, height, color1, color2, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, color2,(x, y, width, height))
            if click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(self.screen, color1, (x, y, width, height))
        button_text_font = pygame.font.SysFont("comicsansms",30)

        # Buttons have a rectangle around them for highlighting (text_rectangle)
        text_surface, text_rectangle = self.pause_menu_text(button_msg, button_text_font)
        text_rectangle.center = ( (x +(width / 2)), (y + (height / 2)) )
        self.screen.blit(text_surface, text_rectangle)

    # The name says it all
    def quitgame(self):
        pygame.quit()
        quit()

    # The name says it all
    def unpause(self):
        pause = False

    # The name says it all
    def paused(self):
        pause_text_font = pygame.font.SysFont("comicsansms",115)
        text_surface, text_rectangle = self.pause_menu_text("Paused", pause_text_font)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        p = True
        # Pause screen color
      

        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    p = False
                    quit()
            self.screen.fill(WHITE)

        # Pause screen covers the game screen
            self.screen.blit(text_surface, text_rectangle)
            self.pause_menu_button("Continue",150, 450, 100, 50, WHITE, RED, self.unpause)
            self.pause_menu_button("Quit", 550, 450, 100, 50, WHITE, RED, self.quitgame)

            # Add load and save buttons

            clock.tick(60)
            pygame.display.update()

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


    def Display(self):
        display = True
        go = False
        while display:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    display = False
                    go = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.paused()

            clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    import chartemplate
    from chartemplate import Character
    
    # Screen dimensions
    display_width = 800
    display_height = 600

    # Pause screen dimensions
    pause_screen = pygame.display.set_mode((display_width,display_height))

    screen = pygame.display.set_mode((800, 600))
    winx = display_width / 16
    winy = display_height / 75
    base = [60, 60, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]
    party = [Character(base, 1, "Test1"), Character(base, 1, "Test2"), Character(base, 1, "Test3"), Character(base, 1, "Test4"), Character(base, 1, "Test5")]

    # The game isn't paused until the 'x' key is pressed
    pause = False

    p = Pause_Menu(screen, 800, 600, party)
    p.Display()


