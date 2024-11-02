from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
class Game(ShowBase):
  def __init__(self):
      ShowBase.__init__(self)
      self.land = MapManager()
      for x in range(0,11):
         for y in range(0,11):
            self.land.addBlock((x, y, 0))
      # self.land.addBlock((1,10,0))
      base.camLens.setFov(120)
game = Game()
game.run()