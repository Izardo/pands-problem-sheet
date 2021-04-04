# This program tells the users whether it is a
# weekday or weekend

# Author: Isabella Doyle

from datetime import datetime           # imports the datetime module from the datetime library
today = datetime.today().strftime('%A') # accesses the current day with the today() method, while the .strftime() 
                                        # method converts the current day to a string value and assigns it to the variable 'today'

# if-else statement determines which print statement will be executed, 
# if the value in variable 'today' matches a weekday, the first statement will be executed 
# otherwise the second statment will be executed
if today == "Monday" or "Tuesday" or "Wednesday" or "Thursday":
    print("Today is {}. It's a weekday!".format(today))
else:
    print("Today is {}. It is the weekend. Yay!")


'''
REFERENCES:

[1] "8.1.7. strftime() and strptime() Behavior"
    Available at: https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior 
    [Accessed: 12/02/2021]
[2] "Python Datetime" - w3schools
    Available at: https://www.w3schools.com/python/python_datetime.asp [Accessed: 12/02/2021]
'''