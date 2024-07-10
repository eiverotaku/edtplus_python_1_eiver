texto = "aprender a programar en python  con un simple paso"

lenguaje_de_pprogramacion = "python"

if lenguaje_de_pprogramacion in texto:
    print("si esta la palabra")
else:
    print("no esta la palabra") 

# longitud de una cadena 
tamano_texto = len(texto)
print(tamano_texto)

#todo mayuscula
texto_mayuscula = texto.upper()

print(texto_mayuscula)

#lower case = todo en minuscula
texto_minuscula =texto.lower()
print(texto_minuscula)

#titlle case = todos iniciales en mayusculas
texto_inicial = texto.title()
print(texto_inicial)

#swap case = pasar todos las palabras a minusculas
texto_invverso = texto.swapcase()
print(texto_invverso)
print(texto_inicial.swapcase())

# count = contar todas las palabras que hay en el texto que coincidan
conteo_palabras = texto.lower().count("python")
print(conteo_palabras)

# capitalize = la primera letra en mayuscula
inicial_mayuscula = texto.capitalize()
print(inicial_mayuscula)

# startswith = comienza con la palabra buscar /booleano
texto_comienza_com =texto.startswith("aprender")
print(texto_comienza_com)

# enswith = termina col ala palabra a buscar
texto_termina_con =texto.lower().endswith("python")
print(texto_termina_con)

# replace = remplazar algun texto
texto2 ="123456"
print(texto2)

texto_remplazar = texto2.replace("123456", "esto es un nuevo texto que remplaza al anterior")
print(texto_remplazar)

# isdigit = para saber si el valor que estamos recibiendo un digito
texto_es_digito = texto2.isdigit()
print(texto_es_digito)


"""

"""
texto1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut lobortis fermentum interdum. Nunc laoreet nulla sit amet massa rhoncus, nec posuere leo convallis. Vivamus venenatis congue consequat. Vestibulum varius arcu leo, eu hendrerit nunc posuere non. Nunc vel nunc vitae velit malesuada mollis ut vitae ipsum. Cras lacinia non est et semper. Proin eget consectetur ligula, lobortis pretium ante. Duis tempor vitae neque sit amet auctor. Cras commodo risus non dui pellentesque, nec condimentum velit suscipit. Suspendisse quis iaculis quam. Quisque faucibus felis id risus semper imperdiet. Vivamus in ex justo. Suspendisse tellus quam, accumsan rhoncus quam sit amet, pellentesque aliquam odio. Pellentesque mollis lacinia commodo. Morbi maximus tincidunt neque sit amet fringilla. Phasellus libero risus, scelerisque id ipsum eget, pulvinar placerat orci. Donec vel libero ac ex sollicitudin mollis in ut odio. Morbi lacus nisi, bibendum id urna ut, consequat elementum tellus. Suspendisse massa nisl, sodales vitae ante non, commodo mollis lorem. Maecenas accumsan, nisl vitae blandit tristique, neque odio sollicitudin lectus, sed faucibus sapien tellus sed est. Aenean aliquam est sit amet sem mollis, non sagittis risus malesuada. Donec egestas diam at aliquet tincidunt. Aenean ac est ut justo ultrices finibus sit amet ac dolor. Morbi lacinia placerat dui. Aliquam vel cursus ipsum, in finibus purus."

texto2 = "Morbi"
texto_es_digito2 =texto1.isdigit()
print(texto_es_digito2)

conteo_palabras = texto1.lower().count("morbi")
print(conteo_palabras)

texto_invverso = texto1.swapcase()
print(texto_invverso)
print(texto_inicial.swapcase())