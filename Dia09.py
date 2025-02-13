#Condicionales if, elif, else 

#Ejercicios Nivel 1
"""
Ejercicio 1
Cree un programa donde pida al usuario ingresar la edad e indiquele que si es mayor de 18
tiene permitido conducir, pero si es menor de 18, debe esperar a cumplir la mayoria de edad
"""
print("Ejercicio 1")
print('Bienvenido al motorometro, donde te decimos si puedes conducir o no')
edad = float(input('Por favor dinos tu edad: '))

if edad >= 18:
    print('Usted es mayor de edad y tiene permitido conducir 🚗')
    print('Esperamos que tengas una licencia')
elif edad < 18:
    print('Usted es menor de edad y aun no tiene permitido manejar')
    print('Le recomendamos que juegue Mario Card o Crash Card  🎮')
else:
    print('Usted a ingresado un valor invalido')

"""
Ejercicio 2
Cree un programa donde le pida a dos usuarios ingresar sus edades y determinar cual 
de ellos es mayor a partir de los valores ingresados. Para esto emplee los condicionales
antes utilizados
"""
 
print("\nEjercicio 2")
edad_1 = float(input('Dinos tu edad: '))
edad_2 = float(input('Dinos la edad un amigo o hermano: '))

if edad_1 > edad_2:
    print(f"La primera persona que ha ingresado al programa tiene {edad_1} por lo que es mayor que la otra persona")
elif edad_2 > edad_1:
    print(f"La segunda persona que ha ingresado al programa tiene {edad_2} por lo que es mayor que la primera persona")
elif edad_1 == edad_2:
    print(f"Ambas personas tienen la misma edad")
else:
    print("Los usuarios no han ingresado valores numericos")
    
"""
Ejercicio 3:
Pidele a dos usuarios que ingresen numeros y empleando los condicionales has que el output indique que valor
es mayor. Si el valor de a es mayor al valor de b, el output deberia decir algo como:
> a es mayor a b 
Y asi de forma inversa. Tambien considera si los valores son iguales
"""
print("\nEjercicio 3")
valor_a = float(input("Ingresa un numero para hacer una comparacion de valores: "))
valor_b = float(input("Ingresa otro numero para hacer una comparacion de valores: "))

if valor_a > valor_b:
    print(f"El valor de la variable A es mayor al valor de la variable B")
    print(f"A es mayor a B")
elif valor_a < valor_b:
    print(f"El valor de la variable A es menor al valor de la variable B")
    print(f"B es mayor a A")
elif valor_a == valor_b:
    print(f"Los valores de las variables A y B son iguales")
    print(f"A es igual a B")
else:
    print("No se han ingresado valores numericos que puedan compararse")

#Ejercicios Nivel 2

"""
Ejercicio 4
Crea un programa donde le pidas a un estudiante que ingrese su promedio de notas
y el resultado lo califique en los niveles A, B, C, D, E, F
A = 100 - 80
B = 79 - 70
C = 69 - 60
D = 59 - 50
F = 49 - 0
"""
print("\nEjercicio 4")
print("Hola, vamos a evaluar el promedio de notas que has alcanzado hasta ahora")
print("El promerdio debe estar en una escala del 1 al 100")

student_name = input("Escribe tu nombre: ").capitalize()
student_note = float(input("Indicanos el promedio de notas que tienes hasta ahora: "))

if student_note <= 100 and student_note >= 80:
    print(f"Hola, {student_name}, tu promedio de notas indica que estas en el rango A")
    print("Mente velocidad galaxia")
elif student_note < 80 and student_note >= 70:
    print(f"Hola, {student_name}, tu promedio de notas indica que estas en el rango B")
    print("Lo esta haciendo bien")
elif student_note < 70 and student_note >= 60:
    print(f"Hola, {student_name}, tu promedio de notas indica que estas en el rango C")
    print("Vas bien, pero puedes mejorar")
elif student_note < 60 and student_note >= 50:
    print(f"Hola, {student_name}, tu promedio de notas indica que estas en el rango D")
    print("Deberias organizar tu horario para estudiar un poco mas")
elif student_note < 50 and student_note >= 0:
    print(f"Hola, {student_name}, tu promedio de notas indica que estas en el rango F")
    print("La verdad, es que no te esta yendo bien, pide ayuda a un amigo o a un profe")
else:
    print("No has ingresado un valor correcto")

"""
Ejercicio 5
Crea un programa que indica la estacion del año, de acuerdo al mes que indique el usuario
Ten en cuenta lo siguiente
Septiembre, Octubre y Noviembre = Otoño
Diciembre, Enero y Febrero = Invierno
Marzo, Abril y Mayo = Primavera
Junio, Julio y Agosto = Verano 
"""
print("\nEjercicio 5")
print("Vamos a determinar la estacion del año en que naciste: ")
user_mes = input("Dinos tu mes de cumple: ").capitalize()

if user_mes == "Septiembre" or user_mes == "Octubre" or user_mes == "Noviembre":
    print("Tu estacion es Otoño")
elif user_mes == "Diciembre" or user_mes == "Enero" or user_mes == "Febrero":
    print("Tu estacion es el Invierno")
elif user_mes == "Marzo" or user_mes == "Abril" or user_mes == "Mayo":
    print("Tu estacion es la Primavera")
elif user_mes == "Junio" or user_mes == "Julio" or user_mes == "Agosto":
    print("Tu estacion es el Verano, la verdad es que en esta epoca nacemos los mejores")
else:
    print("No nos has dicho tu mes de nacimiento")
    
"""
Ejercicio 6
Se tiene la siguiente lista de frutas:
fruits = ['banana', 'orange', 'mango', 'lemon']
Debes crear un programa que consulte por una fruta y verificar si el nombre de la fruta
consultada esta en la lista, en caso de que no, debes añadir la fruta a la lista existente
"""
print("\nEjercicio 6")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("Veamos si la fruta que necesitas esta en nuestro stock de productos ")

user_fruit = input("Escribe el nombre de la fruta que deseas verificar: ").lower() #uso la funcion lower 

if user_fruit in fruits:
    print(f"La fruta {user_fruit} si se encuentra en nuestro stock")
else:
    print(f"La fruta {user_fruit} no se encuentra en nuestro stock")
    print(f"Agregamos la fruta {user_fruit} a nuestro stock")
    fruits.append(user_fruit)
    print(f"Nuestro nuevo stock de productos es: {fruits}")
    
"""
Ejercicio 7
Empleando la informacion almacenada en un diccionario, determina
a. Determina si una de las claves es de las habilidades y en caso de que si, imprime en el output la que esta en medio
b. Comprueba si una de las habilidades es Python
"""

person={'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {'street': 'Space street','zipcode': '02210'}}

print("\nEjercicio 7")
print("Verificamos si la persona tiene la clave skills en el diccionario")

if 'skills' in person:
    print(f"La persona tiene la clave skills en su diccionario")
    #Imprimimos la habilidad que esta en el medio:
    print(f"La habilidad que esta en medio es: {person['skills'][3]}")
else:
    print("La persona no tiene la clave skills en su diccionario")
    
print("\nComprobamos si una de las habilidades almacenadas en la clave skills es Python")

if 'Python' in person['skills']:
    print("La habilidad Python se encuentra en la lista de habilidades")
else:
    print("La habilidad Python no se encuentra en la lista de habilidades")

"""
Si la persona solo tiene las habilidades 
JavaScript y React, imprime('Es un desarrollador front-end')
Si las habilidades de la persona tienen Node, Python, MongoDB, imprime('Es un desarrollador back-end')
Si las habilidades de la persona tienen React, Node y MongoDB, imprime('Es un desarrollador fullstack')
Si no imprime('título desconocido')
"""


if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print("Es un desarrollador front-end")
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print("Es un desarrollador back-end")
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoBD' in person['skills']:
    print("Es un desarrollador fullstack")
else:
    print("Titulo desconocido")

"""
Si la persona está casada y vive en Finlandia, imprime la información en el siguiente formato:
Asabeneh Yetayeh lives in Finland. He is married.
"""

if person['is_marred']:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")



