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
	
