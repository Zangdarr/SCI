##Alexandre Verkyndt


#SCI_Particules  
**Simulation Centrée Indidus**


Ce projet consiste en la réalisation d'un simulateur du comportement de particules entre elles au sein d'une grille deux dimensions.

###Commande de lancement :

*python3 Simulation.py*

###Librairie necessaire
*tkinter* : librairie graphique pour python

###Parametrage

Au sein de fichier **Simulation.py** se trouve un jeu de parametres personnalisables. 
J'ai trouvé cela plus pratique pour la prise en main plutot qu'une ligne de commande a rallonge vu qu'il y a 7 parametres.

- type_environnement        : "th" pour thorique, n'importe quelle autre chaine sinon
- dimension_x               : taille de la grille en x (attention, lire section *Representation cellule*)
- dimension_y               : taille de la grille en y (attention, lire section *Representation cellule*)
- nombre_agents             : nombre d'agents au sein de la grille
- facteur_taille_particules : lire section *Representation cellule*
- nombre_de_tics            : nombre d'iterations
- sleep_time                : temps entre deux iterations

###Fonctionnalites implementees

- grille thorique ou non
- taille de grille variable sur les deux axes
- nombre d'agents dans la grille
- representation de la particule dans la grille (voir section *Representation*)
- nombre d'iterations
- temps entre chaque iteration
- collision entre les agents (voir section *Gestion des collisions*)
- collision avec les murs (voir section *Gestion des collisions*

###Gestion des collisions

Lorsque un agent entre en collision avec un mur ou un autre agent, il multiple par *-1* son *pas de x* et *pas de y*. Il inverse donc sa trajectoire.

###Representation de la particule

La particule est un cercle de 1 pixel (code en dur). Chaque case de la grille fait donc par defaut 1 pixel. 
Cependant une fonctionnalite permettant de faire varier le nombre de pixel a ete implementee. Le parametre *facteur_taille_particules* augmente la taille de base d'une particule (1 pixel) suivant cette formule : taille_de_base * facteur_taille_particule. 
**IMPORTANT:** Les dimensions de la grille subit aussi le facteur multiplicateur.
**PS:** si le facteur prend une valeur nulle, la valeur par defaut est utilisee.
