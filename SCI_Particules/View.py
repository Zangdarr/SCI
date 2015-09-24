import tkinter
import random



class View_Particule:
  
  diametre = 1

  def genColor(self, nb_color):
     tab_color = ["#000000" for i in range(nb_color)]
     r = lambda: random.randint(0,255)

     for i in range(nb_color):
        tab_color[i] = '#%02X%02X%02X' % (r(),r(),r())

     return tab_color


  def __init__(self, w, h, list_agent,facteur_taille=1):
    self.top = tkinter.Tk()
    self.top.title("Particules")
    self.width = w
    self.height = h
    self.facteur_taille = facteur_taille if(facteur_taille != 0) else 1
    self.dia = self.facteur_taille * self.diametre
    self.canvas = tkinter.Canvas(self.top, bg="white", height=h*self.dia, width=w*self.dia)
    self.list_agent = list_agent
    self.nb_particules = len(self.list_agent)
    self.color_agent = self.genColor(self.nb_particules)
    self.particules = []
    for i in range(self.nb_particules):
       coord_x = self.list_agent[i].pos_x
       coord_y = self.list_agent[i].pos_y
        
       coord = coord_x*self.dia, coord_y*self.dia,coord_x*self.dia + self.dia, coord_y*self.dia+self.dia
       self.particules.append(self.canvas.create_oval(coord, fill=self.color_agent[i]))
    self.canvas.pack()


  def update(self):
    self.canvas.delete("all")
    for i in range(self.nb_particules):
       coord_x = self.list_agent[i].pos_x
       coord_y = self.list_agent[i].pos_y
        
       coord = coord_x*self.dia, coord_y*self.dia,coord_x*self.dia + self.dia, coord_y*self.dia+self.dia
       self.particules.append(self.canvas.create_oval(coord, fill=self.color_agent[i]))
    self.canvas.update_idletasks()
      


