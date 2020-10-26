print("Hello, World!")

if 7 < 10:
    print("True")

x = 5
y = "hello"
print(x)
print(y)

x = int(5)
print(type(x)) #I am a comment


#This is called casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



print(10 > 9)
print(10 == 9)
print(10 < 9)


thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana
print(thislist[-1]) #cherry
print(thislist[1:3]) #banana, cherry

thislist[1] = "blackcurrant"
print(thislist) #apple, blackcurrant, cherry

for x in thislist: #prints each item in the list
  print(x)

if "blackcurrant" in thislist:
    print("oh yea!!")

print(thislist)
print("size: ")
print(len(thislist))


thislist.append("orange")
print(thislist)


thislist.insert(1, "melon")
print(thislist)

thislist.remove("apple")
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

del thislist
print(thislist)