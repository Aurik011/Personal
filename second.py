num1 = input("give input")
num2 = input("give input")
result = float(num1) + float(num2)
print(result)

mad libs
color = input()


print("roses are {color}")
print("{plural noun} are blue")
print("I love {celecbriy}")
1st hour 1st minute video check


lists
friends = ["kevin", "karen", "jim"]
print(friends)
print(friends[2]) # 0 1 2
print(friends[-2])  #gives result karen.    -3 -2-1

LIST FUNCTIONS

lucky_numbers = (4, 8, 15, 20, 100)
friends = ["kevin", "karen", "livy"]
friends.append("jim")
friends.extend(lucky_numbers)
print(friends)

friends = ["kevin", "karen", "livy"]
friends.insert(0, "labmard")
print(friends)

To remove an element
friends = ["kevin", "karen", "livy"]
friends.remove("karen")
print(friends)
friends = ["kevin", "karen", "livy"]
friends.clear()
print(friends)

removes last element from list. Just like stack
friends = ["kevin", "karen", "livy"]
friends.pop()
print(friends)


If a specific element is inside array:
friends = ["kevin", "karen", "livy", "jim", "jim"]
print(friends.index("Mike"))

counts how many times
friends = ["kevin", "karen", "livy", "jim", "jim"]
print(friends.count("jim")) #outputs 2(case sensitive)

sorts alphabetically
# friends.sort()

lucky_numbers=[42, 9, 100]
lucky_numbers.sort()
print(lucky_numbers) #shows sorted 9,42,100.


copy the whole list
friends = ["kevin", "karen", "livy", "jim", "jim"]
friends2 = friends.copy()
print(friends2)

tuples in python . tuple is a container which stores values
tuples are initiated by parenthesis(), not angle brackets[]
coordinates = (4, 5) #touple is immutable, meaning: cannot change or modify
coordinates[1] = 10 #TypeError: 'tuple' object does not support item assignment
print(coordinates[0])

list of tuples-use angled brackets just like lists.
coordinates2 = [(4,8), (4,0)]
print(coordinates2)

#Functions
# keyword def should be used so that compiler knows we want functions

def say_hi():
    print("Hello World")
    # gggggg -  indented while on function
    #now, need to call the function
say_hi() #just writing function is needed to print hello world

print("Top")
say_hi()
print("bottom")










