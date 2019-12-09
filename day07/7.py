"""
5 intcode-machine
"""

with open("input.txt") as f:
	for line in f:
		_ = line.split(',') 

	input_data = [int(item) for item in _]



machine_status ={} #machine ID: [[intcodes], position, status]
intcodes= []
def machine(phase, input_signal=0, instance=0):
	output_value=None
	print("MACHINE",instance,"INPUT",input_signal,"PHASE:",phase)

	#retrieve status. Else save
	if instance in machine_status:
		#print("running")
		intcodes = machine_status[instance][0]

	else:
		machine_status[instance] = [input_data.copy(), 0, False]
	
	intcodes = machine_status[instance][0]
	pos = machine_status[instance][1]

	#print("\t INPUT", phase, input_signal)

	halt = None

	while True:
		#if halt: break
		instruction = intcodes[pos]
		status = machine_status[instance][2]
		param1=0
		param2=0
		value1=0
		value2=0

		#print("\tINST",instruction)
		
		# INPUT
		if( instruction == 3): #input, guardar
			param1 = intcodes[pos+1]

			#Variables de arranque
			if status:
				value1 = input_signal
			else: #not running
				value1 = phase
				machine_status[instance][2] = True 
			
			intcodes[param1] = value1

			#print("\t\tinput ", value1)

			pos +=2

		elif( instruction % 10 == 4): #outupt
			param1 = intcodes[pos+1]
			value1 = intcodes[param1]
			output_value=value1
			print("\t""OUTPUT",output_value)
			pos +=2
			break

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
			
			#print("\t",instruction,param1,param2,param3,value1,value2)
			intcodes[param3] = value1 + value2
			
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
			if not output_value: output_value = input_signal
			halt = True
			break

	machine_status[instance][0] = intcodes
	machine_status[instance][1] = pos
	machine_status[instance][2] = True 
	
	if halt: 
		print("Removing machine",instance)
		machine_status.pop(instance)

	#print(machine_status)
	return output_value


#### PART A

def init_secuence(phase_setting):
	#amp A
	a = machine(int(phase_setting[0]),0 ,1)

	#amp B
	b = machine(int(phase_setting[1]), a, 2)

	#amp C
	c = machine(int(phase_setting[2]), b, 3)

	#amp D
	d = machine(int(phase_setting[3]), c, 4)

	#amp B
	e = machine(int(phase_setting[4]), d, 5)

	print("CODE",phase_setting,"to thrusters",e)
	return e

candidates = []
for a in range(0,5):
	for b in range (0,5):
		for c in range (0,5):
			for d in range (0,5):
				for e in range (0,5):

					combi = str(a)+str(b)+str(c)+str(d)+str(e)
					if ''.join(sorted(combi)) == '01234' :
						candidates.append(str(a)+str(b)+str(c)+str(d)+str(e))

print(len(candidates))

solutions = { x : init_secuence(x) for x in candidates}

print("PART a max",solutions.get(max(solutions, key=solutions.get)))

#print(init_secuence('03124'))
#31114 too low.
#despues de aplicar el filtro y sort:
#03124  too low. asegurado que son 120 phase statuse
# resultado: 39867


###  PART B

candidates = []
for a in range(5,10):
	for b in range (5,10):
		for c in range (5,10):
			for d in range (5,10):
				for e in range (5,10):

					combi = str(a)+str(b)+str(c)+str(d)+str(e)
					if ''.join(sorted(combi)) == '56789' :
						candidates.append(str(a)+str(b)+str(c)+str(d)+str(e))

#print(candidates)


def init_secuence_b(phase_setting):

	e=0
	count=True
	while (count or machine_status):

		#amp A
		a = machine(int(phase_setting[0]), e, 1)

		#amp B
		b = machine(int(phase_setting[1]), a, 2)

		#amp C
		c = machine(int(phase_setting[2]), b, 3)

		#amp D
		d = machine(int(phase_setting[3]), c, 4)

		#amp B
		e = machine(int(phase_setting[4]), d, 5)

		count = False

	print("to thrusters",e)
	return e

#init_secuence_b('97856')


solutions_b = { x : init_secuence_b(x) for x in candidates}


print("PART B max",solutions_b.get(max(solutions_b, key=solutions_b.get)))