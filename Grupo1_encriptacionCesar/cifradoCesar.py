#función para realizar el cifrado del mensaje
# parametros de entrada:    tasa - es la tasa que se usara en la encriptación
#                           mensaje_lista - el mensaje a encriptar en modo de lista
def cifrado_cesar(tasa, mensaje_lista):  # funcion 4
    mensaje_cifrado = ""
    for letter in mensaje_lista:
        if letter.isalpha():   #si es letra-->.isalpha
            codigo = ord(letter) + tasa # pasa de char a numreo ascii  -->chr(codigo) pasa de ascci a char
            if(letter.isupper()) and codigo > (ord('Z')):   #.isupper--> si es mayúscula
                codigo = (codigo - ord('Z')) + (ord('A')-1)   # Reasiganción de valor en caso de superar la letra
            if(letter.islower()) and codigo > (ord('z')):   #.islower--> si es minúscula
                codigo = (codigo - ord('z')) + (ord('a')-1)   # Reasiganción de valor en caso de superar la letra
            mensaje_cifrado += chr(codigo)    #asignación a la cadena de código_cifrado 
        else:
            mensaje_cifrado+= letter   # si el elemento es un número o simbolo
    return mensaje_cifrado# retornar el mensaje cifrado en string





    