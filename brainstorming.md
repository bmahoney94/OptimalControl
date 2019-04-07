This file is just a place for me to throw down ideas as they come to me in the hopes that I
will later revisit them and flesh them out a bit.




### IDEA 1:  Creating a more flexible way to integrate an ODE system.  

Currently, all of my attempts to write an ODE system are very procedural, and have
an excess of parameters that have to be passed around.  It can get very tedious and ugly.
I'd like to have something better and more object oriented.


##### DynamicalSystem Interface:
So what should the interface look like?

  * I can use a function to compute the right hand side of the ODE.
  * At the end, I need a solution vector for each timestep.
  * Once the ODE system is constructed, input an initial condition(1), control history(2), and 
	a time discretization(3), returns the solution computed at those points in time.


##### PseudoCode

    class DynamicalSystem
	    def __init__( RHS( t, x, u)) 
		    call a factory method by using the supplied RHS
	
	    def integrate( t, x0, u)
		    Compute the solution using the chosen algorithm

	    def step
		    Compute the solution using a unit step control input.

	    def impulse
		    Compute the solution using an approximate impulse input.
	
 	    def plot( dimension=1)
		    Plot time series for a particular dimension(or return one!)
	    
	    def phase_plot() 

    # Linear model
    def RHS( t, x, u):
	    create F
	    create G
    	return numpy.dot( F, x) + nump.dot( G, u)
			
##### Notes:
  * I'd kind of like to be capable of swapping out integration methods.  That may take
		some finagling.  It may require the use of a Strategy pattern.

  * To allow me to create different kinds of systems(linear, nonlinear w/ defined functions,
		interpolation tables, etc.) it may make sense to use a factory method of some sort.
	
  * The RHS is a supplied function with a standard interface.
	
  * The underlying ODE may not actually be system dependent.  As such, I could make an ODE 
		object within a DynamicalSystem object.

##### Test Cases:
	Use an LTI system with a known solution(like harmonic motion).
	Plot the integrated and exact solutions to compare.


##### System types to explore in the future:
	* LTI systems
	* Linear time varying systems
	* Nonlinear systems with analytical RHS defintions
	* Nonlinear systems with lookup tables for their parameters
	* Special functionality(maybe) for multivariable systems(cross plots, eigenvectors, etc.)

******

###  IDEA 2:  A potentially less bulky solution to iterating during time integration

 * Define a class for state vectors.  Use this for System States, Control States, and possibly
	Parameter States.  In essence, this is a 'struct' I think.
 * Define a class for collections of state vectors.
 * Implement an iterator for the StateArray object.
 * Provide a way to name the elements of the vector.  The StateArray should keep a copy of this.


##### PseudoCode
    class State:
	    pass

    class StateArray:
	    def __init__:
		    pass

	    def __iter__:
		    return State_Iterator(self.data)
    	def plot(index_i, index_j):
	    	plt.plot(index_i, index_j)


    # This could likely be implemented in StateArray.`
    class StateIterator:
	    """  An iterator for state array objects.  Code taken from 'Python for
		    	Computational Science'.
	    """
	    def __init__(self,data):
		    self.index = 0
		    self.data = data

	    def next(self):
		    if self.index < len(self.data):
			    item = self.data[self.index]
			    self.index += 1
			    return item
		    else:
			    raise StopIteration
##### Notes:
  * This might be overlapping a bit with 'Idea 1' listed above.  


