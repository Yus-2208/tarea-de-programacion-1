#solicitar al usuario ingrasar la palabra
palabra = input("ingrese la palabra: ")

#primero asumimos que la palabra ingresada es palindroma
es_palindroma = True

#se utiliza un bucle for para recorrer los indices de la palaba
for i in range(len(palabra)):
    #se verifica si el caracter en la posicion i es diferente al caracter de la posicion -i-1
    if palabra[i] != palabra[-i-1]:
        #si hay una diferancia entre los caracteres i y -i-1, se asigna a la variable es_palindroma el valor false y se rompe el bucle con un break
        es_palindroma = False
        break

#hacemos un condicional para imprimir la respuesta, es dicir si la palabra es palindroma es true y se imprime la palabra es palindroma, pero si es falso se imprime no es palindroma
if es_palindroma:
    print("La palabra es palindroma.")
else:
    print("La palabra no es palindroma")