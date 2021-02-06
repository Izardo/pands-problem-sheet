# This program requests an string input from the user 
# and outputs every second character in reverse order. 
# Author: Isabella Doyle

string = input("Enter text:")   # requests string input from user
modString = string[::-2]        # when printed it will output
                                # every second character in reverse

print("Your string has been modified from this: {} to this: {}".format(string, modString))