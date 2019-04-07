#!/usr/bin/python3


from util import *

## Tests ###

def gradient_test():
	""" The gradient of F at (0,0) should be:  (-4. 6)
		
		Passing the test means the yielded result is 'close'.

	"""
	def F( x):
		return (x[0] - 2)**2 + (x[1] + 3)**2 + 5
	x = [0,0]

	print('\nTesting Gradient Function')
	grad = gradient( F, x)

	print( 'The gradient of F at ' + str(x) + ' is ' + str(grad) )
	print()	

def gradient_descent_test():
	""" This tests the basic functionality of the gradient_descent function. """
	#TODO: This function's code is being copied elsewhere.  Consider breaking it out as a common
	#		test 'fixture' of sorts. 
	def F( x): 
		""" Takes two scalar inputs (x, y) and returns a scalar output.
			
			The min of the function F(x, y) = (x-2)**2 + (y+3)**2 + 5 occurs at the location of
			its vertex: (x,y) = (2, -3).
		"""
		F = (x[0]-2)**2 + (x[1]+3)**2 + 5
		return F

	initial_guess = np.array([ 0, 0])
	
	print('Testing the gradient_descent function')	
	value, location = gradient_descent( F, initial_guess)
	print('Computed min of ' + str(value) + ' at ' + str(location))	
	print('Actual min of ' + str(5) + ' at ' + str((2, -3)) )
	print()


def newton_raphson_test():
	""" This tests the basic functionality of the newton_raphson function. """
	#TODO: This function's code is being copied elsewhere.  Consider breaking it out as a common
	#		test 'fixture' of sorts. 
	def F( x): 
		""" Takes two scalar inputs (x, y) and returns a scalar output.
			
			The min of the function F(x, y) = (x-2)**2 + (y+3)**2 + 5 occurs at the location of
			its vertex: (x,y) = (2, -3).
		"""
		F = (x[0]-2)**2 + (x[1]+3)**2 + 5
		return F

	initial_guess = np.array([ 0, 0])
	
	print('Testing the newton_raphson function')	
	value, location = newton_raphson( F, initial_guess)
	print('Computed min of ' + str(value) + ' at ' + str(location))	
	print('Actual min of ' + str(5) + ' at ' + str((2, -3)) )
	print()



def getHessian_test():
	def F( x): 
		""" Takes two scalar inputs (x, y) and returns a scalar output.
			
			The min of the function F(x, y) = (x-2)**3 + (y+3)**3 + 5 occurs at the location of
			its vertex: (x,y) = (2, -3).
		"""

		# NOTE: This is different from elsewhere!  This function is cubic!
		F = (x[0]-2)*3 + (x[1]+3)**3 + 5
		return F

	def hess( x, y):
		return np.array([ [6 * (x-2), 0], [0, 6 * (y+3)]])
	
	
	print('Testing the getHessian function')
	x = [0, 0]
	hessian = getHessian( F, x)	
	 
	print('Computed Hessian at (0, 0): ' + str(hessian))
	print('Analytical Hessian at (0, 0): ' + str( hess( x[0], x[1])))


def quad_test():
	t = np.linspace(0,10)
	f = np.ones(len(t))

	print('Testing the Quad function.')
	print(Quad( f, t))
	


##  IF: main ##

if  __name__ == '__main__':
	import sys
	
	quad_test()
	gradient_test()
	gradient_descent_test()
	newton_raphson_test()
	getHessian_test();

