"""
5 intcode-machine
"""

with open("5input.txt") as f:
	intcodes = [int(line.rstrip('\n')) for line in f]

#print(intcodes)

initial = 1
pos = 0
instruction = 0

while(pos > len(intcodes) or instruction != 99):

	instruction = intcodes[pos]
	param1=0
	param2=0
	value1=0
	value2=0
	#print(instruction)

	if( instruction == 3): #input, guardar
		param1 = intcodes[pos+1]
		intcodes[param1] = initial

		pos +=1
		#print("input at",pos,intcodes[param1] )

	elif( instruction == 4): #outupt
		param1 = intcodes[pos+1]
		value1 = intcodes[param1]
		
		print("OUTPUT",value1)

		pos +=1
		#print("outupt at",pos)

	elif( instruction % 10 == 1): #1 suma
		mode1 = int(str(instruction).zfill(4)[-3:-2])
		param1 = intcodes[pos+1]
		mode2 = int(str(instruction).zfill(4)[-4:-3])
		param2 = intcodes[pos+2]
		param3 = intcodes[pos+3]

		if(mode1==0):
			value1 = intcodes[param1]
		else: 
			value1 = param1

		if(mode2==0):
			value2 = intcodes[param2]
		else: 
			value2 = param2
		
		intcodes[param3] = value1 + value2


		# print("encontrada suma at",pos)
		# print("instruction",instruction)
		# print("mode1",mode1)
		# print("value1",value1)
		# print("mode2",mode2)
		# print("value2",value2)


		pos+=4

	elif(  instruction % 10 == 2): #2 mult
		#print("mult at pos",pos)

		mode1 = int(str(instruction).zfill(4)[-3:-2])
		param1 = intcodes[pos+1]
		mode2 = int(str(instruction).zfill(4)[-4:-3])
		param2 = intcodes[pos+2]
		param3 = intcodes[pos+3]

		# valores posicionales 0 vs directos 1
		if(mode1==0):
			value1 = intcodes[param1]
		else: 
			value1 = param1

		if(mode2==0):
			value2 = intcodes[param2]
		else: 
			value2 = param2
		
		intcodes[param3] = value1 * value2
		pos+=4

	elif(instruction == 99):	#halt
		print("halt at pos",pos)
		break
	else:
		pos +=1

#first guess: 9654885