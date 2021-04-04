# This program requests a positive integer input from the user and performs 
# various arithmetic depending on whether the number is even or odd

# Author: Isabella Doyle

num = int(input("Enter a positive integer: "))  # requests input of positive int from user, converts to integer and assigns to variable num
numList = [num]                                 # assigns a list (which stores values from the sums below) to the variable numList 

while num <= 0:                                 # while loop filters out negative numbers so program runs smoothly
    print("Bad input")                          # informs the user of wrong input
    num = int(input("Enter a positive integer: ")) # requests another number input and converts to integer

while num != 1:                                 # while loop to repeatedly perform sum until num equals 1
    if num % 2 == 0:                            # checks if num is even using the modulus operator
        num = num / 2                           # if even, this block of code is performed
        numList.append(num)                     # value produced by sum is added to numList
    else:                                       # this will execute if num is odd
        num = ((num * 3) + 1)                   # performs arithmmetic on value stored in num
        numList.append(num)                     # adds the result value to numList

print([int(num) for num in numList])            # converts contents of numList from list objects to integer
                                                # objects and prints the contents of the list


'''
REFERENCES:

[1] "How to Convert a Float List to an Integer List in Python" - Evgeny Erunov <b/>
    Available at:
    https://blog.finxter.com/how-to-convert-a-float-list-to-an-integer-list-in-python/#:~:text=The%20most%20Pythonic%20way%20to,the%20int(x)%20constructor
    [Accessed: 09/01/21]
[2] "While Loops", A Whirlwind Tour of Python - Jake Vanderplas pp. 37
[3] "Python Lists" - w3schools
    Available at: https://www.w3schools.com/python/python_lists.asp [Accessed: 09/01/2021]
[4] "Python For Loops" - w3schools
    Available at: https://www.w3schools.com/python/python_for_loops.asp [Accessed: 09/01/2021]
'''