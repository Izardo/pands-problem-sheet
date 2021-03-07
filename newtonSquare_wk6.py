# This program uses defines a function which calculates the  
# square root of a number using Newton's method

# Author: Isabella Doyle

# This function calculates the approximate square root of a number
def newtonSqrt(number, iterations = 10):  # the function takes in two values, the second is pre-defined

    a = float(number)  # value that we want to get the square root of

    for i in range(iterations):  # this for loop iterates 10 times get an approximate sqaure root of a number
        number = 0.5 * (number + a / number)  # newton's formula to estimate the square of a number
    return round(number, 1)  # rounds the sum of the previous calculation to 1 decimal place

# main program
number = float(input("Please enter a positive number: ")) # requests the user to input a positive number

if number <= 0:  # if/else statement filters out negative numbers and the number 0
    print("Please enter a POSITIVE number: ")  # prompts the user to enter a positive number
else:  # if executed, prints out the important information such as the input and output of the calculation
    print("The square root of {} is approximately {}".format(number, newtonSqrt(number))) 