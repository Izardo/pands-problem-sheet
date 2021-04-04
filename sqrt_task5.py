# This program defines a function which returns the  
# square root of a number using Newton's method

# Author: Isabella Doyle

# the sqrt function takes in two values, the second is pre-defined
def sqrt(number, iterations = 10): 

    a = float(number)           # value that we want to get the square root of

    for _ in range(iterations): # this for loop iterates 10 times get an approximate sqaure root of a number
        number = 0.5 * (number + a / number)  # uses newton's formula to estimate the square of a number
    return round(number, 1)     # rounds number to 1 decimal place

# main program requests the user to input a positive number
number = float(input("Please enter a positive number: ")) 

# If statment filters out negative numbers and the number 0
# If else statement executes, the square root is returned
if number <= 0:  
    print("Please enter a POSITIVE number: ")  # prompts the user to enter a positive number
else:  
    print("The square root of {} is approximately {}".format(number, sqrt(number)))


'''
REFERENCES:

[1] "Find root of a number using Newton's method" - GeeksforGeeks <br/>
Available at: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N 
[2] "Newton Square Root Method in Python" - Siddik Acil <br/>
Available at: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
'''