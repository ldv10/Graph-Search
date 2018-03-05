# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:02:21 2018

@author: Leonel Guillen
"""

from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from funciones import *
#FALTA PROGRA DEFENSIVA

image = Image.open("1.bmp")

laberinto = np.asarray(image,dtype=np.int64)
n = int(input("N a discretizar: "))
#obtiene alto y ancho de la imagen
width, height = image.size
fac = width/ n
fac = int(fac)

xn = 0
yn = 0
facx = fac
facy = fac
fila = []
filacodigo = []
#Recorre la imagen como si fuera una matriz de submatrices
for l in range(0,height,fac):
    xn = 0 
    facx = fac
    if (l == 0):
        yn = 0
    else:
        yn = facy
        facy = facy + fac
        
    for z in range(0,width,fac):
        x = discretizadorFilas(facx,xn,yn,laberinto,facy)
        fila = np.append(fila,x)
        xn = facx
        facx = facx + fac

#Convierte en int y convierte los elemtnos de lista en tuplas
final = tuppler(fila)

#Guarda imagen
imageSaver(final,n)
factxt = str(fac)



#Algoritmo de Breadth first, retorna los nodos visitados
#x = breadthfirst(final,n)
#para costo de BF
#costo = len(x)

#DEPTH FIRST LINK FIRST,retorna nodos visitados
#yL = depthfirstL(final,n)
#costo = len(yL)

#DEPTH FIRST RIGHT FIRST, retorna visitados
#yR = depthFirstR(final,n)
#costo = len(yR)
#Astar q 
#aStar1(final,n)








