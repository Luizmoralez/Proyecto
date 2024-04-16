#importar la clase al main
from procesador import Procesador

#definir los atributos de procesador
objeto02 = Procesador("i5-12400F", "4.4GHz", "22")

#metodo para editar el stock de un procesador
objeto02.set_stock (20) # "( se ingresa el valor a modificar)"

#print para ver los cambios hechos en el atributo "stock"
print(objeto02)
