# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:45:43 2020

@author: Adriana F. ; Margot V.
"""

from tkinter import *
from random import *


from pip import *
x_main=60 #en attente de la position de la main sur l'axe des absices
y_main=380 #en attente de la position de la main sur l'axe des ordonées
nb_poissons=0

def pecher(event):
    global x,y,dx,dy
    ferrer.config(text='férrer')
    can1.delete(ALL)
    x=event.x
    y=event.y
    poisson(x,y)
    dx,dy=(x - x_main)/(-100),(y - y_main)/(-100)
    poisson(x,y)

def poisson(x,y):
        can1.delete(ALL)
        can1.create_line(x_main,y_main,x,y)
        can1.create_polygon((105+x, 5+y),(105+x, -35+y),(145+x, 5+y), width=2,outline='black',fill='grey')
        can1.create_arc(0+x,-45+y,110+x,45+y, extent=180, start=180, width=2,outline='black',fill='grey')
        can1.create_arc(100+x,35+y,50+x,-35+y, extent=90, start=90, width=2,outline='black',fill='grey')
        can1.create_oval(17+x,7+y,25+x,15+y, width=2,outline='white',fill='white')
        can1.create_oval(19+x,9+y,22+x,13+y, width=2,outline='black',fill='black')
        can1.create_arc(11+x,15+y,40+x,36+y, width=2, extent=90, start=180, outline='black')


def remonter():
    global nb_poissons
    if ferrer.cget('text')=='férrer':
        chaine.config(text=nb_poissons+1)
        nb_poissons+=1
        depl()
    ferrer.config(text='vérouillé')


def depl():
    global x,y,dx,dy
    if x<x_main-0.1 or x>x_main+0.1 :
        x=x+dx
        y=y+dy
        poisson(x,y)
        can1.after(10,depl)
    else :
        can1.delete(ALL)









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
    can1.coords(balle, x1, y1, x1+20, y1+10) #On modifie les coordonnées de la balle
    if x1 > 630 or x1 < 10 or y1 > 630 or y1 < 10: #Si la balle se trouve à moins de 10px des bords
        flag = 0 #Flag est passé à 0
        recharger()
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
    if flag>0:  #Si l'objet est toujours en mouvement
        fen1.after(50, tirer) #On rappelle la fonction tirer au bout de 50ms

def recharger():
    """
    Cette fonction est appellée lorsque la balle atteint un bord.
    Cette fonction permet de recharger le pistolet en remettant la balle à ses coordonnées initiales.
    """
    global x1, y1, dx, dy
    can1.coords(balle, 50, 50, 70, 60) #On remet la balle à ses coordonnées initiales
    x1,y1 = 50,50 #On remet x1 et y1 à leurs valeurs initiales
    dx = randint(-10,10) #Pareil pour dx
    dy = randint(-10,10) #et dy
    coul = ['blue','yellow','red','black','dark grey'] #On créé une liste avec les couleurs possibles pour la balle
    couleur = choice(coul) #On choisit une couleur aléatoire pour la balle
    can1.itemconfig(balle, fill=couleur) #On met à jour la couleur de la balle
    #print(f'Après reload ::: x1:{x1} ; y1:{y1} ; dx:{dx} ; dy:{dy}')
        
    
#Création du widget principal
fen1=Tk()
fen1.title("Pirate")

#Création des widgets annexes
can1=Canvas(fen1, bg='dark grey', height=640, width=640)
can1.pack(side=LEFT, padx=5, pady=5)

x1,y1 = 50,50
flag = 0
dx = randint(-10,10)
dy = randint(-10,10)
coul = ['blue','yellow','red','black','dark grey'] #On créé une liste avec les couleurs possibles pour la balle
couleur = choice(coul) #On choisit une couleur aléatoire pour la balle
pistolet = can1.create_oval(x1,y1,x1+50,y1+50, width=2,fill='yellow')
balle = can1.create_oval(x1,y1,x1+20,y1+10, width=2,fill=couleur)

bou1 = Button(fen1, text='Quitter', width = 8, command=fen1.quit)
bou1.pack(side=BOTTOM)

bou2 = Button(fen1, text='Tirer', width = 8, command=tirer)
bou2.pack()

#démarrage du programme principal : construction de la fenêtre et des widgets
can1.bind('<Button-1>', pecher)
#un clic de souris sur le canevas va déclencher l'appel à cette fonction
can1.pack()
etiquette=Label(fen1, text='nb_poissons').pack(side=TOP)
ferrer=Button(fen1, text='vérouillé', command=remonter)
ferrer.pack(side=RIGHT)
chaine = Label(fen1,text='0')
chaine.pack(side=TOP)
#Démarrage du réceptionnaire d'évènements
fen1.mainloop()

#Quand la commande fen1.quit() sera appelée, le programme arrivera ici :
fen1.destroy()