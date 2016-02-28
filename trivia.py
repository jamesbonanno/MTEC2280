import sys

# vars for game

varD = 0 

# the user(s) input
print("for this games just type in 1 2 3 or 4 for you anwser")
x = input("would you like to play?, type in 1 if you want to play" "\n")

# var of user(s) 
userinput = int(x)

if(userinput == 1):
# question 1
	anw1 = 0
	print("question 1: what game was not made in 2007?" "\n")
	print("1: Phoenix Wright: Ace Attorney: Justice for All")
	print("2: Pokémon Diamond and Pearl")
	print("3: Bioshock")
	print("4: The Legend of Zelda: Twilight Princess")
	print("\n")
	anw1 = input("what is the right anwser")
# anwser to qusetion 1
	if(int(anw1) == 4):
		varD = varD +33
	else:
		varD + 0
# question 2
	anw2 = 0
	print("question 2: what game did Kazuma Kaneko did guest artwork in?")
	print("1: Devil May Cry 3: Dante's Awakening")
	print("2: Shin Megami Tensei III: Nocturne")
	print("3: Metal Slug 3")
	print("4: Assassin's Creed")
	print("\n")
	anw2 = input("what is the right anwser")
# anwser to question 2
	if(int(anw2) == 1):
		varD = varD + 33
	else:
		varD + 0
# question 3
	anw3 = 0
	print("question 1: what year did the magnavoz odyssey come out?" "\n")
	print("1: 1967")
	print("2: 1975")
	print("3: 1972")
	print("4: 1958")
	print("\n")
	anw3 = input("what is the right anwser")
# anwser to question 3
	if(int(anw3) == 3):
		varD = varD + 34
	else:
		varD + 0
# user score
	print("you got " + str(varD) + "%"" right")

else:

	print("ok")


# this program was made by James Bonanno, 2/21/16
# this code can be modified 