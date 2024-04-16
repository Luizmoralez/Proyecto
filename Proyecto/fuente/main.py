#importar la clase al main
from fuente_de_poder import Fuente_de_poder

#definir los atributos de fuente de poder
objeto01 = Fuente_de_poder("Evga 600w", "600 W", 53, "ATX")

#metodo para editar el stock de una fuente de poder 
objeto01.set_stock (43) # "( se ingresa el valor a modificar)"

#print para ver los cambios hechos en el atributo "stock"
print(objeto01)














