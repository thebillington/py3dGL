import os

_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_data(folder, path):
	loc = os.path.join(_ROOT, folder, path)
	print(loc)
	return loc
