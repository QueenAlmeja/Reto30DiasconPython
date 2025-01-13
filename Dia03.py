#Operadores 

#1. Declara tu edad en una variable
print("Ejercicio 1")
age = 30
print("I am ", age, " years old")

#2. Declara tu peso en una variable 
print("\n Ejercicio 2")
my_height = 1.66
print("My height is: ", my_height)

#3. Declare un variable que almacene un numero complejo
print("\n Ejercicio 3")
complex_num = 2 + 5j
print("El numero complejo es: ", complex_num)

#4. Haga un codigo donde le solicite al usuario ingresar dos valores para calcular la area de un triguando
#Considere que la ecuacion para calcular el area de un triguanlo es area_triangulo = 0.5 * b * h (b=base, h=height)
print("\n Ejercicio 4")
print("Vamos a calcular la base de un trigulo y necesitamos tu ayuda") 
user_num1 = float(input("Por favor ingresa un numero que represente la base de un triangulo: "))
user_num2 = float(input("Por favor ingresa un numero que represente la altura de un trigulo: "))
area_triangulo = 0.5 * user_num1 * user_num2
print("El area del triangulo, en funcion de los numeros dados es: ", area_triangulo)

#5 Escriba un codigo con le solicite a un usuario ingresar tres valores numericos para calcular el perimero de un triangulo
#considera la ecuacion de perimetro = a + b + c
print("\n Ejercicio 5")
print("Ayudanos a calcular el perimetro de un triangulo")
lado_a = float(input("Asigano un valor numerico al lado a del triangulo: "))
lado_b = float(input("Asigano un valor numerico al lado a del triangulo: "))
lado_c = float(input("Asigano un valor numerico al lado a del triangulo: "))
perimetro_triangulo = lado_a + lado_b + lado_c
print("El perimetro del triangulo en funcion de los valores dados es: ", perimetro_triangulo)

#6. Escriba el un codigo que le permita a un usuario ingresar valores numericos para asignarlos a las variables longitud y ancho
#Calcule el area y el perimetro usando los datos ingresados. Tome en cuenta las siguientes escuaciones
# area = longitud * ancho y perimetro = 2 *(longitud + ancho)
print("\n Ejercicio 6")
print("Necesitamos tu ayuda para calcular la longitud y el ancho de un triangulo ")
longitud = float(input("Ingrese un valor numerico para la longitud del triangulo: "))
ancho = float(input("Ingrese un valor numerico para el ancho del triangulo: "))
area1 = longitud * ancho
perimetro1 = 2 * (longitud + ancho)
print("De acuerdo a los valores dados, el area del triangulo es: ", area1, " minetras que el perimetro es: ", perimetro1)

#7. Escriba un codigo donde le solicite al usuario asignar un valor numerico al radio de un circulo para calcular el area y la circunferencia
#Considere las siguientes escuaciones area_circulo = PI * r**2 y circunferencia = 2 * PI * r. Recuerde que pi es una constante 3.14
print("\n Ejercicio 7")
print("Necesitamos calcular el area y la circunferencia de un circulo")
user_num_circul = float(input("Por favor, asigna un valor numerico al radio de un circulo: "))
PI = 3.14

area_circulo = PI * (user_num_circul ** 2)
circunferencia = 2 * PI * user_num_circul
print("De acuerdo al valor asignado por el usuario, el area del circulo es: ", area_circulo, "y la circunferencia es: ", circunferencia)

#8. Calcule la pendiente de la intercepcion de x y y  de  y = 2x - 2
print("\n Ejercicio 8")
"""
Para calcular la pendiente, tomemos en cuenta la ecuacion de la pendiente y = mx + b. 
m = es la pendiente 
b = es la intersección
Si consideramos la ecuacion antes dadas, tendriamos que 2 es la pendiente y 2 es la intersección

"""
print("Tenemos la ecuacion y = 2x - 2. Debemos calcular la pendiente y la intersección de x & y \n")
print("Si consideramos la ecuacion de la pendiente y = mx + b, podemos decir que")
pendiente_m = 2
interesccion_b = 2
print("El valor de la pendiente sera", pendiente_m, "y de la interseccion sera ", interesccion_b)
print("La interseccion de y ocurre cuando x es igual a 0\n")
x = 0
y = 2 * x - 2
print("El valor de y es su interseccion con x es igual a", y, "\n")
print("La interseccion de x ocurre cuando y es igual a 0")
y_2 = 0
#y_2 = 2* x_2 - 2 y se despeja de esta ecuacion y se obtiene x_2 = 2/2
x_2 = 2/2
print("El valor de x es su interseccion con y es igual a", x_2, "\n")

#Se asiganaron crearon las variables x_2 y y_2 para no reescribir el valor de las variables x y y escritas anteriormente

#9. Calcule la pendiente y la distancia euclidiana de de de los puntos (2,2) y (6,10)
#Tome en cuenta que la ecuacion de la pendiente = y2-y1/x2-x1 y la distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
print("\n Ejercicio 9")
print("Vamos a calcular la distancia euclidiana y la pendiente entre los puntos (2,2) y (6,10)")
x1, x2, y1, y2 = 2, 6, 2, 10
pendiente = y2-y1/x2-x1
distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
print("El valor de pendiente es: ", pendiente, " y el valor de distancia euclidiana es: ", distancia)

#10 Comparamos las pendientes obtenidas en el ejercicio 8 y 9 
print("\n Ejercicio 10")
print(pendiente_m == pendiente)

#11. Calculemos el valor de y de la ecuacion y = x^2 + 6x + 9, asignando distintos valor de x. 
#Plus que yo he agregado, usar un prompt para preguntarle a usuarios que ellos ingresen los valores numericos de x
print("\n Ejercicio 11")
print("Vamos a calcular el valor de y, de la siguiente ecuacion y = x^2 + 6x + 9")
user_x = float(input("Por favor, ingresa el primer valor de x: "))
user_x2 = float(input("Por favor, ingresa el segundo valor de x: "))
y = user_x ** 2 + 6 * user_x2 + 9
print("De acuerdo a los valores ingresador por el usuario, el valor de y es: ", y)

#12 compara las palabras python y dragon y haz una sentencia de comparacion falsa
print("\n Ejercicio 12")
word1 = "Python"
word2 = "Dragon"
print(word1 == word2)
print(not(word1 == word2))

#13 Usa el operador and para revisar si la palabra on se encuentra dentro de Python y Dragon
print("\n Ejercicio 13")
print("on" in word1 and "on" in word2)

#14 Usa el operador in para revisar si la palabra jargon, esta dentro de la oracion I hope this course is not full of jargon
print("\n Ejercicio 14")
sentences = "I hope this course is not full of jargon"
print("jargon" in sentences)

#15 No hay la subcadena de texto en 'on' en las palabras python ni dragon
print("\n Ejercicio 15")
print('on' is not word1 and 'on' is not word2)

#16 Encuentra el largo de la palabra Python y convierte el valor en un numero float y un strg 
print("\n Ejercicio 16")
largo = len(word1)
print("La palabra Python tiene un largo de: ", largo,)
cam_float = float(largo)
print("Hemos modificado el valor del len a un numero float: ", cam_float)
cam_strg = str(largo)
print("Hemos modificado el valor del len a un string: ", cam_strg)

#17 Como podrias crear un codigo donde compares si un numnero divisible entre 2 es par o impar
#🔴Nota, este es un ejercicio avanzado, que no deberia estar en este nivel, pero la forma mas sencilla seria
print("\n Ejercicio 17")
numero = float(input("Por favor, ingrese un valor numerico para comprobar si este es un numero par o no: "))
if numero % 2 == 0:
    print("El numero es par")
elif numero % 2 != 0:
    print("El numero es impar")
else:
    print("No a ingresado un valor numerico")
    
#18 Comprueba si la floor division entre 7//3 es igual a 2.7
print("\n Ejercicio 18")
resultado = 7//3
print(resultado == 2.7) 

#19 Comprueba si "10" es igual a 10
print("\n Ejercicio 19")
print("10" == 10)

#20 Comprueba si int('9.8') es igual a 10
print("\n Ejercicio 20")
print(float('9.8') == 10)

#21 Escribe un codigo que le consulte a un usuario la cantidad de horas trabajas a la semana y le diga su pago total, calculando el pago por hora trabajada
print("\n Ejercicio 21")
horas_trabajadas_semanal = float(input("Indica el numero de horas trabajas a la semana para calcular tu pago semanal: "))
pago_por_hora = 20
pago_total = horas_trabajadas_semanal * pago_por_hora
print("El pago por hora trabaja es de 20 dolares")
print("El monto total de tu pago semana es de: ", pago_total, "dolares")

#22 Escribe un codigo donde le consultes el numero de años que a vivido y con este dato puedes calcular la cantidad de segundo que ha vivido en total
print("\n Ejercicio 22")
edad_user = float(input("Cuantos años tienes: "))
#consideremos que un año tiene 31536000.00 segundos. Sobre esto no consideramos los años bisiestos

segundos_vividos = edad_user * 31536000.00
print("Has vivido: ", segundos_vividos, " segundos en toda tu vida")


