"""ejemploFAdo_basico.py   Evalua una string con un automata finito deterministico
Descripción.
            -Muestra como evaluar una cadena de caracteres hasta evaluar posible estado de aceptación
            -
            https://ed.sjuanrio.tecnm.mx/pluginfile.php/118066/mod_folder/content/0/matemticas-discretas-6edi-johnsonbaugh.pdf
            
"""
from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *
##
##m3 = DFA()
##m3.setSigma(["a","o", "l","h"])
##             
##m3.addState('s1')#0
##m3.addState('s2')#1
##m3.addState('s3')#2
##m3.addState('s4')#3
##m3.setInitial(0)
##m3.addFinal(4)
###                          actual entrada siguiente
##m3.addTransition(3,      "a",             4)# 4de4
##m3.addTransition(1,      "o",            2)# 2de4
##m3.addTransition(2,      "l",              3)# 3de4
##m3.addTransition(0,      "h",            1)# 1de4
###evalua ejemplos
##print(m3.evalWordP("hola"))

m3 = DFA()
m3.setSigma(['0','1', '2','3','4','5','6','7','8','9'])
##
m3.addState('s0')#0
m3.addState('s1')#1
m3.addState('s2')#2
m3.addState('s3')#3
m3.addState('s4')#4
m3.addState('s5')#5
m3.addState('s6')#6
m3.addState('s7')#7
m3.addState('s8')#8
m3.addState('s9')#9
m3.addState('s10')#10
m3.addState('s11')#11
m3.addState('s12')#12
m3.setInitial(0)
m3.addFinal(12)
### entrada con caracter a evaluar
#####            actual entrada siguiente
m3.addTransition(0,      '1',            1)# 1de12
m3.addTransition(1,      '9',            2)# 2de12
m3.addTransition(2,      '2',            3)# 3de12
m3.addTransition(3,      '1',           4)# 4de12
m3.addTransition(4,      '6',           5)# 5de12
m3.addTransition(5,      '8',           6)# 6de12
m3.addTransition(6,      '1',           7)# 7de12
m3.addTransition(7,      '5',           8)# 8de12
m3.addTransition(8,      '5',           9)# 9de12
m3.addTransition(9,      '1',           10)#10de12
m3.addTransition(10,    '2',           11)# 1de12
m3.addTransition(11,    '5',           12)# 2de12
###evalua ejemplos
def ip():
    ipData = input("Teclea la Dirección IP: ")

    ipEsperada = "192168155125"
    es_valida = m3.evalWordP(ipData)  # Evalúa la IP ingresada

    print(f"\nIP ingresada: {ipData}")
    print(f"IP esperada: {ipEsperada}")

    if ipData == ipEsperada:
        print(f"Comparación con IP esperada: {es_valida}")
    else:
        print(f"Comparación con IP esperada: {es_valida}" )