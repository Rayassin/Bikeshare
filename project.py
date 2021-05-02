import time
import math
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    Selected_city = input("Please select the city you want to review it's data:\n(1)For Chicago\n(2)For New York\n(3)For Washington\n ")
    if Selected_city == '1':
        print('Chicago')
    elif Selected_city == '2':
        print('new york'.title())
    elif Selected_city == '3':
        print('washington'.title())
    
    # Validating the user input
    while Selected_city not in ['1','2','3']:
        print("Invalid Input,Please try again!")
        Selected_city = input("Please select the city you want to review it's data:\n(1)For Chicago\n(2)For New York\n(3)For Washington\n ")
    if Selected_city == '1':
        city = 'chicago'
    elif Selected_city == '2': 
        city = 'new york city'
    elif Selected_city == '3':     
        city = 'washington'


    Selected_timeframe = input("\nDo you want to filter {} data via month or day or both or none?\nPlease enter your choice: \n(1)For Month\n(2)For Day\n(3)For Both\n(4)For None\n ".format(city.title()))
    duration = 'All'
    Monthly_duration = ''
    Daily_duration = ''
    print(Selected_timeframe)
    while Selected_timeframe not in ['1','2','3','4']:
        print('Invalid Input,Please try again!')
        Selected_timeframe = input("\nDo you want to filter {} data via month or day or both or none?, \nPlease enter your choice: \n(1)For Month\n(2)For Day\n(3)For Both\n(4)For None \n".format(city.title()))
    if Selected_timeframe == '4':
        duration = 'All'
    else:
        if Selected_timeframe in ['1','3']:
            Monthly_duration = input("\nPlease select the required month:\n(1)For January\n(2)For February\n(3)For March\n(4)For April\n(5)For May\n(6)For June\n")
            while Monthly_duration not in ['1','2','3','4','5','6']:
                print("Invalid Input,Please try again!")
                Monthly_duration = input("\nPlease select the required month: \n(1)For January\n(2)For February\n(3)For March\n(4)For April\n(5)For May\n(6)For June\n")
        if Selected_timeframe in ['2','3']:
            Daily_duration = input("\nPlease select the required day: \n(1)For Sunday\n(2)For Monday\n(3)For Tuesday\n(4)For Wednesday\n(5)For Thursday\n(6)For Friday\n(7)For Saturday\n")
            while Daily_duration not in ['1','2','3','4','5','6','7']: 
                print("Invalid Input,Please try again!")
                Daily_duration = input("\nPlease select the required day: \n(1)For Sunday\n(2)For Monday\n(3)For Tuesday\n(4)For Wednesday\n(5)For Thursday\n(6)For Friday\n(7)For Saturday\n")
    if Selected_timeframe == '1':
        duration = 'Month'
    elif Selected_timeframe == '2':
        duration = 'Day'
    elif Selected_timeframe == '3':
        duration = 'Both'
    Days_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if Daily_duration != '':
        index = int(Daily_duration)-1
        Daily_duration = Days_of_week[index]
    Chosen_timeframe=[duration,Monthly_duration,Daily_duration]

    return city, Chosen_timeframe

def load_data(city,Chosen_timeframe):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (List) Chosen_timeframe - Gives back whether the user chosed to filter by Month,Day,Both or whether chosed not to filter through All
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print(city)
    print(Chosen_timeframe)
    print(type(Chosen_timeframe))
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month and day if applicable
     
     #filter by month or both
    if Chosen_timeframe[0] == 'Month' or Chosen_timeframe[0] == 'Both':
        # we need to convert Chosen_timeframe var.here to integer for the sake of comparison with month
        month = int(Chosen_timeframe[1])
        print(month)
        df = df[df['month'] == month]
    if Chosen_timeframe[0] == 'Day' or Chosen_timeframe[0] == 'Both':    
        day = Chosen_timeframe[2]
        print(day)
        df = df[df['day_of_week'] == day.title()]
    return df  
        


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Most_frequent_month = df['month'].mode()[0]

    Months = ['January','February','March','April','May','June']
    Most_frequent_month = Months[Most_frequent_month-1]
    

    # display the most common day of week
    Most_frequent_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    Most_frequent_hour = df['hour'].mode()[0]

    print('Most common month is: {}'.format(Most_frequent_month))
    print('Most common day is: {}'.format(Most_frequent_day))
    print('Most common hour is: {}'.format(Most_frequent_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Most_frequent_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    Most_frequent_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['Station Combintion'] = df['Start Station'] +' and '+ df['End Station']
    Most_frequent_stations_combination = df['Station Combintion'].mode()[0]

    print('Most common Start Station is: {}'.format(Most_frequent_start_station))
    print('Most common End Station is: {}'.format(Most_frequent_end_station))
    print('Most common Stations Combination is: {}'.format(Most_frequent_stations_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Trip_Duration = df['Trip Duration'].sum()

    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    # another method to find the mean, however care should be given in case of dividing by zero
    # Mean_Travel_Time_1 = Trip_Duration/len(df['Trip_Duration'])

    Days = Trip_Duration // (24 * 3600)

    Remaining_Hours = Trip_Duration % (24 * 3600)
    Hours = Remaining_Hours // 3600

    Remaining_Minutes = Remaining_Hours % 3600 
    Minutes = Remaining_Minutes // 60

    Remaining_Seconds = Remaining_Minutes % 60
    Seconds = Remaining_Seconds
    
    print('The total trip duration is: {} days,{} hours,{} minutes,{} seconds'.format(Days,Hours,Minutes,Seconds))
    Days = Mean_Travel_Time // (24 * 3600)

    Remaining_Hours = Mean_Travel_Time % (24 * 3600)
    Hours = Remaining_Hours // 3600

    Remaining_Minutes = Remaining_Hours % 3600 
    Minutes = Remaining_Minutes // 60

    Remaining_Seconds = Remaining_Minutes % 60
    Seconds = Remaining_Seconds
    print('The average travel time is: {} days,{} hours,{} minutes,{} seconds'.format(Days,Hours,Minutes,Seconds))

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    User_types_counts = df['User Type'].value_counts()
    print('\nThe users type counts as follows:\n')
    print(User_types_counts)


    # Display counts of gender
    if 'Gender' in df.columns:

        print('\nThe users gender found as follows:\n')
        User_gender_counts = df['Gender'].dropna().value_counts()
        print(User_gender_counts)
    else:
        print('Sorry No Gender Data Found')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        Earliest_Birth_Date = df['Birth Year'].dropna().min()
        print('\nThe Earliest Year of Birth is:\n')
        print(Earliest_Birth_Date)
        Most_Recent_Birth_Date = df['Birth Year'].dropna().max()
        print('\nThe Most Recent Year of Birth is:\n')
        print(Most_Recent_Birth_Date)
        The_Most_Common_Year_of_Birth = df['Birth Year'].dropna().mode()[0]
        print('\nThe Most Common Year of Birth is:\n')
        print(The_Most_Common_Year_of_Birth)
        
      
    else:
        print('Sorry No Birth Year Data Found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def Display_raw_data(city):
    """ This function enables the user to review the raw data if needed, 
        and it can be controlled so as to display 5 rows of the raw data 
        at a time, until the user decides to abort"""
    print("Do you want to review the raw data?")
    User_choice = input("Please type Yes or No \n").title()
    print(User_choice)
    if User_choice == 'Yes':
        Raw_Data = pd.read_csv(CITY_DATA[city],chunksize=5)
        print(Raw_Data.get_chunk())
        print("Do you want to review the next five rows?")
        User_choice = input("Please type Yes or No \n").title()
        while User_choice == 'Yes':
            print(Raw_Data.get_chunk())
            print("Do you want to review the next five rows?")
            User_choice = input("Please type Yes or No \n").title()
    print('Thank you and good bye')
         




        
    



    


    
def main():
    while True:
        city,Chosen_timeframe=get_filters()
        df = load_data(city,Chosen_timeframe)
        print(Chosen_timeframe)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




















