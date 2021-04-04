# This program asks the user to input their height and weight
# weight and calculates their BMI (Body Mass Index)

# Author: Isabella Doyle

weight = int(input("Enter weight(Kg):"))        # asks user to input their weight and converts from string to integer
height = int(input("Enter height(cm):"))        # asks user to input their height and converts from string to integer

BMI = str(round(weight/((height/100)**2),2))    # assigns the formula for calculating BMI to the variable BMI
                                                # while rounding the calculation to two decimal places and 
                                                # converting it to a string value so it can be concatenated 
                                                # in the print statement

print("Your BMI is " + BMI)                     # prints the users BMI


'''
REFERENCES:
[1] "How is BMI calculated?" - Ramsey Health Care, 
Available at: https://www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula [Accessed: 28/1/21]
[2] Vanderplas, Jacob T. A Whirlwind Tour of Python. O'Reilly Media, 2016. pp. 9
[3] "BMI Calculator" - WebDoctor, Available at: https://www.bmicalculator.ie/ [Accessed:
28/1/21]
'''