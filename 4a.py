"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

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
		if( digits[dig] == digits[dig+1]): 
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

# 9050: answer too hig (error en logica de creciente, no tomaba el final - range(0,4))
# 1919: OK




