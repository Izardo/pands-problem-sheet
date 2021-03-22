# This program allows the users to to count the number of times
# the character "e" appears in a chosen file

# Author: Isabella Doyle

fileName = str(input("Enter the file you wish to use: "))   # requests the user to input the file name they wish to use 

with open(fileName, 'rt') as f:     # opens the file in read text mode
    readTxt = f.read()              # reads in the file and assigns it to the value readTxt
    count = readTxt.count("e")      # count method returns no. of instances the character "e" appears in the file
    print(count)                    # prints the count 

