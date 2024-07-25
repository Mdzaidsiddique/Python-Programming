# scope: a variable available only inside the region it is created.


# Built-in Scope 
from math import pi 

# pi = 'global pi variable' 

def outer(): 
	# pi = 'outer pi variable' (enclosed scope)
	def inner(): #closure 
		# pi = 'inner pi variable' 
		print(pi) 
	inner() 

outer() 
