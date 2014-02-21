#!/usr/bin/python
import random

def ThrowDice():
	throw = []
	dice1 = random.randrange(1, 6)
	dice2 = random.randrange(1, 6)

	throw.extend([dice1, dice2])

	return throw

def RollCount():
	roll_count = 1

	while ThrowDice() != [1, 1]:
		roll_count += 1
        return roll_count

snakeEyes = RollCount()
print "Number of rolls to get to snake eyes: ", snakeEyes