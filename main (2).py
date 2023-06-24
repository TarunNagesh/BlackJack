import random
import csv

def cardPick(Hand, Deck):
	card = random.randint(0,len(Deck)-1)
	Hand.append(Deck[card])
	Deck.remove(Deck[card])
	pass 

def calcSum(Hand):
	sum = 0
	for i in range(0, len(Hand)):
		sum += int(Hand[i][2])
	return sum

def checkBust(Hand):
	sum = 0
	for i in range(0, len(Hand)):
		sum += int(Hand[i][2])
	if sum > 21:
		return "bust"
	else:
		return "safe"
		

def game():
	cardDeck = []
	with open("cards.csv") as file:
		for line in file:
			reader = csv.reader(file)
			cardDeck = list(tuple(line) for line in reader)
	playerHand = []
	dealerHand = []
	cardPick(playerHand, cardDeck)
	cardPick(playerHand, cardDeck)
	playerSum = 0
	
	print("Your cards are the " + playerHand[0][0] + " of " + playerHand[0][1] + ", and the " + playerHand[1][0] + " of " + playerHand[1][1] + ".")
	print("Your sum is " + str(int(playerHand[0][2]) + int(playerHand[1][2])) +".")
	print("----------------------------------------------------------")
	
	cardPick(dealerHand, cardDeck)
	cardPick(dealerHand, cardDeck)
	
	print("The dealer's shown card is the "+ dealerHand[1][0] + " of " + dealerHand[1][1] +".")
	print("----------------------------------------------------------")
	
	newPlayerTurn = True
	newDealerTurn = True
	
	while newPlayerTurn:
		playerSum = calcSum(playerHand)		
		answer = str(input("Would you like to hit or stand?: "))
		nonValidAnswer = True
		while nonValidAnswer:
			if answer != "hit":
				if answer != "stand":
					answer = str(input("Please enter a valid input(type the word 'hit' or 'stand' exactly): "))
				else:
					nonValidAnswer = False
			else:
				nonValidAnswer = False
				
		if answer == "hit":
			cardPick(playerHand, cardDeck)
			print("You drew the " + playerHand[len(playerHand)-1][0] + " of " + playerHand[len(playerHand)-1][1] + ".")
			playerSum = calcSum(playerHand)
			if checkBust(playerHand) == "bust":
				print("You busted!")
				newPlayerTurn = False
				newDealerTurn = False
				return "loss"
			elif checkBust(playerHand) == "safe":
				print("Your new sum is " + str(calcSum(playerHand)) + ".")
				print("----------------------------------------------------------")
		if answer == "stand":
			newPlayerTurn = False
	
	while(newDealerTurn):
		dealerSum = calcSum(dealerHand)
		if dealerSum == 21:
			if playerSum == 21:
				print("Its a tie!")
				return "tie"
			else:
				print("Dealer hit 21! You lose!")
				return "loss"
		elif dealerSum <= 16:
			print("Dealer hits.")
			cardPick(dealerHand, cardDeck)
			print("Dealer drew the " + dealerHand[len(dealerHand)-1][0] + " of " + dealerHand[len(dealerHand)-1][1] +".")
			print("Dealer's sum is now " + str(calcSum(dealerHand)))
			print("----------------------------------------------------------")
			dealerSum = calcSum(dealerHand)
			if checkBust(dealerHand) == "bust":
				print("Dealer busts! You win!")
				newDealerTurn = False
				return "win"
		elif dealerSum > 16:
			print("Dealer stands.")
			newDealerTurn = False
			print("Your sum: " + str(calcSum(playerHand)))
			print("Dealer's sum: " + str(calcSum(dealerHand)))
			if calcSum(playerHand) > calcSum(dealerHand):
				print("You win!")
				return "win"
			elif calcSum(playerHand) == calcSum(dealerHand):
				print("It's a tie! You get your money back!")
				return "tie"
			else:
				print("Dealer wins!")
				return "loss"
print("Welcome to Black Jack! You start off with $5000, and can bet on each round.")
cash = 5000
nonValidAnswer = True
stillPlaying = True
ask1 = False
while stillPlaying:
	nonValidAnswer = True
	if ask1 == False:
		answer = str(input("Would you like to play?: "))
		ask1 = True
	elif ask1 == True:
		answer = str(input("Would you like to play again?: "))
	while nonValidAnswer:
		if answer != "yes":
			if answer != "no":
				answer = str(input("Please enter a valid input(type the word 'yes' or 'no' exactly): "))
			else:
				nonValidAnswer = False
		else:
			nonValidAnswer = False
	if answer == "yes":
		nonValidAnswer = True
		while nonValidAnswer:
			bet = int(input("How much would you like to bet (Current Balance: " + str(cash) +")?: "))
			print("----------------------------------------------------------")
			if bet > cash or bet <= 1:
				print("Please enter a valid bet. Bets must be over 1 and below or equal to your current balance.")
			else:
				nonValidAnswer = False
		result = game()
		if result == "loss":
			cash -= bet
			print("Thanks for the money!")
			print("----------------------------------------------------------")
		elif result == "win":
			cash += bet
			print("Good game! Congrats on your win!")
			print("----------------------------------------------------------")
	if answer == "no":
		stillPlaying = False
		print("Thank you for playing! You left with " + str(cash) + " dollars.")
	if cash < 1:
		stillPlaying = False
		print("You ran out of money! Come back when you have more!")
		