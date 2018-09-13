from FlightGear import FlightGear
import numpy as np
from AileronRoll import AileronRoll
import os
import time

class Simulation_env:
    """ this class wraps the simulation into a form that
    produces a tuple (r,s_,done) 
    
    """
    port = 5500
    localhost = 'localhost'
    action_lims = np.array([[-1,1],[-1,1],[-1,1],[-1,1]])
    control_limits = np.array([[-20,20],[-20,20],[-35,26],[-1,1]])
    
    def __init__(self): 
        self.initialize()


    def initialize(self):
        #os.chdir(r'C:\Program Files\FlightGear 2017.2.1\bin')
        #os.system('fgfs --telnet=5500 --aircraft=easystar --disable-sound --enable-hud --lon='+repr(lon)+'--lat='+repr(lat)+'--altitude='+repr(alt))
        print('Waiting for simulator connection...')
        self.fg = FlightGear(self.localhost, self.port)
        print('Initializing aircraft ')
        while self.fg['/sim/initialized'] < 1:
            time.sleep(0.1)
        self.fg['/sim/freeze/clock']='true'
        self.starttime = (self.fg['/sim/time/elapsed-sec'])
        #self._pausesim_()
        self.fg['/sim/reset-on-crash']= 'false'
        print('Aircraft Simulation initialized:'+repr(self.fg['/sim/position-finalized']))
        self.state_vector = self._getstatefromsimulation_()
        self.trajectory = AileronRoll(self.state_vector[3],self.state_vector[6],self.state_vector[7],self.state_vector[11])
        print(self.state_vector)
        
    def _reset_(self): 
        self.fg['/sim/reset-on-crash']= 'true'
        while 1:
            if self.fg['/sim/time/elapsed-sec'] > 5:
                break
            time.sleep(1.0)
        print('Initializing aircraft ')
        time.sleep(2.0)
        print('Aircraft Simulation initialized:'+repr(self.fg['/sim/position-finalized']))
        self.state_vector = self._getstatefromsimulation_()
        self.starttime = (self.fg['/sim/time/elapsed-sec'])
        print(self.state_vector)
        self.fg['/sim/reset-on-crash']= 'false'
        return self._getstate_()
        
    def _act_(self,action):
        reward = self._getReward_()
        action_scaled = self.scale_actions(action) # do I need to scale this
        self.fg['/controls/engines/engine/throttle'] = repr(action_scaled[3])
        self.fg['/controls/flight/elevator'] = repr(action_scaled[0])
        self.fg['/controls/flight/aileron'] = repr(action_scaled[1])
        self.fg['/controls/flight/rudder'] = repr(action_scaled[2])
        #
        new_state = self._getstatefromsimulation_()
        new_state,done = self._isdone_(new_state)
        return new_state,reward,done
    
    def _getReward_(self): 
        time = self._getsimtime_()
        desired_state = self.trajectory._getdesiredstate_(time-self.starttime) # returns only desired roll, roll rate, heading and altitude values
        #print(desired_state)
        state = np.array([self.state_vector[3],self.state_vector[6],self.state_vector[7],self.state_vector[11]])
        delta_state = abs(state- desired_state)
        r = 0.01 * np.exp( -delta_state[0])+ 0.001 * np.exp( -delta_state[1]) - 0.5*np.exp(delta_state[2]) - 0.55*np.exp(delta_state[3])
        return r
    
    def _isdone_(self,new_state): 
        
        # crash : 0 height -ve
        #print(new_state[11])
        if (self.fg['\sim\crashed'] is None): # tolerance value
            return new_state,False
        
        return None,True
    
    def scale_actions(self,action):
        # transform each action to its min and max lim values in self.control_limits
        fx =(self.control_limits[:,1] - self.control_limits[:,0])*(action - self.action_lims[:,0])
        fx = fx / (self.action_lims[:,1] - self.action_lims[:,0])
        return fx + self.control_limits[:,0]
    
    def _getstatefromsimulation_(self):
        # get body velocities
        u = self.fg['/velocities/uBody-fps']
        v = self.fg['/velocities/vBody-fps']
        w = self.fg['/velocities/wBody-fps']
        
        # get orientation [roll,pitch,yaw] in radians
        phi = self.fg['/orientation/roll-deg'] #roll
        theta = self.fg['/orientation/pitch-deg'] #pitch
        psi = self.fg['/orientation/yaw-deg'] #yaw
        
        # get angular rates [p,q,r]
        p = self.fg['/orientation/p-body'] 
        q = self.fg['/orientation/q-body'] 
        r = self.fg['/orientation/r-body'] 
        
        #get linear positions
        lat = np.deg2rad(self.fg['/position/longitude-deg']) 
        lon = np.deg2rad(self.fg['/position/latitude-deg'])
        alt = self.fg['/position/altitude-ft']
        
        state = np.array([u,v,w,phi,theta,psi,p,q,r,lat,lon,alt])
        state = np.array([(0.0 if sample is None else sample) for sample in state],dtype=np.float32)
        return state
    
    def _pausesim_(self): 
        self.fg['/sim/freeze/clock']='true'
        
    def _playsim_(self): 
        self.fg['/sim/freeze/clock']='false'
        
    def _getsimtime_(self): 
        return self.fg['/sim/time/elapsed-sec']
        
    def _getstate_(self):
        return self.state_vector
    
        
        
        
        
        
        