#solicitamos al usuario que ingrese la fresa
frase = input("ingresa una frase: ")
#creamos una variable llamada frase_al_reves que es una cadena vacia
frase_al_reves = ""
#creamos un bucle for para que recorra la frase original de forma inversa
for i in range(len(frase)-1, -1, -1):
    #dentro del bucle, se une cada caracter al reves de la variable frase_al_reves usando un operador 
    frase_al_reves += frase[i]
print(frase_al_reves)
