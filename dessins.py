import turtle

"""
 entrée : un nombre taille
 sortie : dessine un carré de taille taille et remet la tortue dans la
          position initiale
"""
def carre(taille):
    turtle.forward(taille)
    turtle.left(90)
    turtle.forward(taille)
    turtle.left(90)
    turtle.forward(taille)
    turtle.left(90)
    turtle.forward(taille)
    turtle.left(90)
    
    
    
"""
 entrée : un nombre taille
 sortie : dessine un triangle équilatéral de taille taille
          et remet la tortue dans la position initiale
"""
def triangleEquilateral(taille):
    turtle.forward(taille)
    turtle.left(120)
    turtle.forward(taille)
    turtle.left(120)
    turtle.forward(taille)
    turtle.left(120)
   
"""
    entrée : un nombre taille Carreau, un entier nbCases
    sortie : dessine une grille de type nbCases X nbCases où chaque case
             est de taille 
"""
def grille(tailleCase, nbCases):
    for y in range(nbCases):
        for x in range(nbCases):
            carre(tailleCase)
            turtle.forward(tailleCase)
        turtle.left(180)
        turtle.forward(nbCases*tailleCase)
        turtle.right(90)
        turtle.forward(tailleCase)
        turtle.right(90)
        