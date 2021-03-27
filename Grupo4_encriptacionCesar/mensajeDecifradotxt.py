# función para escribir el mensaje decifrado en un archivo texto
# parametros de entrada:    mensaje_decifrado - mensaje desencriptado en string
def mensaje_decifrado_a_txt(mensaje_decifrado):  # funcion 10
    archivo = open("mensaje_decifrado_grupo4.txt",'wt')
    archivo.write(mensaje_decifrado + "\n")
    archivo.close()
    # no tiene retorno
    # el archivo texto debe llamarse mensaje_decifrado_grupo1.txt