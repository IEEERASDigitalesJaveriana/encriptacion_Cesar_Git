#función para realizar el cifrado del mensaje
# parametros de entrada:    tasa - es la tasa que se usara en la encriptación
#                           mensaje_lista - el mensaje a encriptar en modo de lista
def cifrado_cesar(tasa, mensaje_lista):  # funcion 4
    mensaje_lista = ""
    msg = upper(mensaje_lista)
    for char in msg:
        if char.isalpha():
            cifrado = ord(char) + tasa
            if char > 'Z':
                cifrado = cifrado -ord('Z') + (ord('A')-1)
        else:
            mensaje +=cifrado
    return mensaje# retornar el mensaje cifrado en string