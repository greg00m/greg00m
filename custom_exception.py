#!/usr/bin/python3

class FileNotFound(Exception):
	def __init__(self):
		pass

class DogAteHomeworkError(Exception):
	def __init__(self, description):
		self.description = description

try:
	raise DogAteHomeworkError("My dog ate my homework.")
	
except: 
	description=("The dog did not eat my homework")
	print(description)

try:
	raise FileNotFound("The file was not found.")

except:
	description=("The file was found.")
	print(description)
