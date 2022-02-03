
# función para escribir el mensaje cifrado en un archivo texto
# parametros de entrada:    mensaje - mensaje encriptado en string

def mensaje_a_txt(mensaje_cifrado):  # funcion 5
<<<<<<< Updated upstream
    # no tiene retorno
    # el archivo texto debe llamarse mensaje_cifrado_grupo1.txt
=======

    in_Stream = open("mensaje_cifrado_grupo1.txt",'wt+') # el archivo texto debe llamarse mensaje_cifrado_grupo1.txt
    in_Stream.write(mensaje_cifrado)

    # no tiene retorno

>>>>>>> Stashed changes
