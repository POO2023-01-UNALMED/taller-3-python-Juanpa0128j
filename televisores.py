class TV():
    marca = None 
    control = None 
    canal = 1
    precio = 500 
    volumen = 1
    estado = False
    numTV = 0
    
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.numTV += 1

    def canalUp(self):
        if self.estado == True and self.canal < 120:
            self.canal += 1

    def canalDown(self):
       if self.estado == True and self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.estado == True and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado == True and self.volumen > 0:
            self.volumen -= 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    @staticmethod
    def getNumTV():
        return TV.numTV

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getControl(self):
        return self.control
    
    def setControl(self, control):
        self.control = control

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        if self.estado == True and 0 < volumen < 7:
            self.volumen = volumen

    def getCanal(self):
        return self.canal
    
    def setCanal(self, canal):
        if self.estado == True and 1 < canal < 120:
            self.canal = canal

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

class Marca():
    nombre = ""
    
    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre