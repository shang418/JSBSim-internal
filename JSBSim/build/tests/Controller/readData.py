from numpy import genfromtxt
import numpy as np 
from pyfme.simulator import Simulation

def readValues():
    my_data = genfromtxt('FlightData.csv', delimiter=',')
    size = np.shape(my_data)


    roll_pwm = np.array([(sample[5]) for sample in my_data], dtype=np.float32)
    pitch_pwm = np.array([(sample[6]) for sample in my_data], dtype=np.float32)
    throttle_pwm = np.array([(sample[7]) for sample in my_data], dtype=np.float32)
    yaw_pwm = np.array([(sample[8]) for sample in my_data], dtype=np.float32)

    return roll_pwm,pitch_pwm,yaw_pwm,throttle_pwm
    

def _convertValues_(roll_pwm,pitch_pwm,yaw_pwm,throttle_pwm): 

    # place conversion functions here
    roll_cmd = roll_pwm 
    pitch_cmd = pitch_pwm
    yaw_cmd = yaw_pwm
    throttle_cmd = throttle_pwm
    return roll_cmd,pitch_cmd,yaw_cmd,throttle_cmd

def getValues(): 
    roll_pwm,pitch_pwm,yaw_pwm,throttle_pwm = readValues()
    
    # convert values here
    roll_cmd,pitch_cmd,yaw_cmd,throttle_cmd= _convertValues_(roll_pwm,pitch_pwm,yaw_pwm,throttle_pwm)
    
    return roll_cmd,pitch_cmd,yaw_cmd,throttle_cmd
