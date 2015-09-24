

class Agent_Base:


  def __init__(self, id_agent, environnement, pos_x, pos_y, pas_x, pas_y):
    self.id_agent = id_agent
    self.envi = environnement
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.pas_x = pas_x
    self.pas_y = pas_y



  def setPos(self,pos_x,pos_y):
     self.pos_x = pos_x
     self.pos_y = pos_y

  def printSelf(self):
    result = []
    result.append("id_agent : ")
    result.append(str(self.id_agent))
    result.append(", pos_x : ")
    result.append(str(self.pos_x))
    result.append(", pos_y : ")
    result.append(str(self.pos_y))
    result.append(", pas_x : ")
    result.append(str(self.pas_x))
    result.append(", pas_y : ")
    result.append(str(self.pas_y))
    print(''.join(result))
    return 0
