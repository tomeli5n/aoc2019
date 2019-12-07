"""
5 intcode-machine
"""

with open("input.txt") as f:
	for line in f:
		_ = line.split(',') 

	intcodes = [int(item) for item in _]





def machine(phase,input_signal=0):
	print("INPUT", phase, input_signal)
	pos = 0
	instruction = 0
	count =0
	while(pos > len(intcodes) or instruction != 99 and count < 2000000):

		instruction = intcodes[pos]
		param1=0
		param2=0
		value1=0
		value2=0

		#print(count,pos,instruction)
		if( instruction == 3): #input, guardar
			param1 = intcodes[pos+1]
			

			intcodes[param1] = phase
			phase = input_signal

			print("\tinput at", pos, intcodes[param1] )

			pos +=2

		elif( instruction % 10 == 4): #outupt
			param1 = intcodes[pos+1]
			value1 = intcodes[param1]
			
			print("OUTPUT",value1)
			return value1

			pos +=2

		elif( instruction % 10 == 1): #1 suma
			#print("\tSum")	
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
			
			#print("\t",instruction,param1,param2,param3,value1,value2)	
			pos+=4

		elif( instruction % 10 == 5): #jump-if-true
			#print("\tJump if true")
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
			
			#print("\t",instruction,param1,param2,value1,value2)	
			if(value1 != 0):
				pos = value2
			else:
				pos +=3
			
		elif( instruction % 10 == 6): #jump-if-false
			#print("\tJump if false")
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
			#print("\tLess Than")
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

			#print("\t",instruction,param1,param2,value1,value2)			
			if(value1 < value2):
				intcodes[param3] = 1
			else:
				intcodes[param3] = 0

			pos += 4

		elif( instruction % 10 == 8): #equals
			#print("\tEquals")
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

			#print("\t",instruction,param1,param2,param3)		

			if(value1 == value2):
				intcodes[param3] = 1
			else:
				intcodes[param3] = 0

			pos +=4
			#print("\t",pos)

		elif(  instruction % 10 == 2): #2 mult
			#print("\tMultipl")
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

			#print("\t",instruction,param1,param2,param3,value1,value2)	

			intcodes[param3] = value1 * value2
			pos += 4

		elif(instruction == 99):	#halt
			#print("halt at pos",pos)
			break

		count +=1


def init_secuence(phase_setting):
	#amp A
	a = machine(int(phase_setting[0]))

	#amp B
	b = machine(int(phase_setting[1]), a)

	#amp C
	c = machine(int(phase_setting[2]), b)

	#amp D
	d = machine(int(phase_setting[3]), c)

	#amp B
	e = machine(int(phase_setting[4]), d)

	#print("to thrusters",e)
	return e
#init_secuence('01234')

candidates = []
for a in range(0,5):
	for b in range (0,5):
		for c in range (0,5):
			for d in range (0,5):
				for e in range (0,5):
					if a+b+c+d+e == 4+3+2+1 :
						candidates.append(str(a)+str(b)+str(c)+str(d)+str(e))

#print(candidates)
print(len(candidates))

solutions = { x : init_secuence(x) for x in candidates}
print(solutions)

print(max(solutions, key=solutions.get))

#31114 too low.