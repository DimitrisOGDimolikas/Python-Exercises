from __future__ import print_function
from random import randint
import sys

matrix = []

filename = raw_input("Enter the dictionary's name: ")

file = open(filename, "r")

dictionary = []

# Get dictionary words from file 
for line in file:
	for word in line.split():
		dictionary.append(word)

file.close()

# Fill crossword with random characters
for i in range(100 * 100):
	matrix.append(chr(randint(65, 90)))

# Initialize helpful variables
x, y = 0, 0

solvedX = []
solvedIndexX = 0
solvedY = []
solvedIndexY = 0

found = 0

# For each word in the dictionary
for word in dictionary:
	for x in range(100):
		for y in range(100): 
			# If the character in the crossword matches
			# the current character of the word, then
			# added to the solved list and if the solved
			# list matches the dictionary word, mark the word
			# as found and clear the solved list.
			# Do the above for both row-column and 
			# column-row navigation.

			if(word[solvedIndexX] == matrix[100 * x + y]):
				solvedX += matrix[100 * x + y];
				solvedIndexX += 1
				

				if(word == "".join(solvedX)):
					found = 1
					del solvedX[:]
					solvedIndexX = 0

			elif(word[0] == matrix[100 * x + y]):
				del solvedX[:]
				solvedIndexX = 0
				solvedX += matrix[100 * x + y];
				solvedIndexX += 1
			
				if(word == "".join(solvedX)):
					found = 1
					del solvedX[:]
					solvedIndexX = 0

			else:
				del solvedX[:]
				solvedIndexX = 0

			if(word[solvedIndexY] == matrix[100 * y + x]):
				solvedY += matrix[100 * y + x];
				solvedIndexY += 1
				

				if(word == "".join(solvedY)):
					found = 1
					del solvedY[:]
					solvedIndexY = 0

			elif(word[0] == matrix[100 * y + x]):
				del solvedY[:]
				solvedIndexY = 0
				solvedY += matrix[100 * y + x];
				solvedIndexY += 1
			
				if(word == "".join(solvedY)):
					found = 1
					del solvedY[:]
					solvedIndexY = 0

			else:
				del solvedY[:]
				solvedIndexY = 0

	if(found):
		print("The word " + word + " appears in the crossword")
		found = 0

raw_input("Press enter to exit...")