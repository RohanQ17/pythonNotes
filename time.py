import time
# epoch = a date and time from which the system measured date n time
#print(time.ctime(0))    #ctime() converts seconds since epoch to readable date and time

#print(time.time()) #current seconds since epoch
#print(time.ctime(time.time()))

time_object =time.localtime()
print(time_object)
time_object=time.strftime("%B %D %H:%M:%S",time_object)
print(time_object)

string = "20 april ,2020"   #parsing a string into a time object
object =time.strptime(string,"%d %B ,%Y")
print(object)

# (year, month,days,hours , minutes,secs, #day of the week<day of the year, daylight savings time)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)



