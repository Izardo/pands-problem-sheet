# This program requests a string input from the user 
# and outputs every second character in reverse order. 

# Author: Isabella Doyle

string = input("Enter text:")   # requests string input from user and assigns input to the variable 'string'
modString = string[::-2]        # modifies value in 'string', starting at index 0, we are left with every 
                                # second character in reverse and assigns it to the variable modString 
                                # (Example: Hello -> olh)

# prints the original string as well as the new modified string, 
# the values are inserted in print statement using the .format method
print("Your original string: {}. New modified string: {}".format(string, modString))


'''
REFERENCES:

[1] "Built-in Functions" - The Python Standard Library 
    Available at: https://docs.python.org/3/library/functions.html [Accessed: 29/01/21]
[2] "Python Numbers" - w3schools
    Available at: https://www.w3schools.com/python/python_numbers.asp [Accessed: 29/01/21]
[3] "7.1. Fancier Output Formatting" - The Python Standard Library 
    Available at: https://docs.python.org/3/tutorial/inputoutput.html [Accessed: 29/01/21]
'''