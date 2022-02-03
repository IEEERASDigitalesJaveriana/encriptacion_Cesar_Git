
#función para leer el archivo txt que contiene  el mensaje encriptado
# el archivo se llama mensaje_cifrado_grupo1.txt

def txt_a_mensaje():  # funcion 7

    in_Stream = open("mensaje_cifrado_grupo1.txt",'r')

    return in_Stream.read() # se devuelve el mensaje en string

