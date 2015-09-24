
"""
  Grille contenant les indices des différents agents qui devront etre contenu
"""
class Environnement_Base:
  
  CASE_VIDE = -1

  def __init__(self, taille_x, taille_y):
     self.espace = [[-1 for i in range(taille_y)] for j in range(taille_x)]
     self.tx = taille_x
     self.ty = taille_y

  def setPos(self,pos_x, pos_y, id_agent):
     self.espace[pos_x][pos_y] = id_agent  

  def printSelf(self):
    result = []
    print("Affichage de l'environnement : ")
      
    for i in range(self.ty):
      for j in range(self.tx):
        tmp_value = self.espace[j][i]
        value = "-" if tmp_value == -1 else tmp_value 
        
        result.append(str(value))
        result.append(" ")
      result.append("\n")                      

    result = ''.join(result)
    print(result)
    return 0
  
"""
  Grille a bords fermes
"""
class Environnement_Classique(Environnement_Base):

  def estAccessible(self,pos_x,pos_y):
     pos_OK = pos_x >= 0 and pos_y >= 0 and pos_x < self.tx and pos_y < self.ty
     
     return (pos_OK and self.espace[pos_x][pos_y] == -1)
       

  def moveAgent(self, agent, next_x, next_y):
     self.setPos(agent.pos_x,agent.pos_y, self.CASE_VIDE)
     self.setPos(next_x, next_y, agent.id_agent)
     agent.setPos(next_x,next_y)


"""
  Grille thorique
"""
class Environnement_Thorique(Environnement_Base):
   
  def estAccessible(self,pos_x,pos_y):
     true_x = pos_x % self.tx
     true_y = pos_y % self.ty
     return self.espace[true_x][true_y] == -1


  def moveAgent(self, agent, next_x, next_y):
     true_x = next_x % self.tx
     true_y = next_y % self.ty
     self.setPos(agent.pos_x,agent.pos_y, self.CASE_VIDE)
     self.setPos(true_x, true_y, agent.id_agent)
     agent.setPos(true_x,true_y)


#----------------------------------------------------------------

  
