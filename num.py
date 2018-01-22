# Asuka 2017

import random

number = random.randint(1,15) #number youll guess between 1 to 15

tries = 1

uname = input("Hello, whats your username?")

print("Hello", uname + ".")
question = input("would you like to play a game? [Y/N]")
if question == "N":
	print ("oh, okay")
	
if question == "Y":
	print ("I'm thinking num between 1 to 15")
	guess = int(input("Have a guess: "))
	if (guess > number):
		print ("Guess lower..")
	if guess < number:
		print ("Guess higher..")
	while guess != number:
		tries += 1 
		guess = int(input("Try again: "))
		if guess > number:
			print ("Guess lower..")
		if guess < number:
			print ("Guess higer..")
	if guess == number:
		print ("You're alright! You win! The number was", number,\
		       "and it only", tries, "tries!")
			   
			   
	