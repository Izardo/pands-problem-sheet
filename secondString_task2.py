# This program requests a string input from the user 
# and outputs every second character in reverse order. 

# Author: Isabella Doyle

string = input("Enter text:")   # requests string input from user
modString = string[::-2]        # when printed it will output
                                # every second character in reverse

print("Your original string: {}. New modified string: {}".format(string, modString))