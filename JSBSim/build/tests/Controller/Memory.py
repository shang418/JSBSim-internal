
import numpy as np
import math 
import random
from collections import deque 

class memory:   # stored as ( s, a, r, s_ )

    def __init__(self, capacity):
        self.capacity = capacity
        self.samples = deque(self.capacity)

    def add(self, sample):
        self.samples.append(sample)        
        if len(self.samples) > self.capacity:
            self.samples.pop()

    def sample(self, n):
        n = min(n, len(self.samples))
        return random.sample(self.samples, n)