import sys
sys.path.insert(0,'../base/')
from Agent import Agent_Base

class Agent_Particule(Agent_Base):

  def collisionReation(self):
    self.pas_x = self.pas_x * (-1)
    self.pas_y = self.pas_y * (-1)
    return 0

  def decide(self):
    next_x = self.pos_x + self.pas_x
    next_y = self.pos_y + self.pas_y
    estAccessible = self.envi.estAccessible(next_x, next_y)

    if(estAccessible):
      self.envi.moveAgent(self, next_x, next_y)
    else:
      self.collisionReation()
