# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:32:39 2018

@author: Ldv
"""
from collections import Counter
import numpy as np
from PIL import Image
#Funcion que discretiza la matriz de la imagen
#Referecia 

def discretizadorFilas(fac,xn,yn,laberinto,facy):
    #Analiza la primera matriz
    
    prueba = []
    for x in range(xn,fac):
        for y in range(yn,facy):
            xy = laberinto[y][x]
            prueba = np.append(prueba,xy)
    
    #Obtiene los el primer, segundo y tercer valor de cada codigo RGB, lista de sublistas
    m1 = prueba[0::3]
    m2 = prueba[1::3]
    m3 = prueba[2::3]
    #Obtiene el varlo RGB mas frecuente
    c1 = Counter(m1)
    c11 = c1.most_common(1)
    c111 = c11[0]
    R = c111[0]    
    c2 = Counter(m2)
    c22 = c2.most_common(1)
    c222 = c22[0]
    G = c222[0]
    c3 = Counter(m3)
    c33 = c3.most_common(1)
    c333 = c33[0]
    B = c333[0]
    val = coloresParser(R,G,B)
    return val

    
def coloresParser(R,G,B):
        #Retorna blanco
    if (R > 250 and G > 250 and B > 250):
        return 255,255,255
    #Retorna rojo
    elif (R > 200 and G < 200 and B < 200):
        return 255,0,0
    #Retorna verde
    elif ((R > 40 and G > 100 and B < 100) or (R <= 100 and G > 200 and B <= 100) ):
        return 0,255,0
    #Caso contrario retorna negro
    else:
        return 0,0,0
    
def tuppler(lista):
    numbers = [ int(x) for x in lista ]
    zipped = list(zip(numbers[0::3], numbers[1::3], numbers[2::3]))
    
    return zipped

def imageSaver(lista,n):
    im2 = Image.new("RGB", (n,n))
    im2.putdata(lista)
    im2 = im2.resize((500, 500))
    im2.save("discretizada.jpg")
    
    
def Breadth(lista,n):
    im2 = Image.new("RGB", (n,n))
    im2.putdata(lista)
    im2 = im2.resize((500, 500))
    im2.save("Breadth.jpg")
    
def Depth(lista,n):
    im2 = Image.new("RGB", (n,n))
    im2.putdata(lista)
    im2 = im2.resize((500, 500))
    im2.save("Depth.jpg")
    
def DepthR(lista,n):
    im2 = Image.new("RGB", (n,n))
    im2.putdata(lista)
    im2 = im2.resize((500, 500))
    im2.save("DepthRightFirst.jpg")
    
def heu1(lista,n):
    im2 = Image.new("RGB", (n,n))
    im2.putdata(lista)
    im2 = im2.resize((500, 500))
    im2.save("PrimeraHeuristica.jpg")

def findStarter(lista):
    for i, j in enumerate(lista):
        if j == (255, 0, 0):
            return i
        
def findGoal(lista):
    verde = [i for i,x in enumerate(lista) if x == (0, 255, 0)]
    return verde 
        
def diccionarioMovimientos(starter,final,n):
    limitesIzquierdo = [] 
    limitesDerecho = []
    limite = n * n
    for i in range(n,limite,n):
        limitesIzquierdo.append(i)
    for i in range(n-1,limite,n):
        limitesDerecho.append(i)
    #Diccionario de movimientos
    movimientos = []
    if (starter == 0):
        if (final[starter+1] == (255,255,255)):
            movimientos.append("derecha")
        if (final[starter+20] == (255,255,255)):
            movimientos.append("abajo")
    elif (starter in limitesIzquierdo):
        if (final[starter+1] == (255,255,255)):
            movimientos.append("derecha")
        if (final[starter-20] == (255,255,255)):
            movimientos.append("arriba")
        #if (final[starter+20] == (255,255,255)):
            #movimientos.append("abajo")   
    elif (starter in limitesDerecho):
        if (final[starter-1] == (255,255,255)):
            movimientos.append("izquierda")
        if (final[starter-20] == (255,255,255)):
            movimientos.append("arriba")
        if (final[starter+20] == (255,255,255)):
            movimientos.append("abajo")
    elif (starter == len(final)):
        if (final[starter-1] == (255,255,255)):
            movimientos.append("izquierda")
        if (final[starter-20] == (255,255,255)):
            movimientos.append("arriba")
    elif (starter <= len(final) and starter >= (len(final) - n)):
        if (final[starter-1] == (255,255,255)):
            movimientos.append("izquierda")
        if (final[starter+1] == (255,255,255)):
            movimientos.append("derecha")
        if (final[starter-20] == (255,255,255)):
            movimientos.append("arriba")
    else:
        if (final[starter-1] == (255,255,255)):
            movimientos.append("izquierda")
        if (final[starter+1] == (255,255,255)):
            movimientos.append("derecha")
        if (final[starter-20] == (255,255,255)):
            movimientos.append("arriba")
        if (final[starter+20] == (255,255,255)):
            movimientos.append("abajo")
    return movimientos


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ALGORITMOS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    

def breadthfirst(final,n):
    #BREADTH FIRST
    #Da el nodo inicial y sus posibles movimientos y nodos que son considerados meta
    starter = findStarter(final)
    fin = findGoal(final)
    nodo = starter
    movimientos = diccionarioMovimientos(nodo,final,n)
    visitados = [nodo]
    for i in visitados:
        movimientos = diccionarioMovimientos(i,final,n)
        if (((i-20) or (i+20) or (i+1) or (i-1)) in fin):
            break
        if ('izquierda' in movimientos):
            final[i-1] = 0,0,255
            visitados.append(i-1)
        if ('derecha' in movimientos):
            final[i+1] = 0,0,255
            visitados.append(i+1)
        if ('arriba' in movimientos):
            final[i-20] = 0,0,255
            visitados.append(i-20)
        if ('abajo' in movimientos):
            final[i+20] = 0,0,255
            visitados.append(i+20)
    Breadth(final,n)
    return visitados

def depthfirstL(final,n):
    #DEPTH FIRST IZQUIERDO PRIMERO
    starter = findStarter(final)
    fin = findGoal(final)
    nodo = starter
    movimientos = diccionarioMovimientos(nodo,final,n)
    visitados = [nodo]
    for i in visitados:
        movimientos = diccionarioMovimientos(i,final,n)
        if (((i-20) or (i+20) or (i+1) or (i-1)) in fin):
            break
        if (i>=0):
            if ('izquierda' in movimientos):
                final[i-1] = 0,0,255
                visitados.append(i-1)
            elif('arriba' in movimientos and (i-20) >= 0):
                final[i-20] = 0,0,255
                visitados.append(i-20)
            elif('derecha' in movimientos):
                final[i+1] = 0,0,255
                visitados.append(i+1)
            elif('abajo' in movimientos):
                final[i+20] = 0,0,255
                visitados.append(i+20)
        else:
            if('derecha' in movimientos):
                final[i+1] = 0,0,255
                visitados.append(i+1)
            elif('abajo' in movimientos):
                final[i+20] = 0,0,255
                visitados.append(i+20)
    Depth(final,n)
    return visitados

def depthFirstR(final,n):
    starter = findStarter(final)
    fin = findGoal(final)
    nodo = starter
    movimientos = diccionarioMovimientos(nodo,final,n)
    visitados = [nodo]
    for i in visitados:
        movimientos = diccionarioMovimientos(i,final,n)
        if (((i-20) or (i+20) or (i+1) or (i-1)) in fin):
            break
        if (i>=0):
            if('derecha' in movimientos):
                final[i+1] = 0,0,255
                visitados.append(i+1)
            elif('arriba' in movimientos and (i-20) >= 0):
                final[i-20] = 0,0,255
                visitados.append(i-20)   
            elif ('izquierda' in movimientos):
                final[i-1] = 0,0,255
                visitados.append(i-1)
            elif('abajo' in movimientos):
                final[i+20] = 0,0,255
                visitados.append(i+20)
    DepthR(final,n)
    return visitados

def heuristica1(inicial,goal1,n):
    i = goal1
    while (goal1 < inicial):
        goal1 = goal1 + n
    a = inicial - goal1
    b = (goal1 - i)/n
    valor = ((a**2) + (b**2))**(1/2)
    return valor


def aStar1(final,n):
    
    starter = findStarter(final)
    fin1 = findGoal(final)
    fin = fin1[0]
    nodo = starter
    movimientos = diccionarioMovimientos(nodo,final,n)
    visitados = [nodo]
    
    #inicial = inicial - 1
    for i in visitados:
        eur = []
        movimientos = diccionarioMovimientos(i,final,n)
        if (((i-20) or (i+20) or (i+1) or (i-1)) in fin1):
            break
        if('derecha' in movimientos):
            #final[i+1] = 0,0,255
            x = heuristica1(i+1,fin,n)
            eur.append(x)
            #visitados.append(i+1)
        if('derecha' not in movimientos):
            eur.append(999)
        if('arriba' in movimientos and (i-20) >= 0):
            #final[i-20] = 0,0,255
            x = heuristica1(i-20,fin,n)
            eur.append(x)
        if('arriba' not in movimientos):
            eur.append(999)
            #visitados.append(i-20)   
        if ('izquierda' in movimientos):
            #final[i-1] = 0,0,255
            x = heuristica1(i-1,fin,n)
            eur.append(x)
        if('izquierda' not in movimientos):
            #visitados.append(i-1)
            eur.append(999)
        if('abajo' in movimientos):
            #final[i+20] = 0,0,255
            x = heuristica1(i+20,fin,n)
            eur.append(x)
        if('abajo' not in movimientos):
            eur.append(999)
            #visitados.append(i+20)
        menor = min(eur)
        verde = [y for y,x in enumerate(eur) if x == menor]
        
        
        if verde == [0]: #izquierda
            if ((i-1) not in visitados):
                visitados.append(i-1)
                final[i-1] =  0,0,255
        elif verde == [1]: #derecha
            if((i+1) not in visitados):
                visitados.append(i+1)
                final[i+1] =  0,0,255
        elif verde == [2]: #abajo
            if((i +20) not in visitados):
                visitados.append(i+20)
                final[i+20] =  0,0,255
        elif verde == [3]: #arriba
            if ((i-20) not in visitados):
                visitados.append(i-20)
                final[i-20] =  0,0,255    
    heu1(final,n)
    return visitados