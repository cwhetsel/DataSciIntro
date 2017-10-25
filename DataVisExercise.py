from pandas import *
from ggplot import *
import datetime

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    turnstile_weather['day_of_month'] = turnstile_weather['DATEn'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').day)
    entries_by_day = {}
    entries_by_day['Day'] = range(1,32)
    entries_by_day['Entries'] = []
    for x in range(1, 32):
        entries_by_day['Entries'].append( sum(turnstile_weather[turnstile_weather['day_of_month'] == x]['ENTRIESn_hourly']))
    #entries by hour 
    df = DataFrame(data=entries_by_day)
    plot = ggplot(df, aes('Day', 'Entries')) + geom_point() + geom_line(color='red') + ggtitle('Subway Entries by date') + xlab('Date in May 2011') + ylab('Entries')
    '''
    entries_by_unit = {}
    entries_by_unit['UNIT'] = turnstile_weather['UNIT'].unique()
    entries_by_unit['Entries'] = []
    for x in entries_by_unit['UNIT']:
        entries_by_unit['Entries'].append( sum(turnstile_weather[turnstile_weather['UNIT'] == x]['ENTRIESn_hourly']))
    #entries by unit
    df = DataFrame(data=entries_by_unit)
    plot = ggplot(df, aes(x='UNIT', fill='Entries')) + geom_bar() + ggtitle('Subway Entries by UNIT') + xlab('UNIT') + ylab('Entries')
    '''
    
    return plot
