import pygame as pg
import sys
import random
import tkinter

#initiating pygame
pg.init()

#variables:
tag_countdown = -300
tag_countdown2 = -300
tag_check_hit1 = False
tag_check_hit2 = False
frame = 0
speed_item_active = False
speed_active1 = False
speed_active2 = False
speed_end = -1
keys_pressed = pg.key.get_pressed()
FPS = 60

# colours
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

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
speed_move = pg.image.load("speedmove.png")
wall_img = pg.image.load("wall_block.png")
continue_button_img = pg.image.load("continue_button.png")
exit_button_img = pg.image.load("exit_button.png")

#image rectangles
character_rect1 = pg.Rect((50,150), character1.get_size())
character_rect2 = pg.Rect((700,150), character2.get_size())
speed_item_rect = pg.Rect((10000,0), speed_item.get_size())
speed_move_rect = pg.Rect((10000, 0), speed_move.get_size())
#wall_rect = pg.Rect((1000, 0), wall.get_size())

#tagged images
character_tag1 = pg.image.load("character_tag.png")
character_tag2 = pg.image.load("character2_tag.png")

#tagged rectangles
character_tag_rect1 = pg.Rect((50, 50), character_tag1.get_size())
character_tag_rect2 = pg.Rect((200, 50), character_tag2.get_size())


#see which player starts with the banana
rng = random.randint(1, 2)
if rng == 1:
    tagged_1 = True
    tagged_2 = False
if rng == 2:
    tagged_1 = False
    tagged_2 = True

# image classes:

def test(word):
    print(word) #this was used to test throughout coding. It would simply print out whatever you wanted in specific locations

class wall():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width*scale), int(height*scale)))
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
    
    def __init__(self, FPS_limit):
        print("game initiated")
        print(FPS_limit)
        self.game_loop()
    
    #showing things
    def blit_images(self):
        screen.fill(green)
        screen.blit(character1, character_rect1)
        screen.blit(character2, character_rect2)
        
        
    #character 1 movement
    def char1_wasd(self):
        keys_pressed = pg.key.get_pressed()
        if speed_active1:
            speed = 10
        if speed_active1 == False:
            speed = 5
            
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
            
    #character 2 movement
    def char2_arrows(self):
        keys_pressed = pg.key.get_pressed()
        if speed_active2:
            speed = 10
        if speed_active2 == False:
            speed = 5
            
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

        if keys_pressed[pg.K_DOWN] == 1 and character_rect2.bottom < 600 and not character_rect2.collidepoint(wall_block.rect.topleft):
            character_rect2.y += speed
            
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

        if keys_pressed[pg.K_SPACE] == 1 and tag_countdown == -300 and tagged_1:
            tag_countdown = 180
            if check_tag(1):
                tagged_1 = False
                tagged_2 = True
        if keys_pressed[pg.K_RSHIFT] == 1 and tag_countdown2 == -300 and tagged_2:
            tag_countdown2 = 180
            if check_tag(2):
                tagged_1 = True
                tagged_2 = False
        # move tagged images to player pos
        character_tag_rect1.x = character_rect1.x
        character_tag_rect1.y = character_rect1.y
        # 2
        character_tag_rect2.x = character_rect2.x
        character_tag_rect2.y = character_rect2.y
        
        #check if player is being tagged by other player
        def check_tag(player):
            if player == 1:
                if character_rect1.colliderect(character_rect2):
                    return True
            if player == 2:
                if character_rect2.colliderect(character_rect1):
                    return True
                
    def show_text(self):
        global textbox_1
        global textbox_2
        global text1
        global text1Rect
        global text2
        global text2Rect
        if tagged_1 == True and tag_countdown == -300:
            text1 = "Blue is tagged \n TAG AVAILABLE"
            text2 = ''
        if tagged_1 == True and tag_countdown != -300:
            text1 = "Blue is tagged\nTAG ON COOLDOWN"
            text2 = ''
        if tagged_2 == True and tag_countdown2 == -300:
            text2 = "Red is tagged \n TAG AVAILABLE"
            text1 = ''
        if tagged_2 == True and tag_countdown2 != -300:
            text2 = "Red is tagged \n TAG ON COOLDOWN"
            text1 = ''
        font = pg.font.Font('freesansbold.ttf', 20)
        textbox_1 = font.render(f"{text1}", True, green, (50, 50, 50))
        textbox_2 = font.render(f"{text2}", True, green, (150, 50, 50))
        text1Rect = textbox_1.get_rect()
        text1Rect.center = (400, 50)
        text2Rect = textbox_2.get_rect()
        text2Rect.center = (400, 550)       
        screen.blit(textbox_1, text1Rect)
        screen.blit(textbox_2, text2Rect)
        
    def speed_spawn(self):
        global speed_item_active
        speed_item_rect.x = random.randint(50,750)
        speed_item_rect.x = random.randint(50,500)
        speed_item_active = True
        
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
            
    def level_builder(self):
        global wall_block
        level1 = [[0, 0, 0, 1, 0, 0, 0, 1], 
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 1, 0, 0, 0], 
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 1, 0, 1, 0], 
                 [1, 0, 0, 0, 0, 0, 0, 1]]
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
        
    def pause_menu(self):
        print("Pausing Game")
        clock = pg.time.Clock()
        paused = True
        while paused:
            screen.fill(white)
            continue_button = button(400, 200, continue_button_img, 2)
            exit_button = button(400, 400, exit_button_img, 2)
            if continue_button.draw():
                break #resumes game loop
            if exit_button.draw():
                pg.quit()
                sys.exit()
            clock.tick(FPS)
            pg.display.update()
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            
        
    #game loop
    def game_loop(self):
        clock = pg.time.Clock()
        frame = 0
        while True:
            #limit fps
            clock.tick(FPS) # limits the frames per second to 60 which is easy to run for all computers
            
            
            global tag_countdown
            global tag_countdown2
            # countdown remover
            if tag_countdown > -300:
                tag_countdown -= 1
            if tag_countdown2 > -300:
                tag_countdown2 -= 1

            # blit characters and screen
            self.blit_images()
            
            #level
            self.level_builder()
            
            # show and calc text
            self.show_text()

            #random number gen to randomly chose when speed boost will spawn
            spawn_chance = 5000
            start_rng = 600 # the amount of frames before the speed boost will spawn
            speed_chance = random.randint(1, spawn_chance)
            if speed_chance == 1234 and not speed_item_active and frame > start_rng:
                print("Number Guessed")
                self.speed_spawn()
            if speed_item_active:
                screen.blit(speed_item, speed_item_rect)
                
            #controls
            self.speed_boost()
            self.char1_wasd()
            self.char2_arrows()
            
            #tagging system
            self.tag()
            
            #pause menu
            if keys_pressed[pg.K_p] == 1:
                self.pause_menu()
            
            frame += 1
            if frame % 100 == 0:
                print(f"Frames Generated: {frame}")
                print(f"Time Elapsed: {pg.time.get_ticks()/1000} \n")
            pg.display.update()
            #print(clock.get_fps())
            
            #exit game
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

print("hi")
game_class = game(60)