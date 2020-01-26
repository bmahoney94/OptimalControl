#!/usr/bin/python3


from util import *



# TODO: Incorporate the unittest module and start making assertions
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




def newton1D_test():

	
	def F(x):
		return x**2 + 5*x + 1

	print('Testing the newton1D function.')

	x0 = 15
	
	x, optima = newton1D( F, x0)

	x_analytical, f_analytical = -2.5, F(-2.5)
	print('Local optima at ' + str(x_analytical) + ' of ' + str(f_analytical))
	print('Newton1D returns: ' + str( (x, optima) ) )	

	if abs( optima - f_analytical) > 0.01:
		print('Test failed!')
	
		
	print()

def deriv1D_test():
	def F(x):
		return x**2 + 5*x + 1

	print('Testing the deriv1D function.')
	
	x0 = 0.5
	
	deriv = deriv1D( F, x0)
	deriv_analytical = 2 * x0 + 5

	print('Computed derivative at x=' + str(x0) + ' is ' + str(deriv))
	print('Analytical derivative is ' + str(deriv_analytical))

	if abs(deriv - deriv_analytical) > 0.5:
		print('Test failed!')	
	
	print()



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
	deriv1D_test()
	newton1D_test()
