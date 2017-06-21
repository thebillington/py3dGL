#Imports
from Engine import Game
from Shapes import Cube

from pygame.locals import *

#Create a game object
g = Game("Cube Game", 800, 600, (0.8,0.8,0.8,1), maxr=120)

#Create cubes
ground = Cube(0, -5, -60, 100, 2, 200, bgcolour=(0.4,0.4,0.4))
player1 = Cube(-2, -3, -25, 2, 2, 2, bgcolour=(1, 0, 0), linecolour=(0, 0, 0))
player2 = Cube(2, -3, -25, 2, 2, 2, bgcolour=(0, 1, 0), linecolour=(0, 0, 0))

#Add the cubes to the game
g.addshape(ground)
g.addshape(player1)
g.addshape(player2)

#Set the movement speed
mspeed = 0.1

#Physics contants
gravity = 0.05
fallspeed = 0.5
p1yspeed = 0
p2yspeed = 0
jumpspeed = 1
jumped = False

#Set the initial camera angle
g.movecamera(0, -10, 0)
g.rotatecamera(15, 1, 0, 0)

#Game loop
while True:
	
	#Update
	g.update()
	
	#Get the pressed keys
	keys = g.getkeys()
	
	#Movement
	if keys[K_w]:
		player1.move(0,0,-mspeed)
	if keys[K_s]:
		player1.move(0,0,mspeed)
	if keys[K_a]:
		player1.move(-mspeed,0,0)
	if keys[K_d]:
		player1.move(mspeed,0,0)
	if keys[K_UP]:
		player2.move(0,0,-mspeed)
	if keys[K_DOWN]:
		player2.move(0,0,mspeed)
	if keys[K_LEFT]:
		player2.move(-mspeed,0,0)
	if keys[K_RIGHT]:
		player2.move(mspeed,0,0)
		
	#Move the cube by the y speed
	player1.move(0, p1yspeed, 0)
		
	#Gravity
	if p1yspeed > -fallspeed:
		p1yspeed -= gravity
		
	#Check if the player has collided with the ground
	if player1.collide(ground):
		#Set jumping to false and yspeed to 0
		jumped = False
		p1yspeed = 0
		#Move the player out of the ground
		while player1.collide(ground):
			player1.move(0, gravity, 0)
		
	#Check if the space key is pressed and the player isn't currently jumping
	if g.ispressed(K_SPACE) and not jumped:
		p1yspeed = jumpspeed
		jumped = True
