import datetime

year = int(input("What year were you born in: "))
month = int(input("What month were you born in: "))
day = int(input("What day were you born on: "))

x = datetime.datetime.now()

y = datetime.datetime(year, month, day)

seconds = x-y

print("The total number of seconds you have lived is:", seconds.total_seconds())