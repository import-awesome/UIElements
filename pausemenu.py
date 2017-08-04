import pygame
import json

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
        self.word_pause_font = pygame.font.Font(None, 30)
        self.weapons_items_font = pygame.font.Font(None, 10)
        self.small = pygame.font.Font(None, 30)
        self.big = pygame.font.Font(None, 50)
        self.char1_x = winx / 16
        self.char_y = winy - 75

        self.weapons = weapons
        self.items = items

        self.test1 = pygame.image.load('Test1.jpeg')
        self.test2 = pygame.image.load('Test2.jpeg')
        self.test3 = pygame.image.load('Test3.jpeg')
        self.test4 = pygame.image.load('Test4.jpeg')
        self.test5 = pygame.image.load('Test5.jpeg')
        
        self.pause = True


    # The text that appears on the screen surface and its color
    def pause_menu_text(self, text, font):
        surface_text = self.word_pause_font.render(text, True, BLACK)
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
    

        # Buttons have a rectangle around them for highlighting (text_rectangle)
        button_text_font = pygame.font.SysFont("comicsansms",30)
        text_surface, text_rectangle = self.pause_menu_text(button_msg, button_text_font)
        text_rectangle.center = ( (x +(width / 2)), (y + (height / 2)) )
        self.screen.blit(text_surface, text_rectangle)


    # The name says it all
    def unpause(self):
        pause = False


    # The name says it all
    def quitgame(self):
        pygame.quit()
        quit()

    # The name says it all
    #def save(self):
    #    with open('save_game.json', 'w+') as file:
    #        saving_text = self.word_pause_font.render("Saving Your Progress", True, RED)
    #        self.screen.blit(saving_text, (400, 300))
    #        saved_data = [(self.characters)
    #                for member in self.characters]
    #        json.dump(saved_data, file)


    # The name says it all
    #def load(self):
            


    # The name says it all
    def paused(self):
        pause_text_font = pygame.font.SysFont("comicsansms",115)
        text_surface, text_rectangle = self.pause_menu_text("Pause Menu", pause_text_font)
        text_rectangle.center = ((display_width / 2), (display_height / 12))
        
        p = True

        # p is short for pause
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    p = False
                    quit()
            
            self.screen.fill(WHITE)

            self.DisplayParty()

            # Pause screen covers the game screen
            self.screen.blit(text_surface, text_rectangle)
            self.pause_menu_button("Continue", 30, 550, 100, 50, WHITE, RED, self.unpause)
            self.pause_menu_button("Quit", 230, 550, 100, 50, WHITE, RED, self.quitgame)
            self.pause_menu_button("Save",450, 550, 100, 50, WHITE, RED, self.unpause)
            self.pause_menu_button("Load", 680, 550, 100, 50, WHITE, RED, self.unpause)

            clock.tick(60)
            pygame.display.update()

    def DisplayParty(self):

        # Set the size of the character images
        self.test1 = pygame.transform.scale(self.test1, (150, 150))
        self.test2 = pygame.transform.scale(self.test2, (150, 150))
        self.test3 = pygame.transform.scale(self.test3, (150, 150))
        self.test4 = pygame.transform.scale(self.test4, (150, 150))
        self.test5 = pygame.transform.scale(self.test5, (150, 150))

        # Make a rectangle to display the character images
        self.test1.get_rect()
        self.test2.get_rect()
        self.test3.get_rect()
        self.test4.get_rect()
        self.test5.get_rect()

        shift = 0
        for x in self.characters:
            name_t = self.big.render(x.name, 1, BLACK)
            hp_t = self.small.render("HP: {} / {}".format(x.hp, x.mhp), 1, BLACK)
            
            if x.isDead():
                hp_t = self.small.render("Dead", 1, WHITE)
                
            mp_t = self.small.render("MP: {} / {}".format(x.mp, x.mmp), 1, BLACK)
            self.test1

            pygame.draw.rect(self.screen, BLACK, (self.char1_x  - 20 + (shift * 3 * self.char1_x), self.char_y - 220, 130, 100))
            pygame.draw.rect(self.screen, BLUE, (self.char1_x  - 20 + (shift * 3 * self.char1_x) + 2, self.char_y - 218, 126, 96))
            self.screen.blit(name_t, (self.char1_x + (shift * 3 * self.char1_x), self.char_y - 255))
            self.screen.blit(hp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y - 200))
            self.screen.blit(mp_t, (self.char1_x - 15 + (shift * 3 * self.char1_x), self.char_y - 170))
        
            shift += 1

        # Move the image to the desired location
        self.screen.blit(self.test1, (7, 110))
        self.screen.blit(self.test2, (160, 110))
        self.screen.blit(self.test3, (313, 110))
        self.screen.blit(self.test4, (466, 110))
        self.screen.blit(self.test5, (619, 110))


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
    import items
    
    # Screen dimensions
    display_width = 800
    display_height = 600

    # Pause screen dimensions
    pause_screen = pygame.display.set_mode((display_width,display_height))

    screen = pygame.display.set_mode((800, 600))
    winx = display_width / 16
    winy = display_height / 75
    base = [60, 60, 26, 26, [9, 5, 8, 6, 4], ["", "", "", ""], 24, 17]
    party = [Character(base, 1, "Rune"), Character(base, 1, "Medic"), Character(base, 1, "Fort"), Character(base, 1, "Night"), Character(base, 1, "Land")]

    weapons = {"Training Sword" : {"Str" : 3, "Attack" : 5}}
    items = {1: "Warp Wire", 2: {"Name": "Potion", "Up": 20}}

    # The game isn't paused until the 'x' key is pressed
    pause = False

    pause_menu = Pause_Menu(screen, 800, 600, party)
    pause_menu.Display()


