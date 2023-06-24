import random

class power:
	def __init__(self, n, d, h, s):
		self.pName = n
		self.baseDamage = d
		self.heavy = h
		self.stock = s
		self.maxStock = s
	def getpName(self):
		return self.pName
	def getDamage(self):
		return self.baseDamage
	def getHeavy(self):
		return self.heavy
	def getStock(self):
		return self.stock
	def getMaxStock(self):
		return self.maxStock
	def useStock(self):
		self.stock-=1
	def resetStock(self):
		self.stock = self.maxStock
	def copy(self):
		return power(self.getpName(), self.getDamage(), self.getHeavy(), self.getMaxStock())

#####################################################################################################################################

class pokemon:
	def __init__(self, n, t, pow1, pow2, pow3, pow4):
		self.name = n
		self.type = t
		self.Powers = [pow1, pow2, pow3, pow4]
		self.health = 200
		self.maxHealth = 200 + int(random.randint(0,31)) + int(random.randint(0,6))
	def getName(self):
		return self.name
	def getType(self):
		return self.type
	def getMaxHealth(self):
		return self.maxHealth
	def getHealth(self):
		return self.health
	def getPower(self, i):
		return self.Powers[i]
	def getPowerName(self, i):
		return self.Powers[i].getpName()
	def printStats(self):
		print("Name: " + self.getName())
		print("Type: " + self.getType())
		if (self.getHealth() >= 0):
			print("HP: " + str(self.getHealth()))
		else:
			print("HP: 0")
		for i in range(0,4):
			print("Power: " + self.getPowerName(i) + "    Stock: " + str(self.Powers[i].getStock()))
	def printLightStats(self):
		print("Name: " + self.getName())
		print("Type: " + self.getType())
		if (self.getHealth() >= 0):
			print("HP: " + str(self.getHealth()))
		else:
			print("HP: 0")
	def setMaxHealth(self, h):
		self.maxHealth = h
	def setHealth(self, h):
		self.health = h
	def isEffective(self, other):
		otherT = other.getType()
		if (self.type == ("water") and (otherT == ("fire") or otherT == ("ground"))):
			return True
		elif (self.type == ("ground") and (otherT == ("water") or otherT == ("electric"))):
			return True 
		elif (self.type == ("fire") and (otherT == ("ground") or otherT == ("ice"))):
			return True
		elif (self.type == ("ice") and (otherT == ("ground") or otherT == ("electric"))): 
			return True
		elif (self.type == ("electric") and (otherT == "fire" or otherT == "water")): 
			return True
		else:
			return False

#####################################################################################################################################

class player:
	def __init__(self, h, n):
		self.healingPotions = h
		self.name = n
		self.mainPokemon = []
		self.inhand = ""
	def getName(self):
		return self.name
	def getPotions(self):
		return self.healingPotions
	def getMainPokemon(self):
		return self.mainPokemon
	def getInHand(self):
		return self.inhand
	def usePotion(self):
		self.healingPotions -= 1
	def setFirstMain(self, p):
		self.mainPokemon.append(p)
	def setInHand(self, index):
		self.inhand = self.mainPokemon[index]
	def printMainPokemonString(self):
		print("(1) " + self.mainPokemon[0].getName() + "        " + "(4) " + self.mainPokemon[3].getName())
		print("(2) " + self.mainPokemon[1].getName() + "        " + "(5) " + self.mainPokemon[4].getName())
		print("(3) " + self.mainPokemon[2].getName() + "        " + "(6) " + self.mainPokemon[5].getName())
	def switchOutPokemon(self):
		Swappable = []
		for i in range(0, len(self.mainPokemon)):
			if(not(self.mainPokemon[i].getName() == self.inhand.getName())):
				Swappable.append(self.mainPokemon[i])
		if len(Swappable) < 1:
			print("Sorry, you can't switch out any pokemon now.")
			return
		print("Which pokemon do you want to call in?")
		for i in range(1, len(Swappable)+1):
			print("(" + str(i) + ") " + Swappable[i-1].getName())
		response = int(input("Pokemon number: "))
		print()
		test2 = True
		while test2:
			if(response < 1 or response > len(Swappable)):
				response = int(input("Please enter a valid response: "))
				print()
			else:
				print("Come back " + self.inhand.getName() + "!")
				self.inhand = Swappable[response - 1] 
				print("Go " + self.inhand.getName() + "!")
				test2 = False
	def moveScreen(self, p2):
		battleAns = ""
		miss = 0
		if(len(self.mainPokemon) <= 0):
			print("All your pokemon have fainted, I guess you need a bit more practice before you can become a trainer!")
			return False
		print()
		print(p2.getName() + "'s pokemon's stats:")
		p2.getInHand().printLightStats()
		print()
		print("Your pokemon's stats:")
		self.inhand.printStats()
		test = True
		if (self.inhand.getHealth() <= 0):
			print()
			print("" + self.inhand.getName() + " fainted!")
			self.mainPokemon.remove(self.inhand)
			j = 0
			while j < len(self.mainPokemon):
				if(self.mainPokemon[j].getHealth() <= 0):
					self.mainPokemon.remove(self.mainPokemon[j])
				j+=1
			j = random.randint(0, len(self.mainPokemon) - 1)
			self.inhand = self.mainPokemon[j]
			print(self.getName() + " sends out " + self.inhand.getName() + "!")
			return True
		print("What will " + self.inhand.getName() + " do?")
		print("(1) Attack")
		print("(2) Heal")
		print("(3) Switch out")
		while (test):
			battleAns = int(input("Action number: "))
			if (battleAns <= 0 or battleAns >= 4):
				print("Please enter a valid response.")
			else:
				test = False
		test = True
		print()
		if (battleAns == 1):
			print("What attack will " + self.inhand.getName() + " use?")
			print("(1) " + self.inhand.getPowerName(0))
			print("(2) " + self.inhand.getPowerName(1))
			print("(3) " + self.inhand.getPowerName(2))
			print("(4) " + self.inhand.getPowerName(3))
			while(test):
				battleAns = int(input("Attack number: "))
				if (battleAns <= 0 or battleAns >= 5):
					print("Please enter a valid response.")
				elif self.inhand.getPower(battleAns - 1).getStock() <= 0:
					print("You have no more stock of that attack left! Pick another attack quick!")
				else:
					print()
					print("" + self.inhand.getName() + " uses " + (self.inhand.getPowerName(battleAns - 1)) + "!")
					self.inhand.getPower(battleAns - 1).useStock()
					test = False
			
			miss = int(random.randint(1,4))
			if (self.inhand.isEffective(p2.getInHand()) and (miss != 3)):
				print(self.inhand.getName() + "'s type: " + self.inhand.getType() + " is super effective against " + p2.getInHand().getName() + "'s type: " + p2.getInHand().getType() + "! Extra damage given!")
				p2.getInHand().setHealth(p2.getInHand().getHealth() - (self.inhand.getPower(battleAns - 1).getDamage() + 20))
			elif (miss == 3):
				print("The attack missed!")
			else:
				print()
				p2.getInHand().setHealth(p2.getInHand().getHealth() - self.inhand.getPower(battleAns - 1).getDamage())
				
		elif (battleAns == 2):
			if (self.inhand.getHealth() > 170):
				print(self.inhand.getName() + " cannot heal right now. You wasted your move!")
			elif (self.getPotions() <= 0):
				print("You do not have any more potions left!")
			else:
				self.inhand.setHealth(self.inhand.getHealth() + 30)
				print("" + self.inhand.getName() + " heals 30 hp!")
				self.usePotion()
		
		elif (battleAns == 3):
			self.switchOutPokemon()
		
		if (len(p2.mainPokemon) <= 0):
			print("You beat " + p2.getName() + "!")
			return False
		return True

	
	def enemyAttack(self, p1):
		x = random.randint(1,4)
		y = 0
		canUse = True
		if (len(self.mainPokemon)) <= 0:
			print("You win!")
			return False
			
		if (self.inhand.isEffective(p1.getInHand())):
			y = 20
			
		if (self.inhand.getHealth() <= 0):
			print(self.inhand.getName() + " fainted!")
			j = 0
			while j < len(self.mainPokemon):
				if(self.mainPokemon[j].getHealth() <= 0):
					self.mainPokemon.remove(self.mainPokemon[j])
				j+=1
			j = random.randint(0, len(self.mainPokemon) - 1)
			self.inhand = self.mainPokemon[j]
			print(self.getName() + " sends out " + self.inhand.getName() + "!")
			return True
			
		if(x == 1 or x == 2):
			x = random.randint(1, 4)
			canUse = True
	
			while(canUse):
				count = 0
				for i in range(0, 4):
					if self.inhand.getPower(i).getStock()>0:
						count+=1
						
				if count == 0:
					print(self.inhand.getName() +" ran out of moves!")
					self.mainPokemon.remove(self.inhand)
					while j < len(self.mainPokemon):
						if(self.mainPokemon[j].getHealth() <= 0):
							self.mainPokemon.remove(self.mainPokemon[j])
						j+=1
					j = random.randint(0, len(self.mainPokemon) - 1)
					self.inhand = self.mainPokemon[j]
					print(self.getName() + " sends out " + self.inhand.getName() + "!")
					return True
					
				elif self.inhand.getPower(x-1).getStock() <= 0:
					x = random.randint(1, 4)
					
				else:
					canUse = False
					
			canUse = True
			print("" + self.inhand.getName() + " uses " + self.inhand.getPowerName(x - 1) + "!")
			p1.inhand.setHealth(p1.inhand.getHealth() - (self.inhand.getPower(x - 1).getDamage() + y))
			if(y == 20):
				print(self.inhand.getName() + "'s type: " + self.inhand.getType() + " is super effective against " + p1.getInHand().getName() + "'s type: " + p1.getInHand().getType() + "! Extra damage taken!")
			self.inhand.getPower(x-1).useStock()

		elif x == 3:
			while(canUse):
				if self.inhand.getPower(x-1).getStock() <= 0:
					x = random.randint(1,4)
				else:
					canUse = False
			canUse = True
			x = random.randint(1,4)
			print("" + self.inhand.getName() + " uses " + self.inhand.getPowerName(x - 1) + "!")
			print("The attack missed!")
			self.inhand.getPower(x - 1).useStock()
		
		elif x == 4 and self.inhand.getHealth() <= 170:
			if(self.getPotions() <= 0):
				x = random.randint(1,4)
				print("" + self.inhand.getName() + " uses " + self.inhand.getPowerName(x - 1) + "!")
				p1.inhand.setHealth(p1.inhand.getHealth() - (self.inhand.getPower(x - 1).getDamage() + y))
				if (self.inhand.isEffective(p1.inhand)):
					print(self.inhand.getName() + "'s type: " + self.inhand.getType() + " is super effective against " + p1.getInHand().getName() + "'s type: " + p1.getInHand().getType() + "! Extra damage taken!")
				self.inhand.getPower(x-1).useStock()
			else:
				self.usePotion()
				self.inhand.setHealth(self.inhand.getHealth() + 30)
				print(self.getName() + " used a heal on " + self.inhand.getName() + "!")
		else: 
			print(self.getName() + " froze! Turn wasted!")
			
		return True
		
#####################################################################################################################################
def fourNum(p):
    heavies = []
    lights = []
    x = []
    for i in range(0, len(p)):
        if p[i].getHeavy():
            heavies.append(p[i])
        else:
            lights.append(p[i])
    random.shuffle(heavies)
    random.shuffle(lights)
    x.append(p.index(heavies[0]))
    x.append(p.index(heavies[1]))
    x.append(p.index(lights[0]))
    x.append(p.index(lights[1]))
    return x
    

starters = []
nums = []
total = []
FireNames = ["Monferno", "Chimchar", "Ponyta", "Blaziken", "Cyndaquil", "Growlithe", "Torchic", "Fennekin", "Litleo", "Tepig", "Charmander", "Magmar", "Dratini"]
ElectricNames = ["Pikachu", "Shinx", "Voltorb", "Electrike", "Electrabuzz", "Magnemite", "Mareep", "Blitzle", "Plusle", "Chinchou", "Jolteon", "Minun"]
WaterNames = ["Squirtle", "Piplup", "Psyduck", "Greninja", "Oshawott", "Lapras", "Spheal", "Totodile", "Octillery", "Mudkip", "Froakie", "Poliwag", "Staryu"]
GroundNames = ["Onyx", "Geodude", "Cubone", "Leafeon", "Larvitar", "Rhyhorn", "Bulbasaur", "Sandshrew", "Phanpy", "Roselia", "Chikorita", "Tangela", "Exeggutor", "Gloom"]
IceNames = ["Glaceon", "Snover", "Snorunt", "Bergmite", "Cubchoo", "Delibird", "Jynx", "Shellder", "Regice", "Vanillite", "Cryogonal"]
battlerNames = ["Jake", "Ian", "Tarun", "Gabriel", "Eric", "Jessie", "Reden", "Professor Brown", "Neth", "Bryant", "Ms. Cojohnny Girl"]

ElectricPower = []
ElectricPower.append(power("Charge", 10, False, 25))
ElectricPower.append(power("Overdrive", 30, True, 10))
ElectricPower.append(power("Spark", 10, False, 20))
ElectricPower.append(power("Thunder Bolt", 40, True, 5))
ElectricPower.append(power("Zap Cannon", 35, True, 5))
ElectricPower.append(power("Electrify", 15, False, 20))
ElectricPower.append(power("Shock Wave", 40, True, 5))
ElectricPower.append(power("Volt Tackle", 10, False, 25))
ElectricPower.append(power("False Ohmen", 30, True, 10))
ElectricPower.append(power("Tickling Thunder", 5, False, 50))
ElectricPower.append(power("Zeus' Wrath", 75, True, 2))
ElectricPower.append(power("Battery", 10, False, 20))




nums = fourNum(ElectricPower)
starters.append(pokemon("Pikachu", "electric", ElectricPower[nums[0]], ElectricPower[nums[1]], ElectricPower[nums[2]], ElectricPower[nums[3]]))


GroundPower = []
GroundPower.append(power("Dig", 10, False, 25))
GroundPower.append(power("Drill Run", 30, True, 10))
GroundPower.append(power("Spike", 10, False, 20))
GroundPower.append(power("Earthquake", 40, True, 5))
GroundPower.append(power("Tectonic Rage", 35, True, 5))
GroundPower.append(power("Overgrowth", 15, False, 20))
GroundPower.append(power("Bulldoze", 40, True, 5))
GroundPower.append(power("Razor Leaf", 10, False, 25))
GroundPower.append(power("Ground Pound", 45, True, 5))
GroundPower.append(power("Drought", 10, False, 25))
GroundPower.append(power("Obsidian Obituary", 40, True, 5))
GroundPower.append(power("Rock Sling", 10, False, 25))

nums = fourNum(GroundPower)
starters.append(pokemon("Bulbasaur", "ground", GroundPower[nums[0]], GroundPower[nums[1]], GroundPower[nums[2]], GroundPower[nums[3]]))


WaterPower = []
WaterPower.append(power("Drip", 10, False, 25))
WaterPower.append(power("Aqua Jet", 30, True, 10))
WaterPower.append(power("Surf", 10, False, 20))
WaterPower.append(power("Hydro Cannon", 40, True, 5))
WaterPower.append(power("Water Pulse", 35, True, 5))
WaterPower.append(power("Wave Crash", 15, False, 20))
WaterPower.append(power("Surging Strikes", 40, True, 5))
WaterPower.append(power("Splash", 10, False, 25))
WaterPower.append(power("Drought", 10, False, 25))
WaterPower.append(power("Tsunami", 40, True, 5))
WaterPower.append(power("Bubble Stream", 10, False, 25))
WaterPower.append(power("Drown", 45, True, 5))

nums = fourNum(WaterPower)
starters.append(pokemon("Squirtle", "water", WaterPower[nums[0]], WaterPower[nums[1]], WaterPower[nums[2]], WaterPower[nums[3]]))

FirePower = []
FirePower.append(power("Ember", 10, False, 25))
FirePower.append(power("Fusion Flare", 30, True, 10))
FirePower.append(power("Burn Up", 10, False, 20))
FirePower.append(power("Heat Wave", 40, True, 5))
FirePower.append(power("Searing Shot", 35, True, 5))
FirePower.append(power("Inferno", 15, False, 20))
FirePower.append(power("Sacred Fire", 40, True, 5))
FirePower.append(power("Overheat", 10, False, 25))
FirePower.append(power("Fury of the Sun", 45, True, 5))
FirePower.append(power("Exothermic Pulse", 10, False, 25))
FirePower.append(power("Exothermic Concussion", 40, True, 5))
FirePower.append(power("Combust", 10, False, 25))

nums = fourNum(FirePower)
starters.append(pokemon("Charmander", "fire", FirePower[nums[0]], FirePower[nums[1]], FirePower[nums[2]], FirePower[nums[3]]))

IcePower = []
IcePower.append(power("Frost Breath", 10, False, 25))
IcePower.append(power("Avalanche", 30, True, 10))
IcePower.append(power("Hail", 10, False, 20))
IcePower.append(power("Ice Beam", 40, True, 5))
IcePower.append(power("Blizzard", 35, True, 5))
IcePower.append(power("Mist", 15, False, 20))
IcePower.append(power("Icicle Crash", 40, True, 5))
IcePower.append(power("Ice Wind", 10, False, 25))
IcePower.append(power("Ice Skull", 10, False, 25))
IcePower.append(power("Freeze", 10, False, 25))
IcePower.append(power("Thermal Drought", 40, True, 5))
IcePower.append(power("Kinetic Termination", 75, True, 2)) 



playerPossiblePokemon = []
for i in range(0, len(FireNames)):
	nums = fourNum(FirePower)
	playerPossiblePokemon.append(pokemon(FireNames[i], "fire", FirePower[nums[0]].copy(), FirePower[nums[1]].copy(), FirePower[nums[2]].copy(), FirePower[nums[3]].copy()))
for i in range(0, len(ElectricNames)):
	nums = fourNum(ElectricPower)
	playerPossiblePokemon.append(pokemon(ElectricNames[i], "electric", ElectricPower[nums[0]].copy(), ElectricPower[nums[1]].copy(), ElectricPower[nums[2]].copy(), ElectricPower[nums[3]].copy()))
for i in range(0, len(WaterNames)):
	nums = fourNum(WaterPower)
	playerPossiblePokemon.append(pokemon(WaterNames[i], "water", WaterPower[nums[0]].copy(), WaterPower[nums[1]].copy(), WaterPower[nums[2]].copy(), WaterPower[nums[3]].copy()))
for i in range(0, len(GroundNames)):
	nums = fourNum(GroundPower)
	playerPossiblePokemon.append(pokemon(GroundNames[i], "ground", GroundPower[nums[0]].copy(), GroundPower[nums[1]].copy(), GroundPower[nums[2]].copy(), GroundPower[nums[3]].copy()))
for i in range(0, len(IceNames)):
	nums = fourNum(IcePower)
	playerPossiblePokemon.append(pokemon(IceNames[i], "ice", IcePower[nums[0]].copy(), IcePower[nums[1]].copy(), IcePower[nums[2]].copy(), IcePower[nums[3]].copy()))

total = playerPossiblePokemon.copy()
random.shuffle(playerPossiblePokemon)
random.shuffle(total)
n1 = str(input("Oh hey! You must be the new Pokemon trainer Professor Brown was talking about! Remind me of your name again?: "))
p1 = player(10, n1)
print("Hi " + p1.getName() + "! Here are our starter pokemon, take your pick!")
print("(1) Pikachu")
print("(2) Bulbasaur")
print("(3) Squirtle")
print("(4) Charmander")
test1 = True
x = int(input("Starter number: "))
if (x >= 1 and x <= 4):
	print()
	print("" + starters[x-1].getName() + "? Great choice!")
	p1.mainPokemon.append(starters[x-1])
	test1 = False
else:
	x = int(input("Please enter a valid input: "))

ind = 0
while ind < len(total):
    if(p1.mainPokemon[0].getName() == playerPossiblePokemon[ind].getName()):
        playerPossiblePokemon.pop(ind)
        ind+= 1000
    ind +=1
        
print()
print("Hmm, one pokemon isn't enough to take on a full team. Here, I'll let you use some of my pokemon so you can have a full team to practice in a friendly battle!")
print()
for i in range(1, 6):
	p1.mainPokemon.append(playerPossiblePokemon.pop(i-1))
print("Here's your full team!")
print()
p1.printMainPokemonString()
p1.inhand = p1.mainPokemon[0]
random.shuffle(playerPossiblePokemon)

battle = True
isStillIn = True
win = True
while(battle):
	random.shuffle(battlerNames)
	p2 = player(10, battlerNames[0])
	for i in range(1, 6):
		p2.mainPokemon.append(total.pop(i-1))
	p2.inhand = p2.mainPokemon[0]
	print()
	print(p2.getName() + " has challenged you to a battle!")
	while(isStillIn and win):
		isStillIn = p1.moveScreen(p2)
		win = p2.enemyAttack(p1)