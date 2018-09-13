import numpy as np 
import math 
from collections import deque
import pickle 
import time 

# import simulator here 
maxlength = 100000000000
max_eps = 200
# divide the action space into bins

def generate_trajectories(dim_actions,num_bins,action_lims,env):
    assert np.shape(action_lims) == (dim_actions,2)
    
    # make action bins for each limit
    action_bins = np.zeros((dim_actions, num_bins))
    for i in range(dim_actions):
        action_bins[i,:] = np.linspace(action_lims[i][0], action_lims[i][1], num=num_bins, dtype=np.float32)
    
    # initialize deque collections
    trajectory= deque(maxlen = max_eps)
    traj_space = deque(maxlen = maxlength)
    state = env._getstate_() # something like this..... edit this
    # iterate for while in actions in bins
    eps_length = 0
    i=0
    R = 0
    print("checkpoint 2")
    for a0 in action_bins[0,:] : 
        for a1 in action_bins[1,:] :
            for a2 in action_bins[2,:]:
                for a3 in action_bins[3,:]:
                    #### edit this to just send constant which would then just be added to trimmed controls
                    env._playsim_()
                    action = np.array([a0,a1,a2,a3])
                    #print(action)
                    new_state,reward,done = env._act_(action)
                    print(f'new state : {new_state} : Crashed : {done} : Reward : {reward}')
                    env._pausesim_()
                    #print(new_state,reward,done)
                    #plotter_3d(new_state[0:3],new_state[6:10],ax)
                    state_tuple = (state,reward,action,new_state,done)
                    # add state_tuple to memory
                    trajectory.append(state_tuple)
                    print(f'Iter: {i} : episode length : {eps_length} : Crashed : {done} : Max Reward : {R}')
                    R+=reward
                    eps_length+=1
                    if done or eps_length==max_eps: 
                        i+=1
                        print(f'Iter: {i} : episode length : {eps_length} : Crashed : {done} : Max Reward : {R}')
                        traj_space.append((trajectory,R))
                        trajectory.clear()
                        done = False
                        R =0
                        env._reset_()
                        eps_length = 0
                    

    pickle.dump(traj_space, open( "trajectories.dat", "wb" ) )
    my_data = pickle.load( open( "trajectories.dat", "rb" ) )

    