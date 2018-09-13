from simulation_env import Simulation_env
import Trajectory_mapping
import numpy as np

""" generate and run trajectories"""

# initialize test environment 
lat = 42.3743
lon = -71.0179
alt = 400
nbins = 100
num_actions = 4
action_lims = np.array([[-1,1],[-1,1],[-1,1],[-1,1]])
env = Simulation_env()
print("checkpoint 1")
trajectories = Trajectory_mapping.generate_trajectories(num_actions,nbins,action_lims,env)
