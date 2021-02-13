from Simulation import simulation



"""
Folder intended to contain the class that creates the molecule objects


Attributes:
* Index
* Velocity (magnitude and direction; x and y velocity)
* Mass


Methods:
* Magnitude
    returns velocity
    abs(vector)
* Change direciton
  eg. if hit horizontal wall, reflects
  what happens if it hits a molecule? Both go in opposite direction.
* New positon: returns new index to sim class
"""

class molecule(object):
    """ 
    Created by the Simulation class as it populates the cell array. 
    """
    
    def __init__(self):
        pass

    ###### PLACEHOLDER #####

    def updatePosition(self):
        """
        called by iterator in simulation class. Takes index
        and adds x + dx and y + dy.
        
        Input:
        Index

        Output:
        New index
        """

        return new_x, new_y


def main():
    pass

if __name__ == "__main__":
    main()