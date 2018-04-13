#Test for List
#List with INT
values = [22, 12, 23, 43, 32]

print(values[2])

values[4] = 99
print(values[4])
print(values)

print("------***-------")

#List with string
grocery = ["Milk","egg","coffee","banana","Tofu"]

print(grocery[2])

grocery[3] = "Mango"

print(grocery)

numGrocery = len(grocery)
print(numGrocery)

print("------***-------")

#Loops in list
for i in range(5):
    print(i, values[i])


print("------***-------")


#List Operation
friends = []

friends.append("Harry")

friends.append("Ray")
friends.append("Mary")
friends.append("Samantha")

print(friends)
print("------***-------")

friends.insert(1,"Raymond")
print(friends)

friends[4]="Mason"
print(friends)


#Removing an element

friends.pop(1)


print(friends)

#Concatenation

herFriends = ["Heather", "Tori"]

ourFriends = friends + herFriends
print(ourFriends)
print("------***-------")
values.sort()
print(values)
print("------***-------")