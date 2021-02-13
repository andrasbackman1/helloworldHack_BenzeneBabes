"""
Intends to simulate the motion of molecules of an ideal gas using cellular automation.

#### SPACE FOR MORE FEATURES ###


"""
from molecules import Molecule
from random import randint
from math import sin, cos, sqrt
import scipy.stats as stats
import matplotlib.pyplot as plt


class simulation(object):
    """
    Attributes:
    * Temperature
    * Number of molecules / density
    * Size of array
    * Dimensions (literall size in nm)


    Methods:
    * Controlling methods
        Calls on the other methods to do their thing
    * Initial Positions (from temperature)
        Use randint to get positons and get the velocities (somehow)
    * Iterator/times stepper
        responsible for updating the array each time step
    * Animation as a method of this class??
        Could also be its own class
    """

    def __init__(self, temperature = 298.15, size = 500, steps = 50, density = 0.01): # Think it should take temperature, density/number of molecules, size, number of time Steps, and array size
        self.temperature = temperature
        self.size = size
        self.steps = steps
        self.density = density

        # Creating an n x n array
        lst=[0 for i in range(self.size)]
        # Indexing is [i][j] where i is the row and j is the column
        self.array = [lst for j in range(self.size)]


        self.controller()
        pass

    def controller(self):
        array = self.initiateArray(self.array, self.temperature)
        # update animation here
        array = self.iterator(array)
        print("finished")
        pass

    def initiateArray(self, array, temperature):
        """
        Method called by class constructor and sets the inital 
        positions and velocities of the molecules.
        
        Positions are simply randomly generated (using randint method) 
        but the velocites need to be fitted to a boltzmann distribution.

        INPUTS:
        Temperature (>0 K)
        Array (2D slice of a 3D array)

        RETURNS:
        Modified array
        """
        number_of_molecules = int(self.density*self.size**2)

        x_indexies = [randint(0, self.size - 1) for i in range(number_of_molecules)]
        y_indexies = [randint(0, self.size - 1) for i in range(number_of_molecules)]
        
        theta = [randint(0, 360) for i in range(number_of_molecules)]
        velocities = self.generateVelocities(number_of_molecules)
        for i in range(len(x_indexies)):
            x_vel = velocities[i]*cos(theta[i])
            y_vel = velocities[i]*sin(theta[i])
            print(x_vel,y_vel)

            array[y_indexies[i]][x_indexies[i]] = Molecule(1, (x_indexies[i], y_indexies[i]), (x_vel, y_vel))
        
        return array 
    
    def generateVelocities(self, array_size):
        boltzmann_constant = 1.38*10**-23
        Hydrogen_mass = 1.67*10**-27
        rms_velocity = sqrt((3*boltzmann_constant*self.temperature)/Hydrogen_mass)

        maxwell = stats.maxwell
        data = maxwell.rvs(loc=0, scale=rms_velocity, size=10000)
        params = maxwell.fit(data, floc=0)

        velocities = maxwell.rvs(*params, size=array_size)
        
        return velocities 

    def iterator(self, array):
        """
        Iterates over array. Calls on the precent objects to update their positions.
        Somehow if new_position = another molecule or is beyond wall it should flip.

        INPUT:
        Array

        Ouput:
        Modified Array
        """
        new_array = array.copy()

        for row in new_array:
            for element in row:
                if element == 0:
                    continue
                else:
                    newX, newY = element.updatePosition() ## x and y are integers that correspond to their new index
                    #new_array[newY][newX] = element
                    
        return new_array

    def animator(self):
        """
        send the updated array to the animation class

        or maybe the animation is controlled here?
        """
        pass


def main():
    Simulation_instance = simulation()
    pass

if __name__ == "__main__":
    main()