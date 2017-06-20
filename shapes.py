#Create a function to get a mesh file 'f'
def getMesh(fname):
	
	#Open the file
	f = open(fname, "r")
	
	#Store the lines as a list
	f = list(f)
	
	#Strip newlines from the list
	for l in range(len(f)):
		f[l] = f[l].replace("\n","")
	
	#Store the number of vertices, edges and sides
	v = int(f[0])
	e = int(f[1])
	s = int(f[2])
	
	#Create empty lists to hold the data
	vertices = []
	edges = []
	sides = []
	
	#Loop over all of the vertices and add them to the list
	for i in range(3, v + 3):
		
		#Split the vertex into a list of coordinates
		vertex = f[i].split(",")
		
		#Turn the coordinates into integers and append to the vertex
		vertices.append((int(vertex[0]), int(vertex[1]), int(vertex[2])))
	
	#Loop over all of the edges and add them to the list
	for i in range(v + 3, e + v + 3):
		
		#Split the edge into a list of vertices
		edge = f[i].split(",")
		
		#Turn the vertices indexes into integers and add to the side
		edges.append((int(edge[0]), int(edge[1])))
	
	#Loop over all of the sides and add them to the list
	for i in range(e + v + 3, s + e + v + 3):
		
		#Split the side into a list of vertices
		side = f[i].split(",")
		
		#Create a new side list to hold the data
		newside = []
		
		#For each vertex index in the side, add it to the new side variable
		for p in side:
			newside.append(int(p))
			
		#Add the side to the list of sides
		sides.append(tuple(newside))
		
	#Return the data
	return (vertices, edges, sides)
	
#Create a class to hold the properties of a basic shape
class Shape(object):
	
	#Types
	POINT = "point"
	CUBE = "cube"
	
	#Constructor
	def __init__(self, x, y, z, type):
		
		#Store the parameters
		self.x = x
		self.y = y
		self.z = z
		self.type = type

	#Define pythagoral function
	def pythagoras(self, s):

		#Return the distance between the shapes
		return math.sqrt(math.pow(abs(self.x - s.x) , 2) + math.pow(abs(self.y - s.y)) + math.pow(abs(self.z - s.z), 2))

