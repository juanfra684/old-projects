import random
import os

class Triqui:

	def __init__(self,l):
		self.movpc   = random.randint(0,8)
		self.ganador = 0
		self.movhuman= 0
		self.level   = l
		self.tablero = ['1','2','3','4','5','6','7','8','9']
		self.printBoard()
		print "\nLos movimientos se introducen indicando el numero de la casilla.\n"
		self.tablero = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

	def printBoard(self):
		os.system("clear")
		print self.tablero[6],'|',self.tablero[7],'|',self.tablero[8]
		print "-"*9	
		print self.tablero[3],'|',self.tablero[4],'|',self.tablero[5]
		print "-"*9
		print self.tablero[0],'|',self.tablero[1],'|',self.tablero[2]

	def comprobarVictoria(self):
		# Humano
		if self.tablero[0]=="X":
			if self.tablero[1]=="X" and self.tablero[2]=="X":
				self.ganador=1
			elif self.tablero[3]=="X" and self.tablero[6]=="X":
				self.ganador=1
			elif self.tablero[4]=="X" and self.tablero[8]=="X":
				self.ganador=1
		elif self.tablero[4]=="X":
			if self.tablero[3]=="X" and self.tablero[5]=="X":
				self.ganador=1
			elif self.tablero[1]=="X" and self.tablero[7]=="X":
				self.ganador=1
			elif self.tablero[2]=="X" and self.tablero[6]=="X":
				self.ganador=1
		elif self.tablero[8]=="X":
			if self.tablero[2]=="X" and self.tablero[5]=="X":
				self.ganador=1
			elif self.tablero[7]=="X" and self.tablero[6]=="X":
				self.ganador=1
		#maquina
		if self.tablero[0]=="O":
			if self.tablero[1]=="O" and self.tablero[2]=="O":
				self.ganador=2
			elif self.tablero[3]=="O" and self.tablero[6]=="O":
				self.ganador=2
			elif self.tablero[4]=="O" and self.tablero[8]=="O":
				self.ganador=2
		elif self.tablero[4]=='O':
			if self.tablero[3]=='O' and self.tablero[5]=='O':
				self.ganador=2
			elif self.tablero[1]=="O" and self.tablero[7]=="O":
				self.ganador=2
			elif self.tablero[2]=="O" and self.tablero[6]=="O":
				self.ganador=2
		elif self.tablero[8]=="O":
			if   self.tablero[2]=="O" and self.tablero[5]=="O":
				self.ganador=2
			elif self.tablero[7]=="O" and self.tablero[6]=="O":
				self.ganador=2

	def resultado(self):
		if self.ganador==1:
			print "Ganaste !!"
		elif self.ganador==2:
			print "Perdiste !!"
		else:
			print "Empate !!"
	
	def humanMove(self,move):
		#self.movhuman  = int(raw_input("Cual es tu movimiento? (1-9): "))
		self.movhuman = move
		self.movhuman -= 1
		#while self.movhuman > 8 or self.movhuman < 0 or self.tablero[self.movhuman] == "X" or self.tablero[self.movhuman] == "O":
		#	self.movhuman = int(raw_input("Movimiento no valido, intente de nuevo (1-9): "))
		#	self.movhuman-= 1
		self.tablero[self.movhuman] = "X"

	def pcMove(self):
		if   (self.level == 1):
			self.moveDummy()
		elif (self.level == 2):
			self.moveBlocker()
		elif (self.level == 3):
			self.moveGodMode()

	def moveDummy(self):
		self.movpc = random.randint(0,8)
		while self.tablero[self.movpc] == "X" or self.tablero[self.movpc] == "O":
			self.movpc = random.randint(0,8)
		self.tablero[self.movpc] = "O"

	def moveBlocker(self):
		randPar = random.randrange(0,9,2)

		#Comprueba si esta iniciando el juego, de ser asi, usa el dummy
		for i in self.tablero:
			if i == ' ':
				Vacio = True
			else:
				Vacio = False ; break
		if Vacio == True:
			return self.moveDummy()

		#Comprueba si es su primer turno o si ya ha jugado antes
		for i in range(len(self.tablero)):
			if (self.tablero[i] == "O") :
				turn = 2; break
			else:
				turn = 1
		
		#Si es Primer turno despues de humano, ejecuta movimientos ya pensados.
		if turn == 1:
			#Si humano a jugado en esquinas:
			if (self.tablero[0] == "X") or (self.tablero[2] == "X") or (self.tablero[6] == "X") or (self.tablero[8] == "X"):
				self.tablero[4] = "O"
			#Si humano a juegado en centro:
			elif self.tablero[4] == "X":
				while randPar == 4:
					randPar = random.randrange(0,9,2)
				self.tablero[randPar] = "O"
			#Si humano a jugado en laterales
			elif (self.tablero[1] == "X") or (self.tabler[3] == "X") or (self.tabler[5] == "X") or (self.tabler[7] == "X"):
				self.tablero[4] = "O"

		#Si es Segundo turno, bloquea, sino hay que bloquear, usa dummy
		else:
			for i in range(len(self.tablero)):
				#Comprobacion de verticales:
				if   i == 0 or i == 3 or i == 6:
					if self.tablero[i] == "X":
						if self.tablero[i+1] == "X":
							if self.tablero[i+2] == ' ': self.tablero[i+2] = "O" ; return 0
						elif self.tablero[i+2] == "X":
							if self.tablero[i+1] == ' ': self.tablero[i+1] = "O" ; return 0

				elif i == 1 or i == 4 or i == 7:
					if self.tablero[i] == "X":
						if self.tablero[i+1] == "X":
							if self.tablero[i-1] == ' ': self.tablero[i-1] = "O" ; return 0
						elif self.tablero[i-1] == "X":
							if self.tablero[i+1] == ' ': self.tablero[i+1] = "O" ; return 0

				elif i == 2 or i == 5 or i == 8:
					if self.tablero[i] == "X":
						if self.tablero[i-1] == "X":
							if self.tablero[i-2] == ' ': self.tablero[i-2] = "O" ; return 0
						elif self.tablero[i-2] == "X":
							if self.tablero[i-1] == ' ': self.tablero[i-1] = "O" ; return 0

				#Comprobacion de horizontales:
				if   i == 0 or i == 1 or i == 2:
					if self.tablero[i] == "X":
						if self.tablero[i+3] == "X":
							if self.tablero[i+6] == ' ': self.tablero[i+6] = "O" ; return 0
						elif self.tablero[i+6] == "X":
							if self.tablero[i+3] == ' ': self.tablero[i+3] = "O" ; return 0

				elif i == 3 or i == 4 or i == 5:
					if self.tablero[i] == "X":
						if self.tablero[i+3] == "X":
							if self.tablero[i-3] == ' ': self.tablero[i-3] = "O" ; return 0
						elif self.tablero[i-3] == "X":
							if self.tablero[i+3] == ' ': self.tablero[i+3] = "O" ; return 0

				elif i == 6 or i == 7 or i == 8:
					if self.tablero[i] == "X":
						if self.tablero[i-3] == "X":
							if self.tablero[i-6] == ' ': self.tablero[i-6] = "O" ; return 0
						elif self.tablero[i-6] == "X":
							if self.tablero[i-3] == ' ': self.tablero[i-3] = "O" ; return 0

				#Comprobacion de diagonales:
				if i == 0 or i == 2 or i == 6 or i == 8:
					if self.tablero[i] == "X":
						if self.tablero[4] == "X":
							if   i==0:
								if self.tablero[i+8] == ' ': self.tablero[i+8] = "O" ; return 0
							elif i==2:
								if self.tablero[i+4] == ' ': self.tablero[i+4] = "O" ; return 0
							elif i==6:
								if self.tablero[i-4] == ' ': self.tablero[i-4] = "O" ; return 0
							elif i==8:
								if self.tablero[i-8] == ' ': self.tablero[i-8] = "O" ; return 0
						else:
							if   i==0:
								if self.tablero[i+8] == "X":
									if self.tablero[4] == ' ': self.tablero[4] = "O" ; return 0
							elif i==2:
								if self.tablero[i+4] == "X":
									if self.tablero[4] == ' ': self.tablero[4] = "O" ; return 0
							elif i==6:
								if self.tablero[i-4] == "X":
									if self.tablero[4] == ' ': self.tablero[4] = "O" ; return 0
							elif i==8:
								if self.tablero[i-8] == "X":
									if self.tablero[4] == ' ': self.tablero[4] = "O" ; return 0
				#Comprueba diagonales desde el centro
				elif i == 4:
					if self.tablero[4] == "X":
						if self.tablero[0] == "X":
							if self.tablero[8] == ' ': self.tablero[8] = "O" ; return 0
						if self.tablero[2] == "X":
							if self.tablero[6] == ' ': self.tablero[6] = "O" ; return 0
						if self.tablero[6] == "X":
							if self.tablero[2] == ' ': self.tablero[2] = "O" ; return 0
						if self.tablero[8] == "X":
							if self.tablero[0] == ' ': self.tablero[0] = "O" ; return 0
				#Si ninguna jugada se puede bloquear usa el dummy
			return self.moveDummy()


	def moveGodMode(self):
		print "Aqui va minmax"