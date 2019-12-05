"""
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is 136818-685979.
"""

answers = []

for password in range(136818, 685979):

	candidate = False

	adyacent = False
	increase = False

	digits=str(password)

	#print(password)
	for dig in range(0,5):

		#print("analysis",dig)

		# rule 1: adyacent
		try:
			third = digits[dig+2]
		except:
			third = digits[dig+1] #nothird

		if( digits[dig] == digits[dig+1] == third): 
			#print(digits[dig],"adyacent found")
			adyacent = True or adyacent # at least one True

		#rule 2: never decrease
		if(digits[dig] <= digits[dig+1]):
			candidate = True
		else:
			candidate = False
			#print(digits[dig],"increase:",increase,digits[dig],digits[dig+1])

			break

	candidate = candidate and adyacent
	#print(password,adyacent,increase,candidate)

	if(not candidate): continue

	answers.append(password)

print(answers)
print("total passwords",len(answers))

# 1417: answer too hig




