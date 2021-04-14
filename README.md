# Pands Problem Sheet Tasks
This repository is dedicated to the fulfilment of the Programming and Scripting assessment as part of the Higher Diploma in Data Analytics at GMIT.</br>

Creator: Isabella Doyle, Email: G00398800@gmit.ie
(add date of completion & maybe add assessment description)
## Task 1:

*Objective: Write a program that calculates somebody's Body Mass Index (BMI).*
### Program: calculateBMI_task1.py
```
weight = int(input("Enter weight(Kg):"))       
height = int(input("Enter height(cm):"))        

BMI = str(round(weight/((height/100)**2),2))


print("Your BMI is " + BMI)
```
Understanding the code: 

1. The input() function prompts the user to enter their height and weight, the string values are then converted to integer (using the int() function) and respectively assigned to the variables height and weight. 
2. The variable BMI contains the mathematical equation for calculating BMI. Also contained in the variable are 2 functions; one which rounds the sum of the equation to two decimal places (using the round() function) and another that converts the sum to a string value (using the str() function) so that it can be concantenated with another string in the print statement. 
3. The program will print the BMI for the input.

#### References:

[1] "How is BMI calculated?" Ramsey Health Care, 28 Jan. 2021,
www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula</br>
[2] Vanderplas, Jacob T. *A Whirlwind Tour of Python.* O'Reilly Media, 2016. pp. 9</br>
[3] "BMI Calculator." WebDoctor, 28 Jan. 2021, www.bmicalculator.ie 

## Task 2:

*Objective: Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*
### Program: secondString_task2.py
```
string = input("Enter text:")
modString = string[::-2]

print("Your original string: {}. New modified string: {}".format(string, modString))

```
Understanding the code: 

1. This program requests an input of text from the user and assigns the string to the variable 'string'.
2. It then modifies the value in string, starting a index 0, so that every second character is placed in reverse order in the variable 'modString'. 
3. Both the original and modified texts are printed using the .format method to concatenate them into a sentence. 
4. Example output: Your original string: hello there. New modified string: eetolh

#### References:

[1] "Built-in Functions." The Python Standard Library, 29 Jan. 2021, docs.python.org/3/library/functions.html</br> 
[2] "Python Numbers." w3schools, 29 Jan. 2021, www.w3schools.com/python/python_numbers.asp</br>
[3] "7.1. Fancier Output Formatting" The Python Standard Library, 29 Jan. 2021, www.docs.python.org/tutorial/inputoutput.html

## Task 3:

*Objective: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.*
### Program: collatz_task3.py
```
while num != 1:         
    if num % 2 == 0:      
        num = num / 2            
        numList.append(num)        
    else:                      
        num = ((num * 3) + 1)           
        numList.append(num)                 
                                               
print([int(num) for num in numList])
```
Understanding the code:

1. The while loop performs a repeat loop as long as the number equals 1.
2. Inside the while loop is an if statement. which will be exected if the number is even (the modulus operand is used to check this). If the if statment is true, the indented code block will be executed - dividing the the value stored in 'num' by two and appending the result to the numList. If the if statement is false, the else statement will be executed - 'num' is multiplied by 3 and 1 is added to it and the resut is appended to 'numList'.
3. When 'num' equals 1, the while statement will evaluate as false causing a break out of the while loop. 
4. The print statment is then executed, which converts the list objects in 'numList' to integer objects, finally, printing the list of integers.

#### References:

[1] "How to Convert a Float List to an Integer List in Python." Evgeny Erunov, 07 Feb. 2021, blog.finxter.com/how-to-convert-a-float-list-to-an-integer-list-in-python</br>
[2] Vanderplas, Jacob T. *A Whirlwind Tour of Python.* O'Reilly Media, 2016. pp. 37</br>
[3] "Python Lists." w3schools, 07 Feb. 2021, www.w3schools.com/python/python_lists.asp</br>
[4] "Python For Loops." w3schools, 07 Feb. 2021, www.w3schools.com/python/python_for_loops.asp

## Task 4:

*Objective: Write a program that outputs whether or not today is a weekday.*
### Program: weekdayWeekend_task4.py
```
from datetime import datetime  
today = datetime.today().strftime('%A')

if today == "Monday" or "Tuesday" or "Wednesday" or "Thursday":
    print("Today is {}. It's a weekday!".format(today))
else:
    print("Today is {}. It is the weekend. Yay!")
```
Understanding the code:

1. The program first imports the datetime module from the datetime library.
2. It then accesses the current day with the .today() method, converts it to a string object (using .strftime) and assigns it to the variable 'today'.
3. The if-else statement determines which block of code will be executed. If the value in the 'today' variable matches a weekday, the if statement will evaluate to true and the indented code will be executed. Otherwise, the else statment will evaluate to true and its indented code will execute.

### References:

[1] "8.1.7. strftime() and strptime() Behavior." The Python Standard Library, 12 Feb. 2021, docs.python.org/2/library/datetime.html#strftime-strptime-behavior</br>
[2] "Python Datetime." - w3schools, 12 Feb. 2021, www.w3schools.com/python/python_datetime.asp

## Task 5:
*Objective: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*
### Program: sqrt_task5.py
```
numList = [0, 0]   

def sqrt(number): 

    a = float(number)                   

    while number != numList[-2]:       
        number = 0.5 * (number + a / number)   
        numList.append(number)     
    return round(number, 1)  

number = float(input("Please enter a positive number: "))

if number <= 0:  
    print("Please enter a POSITIVE number: ")
else:  
    print("The square root of {} is approximately {}".format(number, sqrt(number))) 

```
#### References:

[1] "Find root of a number using Newton's method." GeeksforGeeks, 21 Feb. 2021, www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/</br>
[2] "Newton Square Root Method in Python." Siddik Acil, 23 Feb. 2021, medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

## Task 6:
*Objective: Write a program that reads in a text file and outputs the number of e's it contains.*
### Program: es_task6.py
```
def readText(fileName):                 # creates a function with one parameter (will be used to input a file name)

    with open(fileName, 'rt') as f:     # opens the file in read-text mode and assigns it the alias "f"
        read = f.read()                 # reads in the file and assigns it to the value read
        count = read.count("e")         # count method returns no. of instances the character "e" appears in the file
        print(count)                    # prints the count when the function is called

readText("moby-dick-task6.txt")         # calls the readText function with the file name input as an argument

```
#### References:

[1] "Reading and Writing Files in Python (Guide)." James Mertz, 15 Mar. 2021, realpython.com/read-write-files-python

## Task 7:
*Objectives: Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.*
### Program: plotTask_task7.py
```
# imports numpy and matplotlib for creating an array and plot respectively
import numpy as np
import matplotlib.pyplot as plt

# selects graphical style for plot
plt.style.use('ggplot')

# x-axis value range
x = np.array([0, 1, 2, 3])  # uses numpy to create a multi-dimensional array of x-axes values

# y-axis values
y1 = x          # f(x) = x
y2 = x ** 2     # g(x) = x^2
y3 = x ** 3     # h(x) = x^3

# plots the values on the y-axes
plt.plot(y1,label='f(x) = x')
plt.plot(y2,label='g(x) = x^2')
plt.plot(y3,label='h(x) = x^3')

# add labels for x and y axes and sets font-size
plt.xlabel('x-axis', fontsize=8)
plt.ylabel('y-axis', fontsize=8)

# adds a plot title and sets font-size
plt.title('Plot of functions: f(x) = x, g(x) = x^2, h(x) = x^3', fontsize=10)

# adds legend to plot and sets padding
plt.legend(loc='upper left', borderaxespad=2)

# saves the plot figure
plt.savefig('myPlot.jpg')

# displays the plot figure
plt.show()
```
#### References:

[1] "matplotlib.pyplot.plot" matplotlib, 26 Mar. 2021, matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html</br>
[2] "Style sheets reference" matplotlib, 30 Mar. 2021, matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html</br>
[3] "Matplotlib Pyplot." w3schools, 26 Mar. 2021, www.w3schools.com/python/matplotlib_pyplot.asp</br>
[4] "Python Plotting With Matplotlib (Guide)" Brad Solomon, 28 Mar. 2021, realpython.com/python-matplotlib-guide/</br>
[5] "How to change the font size on a matplotlib plot." Herman Schaaf, 30 Mar. 2021, stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot