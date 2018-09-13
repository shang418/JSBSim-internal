import tensorflow as tf
import numpy as np 
import sklearn 
from sklearn.preprocessing import StandardScaler
from Memory import Memory
import PolicyNetwork
import ValueNetwork

class DDPG_Batch: 
    
    num_actions = 4
    num_states = 9 
    n_components = 100
    
    EPS_LENGTH = 1E6
    
    def __init__(self,TO_LOAD): 
    # put something here
    # create network
    
        self.model = self.create_brain()
        self.memory = memory(MEMORY_CAPACITY)
        if(TO_LOAD): 
            self.model.load_weights("ddpg_modelV0.h5")
    
    def preprocess_trajectories(self): 
        # 1. load trajectories
        # 2. extract relevant features ( angular positions, angular rates, velocities and height)for aileron roll to data np array
        # 3. scale data to distribution 
        statedist_scaler = StandardScaler()
        statedist_scaler.fit(state_data)
        print('Mean: %f, StandardDeviation: %f' % (statedist_scaler.mean_, sqrt(statedist_scaler.var_)))
        standardized_data = statedist_scaler.transform(state_data)
        #4. transformm standardized data to RBF kernel features \phi(x)
        
        # Taken from url: https: // blah blah blah 
        # Used to convert a state to a featurizes represenation.
        # We use RBF kernels with different variances to cover different parts of the space
        
        state_featurizer = FeatureUnion([
                ("rbf1", RBFSampler(gamma=5.0, n_components=self.n_components)),
                ("rbf2", RBFSampler(gamma=2.0, n_components=self.n_components)),
                ("rbf3", RBFSampler(gamma=1.0, n_components=self.n_components)),
                ("rbf4", RBFSampler(gamma=0.5, n_components=self.n_components))
                ])
        features = state_featurizer.fit_transform(standardized_data)
        # 5. Use these features to train neural net
        # 6. save model 
        self.scaler = statedist_scaler
        self.featurizer = state_featurizer
        self.Gt = getBestRewardFromTraj 
    
    def process_state(self,state):
    # use to fit and transform each state into a feature for the net
        # extract relevant states from data 
        extracted_state = state[0:9]
        # standardize extracted states
        standardized_state = self.scaler.transform(extracted_state)
        # transform into RBF feature kernels
        feature = self.featurizer.transform(standardized_state)
        return feature[0]
    
    def _createbrain_(self):
        tf.reset_default_graph()
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        self.policyNN = PolicyNetwork()
        self.valueNN = ValueNetwork()
        
        
    def save_model(self): 
        model_json = self.model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        self.model.save_weights("ddpg_modelV0_trained.h5")
        print("Saved model to disk") 
    ###########################################################################
    ######## edit everything here..... this is from cartpole simulation########
    ###########################################################################
    def _train_actorcritic(self):
        # define this function
        self.preprocess_trajectories()
        for num_eps in range(self.EPS_LENGTH):
            reward,eps_length=run(cart_agent)
            total_rewards+=reward
            reward_save.append(total_rewards)
            print ('%d : %3.2f : %d' % (num_eps, total_rewards,eps_length))
            total_rewards = 0
            num_eps+=1
        cart_agent.save_model()
        plot_rewards(reward_save,total_eps)
        
    def run(cart_agent): 
		s = env.reset() # get current state
		#s = np.array([s], dtype=np.float32)
		R =0
		s_init=s
		eps_length=0
		# run sim does not violate conditions ( excessive pendulum tilt)
		while True: 
			#env.render()
			a = cart_agent.act(np.array([s], dtype=np.float32)) # get action
			s_, r, done, info = env.step(a) # take action and observe reward
			#s_ = np.array([s_], dtype=np.float32)
			# add state, action,next_state to memory
			if done:
				s_ = None
			
			cart_agent.replay((s, a, r, s_))
			R+=r
			eps_length+=1
			if done:
				return R,eps_length
			s = s_
    
    
    
