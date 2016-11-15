import random

guesses = 0

print ('Hello! What is your name? ')
myName = raw_input()

number = random.randint(1,20)
while True:
	print ('Well, '+myName+', I am thinking of a number between 1 and 20. ')
	
	while guesses < 6:
		print ('Take a guess. ')
		guess = input()
		guess = int(guess)
		
		guesses = guesses + 1
	
		if guess < number:
			print ('Your guess is too low.')
	
		if guess > number:
			print ('Your guess is too high')
	
		if guess == number:
			break
	
	if guess == number:
		if guesses > 1:
			guesses = str(guesses)
			print ('Good job, ' +myName+ '! You guessed my number in ' +guesses+ ' guesses!')
		else:
			guesses = str(guesses)
			print ('Wow!, ' +myName+ '! You guessed my number in ' +guesses+ ' guess!')
	if guess != number:
		number = str(number)
		print ('Nope. The number I was thinking of was ' + number)
	
	while True:
		answer=raw_input('Would you like to play again? Y/N \n')
		if answer in ('Y','N'):
			break
		print('Please choose Y or N.')
	if answer == 'Y':
		guesses = 0
		number = random.randint(1,20)
		continue
	else:
		raw_input('See you next time!\n')
		break
	