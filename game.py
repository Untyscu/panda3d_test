from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero
class Game(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.land = MapManager()
		with open("map.txt", "r") as map:
			for row in map:
				row_split = row.split(" ")
				tr = []
				for symbol in row_split:
					tr.append(int(symbol))
				self.land.addBlock(tuple(tr))
		with open("wall.txt", "r") as map:
			for row in map:
				row_split = row.split(" ")
				tr = []
				for symbol in row_split:
					tr.append(int(symbol))
				self.land.addBlock(tuple(tr))
		self.hero = Hero((2, 1, 1), self.land)
		base.camLens.setFov(90)
game = Game()
game.run()