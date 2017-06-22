#Imports
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from Shapes import Shape, Cube

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
		
		#GL settings
		glEnable(GL_DEPTH_TEST)
		glClearColor(bgcolour[0], bgcolour[1], bgcolour[2], bgcolour[3])
		
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
		
		#If the background colour should be drawn
		if cube.line:
		
			#Start the gl drawing specifying a type of lines
			glBegin(GL_LINES)
			
			#Set the colour
			glColor3fv(cube.linecolour)
			
			#For each of the edges
			for edge in cube.edges:
				#For each of the vertices in the edge
				for vertex in edge:
					#Draw the vertex
					glVertex3fv(cube.vertices[vertex])
					
			#End the gl drawing
			glEnd()
			
		#If the lines should be drawn
		if cube.fill:
	
			#Start the gl drawing specifying a type of lines
			glBegin(GL_QUADS)
			
			#Set the colour
			glColor3fv(cube.fillcolour)
			
			#For each of the surfaces
			for surface in cube.surfaces:
				#For each of the vertices in the surface
				for vertex in surface:
					#Draw the vertex
					glVertex3fv(cube.vertices[vertex])
					
			#End the gl drawing
			glEnd()
		
	#Create a function to update the game state
	def update(self):
		
		#Get the events
		self.events = pygame.event.get()
		
		#Exit condition
		for event in self.events:
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
		pygame.time.wait(10)
		
	#Create a function to return the keys that are currently being pressed
	def getkeys(self):
		return pygame.key.get_pressed()
		
	#Create a function to check whether a specific key is pressed
	def ispressed(self, key):
		
		#Check the user has called the update function before checking keys
		try:
			#Check all events to see if a key has been pressed
			for event in self.events:
				if event.type == KEYDOWN:
					if event.key == key:
						return True
		except AttributeError:
			raise RuntimeError("Ensure you have called 'Game.ispressed()' after 'Game.update()' in your execution.")
			
	#Function to move the camera
	def movecamera(self, x, y, z):
		
		#Translate within the world
		glTranslatef(x, y, z)
			
	#Function to move the camera
	def rotatecamera(self, multi, x, y, z):
		
		#Translate within the world
		glRotatef(multi, x, y, z)
