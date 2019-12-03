with open("2input.txt", 'r') as f:
	inputvalues = [line.rstrip('\n') for line in f]

# eachline = ''
# substr = []

# #for eachline in lines:
# substr = substr.append(lines.split(","))


# lines = (eachline)
# # print(lines)

# #lines = str(lines).split(",")

#print(inputvalues)

count = 0
value = 0
#inputvalues = []
# for line in lines:
# 	if(line != ","):
# 		inputvalues.append(line)
#		print(line)

#print(inputvalues)


for noun in range(0,100):
	print(noun)
	inputvalues[1] = noun+0
	inputvalues[2] = 0

	for line in inputvalues:

		#print(count, inputvalues[count])	

		if(((count) % 4) == 0): #  es modulo
			#print("posicion ",count, inputvalues[count])

			if(int(line) == 1): # suma
				#print("suma")
				posvalue1 = int(inputvalues[(count+1)]) 
				posvalue2 = int(inputvalues[(count+2)])
				pos = int(inputvalues[(count+3)])

				value1 = int(inputvalues[posvalue1])
				value2 = int(inputvalues[posvalue2])
				op = value1 + value2

				inputvalues[pos] = op
				#print("posicion ", count, " operacion suma", value1, "(",posvalue1, ") + ", value2 ,"(", posvalue2,")=", op)
				#print("confirmacion: ", inputvalues[pos], "en posicion ", pos)

			elif(int(line) == 2): # 2:multiplicacion
				posvalue1 = int(inputvalues[(count+1)]) 
				posvalue2 = int(inputvalues[(count+2)])
				pos = int(inputvalues[(count+3)])

				value1 = int(inputvalues[posvalue1])
				value2 = int(inputvalues[posvalue2])
				op = value1 * value2
				#print("resultado",value)
				inputvalues[pos] = op
				#print("posicion ", count, " operacion mult", value1, " * ", value2 ,"=", op)
				#print("confirmacion: ", inputvalues[pos], "en posicion ", pos)

			elif(int(line) == 99):
				#halt
				break

		count = count + 1

	print(inputvalues[0])

# 125 too low. . estaba sumando la posicion, no el valor en dicha posicion.
# 530607 too low  no estaba reemplazando los valores de la consigna

# 3516593, habia que leer todas las intrucciones.