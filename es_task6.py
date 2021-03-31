# This program allows the users to count the number of times
# the character "e" appears in a chosen file

# Author: Isabella Doyle

def readText(fileName):                 # creates a function with one parameter (will be used to input a file name)

    with open(fileName, 'rt') as f:     # opens the file in read-text mode and assigns it the alias "f"
        read = f.read()                 # reads in the file and assigns it to the value read
        count = readTxt.count("e")      # count method returns no. of instances the character "e" appears in the file
        print(count)                    # prints the count when the function is called

readText("moby-dick.txt")               # calls the readText function with the file name input as an argument