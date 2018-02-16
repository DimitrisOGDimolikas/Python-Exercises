import sys
import string
from random import randint


filename = raw_input("Enter the file's name: ")

# File manipulation
myFile = open(filename, 'r')

myFile.close()

wordList = []

# Get the words without punctuation
wordList = file.read().translate(None, string.punctuation)

wordList = wordList.split()

# Remove words with capital letters
for word in wordList:
	if(any(x.isupper() for x in word)):
		wordList.remove(word)

triplets = []

# Create triplets
for x in range(len(wordList) - 2):
	triplets.append([wordList[x], wordList[x + 1], wordList[x + 2]])

# Select first triplet
keyTriplet = triplets[randint(0, len(triplets) - 1)]

matching = []

# Triplets that match
for check in range(len(triplets)):
	if(keyTriplet[1] == triplets[check][0] and keyTriplet[2] == triplets[check][1]):
		matching.append(triplets[check])


freqMap = []

# Frequency map of each triplet
for key in range(len(matching)):
	duplicate = False
	
	# In case we have already matched the same triplet
	for x in range(len(freqMap)):
			for y in range(1, len(freqMap[x])):
				if(key == freqMap[x][y]):
					duplicate = True
					duplicateIndex = x
	
	# Check for matching triplets
	for check in range(len(matching)):
		if(matching[key] == matching[check] and not duplicate):
			try:
				freqMap[key][0] += 1
				freqMap[key].extend([check])
			except IndexError:
				freqMap.append([1])
				freqMap[key].extend([check])

output = ""

for word in keyTriplet:
	output += word + " "

# Enter triplets to the output to create a text of
# 198 words.
for x in range(66):
	freqIndex = x % len(freqMap)

	if(freqMap[freqIndex] == 1):
		for word in matching[freqMap[freqIndex][1]]:
			output += word + " "

	# In case there are multiple appearances of a triplet,
	# choose one randomly
	else:
		randomDuplicate = randint(1, len(freqMap[freqIndex]) - 1)

		for word in matching[freqMap[freqIndex][randomDuplicate]]:
			output += word + " "

# Final output
print "Output: "
print output

raw_input("Press enter to exit...")