import tensorflow as tf 
import numpy as np

class PolicyNetwork: 

    def __init__(self,lr,num_features): 
        self.learning_rate = lr
        self.num_features = num_features
        self.num_outputs = 8 # sigma and mu for each action value
        self._buildNN_()
        self.low_actions = np.array([-1,-1,-1,0])
        self.high_actions = np.array([-1,-1,-1,1])
    def _buildNN_(self):
    # build neural net with 2 HL of 64 nodes 
        n_hidden = 64 # number of hidden nodes 
        self.feature_vector = tf.placeholder(tf.float32, [num_features], name="features") 
        self.mu_h1 = tf.layers.Dense(
                        inputs = self.feature_vector,
                        num_outputs = n_hidden,
                        activation = 'tanh',
                        bias_initializer=tf.zeros_initializer(), 
                        use_bias=True
                        )
        self.mu_h2 = tf.layers.Dense(
                        inputs = self.mu_h1,
                        num_outputs = n_hidden,
                        activation = 'tanh',
                        bias_initializer=tf.zeros_initializer(), 
                        use_bias=True
                        )
        self.mu = tf.layers.Dense(
                        inputs = self.mu_h2,
                        num_outputs = 4,
                        activation = None,
                        bias_initializer=tf.zeros_initializer(), 
                        use_bias=True
                        )
        
        self.sigma_h1 = tf.layers.Dense(
                        inputs = self.feature_vector,
                        num_outputs = n_hidden,
                        activation = 'tanh',
                        bias_initializer=tf.zeros_initializer(), 
                        use_bias=True
                        )
        self.sigma_h2 = tf.layers.Dense(
                        inputs = self.sigma_h1,
                        num_outputs = n_hidden,
                        activation = 'tanh',
                        bias_initializer=tf.zeros_initializer(), 
                        use_bias=True
                        )
        self.sigma = tf.layers.Dense(
                        inputs = self.sigma_h2,
                        num_outputs = 4,
                        activation = None,
                        bias_initializer=tf.zeros_initializer(), 
                        use_bias=True
                        )
        self.sigma = tf.nn.softplus(self.sigma) + self.noise
        self.norm_dist = tf.contrib.distributions.Normal(self.mu, self.sigma)
        self.action = self.norm_dist.sample(1)
        self.action = tf.clip_by_value(self.action, self.low_actions, self.high_actions)
        
    def _trainOptimizer_(self): 
    # function that defines the optimizer and loss functions
        self.action_train = tf.placeholder(tf.float32, name="action_train")
        self.advantage_train = tf.placeholder(tf.float32, name="advantage_train")

        self.loss = -tf.log(
            self.norm_dist.prob(self.action_train) + 1e-5) * self.advantage_train - self.lamb * self.norm_dist.entropy()
        self.optimizer = tf.train.AdamOptimizer(self.learning_rate)
        self.train_op = self.optimizer.minimize(self.loss)
        
    def _predict_(self,feature_vector,sess):
        return sess.run(self.action, feed_dict={self.feature_vector: feature_vector)})
        
    def _update_(self,feature_vector,action,advantage,sess):
        feed_dict = {
            self.feature_vector: feature_vector,
            self.action_train: action,
            self.advantage_train: advantage
        }
        sess.run([self.train_op], feed_dict=feed_dict)
    
        
        
    
        