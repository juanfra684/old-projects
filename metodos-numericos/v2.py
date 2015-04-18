#Version 9: Elementos modificados: funcion graficas(..)

# -*- encoding: utf-8 -*-


# ----------------------------------------------------------------------------
#|                    PRIMER PROYECTO DE PROGRAMACION III:                    |                 	                
#|                            METODOS NUMERICOS                               |
#|                                                                            |
#|                             PRESENTADO POR:                                |
#|                       ANDRES FELIPE COLLAZOS ROZO                          |
#|                          SEBASTIAN HOYOS MURIEL                            |
# ----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Inclusionde la libreria sympy, la cual tiene funciones que nos permiten  
# Parametrizar las funciones del programa.
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *

#-----------------------------------------------------------------------------
# Definicion del simbolo principal: 'x'
x=symbols('x')

#-----------------------------------------------------------------------------
# Definicion de las funciones f(x) y su derivada df(x)
def f(x0, f):
	er=f
	er=er.subs(x, x0)
	return er.evalf()

#Hay tres parametros, el parametro orden es por defecto 1, si no es colocado
#Al invocar la funcion
def df(x0, f, orden=1):
	er=f
	er=diff(er, x, orden)
	er=er.subs(x, x0)
	return er.evalf()

#-----------------------------------------------------------------------------
# Metodos numericos para encontrar raices reales

# Newton-Raphson:
def NewtonRaphson(x0, er):
	for i in range(40):
		x0= x0- ((f(x0, er))/(df(x0, er)))	
	return x0;

# Biseccion:
def Biseccion(xu, xl, er):
	i=0
	
	xi=float(xu+xl)/2
	
	if (f(xu,er))*(f(xl,er))<0:
		while abs(xu-xl)>1e-8:
			if ((f(xu,er))*(f(xi,er))<0):
				xl=xi
			elif (f(xl,er))*(f(xi,er))<0:
				xu=xi
			xi=float(xu+xl)/2
			#print "iter", i+1, " Raiz:", xi  #Mostrar cada iteracion
			i=i+1
		return xi	
	else:
		print ("La funcion no es monotona en el interval [a,b]")


#punto fijo
def puntoFijo(x0, er):
	for i in range(10):
		x0= x0 + f(x0, er)
	return x0

#-----------------------------------------------------------------------------
# Metodos numericos integrales

def trapecio(a, b, er):
	I=((b - a)*( (f(a, er)) + (f(b, er)) ))/2 
	return I

def trapecioCompuesto(a, b, n, er):
	s=0
	xi=0
	for i in range(1, n):
		xi=a+i*(float(b-a)/n)
		s=s+f(xi, er)
	return ((b-a)*(f(a,er) + 2*s + f(b,er)))/(2*n)	

def simpson13(a, b, er):
	xi=a+float(b-a)/2
	return ((b-a)*(f(a, er) + 4*f(xi, er) + f(b, er)))/6
	
def simpson13Compuesto(a, b, n, er):
	s1=0
	s2=0
	xi=0
	i=1
	#Para la sumatoria 1
	while i<=n-1:
		#print "I: ", i
		xi=a+i*(float(b-a)/n)
		s1=s1+f(xi, er)
		i=i+2
	#Para la sumatoria 2
	i=2
	while i<=n-2:
		#print "I: ", i
		xi=a+i*(float(b-a)/n)
		s2=s2+f(xi, er)
		i=i+2
	return ((b-a)*( f(a, er) + 4*s1 + 2*s2 + f(b, er) ))/(3*n)

def simpson38(a, b, er):
	x1=a+float(b-a)/3
	x2=xi=a+ 2*float(b-a)/3
	return ((b-a)*( f(a, er) + 3*f(x1, er) +  3*f(x2, er) + f(b, er) ))/8

def simpson38Compuesto(a, b, n, er):
	s1=0 #multiplos de 3
	s2=0 #resto de multiplos
	xi=0
	h=float(b-a)/n
	i=1
	#ciclo
	while i<n:
		if i%3 == 0:
			xi=a+i*h
			s1=s1+ f(xi, er)
		else:
			xi=a+i*h
			s2=s2+ f(xi, er)
		i=i+1	
	return ((3*h)/8.0)*( f(a, er) + 2*s1 + 3*s2 + f(b, er))			


#-----------------------------------------------------------------------------
# Metodo numerico para encontrar minimos
def gradienteDescendiente(x0, alfa):
	print "Metodo del gradiente descendiente"
	print "Ingrese la funcion"
	er=input()
	for i in range(50):
		x0= x0 - alfa*df(x0, er)
		#print "Iter:", i+1," Minimo:", x0 
	return x0


#-----------------------------------------------------------------------------
# FUNCION PARA GRAFICAR A F(X) DEPENDIENDO DEL METODO QUE ESCOGA:

#Esta funcion la usaremos en la interfas grafica, para que el usuario al 
#Presionar uno de los botones correspondientes a cada metodo, la grafica
#De la funcion f(x) sea especial para cada caso
def grafica(funtion, limInf, limSup, cad):
	er=funtion
	#Grafico: Se hace depende de donde haya quedado la raiz
	#Coordenadas para x:
	Ox = np.arange(limInf, limSup, 0.02)
	#Coordenadas para y:
	Oy = []
	for i in Ox:
		Oy.append( f(i, er) )

	plt.title(cad) #Imprimir Titulo en grafico	
	plt.plot(Ox, Oy)
	plt.show()

def BotonParaElMetodo(funtion, M):
	er=funtion
	if M=='NR':
		raiz=NewtonRaphson(input("Digite el punto inicial: "), er)
		cad="Newton Raphson: La raiz es: "+ str(raiz)

		grafica(er, raiz-5, raiz+5, cad)
	else:
		if M=='Biseccion':
			raiz=Biseccion(input("Ingrese a Xu: "), input("Ingrese a Xl: "), er)
			cad="Biseccion: La raiz es "+ str(raiz)

			grafica(er, raiz-5, raiz+5, cad)

		else:
			if M=='puntofijo':
				#OJO! Metodo diverge con facilidad!
				raiz=puntoFijo(input("Ingrese el valor inicial: "), er)
				cad="Punto Fijo: La raiz es "+ str(raiz)

				grafica(er, raiz-5, raiz+5, cad)
			else:
				if M=='trapecio':
					a=input("Ingrese [a]: ")
					b=input("Ingrese [b]: ")
					I=trapecio(a, b, er)
					cad="Trapecio: Area="+ str(I)

					grafica(er, a, b, cad)

				else:
					if M=='trapecioCompuesto':
						a=input("Ingrese [a]: ")
						b=input("Ingrese [b]: ")
						n=input("Con cuantas iteraciones lo quiere? ")
						I=trapecioCompuesto(a, b, n, er)
						cad="Trapecio Compuesto: Area="+ str(I)

						grafica(er, a, b, cad)
					else:
						if M=='simpson13':
							a=input("Ingrese [a]: ")
							b=input("Ingrese [b]: ")
							I=simpson13(a, b, er)
							cad="Simpson 1/3: Area="+ str(I)

							grafica(er, a, b, cad)
						else:
							if M=='simpson13Compuesto':
								a=input("Ingrese [a]: ")
								b=input("Ingrese [b]: ")
								n=input("Con cuantas iteraciones lo quiere? ")
								I=simpson13Compuesto(a, b, n, er)
								cad="Simpson 1/3 Compuesto: Area="+ str(I)

								grafica(er, a, b, cad)
							else:
								if M=='simpson38':
									a=input("Ingrese [a]: ")
									b=input("Ingrese [b]: ")
									I=simpson38(a, b, er)
									cad="Simpson 3/8: Area="+ str(I)

									grafica(er, a, b, cad)
								else:
									if M=='simpson38Compuesto':
										a=input("Ingrese [a]: ")
										b=input("Ingrese [b]: ")
										n=input("Con cuantas iteraciones lo quiere? ")
										I=simpson38Compuesto(a, b, n, er)
										cad="Simpson 3/8 Compuesto: Area="+ str(I)

										grafica(er, a, b, cad)

BotonParaElMetodo(1,"Biseccion")