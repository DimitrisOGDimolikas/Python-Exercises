selectedNum = int(raw_input("Enter a number: "))

numsInLatin = ""

# Numbers in latin and arabic 
ints = (1000000,900000,500000,400000,100000,90000,50000,40000,10000,9000,5000,4000,1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
latins = (u'M\u0305',u'C\u0305M\u0305',u'D\u0305',u'C\u0305D\u0305',u'C\u0305',u'X\u0305C\u0305',u'L\u0305',u'X\u0305L\u0305',u'X\u0305',u'I\u0305X\u0305',u'V\u0305',u'I\u0305V\u0305','M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

# For each number add the letter that corresponds
for i in range(len(ints)):
	count = int(selectedNum / ints[i])
	numsInLatin += latins[i] * count
	selectedNum -= ints[i] * count

print numsInLatin

raw_input("Press enter to exit....")
