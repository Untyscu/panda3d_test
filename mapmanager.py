class MapManager():
    def __init__(self):
        self.land = render.attachNewNode("Land")
        self.model = 'block.egg' # модель кубика у файлі block.egg
        self.texture = 'block.png'# текстура куба
        self.color = (0.2, 0.2, 0.35, 1) #rgba
        self.addBlock((0,10, 0))
    def startNew(self):
        self.land = render.attachNewNode("Land")
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture)) 
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
