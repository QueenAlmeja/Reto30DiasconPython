#Tuplas
"""
Las tuplas tambien pueden almacenar una serie de diferentes tipos de datos, pero a diferencia
de las listas, estas NO PUEDEN MODIFICARSE, por lo tanto, con las tuplas no se pueden emplear
metodos de insercion, agregar o remover elementos.
"""

#Ejercicios Nivel 1

#1. Crea una tupla vacia
print("Ejercicio 1")
tupla_vacia = ()
print(f"Esta es una tupla vacia {tupla_vacia}")

#2. Crea una tupla que contenga tu nombre y el nombre tus hermanos o  familiares
print("\nEjercicio 2")
familia_tuple = ("Alejandra", "Laura", "Gabriela", "Canela", "Patricia", "Mayela")
print(f"La nueva tupla contiene los siguientes nombres {familia_tuple}")

#3. Crea dos tuplas donde almacenes el nombre de tus hermanas y hermanos o usa el nombre de tus amigas y amigos
print("\nEjercicio 3")
mujeres = ("Yessica", "Danelys", "Marirene", "Valeria", "Mariangel")
print(f"Los nombres de algunas de mis amigas son: {mujeres}")
hombres = ("J", "Andres", "Victor", "Jose", "Carlos", "Khaleel")
print(f"Los nombres de algunos de mis amigos son: {hombres}")
#Une las dos tuplas en una sola
all_friends = mujeres + hombres
print(f"\nMis amigos son: {all_friends}")

#4. Cuantos amigos tienes?
print("\nEjercicio 4")
print(f"Tengo {len(all_friends)} amigos")

#5. Modifica la lista de amigos y agrega dos nombres
print("\nEjercicio 5") 
all_friends2 = list(all_friends) #modifico la tupla a una lista para agregar
all_friends2.append("Maria de los Angeles")
all_friends2.append("Luis")
all_friends = tuple(all_friends2) #vuelvo a convertir la lista en una tupla
print(f"Mi nueva lista de amigos es: {all_friends}")

#Ejercicios Nivel 2
#1. Desempaca los elementos almacenados en la tupla all_friends
print("Ejercicios del nivel 1")
print("\nEjercicio 1")
a,b,c,d,e,f,g,h,i,j,k,l,m = all_friends
print("Hemos desempacados los nombres almacenados en la tupla all_friends")
print(a, b)
print(c, d)
print(e, f)
print(g, h)
print(i,j)
print(k,l, m)

#2. Crea tres tuplas que contengan nombres de frutas, vegetales y animales y unelas, creando una sola tupla
print("\nEjercicio 2")
fruta = ("parchita", "cambur", "guayaba", "lechoza")
print(f"Esta tupla contiene frutas {fruta}")
vegetales = ("papa", "zanahoria", "apio", "cebolla",)
print(f"Esta tupla contiene vegetales {vegetales}")
animales = ("zamuros", "guacamayas", "leones", "perritos")
print(f"Esta tupla contiene animales {animales}")
food_stuff_tp = fruta + vegetales + animales
print(f"En esta tupla hemos guardado la informacion de las tres tuplas anteriores{food_stuff_tp}")

#3. Convierta la tupla food_stuff_tp en lista y compruebe con la funcion type() que la variable se ha modificado 
print("\nEjercicio 3")
food_stuff_list = list(food_stuff_tp)
print(f"La variable donde se almacenan los item de la tupla anterior originalmente es del tipo {type(food_stuff_tp)}")
print(f"Hemos modificado el tipo de dato donde se almacenan los items de la tupla anterior ahora el dato es del tipo {type(food_stuff_list)}")

#4. Extraiga los elementos que se ubican en los valores de indice que estan en el medio de la tupla o lista
#Como estamos trabajando con tuplas, hare el slicing con la tupla
print("\nEjercicio 4")
print(f"La tupla tiene: {len(food_stuff_tp)} elementos y la mitad de los elementos esta en : {len(food_stuff_tp)//2} ")
mitad_elementos = food_stuff_tp[5:9]
print(f"Los elementos que estan en la mitad de la tupla son: {mitad_elementos}")

#5. Extraiga los tres primeros y los tres ultimos elementos de la tupla 
print("\nEjercicio 5")
primeros_tres = food_stuff_tp[:3]
print(f"Los tres primeros elementos de la tupla son {primeros_tres}")
ultimos_tres = food_stuff_tp[-3:]
print(f"Los tres utlimos elementos de la tupla son {ultimos_tres}")

#6. Elimini la tupla empleando la funcion del y compruebe que se ha eliminado correctamente
print("\nEjercicio 6")
"""
del food_stuff_tp #elimino
print(food_stuff_tp) #compruebo 
"""

#7. Se tiene una tupla de los paises nordicos. Comprueba si Estonia y Iceland forman parte de los elementos
print("\nEjercicio 7")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Hemos declarado una tupla que contiene los nombres de los siguientes paises {nordic_countries}")
print(f"Estonia esta en la tupla de paises: {("Estonia" in nordic_countries)}")
print(f"Iceland esta en la tupla de paises: {("Iceland" in nordic_countries)}")
