#Imports
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from shapes import Shape, Cube

#Create a game class
class Game(object):
	
	#Constructor
	def __init__(self, title, width, height, bgcolour, fov=45, minr=0.1, maxr=80):
		
		#Initialise pygame
		pygame.init()
		
		#Set the window caption
		pygame.display.set_caption(title)

		#Set the size of the window
		self.size = self.width, self.height = width, height
		
		#Set the default perspective and clipping distances
		self.fov = fov
		self.aspectratio = width / height
		self.minrender = minr
		self.maxrender = maxr
		
		#Set the pygame mode to use double buffering and open gl
		pygame.display.set_mode(self.size, DOUBLEBUF|OPENGL)
		
		#Create an empty list of shapes to render
		self.shapes = []
		
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
		glColor3fv(cube.colour)
		
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
			if event.type == QUIT:
				pygame.quit()
				quit()
			if event.type == KEYDOWN:
				if event.key == K_q:
					pygame.quit()
					quit()
				
		#Clear the buffers
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		#Draw the shapes
		self.render()
		
		#Update the display
		pygame.display.flip()
		
#Create a game object
g = Game("Cube Game", 800, 600, 1, maxr=120)

#Create cubes
ground = Cube(0, -5, -60, 10, 2, 100, (0.4,0.4,0.4))
c = Cube(0, -1, -5, 1, 1, 1, (1, 0, 0))

#Add the cubes to the game
g.addshape(ground)
g.addshape(c)

#Game loop
while True:
	
	#Update
	g.update()
