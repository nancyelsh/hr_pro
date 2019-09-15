#from datetime import *
import datetime
from datetime import date

def check_birthdate(year, month, day):

  if datetime.datetime(year = year, month = month, day = day) <= datetime.datetime.now():
    return calculate_age(year, month, day)

  else:
    return "Birthdate is invalid"

def calculate_age(year, month, day):
  today = date.today()
  age = today.year - year - ((today.month, today.day) < (month, day))
  return age

birthdate = input("Enter your birthdate (year,month,day): ")
year,month,day = birthdate.split(',')
print(check_birthdate(int(year),int(month),int(day)))
