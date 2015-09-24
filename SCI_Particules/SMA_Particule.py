import sys
sys.path.insert(0,"../base/")
import random

from Agent_Particule import Agent_Particule
from View import View_Particule
from SMA import SMA_Base



class SMA_Particule(SMA_Base):


  def addAgents(self, nb_agents):
     self.nb_agents = nb_agents
     for i in range(nb_agents):
        while(True):
          pos_x = random.SystemRandom().randint(0,self.envi.tx-1)
          pos_y = random.SystemRandom().randint(0,self.envi.ty-1)

          if(self.envi.estAccessible(pos_x,pos_y)):
             break
        while(True):
          pas_x = random.SystemRandom().randint(0,2) - 1
          pas_y = random.SystemRandom().randint(0,2) - 1
          if(pas_x != 0 or pas_y != 0):
             break
        self.list_agent.append(Agent_Particule(i,self.envi,pos_x,pos_y,pas_x,pas_y))
        self.ordonnancement_agent.append(i)
        self.envi.setPos(pos_x,pos_y, i)


  def addView(self, facteur_taille=1):
     self.list_vue.append(View_Particule(self.envi.tx, self.envi.ty, self.list_agent, facteur_taille))
     return 0






