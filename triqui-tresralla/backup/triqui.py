import os
from core import *
os.system("clear")

print "Seleccione la dificultad: "
LEVEL = int(raw_input("1. Facil\n2. Medio\n3. Imposible\n"))
while True:
	if LEVEL == 1 or LEVEL == 2 or LEVEL == 3:
		break
	else:
		os.system("clear")
		LEVEL = int(raw_input("Opcion incorrecta\n1. Facil\n2. Medio\n3. Imposible\n"))



Triqui = Triqui(LEVEL)
#Quien inicia el juego?
#6 Para el humano, 5 para la maquina

for turno in range(1,6):
	Triqui.humanMove(move)
	Triqui.printBoard()
	Triqui.comprobarVictoria()
	if Triqui.ganador != 0:
		Triqui.resultado()
	if turno < 5:
		Triqui.pcMove()
		Triqui.printBoard()
		Triqui.comprobarVictoria()
		if Triqui.ganador != 0:
			Triqui.resultado()

Triqui.resultado()