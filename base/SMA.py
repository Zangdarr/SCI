import sys
sys.path.insert(0,"../base/")
import random
from time import sleep
from Environnement import Environnement_Classique
from Environnement import Environnement_Thorique



class SMA_Base:

  THORIQUE = "th"

  def __init__(self, type_env="", taille_x=100, taille_y=100):
    self.list_vue = []
    self.list_agent = []
    self.ordonnancement_agent = []
    self.nb_agents = 0
    if(type_env == self.THORIQUE):
      self.envi = Environnement_Thorique(taille_x,taille_y)
    else:
      self.envi = Environnement_Classique(taille_x,taille_y)



  def run(self,nb_tics, sleep_time):
     for k in range(nb_tics):
       random.shuffle(self.ordonnancement_agent)
       for i in range(self.nb_agents):
          id_agent = self.ordonnancement_agent[i]
          self.list_agent[id_agent].decide()


       for vue in self.list_vue:
           vue.update()
           print("update done(tic "+ str(k) + ")")
       sleep(sleep_time)

     return 0




