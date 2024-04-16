#importar la clase al main
from ram import Ram

#definir los atributos de ram
objeto03 = Ram("Crucial", "3200MHz", "8 GB", 60)

#metodo set para editar el stock de una ram
objeto03.set_stock (20) # "( se ingresa el valor a modificar)"

#print para ver los cambios hechos en el atributo "stock"
print(objeto03)