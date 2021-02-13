"""
Intends to simulate the motion of molecules of an ideal gas using cellular automation.

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

#### SPACE FOR MORE FEATURES ###


"""
from random import randint

class simulation(object):
    def __init__(self, ): # Think it should take temperature, density/number of molecules, size, number of time Steps, and array size
        pass

    ######### PLACEHOLDER #######
    # more methods on their way!!!

    def temperature(self, array, temperature = 298.15):
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
        pass
    
    def controller(self):
        #returns None
        pass

    def iterator(self):
        """
        Iterates over array. Calls on the precent objects to update their positions.
        Somehow if new_position = another molecule or is beyond wall it should flip.

        INPUT:
        Array

        Ouput:
        Modified Array
        """"

        for object in array:
            x, y = object.updatePosition()

        pass
    
    def animator(self):
        """
        send the updated array to the animation class

        or maybe the animation is controlled here?
        """


        pass


def main():
    pass

if __name__ == "__main__":
    main()