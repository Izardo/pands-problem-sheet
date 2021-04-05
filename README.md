# Pands Problem Sheet Tasks
This repository is dedicated to the fulfilment of the Programming and Scripting assessment as part of the Higher Diploma in Data Analytics at GMIT.</br>

Creator: Isabella Doyle, Email: G00398800@gmit.ie

## Task 1:

*Objective: Write a program that calculates somebody's Body Mass Index (BMI).*
### Program : calculateBMI_task1.py
```
weight = int(input("Enter weight(Kg):"))       
height = int(input("Enter height(cm):"))        

BMI = str(round(weight/((height/100)**2),2))


print("Your BMI is " + BMI)
```
Understanding the code: 

1. The input() function prompts the user to enter their height and weight, the string values are then converted to integer (using the int() function) and respectively assigned to the variables height and weight. 
2. The variable BMI contains the mathematical equation for calculating BMI. Also contained in the variable are 2 functions; one which rounds the sum of the equation to two decimal places (using the round() function) and another that converts the sum to a string value (using the str() function) so that it can be concantenated with another string in the print statement. 
3. The program will print the BMI for the input

#### References:

[1] "How is BMI calculated?" Ramsey Health Care, 28 Jan. 2021,
www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula</br>
[2] Vanderplas, Jacob T. *A Whirlwind Tour of Python.* O'Reilly Media, 2016. pp. 9</br>
[3] "BMI Calculator." WebDoctor, 28 Jan. 2021, www.bmicalculator.ie 

## Task 2:

*Objective: Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*
#### References:

[1] "Built-in Functions." The Python Standard Library, 29 Jan. 2021, docs.python.org/3/library/functions.html</br> 
[2] "Python Numbers." w3schools, 29 Jan. 2021, www.w3schools.com/python/python_numbers.asp</br>
[3] "7.1. Fancier Output Formatting" The Python Standard Library, 29 Jan. 2021, www.docs.python.org/          tutorial/inputoutput.html

## Task 3:

*Objective: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.*
#### References:

[1] "How to Convert a Float List to an Integer List in Python." Evgeny Erunov, 07 Feb. 2021, blog.finxter.com/how-to-convert-a-float-list-to-an-integer-list-in-python</br>
[2] Vanderplas, Jacob T. *A Whirlwind Tour of Python.* O'Reilly Media, 2016. pp. 37</br>
[3] "Python Lists." w3schools, 07 Feb. 2021, www.w3schools.com/python/python_lists.asp</br>
[4] "Python For Loops." w3schools, 07 Feb. 2021, www.w3schools.com/python/python_for_loops.asp

## Task 4:

*Objective: Write a program that outputs whether or not today is a weekday.*

[1] "8.1.7. strftime() and strptime() Behavior." The Python Standard Library, 12 Feb. 2021, docs.python.org/2/library/datetime.html#strftime-strptime-behavior</br>
[2] "Python Datetime." - w3schools, 12 Feb. 2021, www.w3schools.com/python/python_datetime.asp

## Task 5:
*Objective: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*
#### References:

[1] "Find root of a number using Newton's method." GeeksforGeeks, 21 Feb. 2021, www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/</br>
[2] "Newton Square Root Method in Python." Siddik Acil, 23 Feb. 2021, medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

## Task 6:
*Objective: Write a program that reads in a text file and outputs the number of e's it contains.*
#### References:

[1] "Reading and Writing Files in Python (Guide)." James Mertz, 15 Mar. 2021, realpython.com/read-write-files-python

## Task 7:
*Objectives: Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.*
#### References:

[1] "matplotlib.pyplot.plot" matplotlib, 26 Mar. 2021, matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html</br>
[2] "Style sheets reference" matplotlib, 30 Mar. 2021, matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html</br>
[3] "Matplotlib Pyplot." w3schools, 26 Mar. 2021, www.w3schools.com/python/matplotlib_pyplot.asp</br>
[4] "Python Plotting With Matplotlib (Guide)" Brad Solomon, 28 Mar. 2021, realpython.com/python-matplotlib-guide/</br>
[5] "How to change the font size on a matplotlib plot." Herman Schaaf, 30 Mar. 2021, stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot