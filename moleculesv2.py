import numpy as np
import time

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

class Molecule(object):
    """ 
    Created by the Simulation class as it populates the cell array. 
    """
    
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return f"Mass: {self.mass}\nPosition: {self.position}\nVelocity: {self.velocity}"

    def flip_x_velocity(self):
        #flip x
        self.velocity = ((-1)*self.velocity[0], self.velocity[1])

    def flip_y_velocity(self):
        self.velocity = (self.velocity[0], (-1)*self.velocity[1])

    def flip_x_position(self):
        x_position = self.position[0]
        y_position = self.position[1]

        x_position = (-1)*x_position
        self.position = np.array([x_position, y_position], dtype = "int32")
        return self.position[0]

    def flip_y_position(self):
        x_position = self.position[0]
        y_position = self.position[1]

        y_position = (-1)*y_position
        self.position = np.array([x_position, y_position], dtype = "int32")
        return self.position[1]


def main():
    hydrogen = Molecule(mass=1,velocity=np.array([-1,0]),position=np.array([5,5]))
    for i in range(8):
        print(f"{hydrogen.position}")
        print(hydrogen)
        hydrogen.next_step()
        hydrogen.collide_with_wall(5)

    
'''
    delta_t = 0.2
    time_horizon = 10
    for i in range(time_horizon):
        print(f"Time: {delta_t*i}")
        print(hydrogen)
        hydrogen.next_step()
        time.sleep(1)
'''



if __name__ == "__main__":
    main()