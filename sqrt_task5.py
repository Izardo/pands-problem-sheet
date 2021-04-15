# This program defines a function which returns the  
# square root of a number using Newton's method

# Author: Isabella Doyle

# numList stores the result of the for loop iterations from the sqrt function
numList = [0, 0]   
# the sqrt function takes in two values, the second is pre-defined
def sqrt(number): 

    a = float(number)                           # value that we want to get the square root of

    while number != numList[-2]:                # the while loop is executed until the result of the code in the next line is the same twice
        number = 0.5 * (number + a / number)    # uses newton's formula to estimate the square of a number
        numList.append(number)                  # number placed in list so it can be compared to the current number breaking the while loop broken when appropriate
    return round(number, 1)                     # rounds number to 1 decimal place

# main program requests the user to input a positive number
number = float(input("Please enter a positive number: ")) # requests input from the user, converts input to float and assigns to variable 'number'

# If statment filters out negative numbers and the number 0
# If else statement executes, the square root is returned

while number <= 0:  # filters out negative
    number = float(input("Please enter a POSITIVE number: ")) # prompts the user to enter a positive number
if number >= 0:
    print("The square root of {} is approximately {}".format(number, sqrt(number))) # prints the approx. square root of 'number' in a sentence

'''
REFERENCES:

[1] "Find root of a number using Newton's method" - GeeksforGeeks <br/>
Available at: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N 
[2] "Newton Square Root Method in Python" - Siddik Acil <br/>
Available at: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
'''