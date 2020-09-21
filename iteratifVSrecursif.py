#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:07:11 2020

@author: fschwarz
"""


"""
entrée : une chaîne de caractères c
sortie : le nombre de 'e' dans c
"""
def compte(c):
    i = 0
    for x in c:
        if x == 'e':
            i = i+1
    return i
    

def compteRec(c):
    if c == '':
         return 0
    elif c[0] == 'e':
        return 1 + compteRec(c[1:])
    else:
        return compteRec(c[1:])
    
    
    
    
"""
entrée : un entier n
sortie : la somme des inverses des carrés des n premiers entiers
"""
def somme(n):
    s = 0
    for k in range(1,n+1):
        s = s + 1 / (k**2)
    return s

def sommeRec(n):
    if n == 0:
        return 0
    else:
        return 1 / (n**2) + sommeRec(n-1)
    
    

        