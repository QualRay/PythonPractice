#Ray Rana


#Define constant variable
NUM_INTEGERS = 10

#Read a collection of values from the user
#adding each to the list if it is not already present
values = []

while len(values) < NUM_INTEGERS:
    x = float(input("Enter a number:"))
    if x not in values:
        values.append(x)
#Sort the random numbers
        values.sort()
#Prints the final 10 values
print("The 10 numbers are:", values)