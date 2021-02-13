import numpy as np
import time
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


    ###### PLACEHOLDER #####

    def next_step(self, delta_t=1.0):
        old_position = self.position
        new_position = old_position + self.velocity*int(delta_t)
        self.position = new_position

    def change_velocity(self, new_velocity):
        self.velocity = new_velocity

    def collide_with_wall(self, wall):
        #from simulation take wall coordinates x,y
        #change velocity wall 
        x_vel = self.velocity[0]
        y_vel = self.velocity[1]

        x_position = self.position[0]
        y_position = self.position[1]

        if y_position == 0: #top
            #change in velocity
            # x_vel stays the same
            # y_vel flips
            y_vel = (-1)*y_vel
            self.change_velocity(np.array([x_vel, y_vel]))
            '''
        elif y_position =bottom #bottom wall
            y_vel = y_vel * (-1)
            self.velocity = change_velocity(np.array(x_vel,y_vel))
            '''
        elif x_position == 0: #left wall
            x_vel = x_vel * (-1)
            self.change_velocity(np.array([x_vel,y_vel]))
            '''
        elif x_position =  right #right
            x_vel = x_vel * (-1)
            self.velocity = change_velocity(np.array(x_vel,y_vel))
            '''




    def collide_with_molecule(self,):
        pass

    def updatePosition(self):
        """
        called by iterator in simulation class. Takes index
        and adds x + dx and y + dy.
        
        Input:
        Index

        Output:
        New index
        """
        return 2, 3


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