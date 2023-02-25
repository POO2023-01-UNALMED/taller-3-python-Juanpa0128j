class Control():
    tv = None

    def enlazar(self, tv):
        tv.control = self
        self.tv = tv

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
       self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()
    
    def setCanal(self, canal):
        self.tv.setCanal(canal)

    def getTV(self):
        return self.tv
    
    def setTV(self, tv):
        self.tv = tv