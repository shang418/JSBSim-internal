import jsbsim
import numpy as np
from AileronRoll import AileronRoll
import os
import time

class Simulation_env:
    """ this class wraps the simulation into a form that
    produces a tuple (r,s_,done) 
    
    """
    
    action_lims = np.array([[-1,1],[-1,1],[-1,1],[-1,1]])
    control_limits = np.array([[-20,20],[-20,20],[-35,26],[-1,1]])
    
    _state = ['velocities/u-fps','velocities/v-fps','velocities/w-fps',
              'attitude/phi-rad','attitude/theta-rad','attitude/psi-rad',
              'velocities/p-rad_sec','velocities/q-rad_sec','velocities/r-rad_sec',
              'position/lat-gc-deg','position/long-gc-deg','position/h-agl-ft'
                ]
    _control = ['fcs/elevator-pos-deg',
                'fcs/left-aileron-pos-deg',
                'fcs/rudder-pos-deg',
                'fcs/throttle-pos-norm']
                
    _ICs = ['ic/u-fps','ic/v-fps','ic/w-fps', # body velocities
            'ic/phi-rad','ic/theta-rad','ic/psi-rad', # angular pos
            'ic/p-rad_sec','ic/q-rad_sec','ic/r-rad_sec', # angular vel
            'ic/lat-gc-deg','ic/long-gc-deg','ic/h-agl-ft' # inertial pos
            ]
    svsize = 12 # 12 states
    icsize = 12 # 12 initial states
    cntrl_size = 4
    dt = 0.1

    def __init__(self,aircraft_name): 
        self.fdm  = jsbsim.FGFDMExec(root_dir='../../')
        assert type(aircraft_name) is str
        self.fdm.load_model(aircraft_name)
        self.fdm.set_property_value("ic/lat-gc-rad",0.761552988)
        self.fdm.set_property_value("ic/long-gc-rad",0.0239284344)
        self.fdm.set_property_value("ic/h-agl-ft",400)
        self.fdm.set_property_value("ic/vc-kts",30)
        #self.fdm.set_property_value("ic/gamma-deg",0)
        self.fdm.set_dt(0.01)
        self.fdm.do_trim(1)
        self.state_vector = self._getstatefromsimulation_()
        self.trajectory = AileronRoll(self.state_vector[3],self.state_vector[5],self.state_vector[6],self.state_vector[11])

       
        
    def _reset_(self): 
        # set initial state here
            # either initial standard vec or randomize
        self.fdm.reset_to_initial_conditions(True)
        #self.fdm.reset_to_initial_conditions(False)
        return self._getstate_()
        
    def _act_(self,action):
        reward = self._getReward_()
        action_scaled = self.scale_actions(action) # do I need to scale this
        for i in range(self.cntrl_size): 
            self.fdm.set_property_value(self._control[i],action_scaled[i])
        self.fdm.set_property_value('fcs/right-aileron-pos-deg',-1.0*action_scaled[1])
        #(t,y) = self.fdm.simulate(t_final=self.dt,dt=0.01,record_properties=self._state)
        self._simulate_()
        new_state = self._getstatefromsimulation_()
        new_state,done = self._isdone_(new_state)
        self._getstate_()
        return new_state,reward,done
    
    def _simulate_(self): 
        starttime = self.fdm.get_sim_time()
        while self.fdm.run():
            #print(self.fdm.get_property_value(self._state[3]))
            if self.fdm.get_sim_time() > starttime + self.dt:
                return
        
    def _getReward_(self): 
        time = self._getsimtime_()
        desired_state = self.trajectory._getdesiredstate_(time) # returns only desired roll, roll rate, heading and altitude values
        #print(desired_state)
        state = np.array([self.state_vector[3],self.state_vector[5],self.state_vector[6],self.state_vector[11]])
        delta_state = abs(state- desired_state)
        r = 1E-6 * np.exp( -delta_state[0])+ 1E-8 * np.exp( -delta_state[1]) - 5E-6*np.exp(delta_state[2]) - 4E-6*np.exp(delta_state[3])
        return r
    
    def _isdone_(self,new_state): 
        
        # crash detection
        if self._getsimtime_( ) > 0.0 and new_state[11] < 100.0: # look some more at
            #print(self.fdm.integration_suspended())
            return None,True
        
        return new_state,False
    
    def _getactions_(self): 
        actions = np.array([self.fdm.get_property_value(sample) for sample in self._control],dtype=np.float32)
        return actions
        
    def scale_actions(self,action):
        # transform each actienvon to its min and max lim values in self.control_limits
        fx =(self.control_limits[:,1] - self.control_limits[:,0])*(action - self.action_lims[:,0])
        fx = fx / (self.action_lims[:,1] - self.action_lims[:,0])
        return fx + self.control_limits[:,0]
    
    def _setinitialstatefromvector_(self,vec): 
        
        # set them 
        for i in range(self.icsize): 
            self.fdm.set_property_value(self._ICs[i],vec[i])
        # confirm setting
        for i in range(self.icsize): 
            if self.fdm.get_property_value(self._ICs[i]) != vec[i]: 
                return False
        return True
        
    def _getstatefromsimulation_(self):
        state = np.array([(0.0 if self.fdm.get_property_value(sample) is None else self.fdm.get_property_value(sample)) for sample in self._state],dtype=np.float32)
        return state
    
    # not utilizing simulation head so don't need these
    
    # def _pausesim_(self): 
        # self.fdm['/sim/freeze/clock']='true'
        
    # def _playsim_(self): 
        # self.fdm['/sim/freeze/clock']='false'
        
    def _getsimtime_(self): 
        return self.fdm.get_property_value('simulation/sim-time-sec')
        
    def _getstate_(self):
        self.state_vector = self._getstatefromsimulation_()
        return self.state_vector
        
        
        
        
        
        