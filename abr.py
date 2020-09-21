#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:53:13 2020

@author: fschwarz
"""

from binarytree import Node

"""
 entrée : un ABR A et une valeur x
 sortie : vrai si x est dans l'ABR
"""
def abrAppartient(A, x):
    if A == None: return False
            
    if A.val == x: return True
    if x < A.val:
        return abrAppartient(A.left, x)
    else:
        return abrAppartient(A.right, x)
        
    
    
    
"""
 entrée : un ABR A et une valeur x
 sortie : un nouvel ABR contenant les même valeurs et x en plus
 exemple : print(abrAjouter(abrAjouter(None, 3), 1))
           print(abrAjouter(abrAjouter(abrAjouter(None, 3), 1), 2))
           print(abrAjouter(abrAjouter(abrAjouter(abrAjouter(None, 3), 1), 2), 5))
"""
def abrAjouter(A, x):
    if A == None: return Node(x, None, None)
            
    if A.val == x: return A
    if x < A.val:
        return Node(A.val, abrAjouter(A.left, x), A.right)
    else:
        return Node(A.val, A.left,  abrAjouter(A.right, x))
        
    
    
"""
 entrée : un ABR A non vide
 sortie : l'arbre dans lequel le maximum est supprimé, ce maximum
"""
def abrSupprimerMax(A):
    if A.right == None:
        return A.left, A.val
    else:
        B, maximum = abrSupprimerMax(A.right)
        return Node(A.val, A.left, B), maximum
    
    
"""
 entrée : un ABR A, une valeur x
 sortie : un ABR contenant les même valeurs mais sans x
"""
def abrSupprimer(A, x):
    if A == None: return None
    
    if A.val == x:
        if A.left == None:
            return A.right
        else:
            B, maximum = abrSupprimerMax(A.left)
            return Node(maximum, B, A.right)
    elif x < A.val:
        return Node(A.val, abrSupprimer(A.left, x), A.right)
    else:
        return Node(A.val,  A.left,  abrSupprimer(A.right, x))
    
    
    
    
"""
classe qui représente un ensemble (type abstrait) implémenté avec la structure
de données ABR

exemple : 
E = EnsembleParABR()
E.ajouter(3)
E.ajouter(1)
E.ajouter(5)
E.appartient(3)
E.supprimer(3)
E.appartient(3)
E.appartient(1)
"""
class EnsembleParABR:
    
    """
    initialise un ensemble vide
    """
    def  __init__(self):
        self.arbre = None
        
    """
    entrée : x
    sortie : oui si x est dans l'ensemble
    """
    def appartient(self, x):
        return abrAppartient(self.arbre, x) 
    
    """
    entrée : x
    sortie : ajoute x à l'ensemble
    """
    def ajouter(self, x):
        self.arbre = abrAjouter(self.arbre, x)
        
    """
    entrée : x
    sortie : supprimer x de l'ensemble (ne fait rien si x n'y est pas)
    """
    def supprimer(self, x):
        self.arbre = abrSupprimer(self.arbre, x)