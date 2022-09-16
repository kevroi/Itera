from os import times
from time import time
import numpy as np

class Walker():
    """
    Class for performingh 1D random walks. Currently implemented for unbiased random
    walks with partially reflecting boundaries
    """
    def __init__(self, street_length, timesteps, start_at, p,
                street_char='_', walker_char=':)'):
        """
        Args:
            street_length (int): Length of finite street for our walker
            timesteps (int): Duration of walk
            start_at (int): Positon along street to start at
            p (float): Probability of taking a step to the right
            street_char: Character used to represent street in output
            walker_char: Character used to represent walker in output
        """
        self.street_length = street_length
        self.timesteps = timesteps
        self.start_at = start_at
        self.position = self.start_at
        self.time = 0 # beginning of time
        self.p = p
        self.street_char = street_char
        self.walker_char = walker_char
        self.output = []

    def makeStreet(self):
        """
        Create a street and place your walker on it
        """
        self.output = self.street_length*[self.street_char]
        self.output += list(str(self.time))
        self.output[self.start_at] = self.walker_char

    def printStreet(self):
        """
        Print what the street currently looks like to console
        """
        print("".join(self.output))

    def walk(self):
        """
        Perform a random walk for the number of timesteps indicated at initialisation.
        Random walk with Partially reflecting boundaries.
        """
        self.makeStreet()

        for t in range(1, self.timesteps+1):
            rand_num = np.random.random()
            if self.p < rand_num and self.position != self.street_length-1:
                self.output[self.position+1], self.output[self.position] = self.output[self.position], self.output[self.position+1]
                self.position += 1
            elif self.p > rand_num and self.position != 0:
                self.output[self.position-1], self.output[self.position] = self.output[self.position], self.output[self.position-1]
                self.position -= 1
            self.time += 1
            self.output[-1] = str(self.time)
            self.printStreet()    