import SMA_Particule

#Voir section "Representation de la cellule" et *Parametre* dans le README.md avant de jouer avec les parametres ;) #
#--PARAMETRES----------------------------------------------------------------------
type_environnement        = ""     # "th" or ""
dimension_x               = 1600    #1600, 400, 150, 160, 400
dimension_y               = 800    # 800, 400, 150,  80, 400
nombre_agents             = 2000   # 200,  50,  20, for fun : dimension_x*dimension_y
facteur_taille_particules = 1      #   1,   5,  10, 10
nombre_de_tics            = 10000
sleep_time                = 0.01     #en sec
#----------------------------------------------------------------------------------
#Voir section "Representation de la cellule" et *Parametre* dans le README.md avant de jouer avec les parametres ;) #





print("start")
sma = SMA_Particule.SMA_Particule(type_environnement,dimension_x,dimension_y)
print("sma OK")
sma.addAgents(nombre_agents)
print("agents OK")
sma.addView(facteur_taille_particules)
print("view OK")
sma.run(nombre_de_tics,sleep_time)
print("run DONE")
