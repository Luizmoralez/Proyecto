class Fuente_de_poder:
 #metodo constructor 
    def __init__(self, modelo, potencia, stock, tipo):
        self.modelo = modelo
        self.potencia = potencia
        self.stock = stock
        self.tipo = tipo 
   
 #metodos accesadores
    def get_modelo(self):
        return self.modelo
    
    def get_potencia(self):
        return self.potencia
    
    def get_stock(self):
        return self.stock
    
    def get_tipo(self):
        return self.tipo 
    
 #metodos mutadores
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def set_potencia(self, nuevo_potencia):
        self.potencia = nuevo_potencia

    def set_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    def set_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo 
    
 #metodo de impresion de la clase
    def __str__(self):
        return f"Modelo: {self.modelo}, Potencia:{self.potencia}, Stock:{self.stock}, Tipo:{self.tipo}"    
   

   