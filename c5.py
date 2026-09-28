
""""
Mateo Lander Bustamante Rosales
Creacion de ciclo for 
Función que permita ingresar elementos a una lista dentro de un ciclo FOR.
"""
lista= ["nombre","apellido_p","apellido_p"]
def Funcion1(lista):
    for i in range(10):
        lista.append(i)
    print (lista)
    return lista

Funcion1(lista)




"""
Función que permita ingresar elementos a un diccionario dentro de un ciclo FOR.

"""
lista2={
"1":{}
}

def Funcion1(lista2):
    for i in range(10):
        lista2["new"]=(i)

    print (lista2)
    return (lista2)

Funcion1(lista2)


"""Función que permita imprimir todos los elementos de una lista y un diccionario dentro de un ciclo FOR."""
lista3 = {0: "l", 1: "b", 2: "c"}
lista4 = ["1", "2", "3"]
#creamos dos listas donde almacenamos nuesto diccionario y nuestra lista.

#definimos una funcion con el nombre funcion3 que nos sirve para agregar dos 
# variables que se igualaran al id de las listas creadas para evitar error 
#entonces lista = lista4, y diccionario=lista3
def Funcion3(lista, diccionario):
    #tenemos que crear una lista vacia en donde empujaremos todos esos valores de que queremos mostras 
    lista5 = []
    #este ciclo for nos sirve para poder empujar todos los valores de la lista dentro de nuesta variable "i"
    for i in lista:
        lista5.append(f"[{i},{diccionario[lista.index(i)]}]")

    
    print(lista5)
    return lista5
"""estamos seleccionando la lista donde introducimos nuestros valores por asignar le pones "." para concatenar "append"
#append nos sirve para empujar lo que este asigando a esa lisa 5
# "f" este lo usamos para decir que queremos traer lo que esta dentro de esa lista ya que si no solo se mostraria nuestro id
#  """

Funcion3(lista4, lista3)
