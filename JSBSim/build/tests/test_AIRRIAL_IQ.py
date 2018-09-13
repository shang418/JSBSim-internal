from Simulation_env import Simulation_env
import TrajectoryGeneration
import numpy as np

""" generate and run trajectories"""

# initialize test environment 
nbins = 10
num_actions = 4
action_lims = np.array([[-1,1],[-1,1],[-1,1],[-1,1]])
env = Simulation_env('bixler3')

trajectories = TrajectoryGeneration.generate_trajectories(num_actions,nbins,action_lims,env)
