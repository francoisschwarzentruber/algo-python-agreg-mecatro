#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:02:35 2020

@author: fschwarz
"""

import turtle


"""
 entrée : un entier n positif, longueurLigne une longueur
 sortie : trace le morceau du flocon de degré n où chaque ligne est de 
          longueur longueurLigne
 exemple : koch(4, 3)
"""
def koch(n, longueurLigne):
    if(n == 0):
        turtle.forward(longueurLigne)
    else:
        koch(n-1, longueurLigne)
        turtle.left(60)
        koch(n-1, longueurLigne)
        turtle.right(120)
        koch(n-1, longueurLigne)
        turtle.left(60)
        koch(n-1, longueurLigne)