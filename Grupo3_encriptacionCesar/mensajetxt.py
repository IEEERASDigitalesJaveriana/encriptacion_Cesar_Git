# función para escribir el mensaje cifrado en un archivo texto
# parametros de entrada:    mensaje - mensaje encriptado en string
def mensaje_a_txt(mensaje_cifrado):  # funcion 5  
    # no tiene retorno
    # el archivo texto debe llamarse mensaje_cifrado_grupo3.txt
    mensaje_Text=open(r'mensaje_cifrado_grupo3.txt','w+') # w+ es para leer y escribir
    mensaje_Text.write(mensaje_cifrado)
    mensaje_Text.close()