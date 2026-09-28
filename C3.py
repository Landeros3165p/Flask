Nums = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]

color = ["rojo", "verde", "azul", "amarillo", "morado", "naranja", "rosa", "negro", "blanco", "gris"]

colors = []
#print(Nums)
#color.append("violeta") sirve para agregar un valor al final
#color.extend(["violeta", "gris"]) agregar mas de un valor al final
#color.insert(0, "violeta") recuperar y extraer posiciones de colores
#colors.clear() borra todos los elementos de la lista
#print(color.pop()) elegir uno 
#print(color.sort(reverse=False)) 
#print(Nums.sort(reverse=True))
#print(color.sort(reverse=False)) ordena por abc
#colors_1 = color.copy() realizar copia superficial
#print(colors_1)
#la  f sirve para concatenar variables
"""for num in Nums:
    salida=f"[{num},{color[num.index(num)]}]"  
    print (salida)
    """

#metodo append agrega un solo elemento al final de la lista

for num in Nums:


    salida=f"[{num},{color[Nums.index(num)]}]"  
    colors.append(salida)
    

    colors.reverse() 
print (colors)
