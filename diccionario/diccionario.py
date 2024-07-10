'''
lista = []
dict = {}
tuple = ()
'''
mi_diccionario = {}
print ("la forma enque lo representa python", type(mi_diccionario))

#los diccionarios se representan por tener llaves -> valor (ingles: key - value)
mi_diccionario ={
    "key": "value",
    "llave": "valor",
    "nombre": "eiver",
    "vida": "es necesario para que estemos vivos",
    "edad":14
}
print(mi_diccionario)
# para saber lo longitud dde nuestro diccionario se aplica el metodo le
longitud_dict = len(mi_diccionario)
print("esta es la la longitud de nuestro diccionario ->", longitud_dict)
# obtener valores segun nuestro su palabra clave (key o llave)

print("el valor de la palabra clave vida es ->",mi_diccionario["vida"])
print("el valor de la palabra clave vida es ->",mi_diccionario["edad"])

# metodo para obtener el valor segun su palabra clave
print("este metodo get me permite obtener el valor segin su llave - >", mi_diccionario.get("vida"))

# metodo in para saber si el key esta dentro del diccionario
print("saber si esta key esta en el diccionario y retorna un booleano ->", "nombre" in mi_diccionario)