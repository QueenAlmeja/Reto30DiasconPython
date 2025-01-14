#Cadenas de texto o String
#🔴Nota importante, todo texto en python debe estar escrito entre comillas, simples, dobles o triples.

#Ejercicios
#1. Agrupa las palabras 'Thirty', 'Days', 'Of', 'Python' en una sola cadena de texto
print("Ejercicio 1")
word1 = "Thirty"
word2 = "Days"
word3 = "Of"
word4 = "Python"
full_sentence = word1 + " " +  word2 + " " + word3 + " " + word4
print(f"La horacion del primer ejercicio es: {full_sentence}\n" )

#2. Agrupa las palabras 'Coding', 'For' , 'All' en una sola cadena de texto
print("Ejercicio 2")

coding ="Coding"
for_word = "For" 
all_words = "All"
full_text =  coding + " " + for_word + " " + all_words
print(f"La horacion del segundo ejercicio es: {full_text}\n" )

#3. Declara una variable inicial que contenga la frase Coding For All y usa la funcion print para mostrarla en la consola
print("Ejercicio 3")
var1 = "Coding For All"
print(f"El valor de la variable var1 es: {var1}\n")

#4.Imprime el tamañon de la variable var1 usando la funcion len() 
print("Ejercicio 4")
print(f"El tamaño de la función var1 es: {len(var1)}\n")

#5 Usando la funciones upper() y lower() modifiquen las letras de la frase almacenada en la variable var1
print("Ejercicio 5")
print(f"La frase almacenada en la variable var1 es {var1}")
print("Usando las funciones upper() y lower(), la frase se modifico a:\n")
print(var1.upper())
print(var1.lower())

#6 Usamos los metodos de string capitalize(), title(), swapcase() para modificar la frase de la variable var1
print("\nEjercicio 6")
print(f"Usando la funcion capitalize tenemos: {var1.capitalize()}")
print(f"Usando la funcion title tenemos: {var1.title()}")
print(f"Usando la funcion swapcase tenemos: {var1.swapcase()}")

#7 Extraiga la palabra Coding de la variable var1, empleando los metodos de slicing
print("\nEjercicio 7")
print(var1[0:6])
#Para esta parte es importante revisar los valores de indices en donde se ubican las letras que componen la palabra que se busca extraer

#8. Revisa si la frase almacenada en la var1 comienza con la palabra Coding usando alguna index, find() o startswith()
print("\nEjercicio 8")
print(f"La frase almacenada en la var1 comienza con la palabra Coding: {var1.startswith("Coding")}")
#Realmente, aqui la opcion correcta es usar startswith() o intentar usar in.

#9. Remplaza la palabra Coding por Python en la frase almacenada en la var1
print("\nEjercicio 9")
print("Usando la funcion replace() modificaremos la oraciones de la var1")
print(var1.replace("Coding", "Python"))

#10. En una nueva variable almacene la frase Python for Everyone y usando el metodo replace() modifique la palabra Everyone por All
print("\nEjercicio 10")
var2 = "Python for Everyone"
print(f"La oracion original de la nueva variable es: {var2}")
print(f"Usando la funcion replace, se ha modificado a {var2.replace("Everyone", "All")}")

#11. Usando la funcion spli(), separamos la frase almacenada en la var2
print("\nEjercicio 11")
print(f"Separamos los argumento de la frase en la var2, usando la funcion split()\n {var2.split()}")

#12. #Se nos da una variable que contiene los nombres de empresas. Usando la funcion split(), separemos los nombres
print("\nEjercicio 12")
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas)
print(empresas.split())

"""
🟡
Notese que la funcion split() retorna una lista que contendra como elementos las palabras que conforman
la cadena de texto, separando los argumentos con ,
"""

#13. Cual es el valor de indice de la palabra Coding en frase almacenada en la var1

print("\nEjercicio 13")
print(f"La palabra Coding se encuentra en la posicion {var1.index("Coding")}")
print(f"La palabra Coding se encuentra en la posicion {var1.find("Coding")}")
#Este ejercicio podemos almacenarla de dos formas

#14. Cual es la palabra o letra almacenada en el ultimo valor del indice de la var1
print("\nEjercicio 14")
print(f"El valor almacenado en indice que corresponde a la ultima posicion de var1 es: {var1[-1]}")

#15. Cual es el caracter que esta almacenado en el indice 10 de la var1
print("\nEjercicio 15")
print(f"El valor de indice 10 de la var1 es: {var1[10]}") #es un espacio en blanco

"""
#16. Cream un acronimo o abreviacion para las frases almacenadas en la var1 y var2
print("\nEjercicio 16")
print(f"Usando los metodos de slicing, creamos las siguientes abreviaciones:")
print(f"Para la var1 tenemos: {var1[::3]}")
print(f"Para la var2 tenemos: {var2[::3]}")
"""

#17. Usa el metodo de indexacion para determinar cuando aparece por primera vez la letra C y F en la var1
print("\nEjercicio 17")
print(f"La posicion de C en la var1 es: {var1.index("C")}")
print(f"La posicion de F en la var1 es: {var1.index("F")}")

#18. Empleando la funcion rfind() determina la posicion en la que aparece por ultima vez la letra l en la var1
print("\nEjercicio 18")
print(f"La ultima posicion en la que podemos encontrar la letra l en la var1 es: {var1.rfind("l")}")

#19. Declare una variable donde almacene la variable You cannot end a sentence with because because because is a conjunction
#Emplee las funciones find o index para determinar la posicion de la primera vez que aparece la palabra because
#Emple la funcion rfind() para terminar la posicion de la ultima vez que aparece la palabra because
print("\nEjercicio 19")
sentencia = "You cannot end a sentence with because because because is a conjunction"
print(f"La frase almacenada en la variable sentencia es:\n {sentencia}")
print(f"El valor de indice donde la palabra because aparece por primera vez en la oracion es: {sentencia.find("because")}")
print(f"El valor de indice donde la palabra because aparece por ultima vez en la oracion es: {sentencia.rfind("because")}")

#20. Extrae la subcadena de texto because bacause because de la frase almacenada en la variable sentencia
print("\nEjercicio 20")
sub_string = sentencia[31:55]
print(f"La subcadena de texto de la oracion almacenada en la variable sentencia es: {sub_string}")

#21.Use las funciones startswith y endswith para determinar si la oracion en la variable var1 comienza y finaliza con la subcadena Coding
print("\nEjercicio 21")
print(f"La oracion almacenada en la var1 comienza con la palabra Codin?: {var1.startswith("Coding")}")
print(f"La oracion almacenada en la var1 finaliza con la palabra codin?: {var1.startswith("coding")}")

#22. Declara una variable donde almacenes la siguiente oracion '   Coding For All      ' y una funcion para eliminar los espacios en blanco
print("\nEjercicio 22")
var3 = '   Coding For All      '
print(f"Se ha declarado la siguiente oracion: {var3}")
print(f"Eliminando los espacios en blanco tenemos: {var3.replace('   ', '')}")

#23. Declare dos variables en las que almacene las siguientes oraciones 30DaysOfPython y thirty_days_of_python
#Determine cual de las dos variables retorna regresa True cuando se emplea el metodo isidentifier()
print("\nEjercicio 23")
var4 = '30DaysOfPytho'
print(f"En la variable var4 hemos almacen: {var4}")
var5 = "thirty_days_of_python"
print(f"En la variable var4 hemos almacen: {var5}")
print(f"La var4 retorna True al usar la funcion isidentifier(): {var4.isidentifier()}")
print(f"La var5 retorna True al usar la funcion isidentifier(): {var5.isidentifier()}")

#24. Se tiene una lista con los nombres de diferentes bibliotecas, emplee la funcion join() para unir las palabras con el simbolo #
print("\nEjercicio 24")
lista = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(f"Se tiene la siguiente lista de elementos: {lista}")
print(f"Usando la funcion join() tendremos: {'# '.join(lista)}")

#25. Use una nueva linea para separar las oraciones: I am enjoying this challenge y I just wonder what is next.
print("\nEjercicio 25")
print("I am enjoying this challenge \nI just wonder what is next")

#26. Use una linea para separar las siguientes palabras: Name, Age, Country, City y Asabeneh, 250, Finland, Helsinki
print("\nEjercicio 26")
print("Name\tAge\tCountry\tCity\n")
print("Asabeneh\t250\tFinland\tHelsinki")

#27. Use algunos de los formatos de string para efectuar las siguientes operaciones
print("\nEjercicio 27")
print("Ejercicio A")
radius = 10
area = 3.14 * radius ** 2
print(f"El area de un circulo que posee un radio de 10 metros es de: {area}")
print("\nEjercicio B")
a = 8
b = 6 
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))
