from pandas import *
from ggplot import *

'''components to effective visualization
    -visual encoding, coordinate system, scaling, context 
-visual encoding, size, position, color, saturation,  area, length, angle 
-data type 
        -numerical, time series, categorical or ordinal 
'''

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/
    
    data = read_csv(hr_year_csv)
    
    gg = ggplot(data, aes('yearID', 'HR')) + geom_point(color='red') + geom_line(color='red') + ggtitle('Homeruns by year') + xlab('Year') + ylab('Homeruns')
    return gg



import pandas

from ggplot import *


def lineplot_compare(hr_by_team_year_sf_la_csv):
    # Write a function, lineplot_compare, that will read a csv file
    # called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot.
    #
    # This csv file has three columns: yearID, HR, and teamID. The data in the
    # file gives the total number of home runs hit each year by the SF Giants 
    # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
    # visualization comparing the total home runs by year of the two teams. 
    # 
    # You can see the data in hr_by_team_year_sf_la_csv
    # at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_by_team_year_sf_la.csv
    #
    # Note that to differentiate between multiple categories on the 
    # same plot in ggplot, we can pass color in with the other arguments
    # to aes, rather than in our geometry functions. For example, 
    # ggplot(data, aes(xvar, yvar, color=category_var)). This might help you 
    # in this exercise.
    data = pandas.read_csv(hr_by_team_year_sf_la_csv)
    
    gg = ggplot(data, aes('yearID', 'HR', color='teamID')) + geom_point() + geom_line() + ggtitle('Homeruns by year') + xlab('Year') + ylab('Homeruns')
    return gg



from pandas import *
from ggplot import *
import datetime
def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    turnstile_weather['day_of_week'] = turnstile_weather['DATEn'].apply(lambda x: datetime.datetime.strftime(datetime.datetime.strptime(x, '%Y-%m-%d'), '%A'))
    entries_by_hour = {}
    entries_by_hour['time_of_day'] = []
    entries_by_hour['Entries'] = []
    entries_by_hour['Day'] = []
    for x in turnstile_weather['day_of_week'].unique():
        for y in turnstile_weather['Hour'].unique():
            entries_by_hour['time_of_day'].append(y)
            entries_by_hour['Entries'].append( sum(turnstile_weather[(turnstile_weather['day_of_week'] == x)][(turnstile_weather['Hour'] == y)]['ENTRIESn_hourly']))
            entries_by_hour['Day'].append(x)
    #entries by hour 
    df = DataFrame(data=entries_by_hour)
    plot = ggplot(df, aes('time_of_day', 'Entries', color='Day')) + geom_point() + geom_line() + ggtitle('Subway Entries by Hour for each day of the week') + xlab('Time of Day') + ylab('Entries')
    return plot
