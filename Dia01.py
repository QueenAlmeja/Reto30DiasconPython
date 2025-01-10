"""
En el siguiente repositorio se dejará brevemente las instrucciones del Reto 30DaysOfPython
Este reto pueden encontrarlo en https://github.com/Asabeneh/30-Days-Of-Python/tree/master/01_Day_Introduction
Cada archivo que precede a este, contendrá las respuesta de los ejercicios indicados en el Reto, según las
Instrucciones correspondientes a cada día. 
"""

#Day 1: Introduction
#Ejemplos usando la funcion print()

print(2+3)  #suma
print(3-1)  #resta
print(2*3)  #multiplicacion
print(3/2)  #division
print(3**2) #exponencial
print(3%2)  #modulo
print(3//2) #floor division

#Revisando el tipo de dato con la funcion type()
print(type(10))     #int
print(type(3.14))   #float
print(type(1+3j))   #numero complejo
print(type("Alejandra")) #string o cadena de texto
print(type([1,2,3,"nombre", [45, True]])) #Lista
print(type({"age":30, "name":"Alejandra"})) #Diccionario
print(type({"Alejandra", "Venezuela", True}))   #Set o Conjunto
print(type((9.8, 3.14, 2.7, "Hola"))) #Tupla

#Ejercicios Dia 1 : Respuestas
#Operaciones con los numeros 3 y 4
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

#Escribe cadenas de texto que correspondan a tu nombre, apellido, pais y una frase
print("Alejandra")
print("Sanchez")
print("Venezuela")
print("Estoy haciendo de nuevo el reto de 30 Dias con Python")
print("Prometo subirlo y completarlo esta vez")

#Revisando el tipo de dato 
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(["Asabeneh", "Python", "Finland"]))
print(type("Alejandra"))
print(type("Sanchez"))
print(type("Venezuela"))

#Crea un ejemplo para los diferentes tipos de datos

print(1994)
print(56.8975)
print(3 + 5j)
print("Canela, perro malvado y loquito")
print(True)
print(['Manzana', 'Pera', 'Cambur', 'Ron con Cocacola'])
print(("Azul,","Verde", "Coco", "Playa"))
print({1,11,22,33,44})
print({"name":"Cocobongo", "comida":"Arroz"})

#Calculamos la distancia Euclidiana de (2,3) y (10,8)
#dos formas de hacer este ejercicio seria asignando valores a variables:
x1, y1 = 2, 3
x2, y2 = 10, 8
distancia = (((x2-x1)**2 + (y2-y1)**2))**0.5
print(distancia)

#la otra forma seria usando directamente los valores dados en la ecuación

distancia2 = ((10-2)**2 + (8-3)**2)**0.5
print(distancia2)

"""
Existen varias formas de sacar la raiz cuadrada en python, pero en este caso la mas basica de todas es elevando a 0.5 ()**0.5
"""