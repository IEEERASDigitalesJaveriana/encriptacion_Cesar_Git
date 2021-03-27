#función para leer el archivo txt que contiene  el mensaje encriptado
# el archivo se llama mensaje_cifrado_grupo1.txt
def txt_a_mensaje():  # funcion 7
    archivo=open("mensaje_cifrado_grupo4.txt","rt")
    mensaje = archivo.read()
    archivo.close()
    return mensaje # se devuelve el mensaje en string