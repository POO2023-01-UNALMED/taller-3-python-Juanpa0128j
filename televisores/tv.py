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
        TV.numTV += 1

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
    
    @staticmethod
    def setNumTV(numTV):
        TV.numTV = numTV

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
        if self.estado == True and 0 <= volumen <= 7:
            self.volumen = volumen

    def getCanal(self):
        return self.canal
    
    def setCanal(self, canal):
        if self.estado == True and 1 <= canal <= 120:
            self.canal = canal