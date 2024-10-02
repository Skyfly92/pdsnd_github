import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']


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
    valid_city = False
    while valid_city == False:
        try:
            selected_city = input('Enter a city name to analyze (available: chicago, new york city, washington): ').lower()
        except:
            print('Thats no valid entry!')
        else:
            if selected_city in CITY_DATA:
                valid_city = True
            else:
                print('There are no data for the selected city. Please enter another one.')

    city = selected_city
    
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_month = False
    while valid_month == False:
        try:
            selected_month = input("Enter a month name to filter by. Enter 'all' to apply no month filter: ").lower()
        except:
            print("Thats no valid entry!")
        else:
            if selected_month in months:
                valid_month = True
            else:
                print("This is no valid entry. Please try again.")    
            
    month = selected_month

    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_names=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    valid_day = False
    while valid_day == False:
        try:
            selected_day = input("Enter a dayname to filter by. Enter 'all' to apply no weekday filter: ").lower()
        except:
            print("Thats no valid entry!")
        else:
            if selected_day in day_names:
                valid_day = True
            else:
                print("This is no valid entry. Please try again")
                
    day = selected_day

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #load city data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #save count of rows before filter
    df_count_unfiltered = df.shape[0]
    
    #convert start time column to datetime and extract month & dayname in new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.day_name()
    
    #filter by month if not 'all' is selected
    if month != 'all':
        #select month by index to get month number
        month = months.index(month) + 1
        
        #create new filtered dataframe
        df = df[ df['month'] == month]
    
    #filter by name of weekday if not 'all' is selected and create new filtered dataframe
    if day != 'all':
        df = df[ df['weekday'] == day.title()]
    
    print("Filtered dataframe: {} of {} rows selected".format(df.shape[0], df_count_unfiltered))
    
    print('-'*40)
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: ", months[common_month-1].title())

    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    print("The most common day of week: ", common_day.title())

    # TO DO: display the most common start hour
    #add column hour
    df['hour'] = df['Start Time'].dt.hour
    #find the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', common_start_hour) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station: ', common_start_station) 

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['From_To'] = df['Start Station'] + " - " + df['End Station']
    common_start_end_combo = df['From_To'].mode()[0]
    print("The most common combination of start and end station: ", common_start_end_combo)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_sum = df['Trip Duration'].sum()
    print("Total travel time {} seconds ({} minutes)".format(travel_time_sum, round(travel_time_sum/60,1)))


    # TO DO: display mean travel time
    travel_time_avg = df['Trip Duration'].mean()
    print("Total travel time {} seconds ({} minutes)".format(round(travel_time_avg,1), round(travel_time_avg/60,1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print("\nCount of user types: \n", counts_user_types)
    
    # TO DO: Display counts of gender
    #not all raw data have column 'Gender'
    if 'Gender' in df.columns:
        counts_genders = df['Gender'].value_counts()
        print("\nCount of genders: \n", counts_genders)
    else:
        print("\nNo information about gender available for this city.")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    #not all raw data have column 'Birth Year'
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nEarliest year of birth: ", earliest_birth_year)
        print("Most recent year of birth: ", most_recent_birth_year)
        print("Most common year of birth: ",  most_common_birth_year)
    else:
        print("No information about birth year available for this city.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def df_parter(df, size):
    """Yields successive parts of the df raw data in legth of size"""
    for i in range(0,df.shape[0],size):
        yield df.iloc[i:i+size]
    return

def display_raw_data(df):
    #show raw data in groups of 5 rows if requested
    while True:
        try:
            while input("Do you want to see five rows of raw data(Yes/No)?").title() == "Yes":
                for part in df_parter(df,5):
                    print(part)
                    print('-'*40)

                    while True:
                        try:
                            if input("Do you want to see the next five rows of raw data (Yes/No)?").title() != "Yes":
                                return
                            break
                        except:
                            print("Please respond with yes or no")
        
            break
        except:
            print("Please answer with yes or no")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        if df.shape[0] == 0 :
            print("There are no data for the selected filters. Please select other filters.")
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            
            display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
