
#función para realizar el decifrado del mensaje
# parametros de entrada:    tasa - es la tasa que se usara en la encriptación
#                           mensaje_lista - el mensaje a desencriptar en modo de lista

def decifrado_cesar(tasa, mensaje_cifrado):  # funcion 8
<<<<<<< Updated upstream
    return # retorne el mensaje decifrado
=======

    for i in range(len(mensaje_cifrado)) :
        
        posASCII = ord(mensaje_cifrado[i])
        
        if (posASCII <= 90) :
            posASCII -= tasa
            mensaje_cifrado[i] = chr((posASCII%65)+65)
          
        elif (posASCII <= 122) :
            posASCII -= tasa
            mensaje_cifrado[i] = chr((posASCII%97)+97)

    return mensaje_cifrado # retorne el mensaje decifrado

>>>>>>> Stashed changes
