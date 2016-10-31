'''
Given a time in AM/PM format, convert it to military (24-hour) time.

NOTE: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

INPUT FORMAT:

A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12.

OUTPUT FORMAT:

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

SAMPLE INPUT:

07:05:45PM

SAMPLE OUTPUT:

19:05:45
'''

#!/bin/python3

import sys

def time_converter(ap_time):
    if int(ap_time[:2]) == 12:
        if ap_time[-2:] == 'AM':
            mili_time = '00' + ap_time[2:-2]
            print(mili_time)
        elif ap_time[-2:] == 'PM':
            print(ap_time[:-2])
        else:
            raise ValueError('Your input is not a valid time')
    else:
        if ap_time[-2:] == 'AM':
            print(ap_time[:-2])
        elif ap_time[-2:] == 'PM':
            mili_time = str(int(ap_time[:2]) + 12) + ap_time[2:-2]
            print(mili_time)
        else:
            raise ValueError('Your input is not a valid time')

time_converter('06:40:03AM')
#time_converter(input().strip())
