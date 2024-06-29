import numpy as np
from OCPUtil import *
import pytest

## Fixtures
def F( x):
    """ Takes two scalar inputs (x, y) and returns a scalar output.
    	
    	The min of the function F(x, y) = (x-2)**2 + (y+3)**2 + 5 occurs at the location of
    	its vertex: (x,y) = (2, -3).
    """
    F = (x[0]-2)**2 + (x[1]+3)**2 + 5
    return F


def F_1D( x):
    return x**2 + 5*x + 1


## Tests
def test_gradient():
    """ The gradient of F at (0,0) should be:  (-4. 6)"""
    x = [0,0]

    print('\nTesting Gradient Function')
    grad = gradient( F, x)

    assert( grad[0] == pytest.approx( -4.0, abs=1e-4))
    assert( grad[1] == pytest.approx( 6.0, abs=1e-4))


def test_gradient_descent():
    """ This tests the basic functionality of the gradient_descent function. """
    initial_guess = np.array([ 0, 0])
    
    print('Testing the gradient_descent function')	
    value, location = gradient_descent( F, initial_guess)
    
    assert( value == pytest.approx( 5., abs=1e-3))
    assert( location == pytest.approx( (2., -3.), abs=1e-3))

def test_newton1D():
    print('Testing the newton1D function.')
    x0 = 15
    x, optima = newton1D( F_1D, x0)
    x_analytical, f_analytical = -2.5, F_1D(-2.5)
    print('Local optima at ' + str(x_analytical) + ' of ' + str(f_analytical))
    print('Newton1D returns: ' + str( (x, optima) ) )	
    
    assert( optima == pytest.approx( -5.25))

def test_deriv1D():
    print('Testing the deriv1D function.')
    x0 = 0.5
    deriv = deriv1D( F_1D, x0)
    deriv_analytical = 2 * x0 + 5
    
    print('Computed derivative at x=' + str(x0) + ' is ' + str(deriv))
    print('Analytical derivative is ' + str(deriv_analytical))
    
    assert( deriv == pytest.approx( deriv_analytical, abs=1e-2))



def test_quad():
    t = np.linspace(0,10)
    f = np.ones(len(t))
    
    print('Testing the Quad function.')
    print(Quad( f, t))
    assert( Quad( f, t) == pytest.approx( 10.))	

##  IF: main ##

if  __name__ == '__main__':
	
	test_quad()
	test_gradient()
	test_gradient_descent()
	test_deriv1D()
	test_newton1D()
