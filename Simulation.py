"""
Intends to simulate the motion of molecules of an ideal gas using cellular automation.

#### SPACE FOR MORE FEATURES ###


"""
from molecules import Molecule
from random import uniform, randint
from math import sin, cos, sqrt, pi
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

    def __init__(self, temperature = 298, size = 1000, steps = 100, density = 0.001, timestep = 1): # Think it should take temperature, density/number of molecules, size, number of time Steps, and array size
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
            array = self.iterator(array)
            All_states = self.record_all_states(array, All_states, step)
        
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
        
        theta = [uniform(0,2*pi) for i in range(number_of_molecules)]
        velocities = self.generateVelocities(number_of_molecules)
        for i in range(len(x_indexies)):
            x_vel = velocities[i]*cos(theta[i])
            y_vel = velocities[i]*sin(theta[i])

            array[x_indexies[i]][y_indexies[i]] = Molecule(1, (x_indexies[i], y_indexies[i]), (x_vel, y_vel))
        return array 
    
    def generateVelocities(self, array_size):
        boltzmann_constant = 1.38*10**-23
        Hydrogen_mass = 1.67*10**-27
        rms_velocity = sqrt((3*boltzmann_constant*self.temperature)/Hydrogen_mass)*pow(10,-3) # Scales to be units per iteration

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

        col_ind = 0
        for column in new_array:
            for element in column:
                if element == 0:
                    continue
                else:
                    new_array[col_ind][column.index(element)] = 0
                    newPosition = self.updatePosition(element) # x and y are integers that correspond to their new index
                    
                    if new_array[newPosition[0]][newPosition[1]] == 0:
                        new_array[newPosition[0]][newPosition[1]] = element
                    else:
                        element2 = new_array[newPosition[0]][newPosition[1]]
                        new_position = simulation.detectCollision(element, element2)
                        new_array[new_position[0]][new_position[1]] = element2
            col_ind += 1
        
        #self.detectCollision(new_array)         
        return new_array
    
    def updatePosition(self, object):
        
        dx = object.velocity[0]*self.timestep
        dy = object.velocity[1]*self.timestep
        dArr = np.array([dx, dy])
        new_position = object.position + dArr
        
        if new_position[0] < 0:
            object.flip_x_velocity()
            newX = (-1)*new_position[0]
            new_position[0] = newX
        elif new_position[0] > self.size: #in x-direction
            object.flip_x_velocity()
            newX = 2*self.size - new_position[0]
            new_position[0] = newX

        if new_position[1] < 0:
            object.flip_y_velocity()
            newY = (-1)*new_position[1]
            new_position[1] = newY
        elif new_position[1] > self.size: #in x-direction
            object.flip_y_velocity()
            newY = 2*self.size - new_position[1]
            new_position[1] = newY
        
        object.change_position(new_position)

        return new_position.astype("int64")

    @staticmethod
    def detectCollision(element1, element2):
        element1.flip_x_velocity()
        element1.flip_y_velocity()

        element2.flip_x_velocity()
        element2.flip_y_velocity()

        new_position = np.array([element2.position[0], element2.position[1]-1])
        element2.change_position(new_position)

        return element2.position.astype("int64")
            
    def record_all_states(self, array, All_states, step):
        numArr = np.zeros((self.size, self.size))
        for column in range(self.size):
            for row in range(self.size):
                if array[row][column] != 0:
                    numArr[row, column] = 1
        All_states[step, :, :] = numArr
        
        return All_states

    def animator(self, array):
        ### Needs more work. IDK how to do this, Give up for today
        fig, _ = plt.subplots()
        ln = plt.imshow(array[0,:,:], origin = "lower", cmap = "plasma")
        
        def anim_func(index):
            data = array[index,:,:]
            ln.set_data(data)
            return ln
        
        anim = FuncAnimation(fig, anim_func, frames = range(1,len(array)), blit = False)
        plt.show()


def main():
    Simulation_instance = simulation()
    

if __name__ == "__main__":
    main()