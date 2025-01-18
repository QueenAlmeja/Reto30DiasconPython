#Diccionarios
"""
Los diccionarios son colecciones de elementos desordenados, que pueden modificarse
y que poseen una esquema de clave-valor. 
Se declaran empleando {} 
"""

#Ejercicios:

#1. Crea un diccionario vacio llamado dog
print("Ejercicio 1")
dog = {}
print(f"Hemos declarado un diccionario vacio llamado dog {dog}")

#2.Añade al diccionario el nombre del perro, color, raza, cantidad de patas, y edad
print("\nEjercicio 2")
dog['nombre'] = 'Canela'
dog['raza'] = 'Criolla'
dog['patas'] = 4
dog['color'] = ("Negro", "Blanco")
dog['edad'] = 11
dog['pronombres'] = ['Pulga malvada', 'Canela de la maldad', 'Perro malandro', 'Nalga Peluda']
print(f"Nuestro diccionario ahora tiene los siguientes valores: {dog}")

#3. Crea un diccionario donde llamado estudiante donde almacene diferentes datos de la persona
print("\nEjercicio 3")
estudiante = {'Nombre': 'Gabriela', 
              'Apellido':'Sanchez',
              'Genero':'Mujer',
              'Edad':'28',
              'Estado_Civil':'Soltera',
              'Habilidades':['escritura', 'redaccion', 'analisis', 'investigacion'],
              'Pais':'Venezuela',
              'Ciudad':'Caracas',
              'Direccion': {'Avenida':'Panteon', 'Calle':'34','Edificio':'El Avila',},}
print(f"El diccionario del estudiante contiene la siguiente informacion\n{estudiante}")

#4. Obten el largo del diccionario declarado anteriormente
print("\nEjercicio 4")
print(f"El diccionario estudiante contiene la siguiente cantidad de elementos clave-valor {len(estudiante)}")

#5. Obten el valor de la clave habilidades y determina el tipo de dato amacenado alli
print("\nEjercicio 5")
valores = estudiante.get('Habilidades')
print(f"Los valores almacenados en el clave habilidades es {valores}")
tipo_dato = type(estudiante.get('Habilidades'))
print(f"El tipo de datos almacenados en esa clave es {tipo_dato}")

#6.Modifique la lista de habilidades agregando una o mas habilidades
print("\nEjercicio 6")
estudiante['Habilidades'].append('lectura')
estudiante['Habilidades'].append('comprension lectora')
print(f"Los nuevos valores almacenados en el clave habilidades son: {valores}")

#7. Obten los valores de la clave en formato de lista de los dos dicciones declarados
print("\nEjercicio 7")
dict1 = dog.keys()
print(f"Los valores claves del diccionario dog son: {dict1}")
dict2 = estudiante.keys()
print(f"Los valores claves del diccionario estudiante son: {dict2}")

#8. Obten los elementos que constituyen los valores de cada dicionario
print("\nEjercicio 8")
dict3 = dog.values()
print(f"Los valores del diccionario dog son: {dict3}")
dict4 = estudiante.values()
print(f"Los valores del diccionario estudiante son: {dict4}")

#.9 Cambie los diccionario a una lista del tipo tupla usando la función items()
print("\nEjercicio 9")
print(f"El tipo de dato de la variable dog originalmente es: {type(dog)}")
print(f"El tipo de dato de la variable estudiante originalmente es: {type(estudiante)}")
print("Hemos modificando los diccionarios usando la función items()\n")
print(f"Ahora dog es una variable del tipo {type(dog.items())}")
print(f"Ahora estudiante es una variable del tipo {type(estudiante.items())}")

#. 10 elimine uno de los elementos de cada diccionario 
print("\nEjercicio 10")
del dog['color']
del estudiante['Direccion']
print(f"Los diccionarios ahora son: dog = {dog}\nestudiante = {estudiante}")

#. 11 elimine una de los diccionarios
del estudiante
#usamos la funcion print() para ver si el diccionario se ha eliminado correctamente
print(estudiante)
