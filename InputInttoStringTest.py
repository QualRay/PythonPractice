name = input("Please enter your name: ")
print("Hello ", name)
age = int(input("Please enter your birth year: "))
birthYear = 2018-age
print(name,"you are",birthYear,"years old")
if birthYear <= 18:
    print("You are way too young, stay in school.")
elif birthYear <=21:
    print("You are allowed to drive now.")
elif birthYear <= 30:
    print("You are allowed to rent a car now.")
elif birthYear > 70:
    print("You need to retire.")
else:
    print("You are awesome!")


