import numpy as np
import pandas as pd
import scipy.stats
#r squared tells us how good our model is. closer to 0 is bad. closer to 1 is good 
def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.
    #datas = y
    #predictions = f
    # YOUR CODE GOES HERE

    avgy = np.mean(data)
    top = (np.square(data - predictions)).sum()
    bottom = (np.square(data - avgy)).sum()
    r_squared = 1 - (top)/(bottom)
    
    
    return r_squared