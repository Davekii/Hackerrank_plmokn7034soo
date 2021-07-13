import calendar
import os 
from datetime import date



m, d, y = input().split()   
m = int(m)    
d = int(d)   
y = int(y)   




day = calendar.weekday(y, m, d)
day_color = ["MONDAY", "TUSEDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]


find_day_color = day_color[day]
print(find_day_color)
