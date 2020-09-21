#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:07:11 2020

@author: fschwarz
"""

"""
entrée : les préférences pour les agents A et les agents B
sortie : un couplage stable
exemples : GS([[0, 1, 2], [1, 2, 0], [2, 1, 0]], [[0, 1, 2], [1, 2, 0], [2, 1, 0]])
           GS([[0, 1, 2], [2, 0, 1], [2, 1, 0]], [[2, 1, 0], [2,1, 0], [2, 1, 0]])
"""
def GS(APref, BPref):
    
    ##initialisation
    n = len(APref)
    A = range(len(APref))
    B = range(len(BPref))
    
    libresA = [a for a in A]
    Next = [0 for a in A]
    ranking = [ [ BPref[b][i] for i in  range(n) ] for b in B]
    current = [None for b in B]
    
			        
    
    def existeLibreA(): return len(libresA) > 0
    def estLibreB(b): return current[b] == None
    def engage(a, b): current[b] = a
    def partenaireA(b): return current[b]
    def isPreferredByB(aa, a, b): return ranking[b][aa] < ranking[b][a]
    def rendreLibreA(a): libresA.append(a)
    
    def getElementPrefereeNonPropose(a):
        b = APref[a][Next[a]]
        Next[a] = Next[a] + 1
        return b
	
    while(existeLibreA()):
        a = libresA.pop()
        b = getElementPrefereeNonPropose(a)
		
        if estLibreB(b):
            engage(a,b)
        else:
            aa = partenaireA(b)
            if isPreferredByB(a, aa, b):
                engage(a,b)
                rendreLibreA(aa)
            else:
                rendreLibreA(a)
                
    return current





