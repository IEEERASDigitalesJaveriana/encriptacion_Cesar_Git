#función para realizar el decifrado del mensaje
# parametros de entrada:    tasa - es la tasa que se usara en la encriptación
#                           mensaje_lista - el mensaje a desencriptar en modo de lista
def decifrado_cesar(tasa, mensaje_cifrado):  # funcion 8
    tamano=len(mensaje_cifrado)
    mensaje_descifrado=[]
    for x in range(tamano):
        mensaje_descifrado.append(chr(ord(mensaje_cifrado[x])+tasa))
return mensaje_descifrado# retorne el mensaje decifrado
