# This program requests a positive integer input from the user and performs 
# various arithmetic depending on whether the number is even or odd
# Author: Isabella Doyle

num = int(input("Enter a positive integer: "))  # requests input of positive int from user
numList = [num]                                 # a list for storing values from sums below

while num <= 0:                     # filters out negative numbers so program runs smoothly
    print("Bad input")              # informs the user of wrong input
    num = int(input("Enter a positive integer: ")) # requests another number input

while num != 1:                     # while loop to repeatedly perform sum until num equals 0
    if num % 2 == 0:                # checks if num is even 
        num = num / 2               # if even, this block of code is performed
        numList.append(num)         # value produced by sum is stored in the list created earlier
    else:                           # this will execute if num is odd
        num = ((num * 3) + 1)       # performs arithmmetic on value stored in num
        numList.append(num)         # adds the resulting value to the list

print([int(num) for num in numList])    # converts contents of numList from list objects to integer
                                        # objects and prints the contents of the list
