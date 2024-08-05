# Sammy Knorr jsm8st and James Richard mxs7mm

import pygame
import gamebox

# Our game covers the four required features as well as player sprite animation, health bars, two players, and an
# ability to restart from game over as our optional features. There are comments within the code that say when each
# feature is implemented.

# To play the game, player 1 used the W and S keys to move and the D key to shoot, player 2 used the up and down keys
# to move and the left key to shoot. Each player has a health bar of 5 shots and the first player to lose their full
# health bar looses. After someone wins the game over screen is showed, and you can press the space bar to restart.

# The previous checkpoints are included at the end of this file as comments. We made no changes to our original plans.

# Our window is within the required limit and is our third required feature.
camera = gamebox.Camera(800, 600)

# Here the background and player sprites are added for movement which is our first optional feature and fourth
# required feature.
player_images = gamebox.load_sprite_sheet("hero-spritesheet.png", 1, 6)
background = gamebox.from_image(400, 300, "coding_project_background.png")
# Here all the objects are created including the two players which is our second optional feature
p1 = gamebox.from_image(40, 300, player_images[-1])
p2 = gamebox.from_image(760, 300, player_images[-1])
healthbar1 = gamebox.from_color(140, 20, "white", 105, 25)
healthbar2 = gamebox.from_color(660, 20, "white", 105, 25)
bottom = gamebox.from_color(800, 600, 'black', 8000, 1)
top = gamebox.from_color(800, 0, 'black', 8000, 1)
current_frame1 = 0
current_frame2 = 0

# These object lists are for the health bars which is our third optional feature
p1_health_bar = [gamebox.from_color(100, 20, "green", 18, 20),
                gamebox.from_color(120, 20, "green", 18, 20),
                gamebox.from_color(140, 20, "green", 18, 20),
                gamebox.from_color(160, 20, "green", 18, 20),
                gamebox.from_color(180, 20, "green", 18, 20),]

p2_health_bar = [gamebox.from_color(620, 20, "green", 18, 20),
                gamebox.from_color(640, 20, "green", 18, 20),
                gamebox.from_color(660, 20, "green", 18, 20),
                gamebox.from_color(680, 20, "green", 18, 20),
                gamebox.from_color(700, 20, "green", 18, 20),]
game_over = gamebox.from_text(400, 100, "GAME OVER", 100, "red")

p1_bullets_list = []
p2_bullets_list = []
counter1 = 0
counter1_1 = 0
counter2 = 0
counter2_2 = 0
p1_counter = 0
p2_counter = 0
p1_score = 5
p2_score = 5
gameon = True

def bullets(keys):
   """
   :param keys: user pressing keys
   :return: bullet objects
   In order to get continuous movement, all bullets in each list are constantly moving. This function adds a new bullet
   to the list for each player when the respective key is pressed. It also resets the counter to 0, so the player has
   to wait for about half a second before firing again.
   """
   global counter1
   global counter2
   if counter1_1 >= 1:
       if pygame.K_d in keys:
           counter1 = 0
           p1_bullets_list.append(gamebox.from_color(100, p1.y - 20, "red", 10, 5))
   if counter2_2 >= 1:
       if pygame.K_LEFT in keys:
           counter2 = 0
           p2_bullets_list.append(gamebox.from_color(700, p2.y - 20, "red", 10, 5))


def p_health():
   """
   :return: Health bar objects
   This function deletes a block from the health bar when the player is hit, and also lowers the score.
   """
   global p1_score
   global p2_score
   for bullet in p2_bullets_list:
       if bullet.touches(p1):
            del p1_health_bar[0]
            del p2_bullets_list[0]
            p1_score -= 1
   for bullet in p1_bullets_list:
       if bullet.touches(p2):
            del p2_health_bar[0]
            del p1_bullets_list[0]
            p2_score -= 1


def gameover():
   """
   :return: new bool for gameon
   This function freezes the game when a player's health reaches zero, and prints a "game over message"
   """
   global gameon
   if p1_score == 0:
       gameon = False
   if p2_score == 0:
       gameon = False
   # if p1_health_bar == []:
   #     camera.draw(game_over)
   # elif p2_health_bar == []:
   #     camera.draw(game_over)


flip = True
def movement(keys):
   """
   :param keys: This parameter is the keys the user inputs
   :return: The sprites of both players moving up and down with the user's input with animation
   This function takes moves player 1 up and down using W and S and moves player 2 by using the UP and DOWN key. it also
   adds animation to the sprites movement.
   """
   #  This function takes in user input using the w,s, up, and down keys and is our first recquired feature
   global current_frame1
   global current_frame2
   global flip
   player1_move = False
   player2_move = False
   if flip:
       p2.flip()
       flip = False

   if pygame.K_UP in keys:
      p2.y -= 5
      player2_move = True
   if pygame.K_DOWN in keys:
      p2.y += 5
      player2_move = True

   if pygame.K_w in keys:
      p1.y -= 5
      player1_move = True
   if pygame.K_s in keys:
      p1.y += 5
      player1_move = True

   if player1_move:
      current_frame1 += .3
      if current_frame1 >= 6:
         current_frame1 = 0
      p1.image = player_images[int(current_frame1)]

   if player2_move:
      current_frame2 += .3
      if current_frame2 >= 6:
         current_frame2 = 0
      p2.image = player_images[int(current_frame2)]
   p1.move_to_stop_overlapping(bottom)
   p2.move_to_stop_overlapping(bottom)
   p1.move_to_stop_overlapping(top)
   p2.move_to_stop_overlapping(top)


def tick(keys):
   """
   :param keys: user pressing keys
   :return: the game
   This function is run 30 times a second, and calls all functions as well as keeping any bullets moving.
   It also draws every gamebox.
   """
   global gameon
   global p1_score
   global p2_score
   global p2_health_bar
   global p1_health_bar
   global counter1
   global counter1_1
   global counter2
   global counter2_2
   camera.clear('black')
   if gameon:
       # Each function is run 30 times a second
       gameover()
       movement(keys)
       bullets(keys)
       p_health()
       camera.draw(background)
       camera.draw(p1)
       camera.draw(p2)
       camera.draw(healthbar1)
       camera.draw(healthbar2)
       for each in p1_health_bar:
           camera.draw(each)
       for each in p2_health_bar:
           camera.draw(each)

       for bullet in p1_bullets_list:
           camera.draw(bullet)
           bullet.x += 20
           if bullet.x >= 900:
               del p1_bullets_list[0]
       for bullet in p2_bullets_list:
           camera.draw(bullet)
           bullet.x -= 20
           if bullet.x <= -100:
               del p2_bullets_list[0]
           # These counters make it so the bullets have a cooldown before they can shoot again
       counter1 = int((counter1 + 1))
       counter1_1 = int(counter1 / 30)
       counter2 = int(counter2 + 1)
       counter2_2 = int(counter2 / 30)

   if gameon == False:
       # Here is where the game over screen is drawn and is our second recquired feature
       camera.draw(game_over)
       if p1_score == 0:
           camera.draw(gamebox.from_text(400, 300, "Player 2 Wins", 100, "red"))
       elif p2_score == 0:
           camera.draw(gamebox.from_text(400, 300, "Player 1 Wins", 100, "red"))
       camera.draw(gamebox.from_text(400, 500, "Press Space to Play Again", 75, "red"))
       if pygame.K_SPACE in keys:
           # This statement allows to restart the game without closing the window and is our fourth optional feature
           gameon = True
           p1_score = 5
           p2_score = 5
           p2_health_bar = [gamebox.from_color(620, 20, "green", 18, 20),
                            gamebox.from_color(640, 20, "green", 18, 20),
                            gamebox.from_color(660, 20, "green", 18, 20),
                            gamebox.from_color(680, 20, "green", 18, 20),
                            gamebox.from_color(700, 20, "green", 18, 20), ]
           p1_health_bar = [gamebox.from_color(100, 20, "green", 18, 20),
                            gamebox.from_color(120, 20, "green", 18, 20),
                            gamebox.from_color(140, 20, "green", 18, 20),
                            gamebox.from_color(160, 20, "green", 18, 20),
                            gamebox.from_color(180, 20, "green", 18, 20), ]


   camera.display()


gamebox.timer_loop(30, tick)

# CHECKPOINT 1

# Sammy Knorr jsm8st and James Richard mxs7mm

# Description: Our game will be a 1v1 battle between two playable characters which are fighting one and other. It will
# allow for two people to play, and they will be using "guns" to try and damage each other. The player who deals the
# required amount of damage will win. The players have health bars and when they are struck a portion of their health
# bar depletes. Players will be able to gain health back by shooting a moving collectable.

# Required Features:

# User Input
#   W-S, movement keys for player 1
#   Up-Down, movement keys for player 2

# Game Over
#   When one player's health runs out, show game over screen and which player won

# Small Enough Window
#   The game window will be 800 width, 600 height

# Graphics/Images
#   Each player will be an image
#   Background is image
#   Health power up is image

# Optional Features:

# Collectables
#   There will be a health power up that drops from above, and if hit will restore a portion of health to the player
#   that hit it.

# Health Bar
#   Each player will have a health bar that goes down when they are hit, and goes up if they get the collectable.

# Two Players Simultaneously
#   The game centers around to players battling each other

# Restart from Game Over:
#   After a player wins, you can hit a button and restart the game without closing the window


# CHECKPOINT 2

# # Sammy Knorr jsm8st and James Richard mxs7mm
#
# # Description: Our game will be a 1v1 battle between two playable characters which are fighting one and other. It will
# # allow for two people to play, and they will be using "guns" to try and damage each other. The player who deals the
# # required amount of damage will win. The players have health bars and when they are struck a portion of their health
# # bar depletes. Players will be able to gain health back by shooting a moving collectable.
#
# # Required Features:
#
# # User Input
# #   W-S, movement keys for player 1
# #   Up-Down, movement keys for player 2
#
# # Game Over
# #   When one player's health runs out, show game over screen and which player won
#
# # Small Enough Window
# #   The game window will be 800 width, 600 height
#
# # Graphics/Images
# #   Each player will be an image
# #   Background is image
# #   Health power up is image
#
# # Optional Features:
#
# # Collectables
# #   There will be a health power up that drops from above, and if hit will restore a portion of health to the player
# #   that hit it.
#
# # Health Bar
# #   Each player will have a health bar that goes down when they are hit, and goes up if they get the collectable.
#
# # Two Players Simultaneously
# #   The game centers around to players battling each other
#
# # Restart from Game Over:
# #   After a player wins, you can hit a button and restart the game without closing the window
#
#
# # CODE:
#
# import pygame
# import gamebox
# camera = gamebox.Camera(800, 600)
#
# # Current sprite is a stand in and grader will have to download the sprite sheet which is a dude holding a sword and has
# # four positions and can be found if you look up the file name and is called adventure style character sheet
# player_images = gamebox.load_sprite_sheet("hobbit-style-sprite-sheet-walk-left.png", 1, 4)
# background = gamebox.from_image(400, 300, "grass_14.png")
# p1 = gamebox.from_image(20, 300, player_images[-1])
# p2 = gamebox.from_image(780, 300, player_images[-1])
# healthbar1 = gamebox.from_color(140, 20, "white", 105, 25)
# healthbar2 = gamebox.from_color(660, 20, "white", 105, 25)
# current_frame = 0
#
# p1_health_bar = [gamebox.from_color(100, 20, "red", 18, 20),
#                 gamebox.from_color(120, 20, "red", 18, 20),
#                 gamebox.from_color(140, 20, "red", 18, 20),
#                 gamebox.from_color(160, 20, "red", 18, 20),
#                 gamebox.from_color(180, 20, "red", 18, 20),]
#
# p2_health_bar = [gamebox.from_color(620, 20, "green", 18, 20),
#                 gamebox.from_color(640, 20, "green", 18, 20),
#                 gamebox.from_color(660, 20, "green", 18, 20),
#                 gamebox.from_color(680, 20, "green", 18, 20),
#                 gamebox.from_color(700, 20, "green", 18, 20),]
# game_over = gamebox.from_text(400, 300, "GAME OVER", 100, "red", True, False)
#
# p1_bullets_list = []
# p2_bullets_list = []
# counter1 = 0
# counter1_1 = 0
# counter2 = 0
# counter2_2 = 0
# p1_counter = 0
# p2_counter = 0
# p1_score = 5
# p2_score = 5
#
# def bullets(keys):
#    global counter1
#    global counter2
#    if counter1_1 >= 1:
#        if pygame.K_d in keys:
#            counter1 = 0
#            p1_bullets_list.append(gamebox.from_color(20, p1.y, "red", 10, 5))
#    if counter2_2 >= 1:
#        if pygame.K_LEFT in keys:
#            counter2 = 0
#            p2_bullets_list.append(gamebox.from_color(780, p2.y, "green", 10, 5))
#
# def p_health():
#    global p1_score
#    global p2_score
#    for bullet in p2_bullets_list:
#        if bullet.touches(p1):
#            del p1_health_bar[0]
#            del p2_bullets_list[0]
#            p1_score -= 1
#    for bullet in p1_bullets_list:
#        if bullet.touches(p2):
#            del p2_health_bar[0]
#            del p1_bullets_list[0]
#            p2_score -= 1
#
# def gameover():
#    if p1_score == 0:
#        camera.draw(game_over)
#    if p2_score == 0:
#        camera.draw(game_over)
#
#
# def movement(keys):
#    global current_frame
#    player1_move = False
#    player2_move = False
#    if pygame.K_UP in keys:
#       p2.y -= 5
#       player2_move = True
#    if pygame.K_DOWN in keys:
#       p2.y += 5
#       player2_move = True
#
#    if pygame.K_w in keys:
#       p1.y -= 5
#       player1_move = True
#    if pygame.K_s in keys:
#       p1.y += 5
#       player1_move = True
#
#    if player1_move:
#       current_frame += .3
#       if current_frame >= 4:
#          current_frame = 0
#       p1.image = player_images[int(current_frame)]
#
#    if player2_move:
#       current_frame += .3
#       if current_frame >= 4:
#          current_frame = 0
#       p2.image = player_images[int(current_frame)]
#
# def tick(keys):
#    global counter1
#    global counter1_1
#    global counter2
#    global counter2_2
#    camera.clear('black')
#
#    movement(keys)
#    bullets(keys)
#    p_health()
#    gameover()
#
#    camera.draw(background)
#    camera.draw(p1)
#    camera.draw(p2)
#    camera.draw(healthbar1)
#    camera.draw(healthbar2)
#    for each in p1_health_bar:
#       camera.draw(each)
#    for each in p2_health_bar:
#       camera.draw(each)
#
#    for bullet in p1_bullets_list:
#       camera.draw(bullet)
#       bullet.x += 10
#       if bullet.x >= 900:
#          del p1_bullets_list[0]
#    for bullet in p2_bullets_list:
#       camera.draw(bullet)
#       bullet.x -= 10
#       if bullet.x <= -100:
#          del p2_bullets_list[0]
#       # bullet lag
#    counter1 = int((counter1 + 1))
#    counter1_1 = int(counter1 / 30)
#    counter2 = int(counter2 + 1)
#    counter2_2 = int(counter2 / 30)
#    print(p2_bullets_list)
#    camera.display()
#
# gamebox.timer_loop(30, tick)
