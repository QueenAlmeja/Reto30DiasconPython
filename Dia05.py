#Listas 
print("Lista, coleccion de elementos ordenados que pueden tener datos repetidos y pueden modificarse\n")
#Ejercicios Nivel 1

#1. Declara una lista que este vacia
print("Ejercicio 1")
lista1 = []
print(f"Hemos declarado una lista vacia en la variable lista1: {lista1}")

#2. Declara una lista que contenga 5 elementos y determina el largo de la lista empleando len()
print("\nEjercicio 2")
lista2 = ["Palabra", "Patacon", 456, True, 9.8, {"Nombre":"Pandora"}]
print(f"Hemos creado una nueva lista: {lista2} el largo de esta lista es de {len(lista2)} elementos")

#3. Usa el metodo slicing para obtener el primer elemento, elemento del medio y el ultimo
print("\nEjercicio 3")
print(f"El primer elemento es {lista2[0]}")
print(f"El elemento del medio es {lista2[2]}")
print(f"El ultimo elemento es {lista2[-1]}")

#4. Declare una lista con dato mixtos en donde almacene su nombre, edad, estatura, estado civil y direccion
print("\nEjercicio 4")
lista_mixta = ["Alejandra", 30, 1.66, {"is_single": False}, "Venezuela"]
print(f"Esta es una lista con datos de diferentes tipos: {lista_mixta}")

#5. Declare una lista donde almacene el nombre de diferentes empresas y con la funcion len() determine el tamaño de la lista
print("\nEjercicio 5")
lista_empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f"Algunas de las empresas en mas conocidas en tecnologia son: {lista_empresas}")
print(f"La lista posee {len(lista_empresas)} elementos")

#6. Usando indexing, imprima en consola el nombre de la primera empresa, la que está en el medio y la última
print("\nEjercicio 6")
print(f"La primera empresa de la lista es: {lista_empresas[0]}")
print(f"La empresa que esta en mitad de lista es: {lista_empresas[3]}")
print(f"La ultima empresa de la lista es: {lista_empresas[-1]}")

#7. Usando la funcion replace() modifique uno de los nombres de la lista e imprima la nueva lista
print("\nEjercicio 7")
print(f"La lista original es: {lista_empresas}")
lista_empresas[3] = "LinkedIn"
print(f"La lista modificada es: {lista_empresas}")

#8. Añade un elemento a la lista
print("\nEjercicio 8")
lista_empresas.append("Apple")
print(f"La lista con un elemento agregado es: {lista_empresas}")

#9. Agregue un elemento a la lista en la mitad de la lista con la funcion insert()
print("\nEjercicio 9")
lista_empresas.insert(3, "Youtube")
print(f"La lista con un elemento agregado en la mitad es: {lista_empresas}")

#10. Cambie el nombre de un elemento de la lista y que el nuevo nombre sea mayuscula con la funcion uppercase
print("\nEjercicio 10")
print(f"Se ha modificado uno de los elemento de la lista con la funcion uppercase")
lista_empresas[4] = lista_empresas[4].upper()
print(f"La lista con un elemento modificado es: {lista_empresas}")

#11. Une el nombre de la empresas en la lista con el simbolo # usando la funcion join()
print("\nEjercicio 11")
nueva_lista = '# '.join(lista_empresas)
print(f"La lista modificada es: {nueva_lista}") 

#12. Verifica si el nombre de una empresa se encuentra dentro de la lista
print("\nEjercicio 12")
print(f"Verificamos si la empresa Google esta en la lista original: {"Google" in lista_empresas}" )
print(f"Verificamos si la empresa Kakaotalk esta en la lista original: {"Kakaotalk" in lista_empresas}" )

#13. Organiza la lista de elements usando la funcion sort()
print("\nEjercicio 13")
lista_empresas.sort()
print(f"Hemos organizado la lista de elementos en orden alfabetido, el resultado es: {lista_empresas}")

#14. Invierta el orden de los nombres de la lista usando la funcion reverse()
print("\nEjercicio 14")
lista_empresas.reverse()
print(f"Hemos invertido el orden la lista de elementos, el resultado es: {lista_empresas}")

#15. Usando los metodos de slicing, extraiga los nombres de las 3 empresas que estan al inicio, en el medio y al final
print("\nEjercicio 15")
print(f"El numero de elementos en la lista es de: {len(lista_empresas)}")
print(f"Los nombres de las tres primeras empresas son: {lista_empresas[0:3]}")
print(f"Los nombres de las tres empresas que estan en el medio son son: {lista_empresas[4:7]}")
print(f"Los nombres de las tres ultimas empresas son: {lista_empresas[-3:]}")

#16. Remueva el primer elemento, el elemento del medio y el ultimo elemento de la lista usando la funcion
print("\nEjercicio 16")
lista_empresas.pop(0)
print(f"Hemos removido el primer elemento de la lista con la funcion pop {lista_empresas}")
del lista_empresas[5]
print(f"Hemos removido el elemento que esta en la mitad de la lista con la funcion del {lista_empresas}")
lista_empresas.pop(-1)
print(f"Hemos removido el ultimo elemento de la lista con la funcion pop {lista_empresas}")

#17. Eliminemos todos los elementos de la lista con la funcion del
print("\nEjercicio 17")
del lista_empresas[:]
print(f"La lista tiene los siguientes elementos {lista_empresas}")

#18. Destruyamos la lista de empresas de la funcion del
print("\nEjercicio 18")
#del lista_empresas #asi destruimos la lista completamente y el output nos dira que la lista no esta declarada
#print(f"La lista tiene los siguientes elementos {lista_empresas}")

#19. Une los elementos de dos lista
print("\nEjercicio 19")
print(f"Hemos creados dos nuevas listas")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print(front_end)
back_end = ['Node','Express', 'MongoDB']
print(back_end)
full_list = front_end + back_end
print(f"Hemos unido las dos lista, creando una sola: {full_list}")

#Hgamos una copia de la lista para modificar y agregar elementos
print("\nEjercicio 20")
lista_copiada = full_list.copy()
print(lista_copiada)
#A la lista copiada agregaremos dos valores 
#Nota: Esta operacion no modifica la lista original, crea una nueva
lista_copiada.append('Python')
lista_copiada.append('Django')
print(f"La lista original sin modificar es: {full_list}")
print(f"La lista con los valores agregados es: {lista_copiada}")

#Ejercicios Nivel 2