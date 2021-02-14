"""
Central file that executes the program.


self, temperature, size, steps, density, timestep
"""

from Simulation import simulation
from molecules import Molecule
from animator import animator

def main():
    T = float(input("Enter Temperature: "))
    Size = int(input("Enter Box Dimension: "))
    Steps = int(input("Enter Number of steps: "))
    Density = float(input("Enter Density (0<1): "))

    
    simulation()

if __name__ == "__main__":
    main()