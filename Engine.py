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
		
		#Set the window caption
		pygame.display.set_caption(title)

		#Set the size of the window
		self.size = self.width, self.height = width, height
		
		#Set the default perspective and clipping distances
		self.fov = 45.0
		self.aspectratio = width / height
		self.minrender = 0.1
		self.maxrender = 80
		
		#Set the pygame mode to use double buffering and open gl
		pygame.display.set_mode(self.size, DOUBLEBUF|OPENGL)
		
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
		for s in self.shapes:
			#If the shape is a cube, call the rendercube method
			if s.type == Shape.CUBE:
				self.rendercube(s)
				
	#Create a function to render a cube
	def rendercube(self, cube):
	
		#Start the gl drawing specifying a type of lines
		glBegin(GL_QUADS)
		
		#Set the colour
		glColor3fv((1, 0, 1))
		
		#For each of the surfaces
		for surface in cube.surfaces:
			#For each of the vertices in the surface
			for vertex in surface:
				#Draw the vertex
				glVertex3fv(cube.vertices[vertex])
				
		#End the gl drawinf
		glEnd()
		
		#Start the gl drawing specifying a type of lines
		glBegin(GL_LINES)
		
		#Set the colour
		glColor3fv((1, 1, 1))
		
		#For each of the edges
		for edge in cube.edges:
			#For each of the vertices in the edge
			for vertex in edge:
				#Draw the vertex
				glVertex3fv(cube.vertices[vertex])
				
		#End the gl drawing
		glEnd()
		
	#Create a function to update the game state
	def update(self):
		
		#Exit condition
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		#Clear the buffers
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		#Draw the shapes
		self.render()
		
		#Update the display
		pygame.display.flip()
		
#Create a game object
g = Game("Cube Game", 800, 600, 1)

#Create a cube
c = Cube(0, 0, -5, 1, 1, 1)

#Add the cube to the game
g.addshape(c)

#Game loop
while True:
	
	#Update
	g.update()
