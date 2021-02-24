# This program tells the users whether it is
# weekday or weekend
# Author: Isabella Doyle

from datetime import datetime           # imports the datetime module
today = datetime.today().strftime('%A') # assigns today's date to the variable today

# uses if-else statement to determine which print statement 
# will be executed, depending on whether or not its a weekday
if today == "Monday" or "Tuesday" or "Wednesday" or "Thursday":
    print("Today is {}. It's a weekday!".format(today))
else:
    print("Today is {}. It is the weekend. Yay!")