# Pands Problem Sheet Tasks
This repository is dedicated to the fulfilment of the Programming and Scripting assessment as part of the Higher Diploma in Data Analytics at GMIT.</br>

Creator: Isabella Doyle</br>
Email: G00398800@gmit.ie

## Task 1:

*Objective: Write a program that calculates somebody's Body Mass Index (BMI).*
#### Program: calculateBMI_task1.py
```
weight = int(input("Enter weight(Kg): "))       
height = int(input("Enter height(cm): "))        

BMI = str(round(weight/((height/100)**2),2))


print("Your BMI is " + BMI)
```
#### Understanding the code: 

1. The input() function prompts the user to enter their height and weight. The string values are then converted to integer values using the int() function, and respectively assigned to the variables height and weight. 
2. The variable BMI contains the mathematical equation for calculating BMI. Also contained in the variable are 2 functions; one that rounds the sum of the equation to two decimal places, using the round() function. The other  converts the sum to a string value, using the str() function, so that it can be concantenated with another string in the print statement. 
3. The program will print the BMI for the inputted information in a sentence.

#### References:

[1] "How is BMI calculated?" Ramsey Health Care, 28 Jan. 2021,
www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula</br>
[2] Vanderplas, Jacob T. *A Whirlwind Tour of Python.* O'Reilly Media, 2016. pp. 9</br>
[3] "BMI Calculator." WebDoctor, 28 Jan. 2021, www.bmicalculator.ie 

## Task 2:

*Objective: Write a program that asks a user to input a string and outputs every second letter in reverse order.*
#### Program: secondString_task2.py
```
string = input("Enter text:")
modString = string[::-2]

print("Your original string: {}. New modified string: {}".format(string, modString))
```
#### Understanding the code: 

1. This program requests an input of text from the user and assigns the string to the variable 'string'.
2. It then modifies the value in string, starting a index 0, so that every second character is placed in reverse order in the variable 'modString'. 
3. Both the original and modified texts are printed using the .format method, concatenating them into a sentence. 
4. Example output: Your original string: hello there. New modified string: eetolh

#### References:

[1] "Built-in Functions." The Python Standard Library, 29 Jan. 2021, https://docs.python.org/3/library/functions.html</br> 
[2] "Python Numbers." w3schools, 29 Jan. 2021, www.w3schools.com/python/python_numbers.asp</br>
[3] "7.1. Fancier Output Formatting" The Python Standard Library, 29 Jan. 2021, https://docs.python.org/tutorial/inputoutput.html

## Task 3:

*Objective: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.*
#### Program: collatz_task3.py
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
#### Understanding the code:

1. The while loop performs a repeat loop as long as the value in num does not equal 1.
2. Inside the while loop is an if statement. The if statement is executed if the number is even (the modulus operand is used to check this). If even, the indented code block will be executed - dividing the the value stored in 'num' by two and appending the result to the numList. If the if statement is false, the else statement will be executed - 'num' is multiplied by 3 and 1 is added to it and the result is appended to 'numList'.
3. When 'num' equals 1, the while statement will evaluate as false causing a break out of the while loop. 
4. The print statment is then executed, which converts the list objects in 'numList' to integer objects, finally printing the list of integers.

#### References:

[1] "How to Convert a Float List to an Integer List in Python." Evgeny Erunov, 07 Feb. 2021, https://blog.finxter.com/how-to-convert-a-float-list-to-an-integer-list-in-python</br>
[2] Vanderplas, Jacob T. *A Whirlwind Tour of Python.* O'Reilly Media, 2016. pp. 37</br>
[3] "Python Lists." w3schools, 07 Feb. 2021, www.w3schools.com/python/python_lists.asp</br>
[4] "Python For Loops." w3schools, 07 Feb. 2021, www.w3schools.com/python/python_for_loops.asp

## Task 4:

*Objective: Write a program that outputs whether or not today is a weekday.*
#### Program: weekdayWeekend_task4.py
```
from datetime import datetime  
today = datetime.today().strftime('%A')

if today != "Saturday" or today != "Sunday":
    print("Today is {}. It's a weekday!".format(today))
else:
    print("Today is {}. It is the weekend. Yay!")
```
#### Understanding the code:

1. The program first imports the datetime module from the datetime library.
2. It then accesses the current day with the .today() method, converts it to a string object (using .strftime) and assigns it to the variable 'today'.
3. The if-else statement determines which block of code will be executed. If the value in the 'today' variable matches a weekday, the if statement will evaluate to true and the indented code will be executed. Otherwise, the else statment will evaluate to true and its indented code will execute.

### References:

[1] "8.1.7. strftime() and strptime() Behavior." The Python Standard Library, 12 Feb. 2021, https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior</br>
[2] "Python Datetime." - w3schools, 12 Feb. 2021, www.w3schools.com/python/python_datetime.asp

## Task 5:
*Objective: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*
#### Program: sqrt_task5.py
```
numList = [0, 0]   

def sqrt(number): 

    a = float(number) 

    while number != numList[-2]:
        number = 0.5 * (number + a / number) 
        numList.append(number)
    return round(number, 1)

number = float(input("Please enter a positive number: ")) 

while number <= 0:
    number = float(input("Please enter a POSITIVE number: "))
if number >= 0:
    print("The square root of {} is approximately {}".format(number, sqrt(number)))
```

#### Understanding the code:

1. First, the program prompts the user to enter a positive number. This number is then converted to a floating point number and stored in the variable 'number'. 
2. The while loop coupled with the if statement filters out negative numbers and the number 0. If a positive number is not entered, the while loop continously prompts the user to enter a postive number.
3. When a positive number is entered, the code inside the final if statement will be executed which contains a call to the function sqrt(number). This will print a sentence containing the original number entered and its approximate square root.
4. The sqrt() function takes in one parameter: a number. While the while loop is true (when 'number' is not equal to the second last value in numList) it continuously executes and the indented code performs aritmetic to get the approximate square root of a number. After each iteration, the result of the calculation is added to numList. The while loop stops when the result of the arithmetic is the same twice in a row. This is done by comparing the current value stored in 'number' to the the value at index -2 in the numList. 

#### References:

[1] "Find root of a number using Newton's method." GeeksforGeeks, 21 Feb. 2021, www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/</br>
[2] "Newton Square Root Method in Python." Siddik Acil, 23 Feb. 2021, https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

## Task 6:
*Objective: Write a program that reads in a text file and outputs the number of e's it contains.*
#### Program: es_task6.py
```
def readText(fileName):

    with open(fileName, 'rt') as f:   
        read = f.read()          
        count = read.count("e")       
        print(count)                  

readText("moby-dick-task6.txt")         
```

#### Understanding the code:
1. This program defines a function called readText(). It has one parameter called fileName where we input the name of the file we want to access.
2. When the function is called the program opens the file passed through as an argument in read-text mode and aliases this as f. 
3. The read() method reads in the text contained in f and assigns it to the variable read. 
4. The count() method is then applied to the read variable to count how many e's appear in the text.
5. Finally, the function prints out the number of instances the letter e appears in the text.
#### References:

[1] "Reading and Writing Files in Python (Guide)." James Mertz, 15 Mar. 2021, https://realpython.com/read-write-files-python

## Task 7:
*Objectives: Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.*
#### Program: plotTask_task7.py
```
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

x = np.array([0, 1, 2, 3])

y1 = x          # f(x) = x
y2 = x ** 2     # g(x) = x^2
y3 = x ** 3     # h(x) = x^3

plt.plot(y1,label='f(x) = x')
plt.plot(y2,label='g(x) = x^2')
plt.plot(y3,label='h(x) = x^3')

plt.xlabel('x-axis', fontsize=8)
plt.ylabel('y-axis', fontsize=8)

plt.title('Plot of functions: f(x) = x, g(x) = x^2, h(x) = x^3', fontsize=10)

plt.legend(loc='upper left', borderaxespad=2)

plt.savefig('myPlot.jpg')

plt.show()
```
#### Understanding the code:

1. First, the numpy and matplotlib libraries are imported.
2. A style for the graphical plot, called ggplot, is selected from the matplotlib library. 
3. A multi-dimensional numpy array is created with the x-axis values. The values are stored in a tuple in the array. 
4. The y-axis functions are stored in variables y1, y2, y3. 
5. Plt.plot() plots the values on the y-axis. The first argument is the plot itself, and the second is the label for each plot, which is the corresponding function.
6. The plt.xlabel() and plt.ylabel() methods label the y and x-axes. The first argument is the label title and the second is the fontsize of the label. 
7. The plt.title() method sets a title for the entire plot.
8. Plt.legend() inserts a legend onto the plot in a specified location. The legend indicates which function corresponds to which line, using color code. 
9. Plt.savefig() saves the graphical plot. The file name for saving the plot is specified in the brackets in single quotes. 
10. Finally, the plt.show() method opens up a seperate window displaying the graphical plot created in this program.

#### References:

[1] "matplotlib.pyplot.plot" matplotlib, 26 Mar. 2021, https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html</br>
[2] "Style sheets reference" matplotlib, 30 Mar. 2021, https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html</br>
[3] "Matplotlib Pyplot." w3schools, 26 Mar. 2021, www.w3schools.com/python/matplotlib_pyplot.asp</br>
[4] "Python Plotting With Matplotlib (Guide)" Brad Solomon, 28 Mar. 2021, https://realpython.com/python-matplotlib-guide/</br>
[5] "How to change the font size on a matplotlib plot." Herman Schaaf, 30 Mar. 2021, https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot