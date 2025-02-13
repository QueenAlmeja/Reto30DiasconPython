#Loops en Python : While and For loops
"""
Notas importantes
El Loop While ejecutara un bloque de codigo hasta que una condicion se cumpla
El Loop For se emplea para interectuar sobre una secuencia de elementos almacenados
en una lista, tupla, diccionario, set o string
La identacion es SUPERMEGA IMPORTANTE cuando usamos los loops
"""

#Ejercicios Nivel 1
"""
Itera una lista de numeros empleando el loop for e imprime los numeros del 1 a 10. 
Realiza el mismo ejemplo con el loop while
"""
print('Ejercicio 1')
print('Iterando con el loop for')
list_num = [1,2,3,4,5,6,7,8,9,10]
#Loop For
for num in list_num:
    print(num) #cada print que se genere, se mostrara en una linea

#Loop While
print('\nIterando con el loop while')
num = 1
while num <= 10: #aqui es donde se indica la condicion 
    print(num) #cada print que se genere, se mostrara en una linea
    num += 1 #aumentamos i en 1 cada vez que se ejecuta el loop

"""
Ejercicio 2:
Escriba un codigo que genere 7 print y genere el siguiente triangulo:
#
##
###
####
#####
######
#######
"""
print('\nEjercicio 2')
a = 1
while a <= 7:
    print('#' * a)
    a += 1
    if a > 7:
        break

"""
Ejercicio 3:
Escriba un codigo anidado para imprimir el siguiente patron:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

print('\nEjercicio 3')
for i in range(8):
    print('#' * 8)

"""
Ejercicio 4:
Empleando un loop, crea un codigo para realizar generar un output que muestre 
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

print('\nEjercicio 4')
for i in range(11):
    print(f"{i} x {i} = {i*i}")
    
"""
Ejercicio 5:
Itera sobre una lista de elementos dados con el loop for e imprime los elementos contenidos
en la lista
"""
print('\nEjercicio 5')
lista = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lista:
    print(f"Este es un elemento alamacenado en la lista: {i}")
    
"""
Ejercicio 6
Crea un codigo donde empleando el loop iteres sobre una lista de numero e imprima los
numeros pares e impares
"""
print('\nEjercicio 6')
print('Mostramos los numeros pares del 1 al 100 usando el loop for')
for i in range(101):
    if i % 2 == 0:
        print(f"{i} es un numero par")
    elif i % 2 != 0:
        continue
print('\nMostramos los numeros impares del 1 al 100 usando el loop for')
for i in range(101):
    if i % 2 != 0:
        print(f"{i} es un numero impar")
    elif i % 2 == 0:
        continue
    
#Ejercicios nivel 2

"""
Ejercicio 7: Usando el loop for crea un codigo que permita iterar del 0 al 100 y print
muestre la suma de todos los numeros
"""

print('\nEjercicio 7')
suma = 0 #desde aqui parte la suma de mis numeros
for i in range(101): 
    suma += i #aqui es donde ocurre la suma
print(f"La suma de todos los numeros del 0 al 100 es: {suma}")

"""
Ejercicio 8: Usando el loop for crea un codigo que permita iterar del 100 al 0 y print
muestre la suma de los numeros pares y los impares
"""
print('\nEjercicio 8')
suma_par = 0
suma_impar = 0

print('Suma de numeros pares del 0 al 100')
for i in range(101): 
    if i % 2 == 0:
        suma_par += i
print(f'La suma de los numeros pares es {suma_par}')

print('\nSuma de numeros impares del 0 al 100')
for i in range(101):    
    if i % 2 != 0:
        suma_impar += i
print(f'La suma de los numeros impares es {suma_impar}')

"""
Ejercicio 9:
Dada una lista de fruta, empleando el loop while, invierte el orden de los
elementos en la lista de frutas
"""

print('\nEjercicio 9')
frutas = ['banana', 'orange', 'mango', 'lemon']
invertida = []
i = len(frutas) - 1
while i >= 0:
    invertida.append(frutas[i]) #en esta parte es donde voy a ir agregando los elementos
    i -= 1
print(f'La lista original es: {frutas}')
print(f'La lista invertida es: {invertida}')

"""
Ejercicio 10
Empleando la informacion almacenada en el enlace: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py
Responde a los siguiente
"""
#usando un loop estrae todos los nombres de los paises que tengan land
"""la informacion esta en el link, en este caso el codigo no correra porque la variable countries
no esta declara, solo la he puesto para simplificar el codigo que hice en otro archivo ya que
la lista de elementos supera los 2000 mil lineas de codigo"""
for country in countries: 
    if "land" in country["name"].lower():
        print(country["name"])
#1. cual es el numero total de idioma en la lista countries

total_languages = sum(len(country["languages"]) for country in countries)
print(f"El numero total de idiomas en la lista countries es: {total_languages}")

#cual es el idioma que mas se repite en la lista countries

most_common_language = max(set(language for country in countries for language in country["languages"]), key=country["languages"].count)
print(f"El idioma que mas se repite en la lista countries es: {most_common_language}")

#cuales son los 10 paises con mayor poblacion de la lista countries

sorted_countries = sorted(countries, key=lambda country: country["population"], reverse=True)
top_10_countries = sorted_countries[:10]
for country in top_10_countries:
    print(f"{country['name']} - Poblacion: {country['population']}")
