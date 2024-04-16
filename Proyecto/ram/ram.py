class Ram:
 #metodo contructor  
    def __init__(self, modelo, velocidad, capacidad, stock):
        self.modelo = modelo
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.stock = stock

 #metodos accesadores     
    def get_modelo(self):
        return self.modelo
    
    def get_velocidad(self):
        return self.velocidad
    
    def get_capacidad(self):
        return self.capacidad
    
    def get_stock(self):
        return self.stock
    
 #metodos mutadores
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def set_velocidad(self, nuevo_velocidad):
        self.velocidad = nuevo_velocidad

    def set_capacidad(self, nuevo_capacidad):
        self.capacidad = nuevo_capacidad

    def set_stock(self, nuevo_stock):
        self.stock = nuevo_stock

     #metodo de impresion de la clase
    def __str__(self):
        return f"Modelo: {self.modelo}, Velocidad:{self.velocidad}, Capacidad:{self.capacidad}, Stock:{self.stock}"