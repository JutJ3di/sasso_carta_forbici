
import random


def sfida(scelta,vec):
	i = random.randrange(0,2)
	print("io ho scelto : ",vec[i])
	
	if(vec[i] == "sasso" and scelta == "carta"):
		print("\nHAI VINTO!\n")
	elif(vec[i] == "sasso" and scelta == "forbici"):
		print("\nHAI PERSO!\n")
	elif(vec[i] == "carta" and scelta == "sasso"):
		print("\nHAI PERSO!\n")
	elif(vec[i] == "carta" and scelta == "forbici"):
		print("\nHAI VINTO!\n")
	elif(vec[i] == "forbici" and scelta == "carta"):
		print("\nHAI PERSO!\n")
	elif(vec[i] == "forbici" and scelta == "sasso"):
		print("\nHAI VINTO!\n")
	elif(vec[i] == scelta):
		print("\nHAI PREGGIATO!\n")


print("Benvenuto in questo gioco molto semplice  (exit per uscire)\n")

print("Il gioco già lo conosci è sasso carta forbici\ni valori che puoi scegliere sono tra:")

vec = ["sasso","carta","forbici"]

for x in vec:
	print(x)


while 1:


	print("ricorda che sasso > forbici , forbici > carta e carta > sasso\n")
	
	while 1 :
		scelta = input ("\nfai la tua scelta : ")
		if(scelta == "sasso" or scelta == "forbici" or scelta =="carta" or scelta == "exit"):
			break

	
	
	if(scelta == "exit"):
		break
	else:
		sfida(scelta,vec)
