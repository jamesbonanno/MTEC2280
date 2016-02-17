import sys
import random

# vars for RNG
varA = 0
varB = 101

# the user(s) input
x = input("im thinking of a number between 1 and 100, what it it ?" "\n")

# var of user(s) imput turned into a int 
var1 = int(x)

# RNG 
var3 = random.randrange(varA,varB)

#check if right or wrong
if(var3 == var1):

	print("\n"'you are right')

elif(var1 > 100 or var1 < 0):

	print("\n"'do you even read?')

else:

	print("\n"'you are wrong')

# this program was made by James Bonanno, 2/16/16
# this code can be modified 