"""
5 intcode-machine
"""

with open("5input.txt") as f:
	intcodes = [int(line.rstrip('\n')) for line in f]

#print(intcodes)

initial = 5 #5 part B
pos = 0
instruction = 0
count =0

while(pos > len(intcodes) or instruction != 99 and count < 2000000):

	instruction = intcodes[pos]
	param1=0
	param2=0
	value1=0
	value2=0

	print(count,pos,instruction)

	if( instruction == 3): #input, guardar
		param1 = intcodes[pos+1]
		intcodes[param1] = initial

		print("\tinput at", pos, intcodes[param1] )
		pos +=2

	elif( instruction % 10 == 4): #outupt
		param1 = intcodes[pos+1]
		value1 = intcodes[param1]
		
		print("OUTPUT",value1)

		pos +=2

	elif( instruction % 10 == 1): #1 suma
		print("\tSum")	
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
		
		print("\t",instruction,param1,param2,param3,value1,value2)	
		pos+=4

	elif( instruction % 10 == 5): #jump-if-true
		print("\tJump if true")
		mode1 = int(str(instruction).zfill(4)[-3:-2])
		param1 = intcodes[pos+1]
		mode2 = int(str(instruction).zfill(4)[-4:-3])
		param2 = intcodes[pos+2]

		if(mode1==0):
			value1 = intcodes[param1]
		else: 
			value1 = param1

		if(mode2==0):
			value2 = intcodes[param2]
		else: 
			value2 = param2
		
		print("\t",instruction,param1,param2,value1,value2)	
		if(value1 != 0):
			pos = value2
		else:
			pos +=3
		
	elif( instruction % 10 == 6): #jump-if-false
		print("\tJump if false")
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
		
		if(value1 == 0):
			pos = value2
		else:
			pos +=3

	elif( instruction % 10 == 7): #less than
		print("\tLess Than")
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

		print("\t",instruction,param1,param2,value1,value2)			
		if(value1 < value2):
			intcodes[param3] = 1
		else:
			intcodes[param3] = 0

		pos += 4

	elif( instruction % 10 == 8): #equals
		print("\tEquals")
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

		print("\t",instruction,param1,param2,param3)		

		if(value1 == value2):
			intcodes[param3] = 1
		else:
			intcodes[param3] = 0

		pos +=4
		print("\t",pos)

	elif(  instruction % 10 == 2): #2 mult
		print("\tMultipl")
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

		print("\t",instruction,param1,param2,param3,value1,value2)	

		intcodes[param3] = value1 * value2
		pos += 4

	elif(instruction == 99):	#halt
		print("halt at pos",pos)
		break

	count +=1
#first guess: 9654885

#parte B: 7079459