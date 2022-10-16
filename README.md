# Personal
Personal Files are included here

# Python

## W3SCHOOLS TEST OWN

You can get the data type of a variable with the type() function.

String variables can be declared either by using single or double quotes:

Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a

Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"


One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
Example
x = y = z = "Orange"
print(x)
print(y)
print(z)
—---------
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
—----------------




There are three numeric types in Python:
int
float
Complex
 
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".

Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])


Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
Example
Loop through the letters in the word "banana":
for x in "banana":
  print(x)

The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)
print(“free” not in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")






