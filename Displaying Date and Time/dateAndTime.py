import time;
print(time.time());

import calendar;
print calendar.calendar(2010);
print calendar.month(2016,6);
 
import datetime;
user=datetime.now();

#it will display date and time both

print str(user);
print user.year;
print user.month;
print user.day;
print user.hour;
print user.minute;
print user.second;
print user.microsecond;
