#Imports
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from shapes import Shape, Cube

#Create a game class
class Game(object):
	
	#Constructor
	def __init__(self, title, width, height, bgcolour):
		
		#Initialise pygame
		pygame.init()

		#Set the size of the window
		self.size = self.width, self.height = width, height
		
		#Set the default perspective and clipping distances
		self.fov = 45.0
		self.aspectratio = width / height
		self.minrender = 0.1
		self.maxrender = 80
		
		#Set the pygame mode to use double buffering and open gl
		pygame.set_mode(self.size, DOUBLEBUF|OPENGL)
		
		#Set the perspective
		self.setperspective()
		
		#Create an empty list of shapes to render
		self.shapes = []
		
	#Create a function to update the perspective
	def setperspective(self):
		
		#Set the perspective
		gluPerspective(self.fov, self.aspectratio, self.minrender, self.maxrender)
		
	#Create a function to add a shape
	def addshape(self, s):
		self.shapes.append(s)
		
	#Create a function to render the shapes
	def render(self):
		#For each of the shapes, check the type and render it
		for s in shapes:
			#If the shape is a cube, call the rendercube method
			if s.type == Shape.CUBE:
				rendercube(s)
	
