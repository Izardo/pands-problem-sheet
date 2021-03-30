# This program asks the user to input their height 
# and weight and calculates their BMI

# Author: Isabella Doyle

weight = int(input("Enter weight(Kg):"))    # asks user to input their weight and converts from string to integer
height = int(input("Enter height(cm):"))    # asks user to input their height and converts from string to integer

BMI = str(round(weight/((height/100)**2),2))    # assigns the formula for calculating BMI to the variable BMI
                                                # while rounding the calculation to two decimal places and 
                                                # converting it to a string value so it can be concatenated 
                                                # in the print statement

print("Your BMI is " + BMI)                     # prints the users BMI
