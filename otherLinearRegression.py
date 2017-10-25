# -*- coding: utf-8 -*-

import numpy as np
import pandas
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt

"""
In this optional exercise, you should complete the function called 
predictions(turnstile_weather). This function takes in our pandas 
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.  

In exercise 3.5 we used Gradient Descent in order to compute the coefficients
theta used for the ridership prediction. Here you should attempt to implement 
another way of computing the coeffcients theta. You may also try using a reference implementation such as: 
http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.OLS.html

One of the advantages of the statsmodels implementation is that it gives you
easy access to the values of the coefficients theta. This can help you infer relationships 
between variables in the dataset.

You may also experiment with polynomial terms as part of the input variables.  

The following links might be useful: 
http://en.wikipedia.org/wiki/Ordinary_least_squares
http://en.wikipedia.org/w/index.php?title=Linear_least_squares_(mathematics)
http://en.wikipedia.org/wiki/Polynomial_regression

This is your playground. Go wild!

How does your choice of linear regression compare to linear regression
with gradient descent computed in Exercise 3.5?

You can look at the information contained in the turnstile_weather dataframe below:
https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
give you a random subset (~10%) of the data contained in turnstile_data_master_with_weather.csv

If you receive a "server has encountered an error" message, that means you are hitting 
the 30 second limit that's placed on running your program. See if you can optimize your code so it
runs faster.
"""
def normalize_features(df):
    """
    Normalize the features in the data set.
    """
    mu = df.mean()
    sigma = df.std()
    
    if (sigma == 0).any():
        raise Exception("One or more features had the same value for all samples, and thus could " + \
                         "not be normalized. Please do not include features with only a single value " + \
                         "in your model.")
    df_normalized = (df - df.mean()) / df.std()

    return df_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    
    This can be the same code as the compute_cost function in the lesson #3 exercises,
    but feel free to implement your own.
    """
    
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This can be the same gradient descent code as in the lesson #3 exercises,
    but feel free to implement your own.
    """
    
    m = len(values)
    cost_history = []

    while num_iterations > 0:
        #compute the cost for the current theta values
        cost_history.append(compute_cost(features, values, theta))
        #update theta values
        theta = theta + ((alpha)/(m))*(np.dot((values - np.dot(features, theta)),features))
        num_iterations -= 1
        
    return theta, pandas.Series(cost_history)

def predictions(weather_turnstile):
    
    # Select Features (try different features!)
    features = weather_turnstile[['Hour', 'maxtempi', 'meanwindspdi']]
    #    
    # Add UNIT to features using dummy variables, it is a constant identifier 
    dummy_units = pandas.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    
    # Values
    values = weather_turnstile['ENTRIESn_hourly']
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)

    # Set values for alpha, number of iterations.
    alpha = .03 # please feel free to change this value
    num_iterations = 100 # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    fig = plt.figure(figsize=(8,4))
    splt = plt.subplot(121)

    splt.scatter(weather_turnstile['Hour'], values, alpha=0.3)  # Plot the raw data
    #plt.ylim(30, 100)  # Set the y-axis to be the same
    plt.xlabel("Hour")
    plt.ylabel("Entries")
    plt.title("Entries by Hour")
    splt.plot(features['Hour'], predictions, 'r', alpha=0.9)  # Add the regression line, colored in red
    print(splt)
    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    #plot = plot_cost_history(alpha, cost_history)
    # 
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed 
    # the 30 second limit on the compute servers.
    
    predictions = np.dot(features_array, theta_gradient_descent)
    #print plot; 
    
    
    
    
    
    
    '''OLS
    features = weather_turnstile[['Hour', 'maxtempi', 'meanwindspdi']]
    #    
    # Add UNIT to features using dummy variables, it is a constant identifier 
    #dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    #features = features.join(dummy_units)
    
    # Values
    values = weather_turnstile['ENTRIESn_hourly']
    features_array = np.array(features)
    values_array = np.array(values)
    features_array = sm.add_constant(features_array)
    model = sm.OLS(values,features, missing='drop').fit()
    print model.summary()
    print model.params
    predictions = model.predict()
    '''
    
    
    return predictions
    

data = pandas.read_csv('turnstile_data_master_with_weather.csv')
print(predictions(data))
