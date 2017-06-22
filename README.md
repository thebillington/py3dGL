# pyPhys3D
pyPhys3D is a three dimensional physics engine built using Pygame and pyOpenGL.
The engine implementes basic three dimensional collision detections on a non-rotated axis and handles drawing of shapes in 3 dimensions.

### Supported Versions:
* Python 2.7.13

## Contents

### [Installation](#install)

### [Basics](#getting-started)

* [Creating a game](#creating-a-game-object)
* [Shapes](#creating-a-shape)
* [Screen Updates](#updating-the-screen)
* [Shapes properties](#properties-of-shapes)
* [Movement](#physics)
* [Collisions](#collision-detection)
* [Camera](#controlling-the-camera)
* [Key presses](#keys)

### [Examples](#pyphys3d-examples)

* [Gravity](#gravity-example)

## Install

pyPhys3D is set up as a python package and can be installed through pip on Mac OSx, however it is not registered with PyPi and requires manual installation.

To get started using pip read the documentation [here](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip).

There are also some issues with install on Windows (untested on unix) as the setup **data_files** are not installed correctly in the **site-packages/pyPhys3D** folder.
If you know a fix for this issue please contact me and fork a new branch to help me resolve.

pyPhys3D can still be used without installing the package, however it requires manual use of the **Engine.py**, **Shapes.py** and **FileHandler.py** files.
Ensure these files are located in the same folder that you are using to write your game and use:

```python
#Manual imports
from Engine import Game
from Shapes import Cube
```

#### Step One

Clone this repository onto your local file system, either using a Git manager or through terminal with the following command:

```
git clone https://github.com/thebillington/pyPhys3D
```

#### Step Two

Once you have the repository downloaded locally, navigate to the root folder of the project in your terminal window or command prompt. The root folder is the one that holds **setup.py**.

#### Step Three

Now you are ready to run the pip install command install pyPhys3D as a python package:
```
pip install .
```

Depending on your permissions, you may need to run this as root:

```
sudo pip install .
```

And if you already have an earlier version of pyPhys3D installed you may have to use the **upgrade** flag:


```
sudo pip install . --upgrade
```

#### Step Four

The last step is to check that the package has installed correctly. Create a new python file and **import pyPhys3D**:

```python
import pyPhys3D
```

If you get an **ImportError** then you have not installed the package correctly. Go back and ensure you have successfully installed using pip.

## Getting Started

#### Creating a game object

First, create a new game object with the desired title, width, height and background colour:

```python
#Imports
from pyPhys3D import Game, Cube

#Create a new Game(title, width, height, (R,G,B,A))
g = Game("Example Game", 800, 600, (1,1,1,1))
```

The colour must be provided as an RGBA list or tuple.

There are also extra options that can be set, namely the fov (field of view) and minimum/maximum render distances:

```python
g = Game("Example Game", 800, 600, (1,1,1,1), fov=65.0, minr=1.0, maxr=100.0)
```

#### Creating a shape

Creating shapes and adding them to the game for rendering is extremely simple.
So far only cubes are implemented:

```python
#Create some cubes Cube(x,y,z,width,height,depth)
ground = Cube(0, -1, 0, 10, 2, 10)
player = Cube(0, 1, 0, 2, 2, 2)

#Add the shapes to the game
g.addshape(ground)
g.addshape(player)
```

#### Updating the screen

To update the screen, simply create a game loop and call the update function on your game object:

```python
#Game loop
while True:

	#Update the game
	g.update()
```

#### Properties of shapes

It is easy to change the properties of shapes, either at time of instantiation or afterwards:

```python
#Set the background colour and line colour of the ground Cube(x,y,z,width,height,depth,fillcolour=,linecolour=)
ground = Cube(0, -1, 0, 10, 2, 10, fillcolour=(0.4,0.4,0.4), linecolour=(0,0,0))

#Disable line drawing and fill Cube(x,y,z,width,height,depth,line=,fill=)
ground = Cube(0, -1, 0, 10, 2, 10, line=False, fill=False)

#Disable fill and line drawing
ground.enablefill(False)
ground.enableline(False)

#Enable fill and line drawing
ground.enablefill(True)
ground.enableline(True)
```

#### Physics

To move a shape, simply call the move function and provide the values for how much to translate on each axis:

```python
#Move the cube by 1 on each axis
player.move(1, 1, 1)
```

#### Collision Detection

To check for collisions use the collide function on one shape, passing the other shape as a parameter:

```python
#If the player collides with the ground, move them out of the ground (on the y axis)
while player.collide(ground) {
	player.move(0, 0.1, 0)
}
```

#### Controlling the camera

You can move the camera with the **movecamera(x, y, z)** function:

```python
#Move the camera up on the y axis
g.movecamera(0, -10, 0)
```
Note that we have a negative on the y axis to move the camera up.
This actually uses perspective to move the world negatively on the y axis as the camera does not move in the world, the world moves around the camera.

You can rotate the camera with the **rotatecamera(degrees, xaxis, yaxis, zaxis)** function:

```python
#Face the camera 15 degrees to the left (turn negatively through the y axis)
g.rotatecamera(15, 0, -1, 0)
```

When doing multiple rotations you should aim to have one rotation per axis.
Use the positive and negative 1 to flag which axis to turn through and which direction and use the degrees variable to state how much to turn by.

```python
#Rotate 10 on the x axis
g.rotatecamera(10, 1, 0, 0)

#Rotate -15 on the y axis
g.rotatecamera(15, 0, -1, 0)

#Rotate 20 on the z axis
g.rotatecamera(20, 0, 0, 1)
```

The below method looks like it will have the same results as the previous code, but you should not use it as it will have unpredictable functionality:

```python
#DO NOT USE THIS METHOD
g.rotatecamera(1, 10, -15, 20)
```

#### Keys

There are two ways to handle keys:

1. Get a list of all the keys that are currently being pressed (useful for continuous movement)
2. Check whether a specific key has been pressed since the last update (useful for one off events that require debouncing)

The first method is very easy and simply uses the pygame keyboard poll to return a list of keys:

```python
#Import pygame locals
from pygame.locals import *

#Inside the game loop
while True:

	#Get the list of pressed keys
	keys = g.getkeys()
	
	#If the up key is pressed, move the player on the z axis
	if keys[K_UP]:
		player.move(0,0,-1)
````

Note: pyPhys3D uses the default pygame methods for handling key clicks meaning you need to import the locals from pygame.
For a full list of keys see [here](https://www.pygame.org/docs/ref/key.html).

Polling single key presses is also relatively simple:

```python
#Import pygame locals
from pygame.locals import *

#Inside the game loop
while True:

	#Update the game
	g.update()

	#Get the list of pressed keys
	keys = g.getkeys()
	
	#If the space key is clicked, jump
	if g.ispressed(K_SPACE):
		jump()
```
	
Note: Due to the way pygame handles events, you **MUST** call your update function **BEFORE** you call the ispressed function in your game loop.
Failure to do so will lead to a runtime error.

## pyPhys3D Examples

#### Gravity Example

The below piece of code creates a player object and ground object, allowing the player to move around and jump up and down with realistic physics:

```python
#Imports
from pyPhys3D import Game, Cube
from pygame.locals import *

#Create a game object
g = Game("Cube Game", 800, 600, (0.8,0.8,0.8,1), maxr=120)

#Create cubes
ground = Cube(0, -5, -60, 100, 2, 200, fillcolour=(0.4,0.4,0.4))
player = Cube(-2, -3, -25, 2, 2, 2, fillcolour=(1, 0, 0), linecolour=(0, 0, 0))

#Add the cubes to the game
g.addshape(ground)
g.addshape(player)

#Set the movement speed
mspeed = 0.1

#Physics contants
gravity = 0.05
fallspeed = 0.5
yspeed = 0
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
		player.move(0,0,-mspeed)
	if keys[K_s]:
		player.move(0,0,mspeed)
	if keys[K_a]:
		player.move(-mspeed,0,0)
	if keys[K_d]:
		player.move(mspeed,0,0)
		
	#Move the cube by the y speed
	player.move(0, yspeed, 0)
		
	#Gravity
	if yspeed > -fallspeed:
		yspeed -= gravity
		
	#Check if the player has collided with the ground
	if player.collide(ground):
		#Set jumping to false and yspeed to 0
		jumped = False
		yspeed = 0
		#Move the player out of the ground
		while player.collide(ground):
			player.move(0, gravity, 0)
		
	#Check if the space key is pressed and the player isn't currently jumping
	if g.ispressed(K_SPACE) and not jumped:
		yspeed = jumpspeed
		jumped = True
```

[![Gravity Example on Youtube](https://img.youtube.com/vi/BhxI-G_h5Z8/0.jpg)](https://www.youtube.com/watch?v=BhxI-G_h5Z8)
