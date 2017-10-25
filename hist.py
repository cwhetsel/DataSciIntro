import numpy as np
import pandas
import matplotlib.pyplot as plt
import scipy
import scipy.stats



def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
    '''
    
    plt.figure()
    turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly'].plot.hist(range=(0,8000)) # your code here to plot a historgram for hourly entries when it is raining
    turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly'].plot.hist(range=(0,8000)) # your code here to plot a historgram for hourly entries when it is not raining
    return plt




def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    You should feel free to use scipy's Mann-Whitney implementation, and you 
    might also find it useful to use numpy's mean function.
    
    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    You can look at the final turnstile weather data at the link below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
    
    Mann Whiteny test is a nonparametric test of two random variables from two samples.
    It does not need to be a normal distribution and can be used to detect if two independent samples 
    came from the same distribution. 
    '''
    
    ### YOUR CODE HERE ###
    x = turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly'] # your code here to plot a historgram for hourly entries when it is raining
    y = turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly'] # your code here to plot a historgram for hourly entries when it is not raining
    with_rain_mean = np.mean(x)
    without_rain_mean = np.mean(y)
    
    #can do two-sided, lt, gt or none tests 
    U, p = scipy.stats.mannwhitneyu(x, y)
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader
