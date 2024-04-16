class Procesador:
 #metodo constructor
    def __init__(self, modelo, frecuencia, stock):
        self.modelo = modelo
        self.frecuencia = frecuencia
        self.stock = stock

 #metodos accesadores
    def get_modelo(self):
        return self.modelo
    
    def get_frecuencia(self):
        return self.frecuencia
    
    def get_stock(self):
        return self.stock
    
 #metodos mutadores
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def set_frecuencia(self, nuevo_frecuencia):
        self.frecuencia = nuevo_frecuencia

    def set_stock(self, nuevo_stock):
        self.stock = nuevo_stock

 #metodo de impresion de la clase
    def __str__(self):
        return f"Modelo: {self.modelo}, Frecuencia:{self.frecuencia}, Stock:{self.stock}"

   