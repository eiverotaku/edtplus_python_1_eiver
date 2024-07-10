# listas en python []
numero = [1, 2, 3, 4, 5]
print(type(numero))

#lista de str o cadena de texto
tareas = ["Aprender python", "Resolver retos", "Resolver problemas"]
print(tareas)

#lista de diferentes tipos de datos
diferentes_tipos_datos =[1, "cadena de texto", True, False]
print(diferentes_tipos_datos)

# Indice de cada arreglo
print("mostrando el indece [0] del elemento del arreglo numero  ->", numero[0])
print("mostrando el indece [1] del  arreglo tareas  ->", tareas[1])
print("mostrando el indece [3] del  arreglo diferentes_tipos_datos  ->", diferentes_tipos_datos[3])

# mutacion = modificar el arreglo original
tareas[1] = "ya he resuelto el reto 1"
tareas[2] = "ya he resuelto el reto 2"
print("lista modificada ->", tareas)

# slicing o recorte o pedazo
print(numero[:3])
print(numero[2:])
print(numero[2:3])

#Operador in = en booleano
print(True in diferentes_tipos_datos)
print("cadena de texto" in diferentes_tipos_datos)
print("otro cosa que no esta" in diferentes_tipos_datos)