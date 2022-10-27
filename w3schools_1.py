#comment 1
#multi line comments
#W3schoools_files_test_examples
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)
#new
p=3
q=3
r=3
print(p + q + r)

#new
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#new
def amarFunc():
    print(x)
amarFunc()

#new
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)

#new
a = "Hello, World!"
print(a[1])
print(a[0])
print(len(a))
b = "Hello GTA V"
print(b[0], b[1])
print(len(b))

txt = "The best things in life are free!"
print("free" in txt)
tm = "Laddu is delicious"
print("Laddu" in tm, "is" in tm)

txt = "The best things in life are free!"
print("expensive" not in txt)
print(txt[0:4])
#new- python slicing
b = "Hello, World!"
print(b[2:])
print(b[:2])
t = "CONCATENATION"
print(t[0:])
#new-upper case
c = "Hello World"
print(c.upper())
#prints HELLO WORLD
#new
a = "Hello, World!"
print(a.lower())
#The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
b = "    mishti"
print(b) #prints     mishti
print(b.strip()) #removes whitespace and prints mishti
#replacing from a string
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("e", "F"))
print(a.replace("l", "F"))
# Jello, World!
# HFllo, World!
# HeFFo, WorFd!
#new
a = "Hello "
b = "World "
x = "Programmers"
c = a + b + x
print(c)
#prints Hello World Programmers
a = "Hello"
b = "World"
x = "Programmers"
c = a + " "+ b + x
print(c)
#NEW- using the format method to insert string
age = 36
HEIGHT = 20
txt = "My name is John, and I am {} {}"
print(txt.format(age, HEIGHT))
#The format() method takes unlimited number of arguments, and are placed
# into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#
x=2
y=3
z=4
car = "Engine transmission {} {} {}"
print(car.format(x,y,z))
#ESCAPE CHARACTER
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "We are the so-called vikings from the \"north\" "
print(txt)
#
txt = 'It\'s alright.'
print(txt)
txt = "It\'s alright." #same as before
print(txt)
#BOOLEAN
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(100==100)
#
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#returns true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#retuens false:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(0))
#
def myFunction() :
  return False

print(myFunction())
#
x = 200
print(isinstance(x, int))
#
thislist = ["apple", "banana", "cherry"]
print(thislist)
#
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# To determine how many items a list has, use the len() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
x=["couper"]
print(len(x))
#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#
list1 = ["abc", 34, True, 40, "male"]
print(list1)

x = [2]
print(x)
print(type(x))
#FIRST ITEM IS 0 AS ALWAYS
thislist = ["apple", "banana", "cherry"]
print(thislist[0])
print(thislist[1])
print(thislist[2])
#LAST ITEM IS -1
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
#By leaving out the start value, the range will start at the first item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#
cat= ["food", "care", "house"]
print(cat[:3])
# This example returns the items from "cherry" to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# Including 4th and excluding last
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# changing vales in a list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
thislist[0] = "Sierra"
print(thislist)
# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
















