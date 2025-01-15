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
print("Parte 2")

#1. Declare una lista con valores numericos que corresponden a edades aleatorias
print("\nEjercicio 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f"Hemos creado una nueva lista de edades {ages}")

#2. Organiza la lista con la funcion sort() y encuentra el valor max y min
print("\nEjercicio 2")
ages.sort()
print(f"La lista organizada con la funcion sort() es: {ages}")
#el valor max a min es:
max_ages = max(ages)
print(f"El valor max de la lista es: {max_ages}")
min_ages = min(ages)
print(f"El valor min de la lista es: {min_ages}")

#3. Edad la edad que esta en la mitad de la lista y dividi el valor entre 2
print("\nEjercicio 3")
edad_mitad_lista = (len(ages)//2)
ages_div = ages[edad_mitad_lista] / 2
print(f"El valor de index del elemento que esta en la mitad de la lista es: {edad_mitad_lista}\n y e valor de la division de este numero entre 2 es {ages_div}")

#4. Encuentra el rango de edades restando el valor max entre el min
print("\nEjercicio 4")
rango = max_ages - min_ages
print(f"El rango de edades es de: {rango}")

#5. Comparen los valores del promedio minimo y promedio maximo usando la funcion abs()
#abs() devuelve el valor absoluto de un numero
print("\nEjercicio 5")
promedio_min = min_ages / len(ages)
promedio_max = max_ages / len(ages)
promedio_min_abs = abs(promedio_min)
print(f"La diferencia de promedio minimo empleando la funcion abs es: {promedio_min_abs}")
promedio_max_abs = abs(promedio_max)
print(f"La diferencia de promedio maximo empleando la funcion abs es: {promedio_max_abs}")
print(f"Son iguales los valores del promedio maximo y minimo {promedio_max_abs == promedio_min_abs}")

#Se ha declarado una lista con paises. Encuentre el valor de indice y nombre del pais que esta en el medio de la lista
countries = [
'Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria',
'Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina',
'Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad',
'Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic',
'Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea',
'Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada',
'Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq',
'Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait',
'Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar',
'Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova',
'Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger',
'Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal',
'Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia',
'Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain',
'Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo',
'Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States',
'Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']
print("\nEjercicio 6")
index_middle_countries = len(countries)//2
print(f"El valor del indice del pais que esta en la mitad de la lista es {index_middle_countries}")
print(f"El nombre del pais es: {countries[index_middle_countries]}")

#7. Divide la lista en dos lista de forma equitativa
print("\nEjercicio 7")
primera_mitad = countries[:index_middle_countries]
print(f"La primera mitad de la lista tiene los siguientes paises {primera_mitad}")
segunda_mitad = countries[index_middle_countries:]
print(f"La segunda mitad de la lista tiene los siguientes paises {segunda_mitad}")

#8. De la siguiente lista de elementos declrados, desempaque los tres primero y cree una lista nueva con los elementos restantes
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
pais1, pais2, pais3 = paises[:3]
print(f"Los tres primeros elementos de la lista son: {pais1, pais2, pais3}")
new_lista = paises[3:]
print(f"La lista de elementos restantes es: {new_lista}")


