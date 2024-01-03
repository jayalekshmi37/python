class time:
   def __init__(self, hour=0, minute=0, second=0):
     self._hour = hour
     self._minute = minute 
     self._second = second 
   def __add__(self, other):
     total_seconds = self._hour * 3600 + self._minute * 60 + self._second + \
     other._hour * 3600 + other._minute * 60 + other._second
     new_hour, remainder = divmod(total_seconds, 3600)
     new_minute, new_second = divmod(remainder, 60)
     return time(new_hour, new_minute, new_second)
   def __str__(self):
     return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"
h1=int(input("Enter hour: "))     
m1=int(input("Enter minute: "))
s1=int(input("Enter second: "))
h2=int(input("Enter hour: "))     
m2=int(input("Enter minute: "))
s2=int(input("Enter second: "))
time1=time(h1,m1,s1)
time2=time(h2,m2,s2)
sum_time=time1+time2  
print("Sum of time1 and time2 is ",sum_time)
