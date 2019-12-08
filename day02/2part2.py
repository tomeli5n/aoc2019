with open("2input.txt", 'r') as f:
	raw = [line.rstrip('\n') for line in f]

# eachline = ''
# substr = []

# #for eachline in lines:
# substr = substr.append(lines.split(","))


# lines = (eachline)
# # print(lines)

# #lines = str(lines).split(",")

# print(inputvalues)


value = 0
#inputvalues = []
# for line in lines:
# 	if(line != ","):
# 		inputvalues.append(line)
#		print(line)

# print(inputvalues)

#noun = 1
#verb = 1

for verb in range(1,100):
#	inputvalues = raw
#	inputvalues[2] = verb

	for noun in range(1, 100):

		inputvalues = []
		inputvalues = raw

		inputvalues[1] = int(noun)
		inputvalues[2] = int(verb)

		print("noun=",noun, " verb=",verb)
		print("------->",inputvalues[1], "-",inputvalues[2])
		
		count = 0

		for line in inputvalues:

			#print("-------<",inputvalues[1], "-",inputvalues[2])

			if(((count) % 4) == 0): #  es modulo
				#print("posicion ",count, inputvalues[count])

				if(int(line) == 1): # suma
					posvalue1 = int(inputvalues[(count+1)]) 
					posvalue2 = int(inputvalues[(count+2)])
					pos = int(inputvalues[(count+3)])

					while(max(pos,posvalue1,posvalue2)+1 > len(inputvalues)):
						inputvalues.append(0)

					value1 = int(inputvalues[posvalue1])
					value2 = int(inputvalues[posvalue2])
					op = value1 + value2

					inputvalues[pos] = op
					print("posicion ", count, " operacion suma", value1, "(",posvalue1, ") + ", value2 ,"(", posvalue2,")=", op ,"(",pos,")")
					#print("confirmacion: ", inputvalues[pos], "en posicion ", pos)

				elif(int(line) == 2): # 2:multiplicacion
					posvalue1 = int(inputvalues[(count+1)]) 
					posvalue2 = int(inputvalues[(count+2)])
					pos = int(inputvalues[(count+3)])

					while(max(pos,posvalue1,posvalue2)+1 > len(inputvalues)):
						inputvalues.append(0)
						#print("agregado!")

					#print("posicion:",posvalue2," largo",len(inputvalues))
					value1 = int(inputvalues[posvalue1])
					#print(posvalue2)
					value2 = int(inputvalues[posvalue2])
					op = value1 * value2
					#print("resultado",value)
					inputvalues[pos] = op
					#print("posicion ", count, " operacion mult", value1, " * ", value2 ,"=", op)
					#print("confirmacion: ", inputvalues[pos], "en posicion ", pos)

				elif(int(line) == 99):	#halt
					break

			count = count + 1
		
		print("resultado= ", inputvalues[0])
		




# 3516593, habia que leer todas las intrucciones.