import pygame as pg
import sys
import random
import tkinter


#initiating pygame
pg.init()


#variables:
# tag_countdown = -100
# tag_countdown2 = -100
# tag_check_hit1 = False
# tag_check_hit2 = False
# frame = 0
# speed_item_active = False
# speed_active1 = False
# speed_active2 = False
# speed_end = -1
# slow_end = -1
# keys_pressed = pg.key.get_pressed()
# FPS = 60
# slow_item_active = False
# slow_active1 = False
# slow_active2 = False
# time_left = 15
# time = 0

# colours
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 48, 48)
black = ((238, 207, 161))
aqua = (174, 238, 238)
light_blue = (176, 224, 230)
#window name
pg.display.set_caption("Banana Tag")


#screen
screenx = 800
screeny = 600
screen = pg.display.set_mode((screenx, screeny))

#importing images
character1 = pg.image.load("character.png")
character2 = pg.image.load("character2.png")
speed_item = pg.image.load("speeditem.png")
wall_img = pg.image.load("wall_block.png")
resume_button_img = pg.image.load("resume_button.png")
finish_button_img = pg.image.load("finish_button.png")
grass_backround = pg.image.load("grass_backround.png")
slow_item = pg.image.load("cobweb.png")
help_button = pg.image.load("help_button.png")
start_button_img = pg.image.load("start_button.png")
replay_button_img = pg.image.load("replay_button.png")

#image rectangles
character_rect1 = pg.Rect((50, 150), character1.get_size())
character_rect2 = pg.Rect((700, 150), character2.get_size())
speed_item_rect = pg.Rect((10000, 0), speed_item.get_size())
grass_backround_rect = pg.Rect((0, 0), grass_backround.get_size())
grass_backround_rect.topleft = (0, 0)
slow_item_rect = pg.Rect((10000, 0), slow_item.get_size())
#wall_rect = pg.Rect((1000, 0), wall.get_size())

#tagged images
character_tag1 = pg.image.load("character_tag.png")
character_tag2 = pg.image.load("character2_tag.png")

print(character_tag1.get_size())
#tagged rectangles
character_tag_rect1 = pg.Rect((50, 50), character_tag1.get_size())
character_tag_rect2 = pg.Rect((200, 50), character_tag2.get_size())



# image classes:
#def backround_image():

#usman
def test(word):
    print(
        word
    )  #this was used to test throughout coding. It would simply print out whatever you wanted in specific locations

#usman
class wall():

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
      

#Zakariya
class button():

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

    
#MAIN GAME CLASS
class game():
#usman
    def __init__(self, FPS_limit):
        global tagged_1 
        global tagged_2
        global time_left
        global time
        global tag_countdown
        global tag_countdown2
        global tag_check_hit1
        global tag_check_hit2
        global frame
        global speed_item_active
        global speed_active1
        global speed_active2
        global speed_end
        global slow_end
        global keys_pressed
        global FPS
        global slow_item_active
        global slow_active1
        global slow_active2
      
        print("game initiated")
        print(FPS_limit)

      #Omar
        #see which player starts with the banana
        rng = random.randint(1, 2)
        if rng == 1:
            tagged_1 = True
            tagged_2 = False
        if rng == 2:
            tagged_1 = False
            tagged_2 = True
          
        #variables
        tag_countdown = -100
        tag_countdown2 = -100
        tag_check_hit1 = False
        tag_check_hit2 = False
        frame = 0
        speed_item_active = False
        speed_active1 = False
        speed_active2 = False
        speed_end = -1
        slow_end = -1
        keys_pressed = pg.key.get_pressed()
        FPS = 60
        slow_item_active = False
        slow_active1 = False
        slow_active2 = False
        time_left = 60
        time = 0
          
        #start game        
        self.main_menu()

   #Omar
    #showing things 
    def blit_images(self):
        screen.blit(grass_backround, grass_backround_rect)
        screen.blit(character1, character_rect1)
        screen.blit(character2, character_rect2)

      #Usman
    #character 1 movement
    def char1_wasd(self):
        keys_pressed = pg.key.get_pressed()
        if speed_active1:
            speed = 10
        if speed_active1 == False:
            speed = 5
        if tagged_1 == True:
            speed += 1
        if slow_active1 == True:
            speed -= 3

        # screen continuation
        if character_rect1.x > 749:
            character_rect1.x = 1
        if character_rect1.x < 0:
            character_rect1.x = 748

        if keys_pressed[pg.K_a] == 1:
            character_rect1.x -= speed

        if keys_pressed[pg.K_d] == 1:
            character_rect1.x += speed

        if keys_pressed[pg.K_w] == 1 and character_rect1.y > 0:
            character_rect1.y -= speed

        if keys_pressed[pg.K_s] == 1 and character_rect1.bottom < 600:
            character_rect1.y += speed
  #Usman
    #character 2 movement
    def char2_arrows(self):
        keys_pressed = pg.key.get_pressed()
        if speed_active2:
            speed = 10
        if speed_active2 == False:
            speed = 5
        if tagged_2 == True:
            speed += 1
        if slow_active2 == True:
            speed -= 3

            #screen continuation
        if character_rect2.x > 749:
            character_rect2.x = 1
        if character_rect2.x < 0:
            character_rect2.x = 748

        if keys_pressed[pg.K_LEFT] == 1:
            character_rect2.x -= speed

        if keys_pressed[pg.K_RIGHT] == 1:
            character_rect2.x += speed

        if keys_pressed[pg.K_UP] == 1 and character_rect2.y > 0:
            character_rect2.y -= speed

        if keys_pressed[
                pg.
                K_DOWN] == 1 and character_rect2.bottom < 600 and not character_rect2.collidepoint(
                    wall_block.rect.topleft):
            character_rect2.y += speed

    #Usman
    #tagging other player
    def tag(self):
        global check_tag
        global tag_countdown
        global tag_countdown2
        global tagged_1
        global tagged_2
        global keys_pressed
        keys_pressed = pg.key.get_pressed()
        if tagged_1:
            screen.blit(character_tag1, character_tag_rect1)

        if tagged_2:
            screen.blit(character_tag2, character_tag_rect2)

        if keys_pressed[
                pg.K_SPACE] == 1 and tag_countdown == -300 and tagged_1:
            tag_countdown = -180
            if check_tag(1):
                tagged_1 = False
                tagged_2 = True
        if keys_pressed[
                pg.K_RSHIFT] == 1 and tag_countdown2 == -300 and tagged_2:
            tag_countdown2 = -180
            if check_tag(2):
                tagged_1 = True
                tagged_2 = False
        # move tagged images to player pos
        character_tag_rect1.x = character_rect1.x
        character_tag_rect1.y = character_rect1.y
        # 2
        character_tag_rect2.x = character_rect2.x
        character_tag_rect2.y = character_rect2.y

      #Usman
        #check if player is being tagged by other player
        def check_tag(player):
            if player == 1:
                if character_rect1.colliderect(character_rect2):
                    return True
            if player == 2:
                if character_rect2.colliderect(character_rect1):
                    return True

    #Omar
    def show_text(self):
        global textbox_1
        global textbox_2
        global text1
        global text1Rect
        global text2
        global text2Rect
        global time_left
        if tagged_1 == True and tag_countdown == -300:
            text1 = "Blue is tagged TAG AVAILABLE"
            text2 = ''
        if tagged_1 == True and tag_countdown != -300:
            text1 = "Blue is tagged TAG ON COOLDOWN"
            text2 = ''
        if tagged_2 == True and tag_countdown2 == -300:
            text2 = "Red is tagged TAG AVAILABLE"
            text1 = ''
        if tagged_2 == True and tag_countdown2 != -300:
            text2 = "Red is tagged TAG ON COOLDOWN"
            text1 = ''

      #Zakariya
        time_left = 60 - time
        if time_left > 10:
            time_left = round(time_left, 0)
            time_left = int(time_left)
        if time_left <= 10:
            time_left = round(time_left, 2)

        font = pg.font.Font('freesansbold.ttf', 20)
        timer_font = pg.font.Font('freesansbold.ttf', 40)
        textbox_1 = font.render(f"{text1}", True, green, (50, 50, 50))
        textbox_2 = font.render(f"{text2}", True, green, (150, 50, 50))
        timerbox = timer_font.render(f"{time_left}", True, green,
                                     (50, 50, 50))  #timer
        text1Rect = textbox_1.get_rect()
        text1Rect.center = (400, 50)
        text2Rect = textbox_2.get_rect()
        text2Rect.center = (400, 50)
        timer_rect = timerbox.get_rect()  #timer
        timer_rect.center = (400, 550)  #timer
        screen.blit(textbox_1, text1Rect)
        screen.blit(textbox_2, text2Rect)
        screen.blit(timerbox, timer_rect)
#Omar
    def speed_spawn(self):
        global speed_item_active
        speed_item_rect.x = random.randint(50, 750)
        speed_item_rect.y = random.randint(50, 500)
        speed_item_active = True
#Omar
    def speed_boost(self):
        global speed_active1
        global speed_active2
        global speed_end
        if character_rect1.colliderect(speed_item_rect):
            speed_item_rect.x = 1000
            speed_start = frame
            speed_end = speed_start + 300
            speed_active1 = True
        if speed_end == frame:
            speed_active1 = False

        if character_rect2.colliderect(speed_item_rect):
            speed_item_rect.x = 1000
            speed_start = frame
            speed_end = speed_start + 300
            speed_active2 = True
        if speed_end == frame:
            speed_active2 = False
#Omar
    def slow_spawn(self):
        global slow_item_active
        slow_item_rect.x = random.randint(50, 750)
        slow_item_rect.y = random.randint(50, 500)
        slow_item_active = True

#Omar
    def slow_player(self):
        global slow_active1
        global slow_active2
        global slow_start
        global slow_end
        if character_rect1.colliderect(slow_item_rect):
            slow_item_rect.x = 1000
            slow_start = time
            slow_end = time + 3
            slow_active1 = True
        if time > slow_end:
            slow_active1 = False

        if character_rect2.colliderect(slow_item_rect):
            slow_item_rect.x = 1000
            slow_start = time
            slow_end = time + 3
            slow_active2 = True
        if time > slow_end:
            slow_active2 = False
    
    #usman
    def level_builder(self):
        global wall_block
        level1 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        y = 0
        for row in level1:
            x = 0
            for column in row:
                if column == 1:
                    wall_block = wall(x, y, wall_img)
                    wall_block.draw()

                x += screenx / 8
            y += screeny / 6

            x += 50
        y += 50
      
    #zakariya
    def pause_menu(self):
        print("Pausing Game")
        clock = pg.time.Clock()
        paused = True
        while paused:
            screen.fill(aqua)
            resume_button = button(400, 200, resume_button_img, 0.6)
            finish_button = button(400, 400, finish_button_img, 0.5)
            if resume_button.draw():
                break  #resumes game loop
            if finish_button.draw():
                pg.quit()
                sys.exit()
            clock.tick(FPS)
            pg.display.update()
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
    #Zakariya
    def end_game(self):
        if time_left <= 0:
            clock = pg.time.Clock()
            end = True
            while end:
                screen.fill(aqua)
                font = pg.font.SysFont("comicsansms", 72)
                if tagged_1:
                    end_winner = font.render("Red has won", True, red,
                                             (50, 50, 50))
                if tagged_2:
                    end_winner = font.render("Blue has won", True, light_blue,
                                             (50, 50, 50))

                end_rect = end_winner.get_rect()
                end_rect.center = (400, 550)
                screen.blit(end_winner, end_rect)
                finish_button = button(400, 400, finish_button_img, 0.5)
                replay_button = button(400, 200, replay_button_img, 0.09)

                if replay_button.draw():
                    self.__init__(60)
                    self.game_loop()

                if finish_button.draw():
                    pg.quit()
                    sys.exit()
                clock.tick(FPS)
                pg.display.update()
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
    #Zakariya
    def main_menu(self):

        clock = pg.time.Clock()
        main = True
        while main:
            screen.fill(green)
            start_button = button(400, 200, start_button_img, 0.4)
            finish_button = button(400, 400, finish_button_img, 0.3)
            if start_button.draw():
                self.game_loop()
            if finish_button.draw():
                pg.quit()
                sys.exit()
            clock.tick(FPS)
            pg.display.update()
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

    #Usman
    #game loop
    def game_loop(self):
        global frame
        global time
        clock = pg.time.Clock()
        frame = 0
        while True:
            #limit fps
            clock.tick(
                FPS
            )  # limits the frames per second to 60 which is easy to run for all computers

            global tag_countdown
            global tag_countdown2
            # countdown remover
            if tag_countdown > -300:
                tag_countdown -= 1
            if tag_countdown2 > -300:
                tag_countdown2 -= 1

            #end game
            self.end_game()

            # blit characters and screen
            self.blit_images()

            # create levels
            self.level_builder()

            # show and calc text
            self.show_text()

            #random number gen to randomly chose when speed boost will spawn
            rng_chance = 200
            start_rng = 600  # the amount of frames before the speed boost will spawn
            spawn_chance = random.randint(1, rng_chance)
            if spawn_chance == 178 and not speed_item_active and frame > start_rng:
                print("Number Guessed")
                self.speed_spawn()
            if spawn_chance == 95 and not slow_item_active and frame > start_rng:
                print("Number Guessed")
                self.slow_spawn()
            if speed_item_active:
                screen.blit(speed_item, speed_item_rect)
            if slow_item_active:
                screen.blit(slow_item, slow_item_rect)

            #controls
            self.speed_boost()
            self.slow_player()
            self.char1_wasd()
            self.char2_arrows()

            #tagging system
            self.tag()

            #pause menu
            if keys_pressed[pg.K_p] == 1:
                self.pause_menu()

            #Omar
            frame += 1
            time = pg.time.get_ticks() / 1000
            if frame % 100 == 0:
                print(f"Frames Generated: {frame}")
                print(f"Time Elapsed: {time} \n")
            pg.display.update()
            print(clock.get_fps())

            #Omar
            #exit game
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()


game_class = game(60)
