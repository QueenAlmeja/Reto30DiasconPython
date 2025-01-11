#Funciones integradas de python y variables 

#Ejercicios Nivel 1:

firstname = "Alejandra"
lastname = "Sanchez"
fullname = "Alejandra Sanchez"
country = "Venezuela"
city = "Valera"
age = 987
year = 2025
is_married =  False
is_true = False
is_light_on = False

like_dogs, favorite_food, lucky_num, color, second_name, fav_float_num = True, "Arepa", 12, "Yellow", "Carolina", 9.81

#Ejercicios Nivel 1:
#1 Usemos la funcion integrada tyoe() para saber los tipos de datos almacenados en cada variable declarada

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(like_dogs))
print(type(favorite_food))
print(type(lucky_num))
print(type(color))
print(type(second_name))
print(type(fav_float_num))

#2 Usando la funcion len, revisa el largo de tu nombre 
print(len(firstname))

#3Compara el largo de tu nombre y apellido usando la funcion len
print(len(firstname) == len(lastname))

#4 Crea dos variables y almacenas los valores de 5 y 4
num1, num2 = 5, 4
print("El valor de la variable num1 es: ", num1, "El valor de la variable num2 es: ", num2)
#5 Crea una variable donde sume los valores de las variables que almacenas los numeros
total_val = num1 + num2
print(total_val)
#6 Extrae el valor de la segunda variable y asignale un nuevo valor 
num2 = 7 #aqui estoy reescribiendo el valor de la variable num2 anteriormente declarada
print(num2)
#7 Multiplica los valores de la variable num1 y num2 y asigna el resultado a una variable
multi_var = num1 * num2
print(multi_var)
#8 Divide los valores de la variable num1 y num2 y asigna el resultado a una variable
div_val = num1 / num2
print(div_val)
#9 Usa el operador modulo % para encontrar el numero resultante de la division entre la variable num1 y num2
modulo_div = num1 % num2
print(modulo_div)
#10 Calcule el valor de la variable num1 elevada al num2 y asigne el resultado a una variable
expone_operation = num1 ** num2
print(expone_operation)
#11 Encuentre el resultado entre la variable num1 y num2 usando el operador // y guarde el resultado en una variable
floor_div = num1 // num2
print(floor_div)
"""
Ejercicio especial: Calculemos el valor del radio

El radio de un circulo es de 30 metros
a. Calcule el area de un circulo y almacene el valor en la variable area_circulo
b. Calcule la circunferencia de un circulo y asigne el valor a la variable circunferencia_circulo
c. Asigne el radio de un circulo usando la funcion input y calcule el area
"""

#Si mi radio es de 30 entonces para calcular el area y la circunferencia seria 

area_circulo = 3.14 * (30**2)
print("El area del circulo con radio 30 es de: ", area_circulo)
circunferencia_circulo = (2 *3.14* 30)
print("La circunferencia del circulo con radio 30 es de: ", circunferencia_circulo)

#Asignando nosotros el valor del radio usando la funcion input

valor_radio = int(input("Dinos un valor aleatorio para calcular el area de un circulo: "))
area_circulo2 = 3.14 * (valor_radio**2)
print("El valor del area del circulo, sera: ", area_circulo2)

#12 Use la funcion integrada input para solicitar a un usuario su nombre, apellido, pais y edad
user_name = input('Por favor, danos tu nombre: ')
print(user_name)
user_lastname = input('Por favor, dinos tu apellido: ')
print(user_lastname)
user_country = input('Por favor, dinos en que pais vives: ')
print(user_country)
user_age = int(input('Por favor, dinos tu edad: '))
print(user_age)

"""
⚠️
Nota importante
La funcion input siempre recogera un dato de tipo string, por lo tanto, cuando se le consulta 
al usuario la edad, se antepone a la funcion input, la funcion int(), de esta manera almacenaremos
el dato ingresado por el usuario como un dato numerico
"""