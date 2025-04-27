""" INFORMATION

Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

1. Calling add_time('3:30 PM', '2:12') should return '5:42 PM'.
2. Calling add_time('11:55 AM', '3:12') should return '3:07 PM'.
3. Expected time to end with '(next day)' when it is the next day.
4. Expected period to change from AM to PM at 12:00.
5. Calling add_time('2:59 AM', '24:00') should return '2:59 AM (next day)'.
6. Calling add_time('11:59 PM', '24:05') should return '12:04 AM (2 days later)'.
7. Calling add_time('8:16 PM', '466:02') should return '6:18 AM (20 days later)'.
8. Expected adding 0:00 to return the initial time.
9. Calling add_time('3:30 PM', '2:12', 'Monday')should return '5:42 PM, Monday'.
10. Calling add_time('2:59 AM', '24:00', 'saturDay') should return '2:59 AM, Sunday (next day)'.
11. Calling add_time('11:59 PM', '24:05', 'Wednesday') should return '12:04 AM, Friday (2 days later)'.
12. Calling add_time('8:16 PM', '466:02', 'tuesday') should return '6:18 AM, Monday (20 days later)'.

"""

# Solution by Javier Serrano Jodral

def add_time(start, duration, starting_day=False):
    """
    This function takes a start time and a duration, and returns the new time after adding the duration to the start time.
    Starting day is optional and if provided, the function will also return the new day of the week.
    """
    
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    time, ampm = start.split(' ')
    start_hour, start_minutes = list(map(int, time.split(':')))
    dur_hour, dur_minutes = list(map(int, duration.split(':')))
    
    # Minutes computing -> Extra hours
    sum_minutes = start_minutes + dur_minutes
    add_hour = 0
    if sum_minutes >= 60:
        new_minutes = sum_minutes%60
        add_hour = 1
    else:
        new_minutes = sum_minutes

    if new_minutes < 10: new_minutes = '0'+str(new_minutes)

    # Hours computing -> Extra days and AM or PM
    sum_hour = start_hour + dur_hour + add_hour
    add_days = 0

    if ampm == 'AM':
        if sum_hour >= 24:     # add new days and recalculate AM or PM
            add_days = int(sum_hour/24)
            new_hour = sum_hour%12
            if new_hour == 0: new_hour=12
            if int(sum_hour/12) %2 == 0:   # if even, AM -> AM
                new_ampm = 'AM'
            else:                          # if odd, AM -> PM
                new_ampm = 'PM'
        elif sum_hour >= 12:   # change to PM
            new_hour = sum_hour%12
            if new_hour == 0: new_hour=12
            new_ampm = 'PM'
        else:                  # still AM
            new_hour = sum_hour
            new_ampm = 'AM'

    else:   # PM
        if sum_hour >= 12:     # add new days and recalculate AM or PM
            add_days = int(sum_hour/24) + 1
            new_hour = sum_hour%12
            if new_hour == 0: new_hour=12
            if int(sum_hour/12) %2 == 0:   # if even, PM -> PM
                new_ampm = 'PM'
            else:                          # if odd, PM -> AM
                new_ampm = 'AM'          

        else:  # still PM, same day
            new_hour = sum_hour
            new_ampm = 'PM'


    # Returning string
    new_time = str(new_hour) + ":" + str(new_minutes) + ' ' + new_ampm

    if starting_day:
        # Computing day of the week and adding it to the string
        current_day = starting_day.capitalize()
        new_day_index = DAYS.index(current_day) + add_days
        new_day = DAYS[new_day_index%len(DAYS)]   # reset index in case of out of range

        new_time += ', ' +new_day
    

    if add_days == 1:
        new_time += ' (next day)'
    elif add_days > 1:
        new_time += f' ({add_days} days later)'
    

    print('New time: '+ str(new_time))
    return new_time





add_time('11:55 AM', '3:12')
add_time('2:59 AM', '24:00')
add_time('8:16 PM', '466:02')

add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday')