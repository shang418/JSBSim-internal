""" class that implements the Value Network for the ddpg algorithm 
"""
import tensorflow as tf
import numpy as np 

class ValueNetwork:

    def __init__(self,lr,num_features): 
        # initialize whatever here
        self.learning_rate = lr
        self.num_features = num_features
        self.num_outputs = 1
        self._buildNN_()
        
    def _buildNN_(self):
    # build neural net with 2 HL of 64 nodes 
    n_hidden = 64 # number of hidden nodes 
    self.feature_vector = tf.placeholder(tf.float32, [num_features], name="features") 
    self.h1 = tf.layers.Dense(
                    inputs = self.feature_vector,
                    num_outputs = n_hidden,
                    activation = 'tanh',
                    bias_initializer=tf.zeros_initializer(), 
                    use_bias=True
                    )
    self.h2 = tf.layers.Dense(
                    inputs = self.h1,
                    num_outputs = n_hidden,
                    activation = 'tanh',
                    bias_initializer=tf.zeros_initializer(), 
                    use_bias=True
                    )
    self.value = tf.layers.Dense(
                    inputs = self.h2,
                    num_outputs = 1,
                    activation = None,
                    bias_initializer=tf.zeros_initializer(), 
                    use_bias=True
                    )
                    
    def _trainOptimizer_(self): 
    # function that defines the optimizer and loss functions
        self.target_value = tf.placeholder(tf.float32, name="features") # best aggregate value for preprocess stage
        self.loss = tf.reduce_mean(tf.squared_difference(self.value, self.target_value))
        # edit these for better optimization
        self.optimizer = tf.train.AdamOptimizer(self.learning_rate)
        self.train_op = self.optimizer.minimize(self.loss)
        
    def _predict_(self,feature_vector,sess):
        return sess.run(self.value, feed_dict={self.feature_vector: feature_vector)})
        
    def _update_(self.feature_vector,target_value,sess):
        feed_dict = {
            self.feature_vector: feature_vector,
            self.target_value: target_value
        }
        sess.run([self.train_op], feed_dict=feed_dict)
    