#a
values = []
for i in range (1,11):
    values.append(i)

#b
values = []
for i in range (0,21,2):
    values.append(i)

#c
values = []
for i in range (1,11):
    values.append(i*i)

#d
values = [0] * 10

#e
values = [1,4,9,16,9,7,4,9,11]

#f

values = [0,1]* 5

#g
values = []
for i in range(0,5):
    values.append(i)
    values = values * 2



#Ch6 r05
# following code for 10 random values from 1 and 100
from random import randint

values = []
for i in range (0,10):
    values.append(randint(1,100))

#for 10 unique random values between 1 and 100
from random import randint

values = []
 for i in range(0,100):
     r = randint(1,100)
     while r in values:
         r = randint(1,100)
         values.append(r)