myInt = int(raw_input("Enter a number: "))
numsInRoman = ""

# Numbers in latin and regular form
ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

# For each number add the letter that corresponds
for i in range(len(ints)):
	count = int(myInt / ints[i])
	numsInRoman += nums[i] * count
	myInt -= ints[i] * count

print numsInRoman

raw_input("Press enter to exit....")