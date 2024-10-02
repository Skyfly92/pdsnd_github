### Date created
2024-10-02

### Project Title
Explore US Bikeshare Data


### Description
Python tool to analyse bikeshare data from different cities.

It displays the statistics for

+ the times of travel with most common 
    + month (_only providable if month filter is_ `all`)
    + day if week (_only providable if day of week filter is_ `all`)
    + start hour


+ the most polular stations and trips with most common
    + start station
    + end station
    + combination of start and endstation


+ trip durations like
    + total time of travels with bikeshare
    + Average travel time


+ bikeshare users
    + count of usertypes
    + count of genders
    + earliest year of birth
    + most recent year of birth
    + most common year of birth

After the statistics you are able to look at raw data in blocks of 5 rows.


### Filters
The filter for **city** chooses the csv file to look at. Please be sure of the spelling and that you have the csv for the selected city.

The filter for **month** needs the name of the month (like `january`)

The filter for **dayname** needs the name of the weekday (like `monday`) 

To see **all months and weekdays**, just enter `all` on both inputs.

If your selected filter left no data to look at, a message inform you about it and let you restart with new filter values.


### Files used
+ chicago.csv
+ new_york_city.csv
+ washington.csv

**be sure to locate them in the same folder as the python file**


### Credits
This file is inspired by the [create-your-own-adventure-Readme](https://github.com/udacity/create-your-own-adventure)
