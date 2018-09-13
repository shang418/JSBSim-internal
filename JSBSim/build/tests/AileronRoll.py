import math 
import numpy as np

class AileronRoll(): 
    
    def __init__(self,phi0,phi_dot0,heading,alt):
        self.alt = alt
        self.heading = heading
        self.omega = 2.0*math.pi/1.5
    
    # not the true trajectory 
    def _getdesiredstate_(self,time): 
        phi_desired = np.sin(self.omega * time)
        phidot_desired = self.omega*np.cos(self.omega * time) 
        return [phi_desired,phidot_desired,self.heading,self.alt]