# This program calculates BMI
# Author: Isabella Doyle

weight = int(input("Enter weight(Kg):"))    # asks user to input their weight
height = int(input("Enter height(cm):"))    # asks user to input their height

BMI = str(round(weight/((height/100)**2),2))  # calculates BMI

print("Your BMI is " + BMI + ".")           # prints the users BMI
