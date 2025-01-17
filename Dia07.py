#Set : Ejercicios Nivel 1

#1. Declare una variable donde almacene el nombre de varias empresas en formato set y determine el largo del conjunto
print("Ejercicio 1")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(f"La lista original es: {it_companies}")
print(f"La cantidad de items almacenados en la variable it_companies es: {len(it_companies)}")

#2. Agrega el nombre de Twitter a la variable it_companies
print("\nEjercicio 2")
it_companies.add("Twitter")
print(f"La lista actualizada es: {it_companies}")

#3. Agregue varios nombre de empresa al conjunto de la variable it_companies
print("\nEjercicio 3")
it_companies.update(["Youtube", "ASUS", "Dell", "HP"])
print(f"La el nuevo conjunto de empresas es: {it_companies}, la nueva lista tiene {len(it_companies)} items")

#4. Remueve un elemento del conjunto y compruebe que la palabra ya no forma parte del conjunto
print("\nEjercicio 4")
it_companies.remove("Twitter")
print(f"Se ha eliminado el nombre de Twitter del conjunto declarado {it_companies}")
print(f"Twitter forma parte del conjunto: {("Twitter" in it_companies)}") #forma de comprobar
it_companies.discard("Youtube")
print(f"Se ha eliminado el nombre de Youtube del conjunto declarado {it_companies}")
print(f"Youtube forma parte del conjunto: {("Youtube" in it_companies)}")

#5.Cual es la diferencia entre usar la funcion remove y discard 
print("\nEjercicio 5")
print(f"La funcion remove() puede arrojar un error si el elemento no se encuentra en el conjunto")
print(f"La funcion discar() no genera el error")
print(f"Se recomienda consultar si el elemento forma parte del conjunto antes de usar alguna de las funciones")

#Ejercicios Nivel 2
print("Ejercicios Nivel 2")

#1. Cree dos conjunto A y B y unalos con la funcion union()
print("\nEjercicio 1")
A = {"a", "b", "c", "d", "e"}
print(f"El conjunto A es: {A}")
B = {"a", "f", "k", "l", "c"}
print(f"El conjunto B es: {B}")
print(f"La union de los conjuntos es: {A.union(B)}")
#Otra forma es usar |
print(f"La union de los conjuntos es: {(A | B)}")

#2. Encuentre  la intersecion del conjunto A y B con la funcion intersection()
print("\nEjercicio 2")
print(f"La intersecion del conjunto A y B es: {A.intersection(B)}")
#Otra forma es usando &
print(f"La intersecion del conjunto A y B es: {(A&B)}")

#3. Confirma si el conjunto A es un subconjunto de B
print("\nEjercicio 3")
print(f"El conjunto A es un subconjuto de B? {A.issubset(B)}")

#4. Los conjuntos A y B no tienen elementos en comun?
print("\nEjercicio 4")
print(f"El conjunto A y B no tienen elementos comunes? {A.isdisjoint(B)}")

#5. Haga una union del conjunto A al B y el conjunto B al A
print("\nEjercicio 5")
print(f"El resultado de la union A a B es: {A.union(B)}")
print(f"El resultado de la union de B a A es: {(B | A)}")

#6. Usando la funcion symmetric_difference() encuentre la diferencia simetrica entre los dos conjuntos
print("\nEjercicio 6")
print("La funcion symmetric_difference retorna un conjunto\n que contiene solo los elementos distinto presentes en cada conjunto")
C = A.symmetric_difference(B)
print(f"Empleando la funcion symmetric_difference a A y B el resultado es: {C}")

#7. Elimine los conjuntos y compruebe que se han eliminado correctamente
#del A, B,
#print(f"El conjunto A es: {A} y el conjunto B es: {B}")
#El output indica que A no se ha definido, por ende B tampoco

#Ejercicios Nivel 3
print("Ejercicios Nivel 3")

#1. Declare una lista donde almacene edades y convierta la variable en un conjunto
print("\nEjercicio 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f"La variable ages es del tipo {(type(ages))}")
ages2 = set(ages)
print(f"La variable ages2 es del tipo {(type(ages2))}")
#Compare el largo de la lista y determine cual es mas grande
print(f"El largo de la variable es ages es {len(ages)} y el de la variable ages2 es: {(len(ages2))}")
print(f"El largo de la variable ages es mayor a de ages2: {(len(ages)>(len(ages2)))}")

#2. Ejercicios 2
print("\nEjercicio 2")
"""
Declare una variable donde almacene la siguiente oracion. 
A esa variable debe identificar cuantas palabras unicas conforman la oracion
Para esto emplee los diferentes metodos que se han explicado hasta ahora, teniendo
en cuenta el uso del metodo slit() y los datos de tipo set()
"""
#Paso 1: Declaramos la variable oracion e imprimos el string de la variable con print()
oracion = "I am a teacher and I love to inspire and teach people"
print(oracion) 
#Paso 2: Usamos la funcion slipt() para convertir cada palabra de la oracion en un elemento
new_set = oracion.split(" ")
#Paso 3: Convertimos la oracion en un dato de tipo list()
new_set = list(new_set) 
#El metodo list nos permites usar los metodos de indexing y separaremos la lista en dos listas
mitad = len(new_set)//2 - 1 #Si estas aqui te reto a que elimines el la operacion con el -1 y veas como da el resultado.
primera_parte = new_set[:mitad]
print(f"Los elementos de la primera lista es: {primera_parte}")
segunda_parte = new_set[mitad:]
print(f"Los elementos de la segunda lista es: {segunda_parte}")
#Convertimos las dos lista en set()
primer_set, segundo_set = set(primera_parte), set(segunda_parte)
#Usamos la funcion difference()
print(f"Uniremos los elementos de ambos conjuntos con la funcion symemetric_difference: {primer_set.symmetric_difference(segundo_set)}")
palabras_unicas = len(primer_set.symmetric_difference(segundo_set))
print(f"El numero de palabras unicas en toda la oracion es de: {palabras_unicas}")

#3. Ejercicio 3 Explique la diferencia entre datos tipo string, listas, tuplas y set
print("\nEjercicio 3")
print("Diferencias entre datos tipo string, listas, tuplas y set\n")
print("Un 'string' es un dato de texto que para declararse empleando el uso de comillas simples, dobles y triples")
print("Una 'lista' es un conjunto de datos almacenados en orden, que pueden ser de diferentes tipos y puede modificarse")
print("Una 'tupla' es un conjunto de datos almacenados en orden, que pueden ser de diferentes tipos y no pueden modificarse")
print("Un 'set' es un conjunto de datos almacenados, de forma no ordenado, que pueden ser de diferentes tipos y se pueden agregar o remover elementos")
