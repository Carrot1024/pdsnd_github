# -*- coding: utf-8 -*-
"""Created on Fri Nov 24 13:39:27 2023@author: u0046369"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':'chicago.csv',
              'new york city':'new_york_city.csv',
              'washington':'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    month_list = ['january','february','march','april','may','june','all']
    week_day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        
        try:
            user_input_city = str(input('which city you want to select? chicago, new york city or washington?\n'))
            if user_input_city.lower() in CITY_DATA:
               city=user_input_city.lower()
               break
            else:
               print('Please confirm your input\n')
        except ValueError:
            print('Please confirm your input\n')
    # get user input for month (all, january, february, ... , june)
    while True:
        
        try:
            user_input_month = str(input('which month you want to select from January to June or All of them?\n'))
            if user_input_month.lower() in month_list:
               month=user_input_month.lower()
               break
            else:
               print('Please confirm your input\n')
        except ValueError:
            print('Please confirm your input\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        
        try:
            user_input_weekday = str(input('which weekday you want to select from Monday to Sunday or All of them?\n'))
            if user_input_weekday.lower() in week_day_list:
               day=user_input_weekday.lower()
               break
            else:
               print('Please confirm your input\n')
        except ValueError:
            print('Please confirm your input\n')

    print('-'*40)
    return city, month, day

def load_data(city,month,day):
    """Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""
        
    month_dictionary = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
    week_day_dictionary = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.DataFrame(df['Start Time'])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Start Time Month']=df['Start Time'].dt.month
    df['Start Time weekday'] = df['Start Time'].dt.weekday
    df['Start hour'] = df['Start Time'].dt.hour
    if month == 'all':
       df=df[df['Start Time Month']>=0]
    else:
       df=df[df['Start Time Month']==month_dictionary[month]]
    if day == 'all':
       df=df[df['Start Time weekday']>=0]
    else:
       df=df[df['Start Time weekday']==week_day_dictionary[day]]
       
    """ask user if he/she wants to read 5 rows of raw data, and if they wants to read 5 more rows till the answer is 'no'"""   
    row = 0
    while True:
           
        try:
            user_input_rawdataview = str(input('would you like to read 5 (more) rows of raw data?\n'))
            if user_input_rawdataview == 'no':
               break
            else:
                 row+=5
                 print(df.head(row))
        except ValueError:
            print('Please confirm your input\n')

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['Start Time Month'].mode()[0]
    print('the most common month:', popular_month)
    
    # display the most common day of week
    popular_weekday = df['Start Time weekday'].mode()[0]+1
    print('the most common day of week:', popular_weekday)

    # display the most common start hour
    popular_hour = df['Start hour'].mode()[0]
    print('the most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_counts = df.value_counts(df['Start Station'])
    popular_start_station = start_station_counts.head(1)
    print('the most commonly used start station is:\n',popular_start_station)
    
    # display most commonly used end station
    end_station_counts = df.value_counts(df['End Station'])
    popular_end_station = end_station_counts.head(1)
    print('the most commonly used end station is:\n',popular_end_station)

    # display most frequent combination of start station and end station trip
    start_and_end_station = df['Start Station'].append(df['End Station'])
    start_and_end_station_counts = start_and_end_station.value_counts()
    popular_start_and_end_station = start_and_end_station_counts.head(1)
    print('the most frequent combination of start station and end station trip is:\n',popular_start_and_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('total travel time:\n',total_travel_time/60,'mins')

    # display mean travel time
    average_travel_time = np.mean(df['Trip Duration'])
    print('mean travel time:\n',average_travel_time)
    print('mean travel time:\n',average_travel_time/60,'mins')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('count of user types:\n',user_types_count)
    
    # Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('count of gender:\n',gender_count)   

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year_earliest = int(df['Birth Year'].min())
    birth_year_most_recent = int(df['Birth Year'].max())
    birth_year_most_common = int(df['Birth Year'].mode()[0])
    print('the earliest birth year:\n',birth_year_earliest)
    print('the most recent birth year:\n',birth_year_most_recent)
    print('the most common year of birth:\n',birth_year_most_common)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

