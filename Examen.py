"""operadoresLogicos.py   Opera con 7 operadores lógicos predicados hasta obtener un valor de verdad

Descripción.
                Muestra la definición de 7 operadores lógicos para evaluar una colección de predicados
                hasta encontrar valores de verdad en los mismos.

                Muestra como operar una colección de proposiciónes para evaluar una suma de productos
                        S=B ∧C + B∧C
                        AL= A + BC
ver. 1.1.0   incorporación de función: generadorArgumentos() 17sept24.                
ver. 1.0.0   funcional operadoresLogicos.py

"""
import numpy as np
from inspect import signature
import time
#from playPySound import *
import sys
import pygame

def neg(p:bool)-> bool:
    """ La negación de una proposición
            Devuelve el valor de verdad opuesto a p.
    """
    if p:
        return False
    else:
        return True

def T(p:bool,q:bool)-> bool:
    """ Predicado Verdad
     Sin importar los par\'ametros, devuelve True.
    """
    return True

def F(p:bool,q:bool)-> bool:
    """ Predicado Falsedad
            Sin importar los par\'ametros, devuelve False.
    """
    return False

def P(p:bool, q:bool)-> bool:
    """ Primera componente
        Devuelve el valor del primer parámetro p.
    """
    return p

def Q(p:bool, q:bool)-> bool:
    """ Segunda componente
            Devuelve el valor del segundo parámetro q.
    """
    return q

def y(p:bool, q:bool)-> bool:
    """ Conjunción
            Devuelve True cuando ambas proposiciones son True,
            devuelve False en cualquier otro caso.
    """
    if p:
        return q
    else:
        return False
    
def o(p:bool, q:bool)-> bool:
    """ Disyunción de dos proposiciones:
        Devuelve True cuando al menos una de las proposiciones es True,
        si ambas proposiciones son False, entonces devuelve False.
    """
    if p:
        return True
    else:
        return q

def ox(p:bool, q:bool)-> bool:
    """ Disyunción exclusiva:
            Devuelve True cuando ambas proposiciones tienen valor diferente.
            Cuando las proposiciones coinciden en su valor, devuelve False.
        """
    if p:
        return neg(q)
    else:
        return q

def car(L:list):
    """ car Content of Address part of Register [1950s]
        Devuelve el primer elemento de una lista no vacía.
    """
    return L[0]

def cdr(L:list)-> list:
    """ cdr Content of Decrement part of Register [1950s]
        Devuelve una lista con todos excepto el primer
        elemento de una lista no vacía.
    """
    return L[1:]

def Y(*Lprop:list)->bool:
    """
        Disyunción extendida
        Recibe una lista no determinada de proposiciones.
    """
    if Lprop == ():
        return True
    elif car(Lprop):
        return Y(*cdr(Lprop))
    else:
        return False

def O(*Lprop:list)->bool:
    """
        Conjunción extendida
        Recibe una lista no determinada de proposiciones.
    """
    if Lprop == ():
        return False
    elif car(Lprop):
        return True
    else:
        return O(*cdr(Lprop))

def sC(D):
    
   if D:
      pygame.mixer.init()
      pygame.mixer.music.load("cerradura.WAV")
      pygame.mixer.music.play()
      print("Segunda cerradura abierta")
   else:
      print ("Segunda cerradura cerrada")
      
def pC(D):
    
    if D:
      pygame.mixer.init()
      pygame.mixer.music.load("cerraduraDos.WAV")
      pygame.mixer.music.play()
      print("Primera cerradura abierta")
    else:
      print("Segunda cerradura cerrada")
       
def main() -> int:

    #Segunda cerradura
    
    A=True
    B=False
    C=False

    _B_C=y(neg(B),neg(C))
    D=y(A,_B_C)
    
    sC((D))
    pC((D))

    #Primera cerradura

    A=True
    B=True
    C=False
   # D=True 

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nPrograma finalizado por usuario.")
        sys.exit(0)