lucky_numbers=[42, 9, 100]
lucky_numbers.sort()
print(lucky_numbers) #shows sorted 9,42,100.

gaz=[1,9,7]
gaz.sort()
print(gaz)

print("Hello")
a = "Georgeo"
print(a)  #prints contents of a

# open read write
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())


