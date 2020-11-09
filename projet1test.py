# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:45:43 2020

@author: Adriana F. ; Margot V.
"""

from tkinter import *
import random



def tirer():
    """
    Cette fonction est appellée lorsque le bouton "Tirer" est pressé.
    Elle gère le mouvement de la balle.
    """
    global flag
    global x1, y1, dx, dy
    #print(f'Avant reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
    if flag==0: #On teste si l'objet est statique
        flag=1  #Si c'est le cas, on passe flag à 1
    x1, y1 = x1+dx, y1+dy #On ajoute les valeurs de dx et dy respectivement à x1 eet y1
    can1.coords(balle, x1, y1, x1+40, y1+25) #On modifie les coordonnées de la balle
    if x1 > 240 or x1 < 10 or y1 > 240 or y1 < 10: #Si la balle se trouve à moins de 10px des bords
        flag = 0 #Flag est passé à 0
        """
        can1.coords(balle, 50, 50, 90, 75)
        x1,y1 = 50,50
        dx = random.randint(-10,10)
        dy = random.randint(-10,10)
        coul = ['blue','yellow','red','black','dark grey']
        couleur = random.choice(coul)
        can1.itemconfig(balle, fill=couleur)
        """
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
    if flag>0:  #Si l'objet est toujours en mouvement
        fen1.after(50, tirer) #On rappelle la fonction tirer au bout de 50ms

def recharger():
    """
    Cette fonction est appellée lorsque le bouton "Recharger" est pressé.
    Cette fonction permet de recharger le pistolet en remettant la balle à ses coordonnées initiales.
    """
    global x1, y1, dx, dy
    can1.coords(balle, 50, 50, 90, 75) #On remet la balle à ses coordonnées initiales
    x1,y1 = 50,50 #On remet x1 et y1 à leurs valeurs initiales
    dx = random.randint(-10,10) #Pareil pour dx
    dy = random.randint(-10,10) #et dy
    coul = ['blue','yellow','red','black','dark grey'] #On créé une liste avec les couleurs possibles pour la balle
    couleur = random.choice(coul) #On choisit une couleur aléatoire pour la balle
    can1.itemconfig(balle, fill=couleur) #On met à jour la couleur de la balle
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
        
    
#Création du widget principal
fen1=Tk()
fen1.title("Pirate")

#Création des widgets annexes
can1=Canvas(fen1, bg='dark grey', height=250, width=250)
can1.pack(side=LEFT, padx=5, pady=5)

x1,y1 = 50,50
dx = random.randint(-10,10)
dy = random.randint(-10,10)
pistolet = can1.create_oval(x1,y1,x1+50,y1+50, width=2,fill='yellow')
balle = can1.create_oval(x1,y1,x1+40,y1+25, width=2,fill=couleur)

bou1 = Button(fen1, text='Quitter', width = 8, command=fen1.quit)
bou1.pack(side=BOTTOM)

bou2 = Button(fen1, text='Recharger', width = 8, command=recharger)
bou2.pack()

bou2 = Button(fen1, text='Tirer', width = 8, command=tirer)
bou2.pack()


#Démarrage du réceptionnaire d'évènements
fen1.mainloop()

#Quand la commande fen1.quit() sera appelée, le programme arrivera ici :
fen1.destroy()