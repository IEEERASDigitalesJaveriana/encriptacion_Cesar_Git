# función para escribir el mensaje cifrado en un archivo texto
# parametros de entrada:    mensaje - mensaje encriptado en string
def mensaje_a_txt(mensaje_cifrado):  # funcion 5
    f = open("mensaje_cifrado_grupo1.txt","w+")
    f.write(str(mensaje_cifrado))
    f.close()
    # no tiene retorno
    # el archivo texto debe llamarse mensaje_cifrado_grupo1.txt
