"""
Intends to simulate the motion of molecules of an ideal gas using cellular automation.

#### SPACE FOR MORE FEATURES ###


"""
from moleculesv2 import Molecule
from random import randint
from math import sin, cos, sqrt
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib.animation import FuncAnimation


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

    def __init__(self, temperature = 298.15, size = 10, steps = 5, density = 0.05, timestep = pow(10,-9)): # Think it should take temperature, density/number of molecules, size, number of time Steps, and array size
        self.temperature = temperature
        self.size = size
        self.steps = steps
        self.density = density
        self.timestep = timestep

        # Creating an n x n array
        lst=[0 for i in range(self.size)]
        # Indexing is [i][j] where i is the row and j is the column
        self.array = [lst.copy() for j in range(self.size)]

        self.controller()
        pass

    def controller(self):
        All_states = np.zeros((self.steps, self.size, self.size))

        array = self.initiateArray(self.array, self.temperature)
        # update animation here
        
        for step in range(self.steps):
            All_states = self.record_all_states(array, All_states, step)
            array = self.iterator(array)

        self.animator(All_states)
        
        print("finished")
        

    def initiateArray(self, array, temperature):
        """
        Method called by class constructor and sets the inital 
        positions and velocities of the molecules.
        
        Positions are simply randomly generated (using randint method) 
        but the velocites need to be fitted to a boltzmann distribution.

        INPUTS:
        Array
        Temperature (>0 K)

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

            array[x_indexies[i]][y_indexies[i]] = Molecule(1, (x_indexies[i], y_indexies[i]), (x_vel, y_vel))
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
                    newPosition = self.updatePosition(element) ## x and y are integers that correspond to their new index
                    new_array[newPosition[0]][newPosition[1]] = element
        self.detectCollision(new_array)            
        return new_array
    
    def updatePosition(self, object):
        
        dx = object.velocity[0]*self.timestep
        dy = object.velocity[0]*self.timestep
        dArr = np.array([dx, dy])
        new_position = object.position + dArr
        
        if new_position[0] <= 0 or new_position[0] >= self.size: #in x-direction
            object.flip_x_velocity()
            newX = object.flip_x_position()
            new_position[0] = newX
        if new_position[1] <= 0 or new_position[1] >= self.size: #in y-direction
            object.flip_y_velocity()
            newY = object.flip_y_position()
            new_position[1] = newY

        return new_position.astype("int64")

    def detectCollision(self, array):
        pass
            

    def record_all_states(self, array, All_states, step):
        numArr = np.zeros((self.size, self.size))
        for row in range(self.size):
            for column in range(self.size):
                if array[row][column] != 0:
                    numArr[row, column] = 1
        All_states[step, :, :] = numArr
        return All_states
        
        """
        if step == 0:
            plt.imshow(numArr, cmap = "plasma")
            plt.show()
        else:
            pass
        """

    def animator(self, array):
        ### Needs more work. IDK how to do this, Give up for today
        def animation_func(array):
            for timestep in range(self.steps):
                return array[timestep, :, :]
        
        
        plt.imshow(animation_func(array))
        plt.show()



def main():
    Simulation_instance = simulation()
    

if __name__ == "__main__":
    main()