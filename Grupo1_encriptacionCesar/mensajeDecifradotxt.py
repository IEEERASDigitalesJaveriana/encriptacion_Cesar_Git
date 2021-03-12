# función para escribir el mensaje decifrado en un archivo texto
# parametros de entrada:    mensaje_decifrado - mensaje desencriptado en string
def mensaje_decifrado_a_txt(mensaje_decifrado):  # funcion 10
   texto_t=open("mensaje_decifrado_grupo1.txt","w")
   texto_t.close()
   texto_t=open("mensaje_decifrado_grupo1.txt","a")
   texto_t.write("El mensaje decifrado es:  " + mensaje_decifrado)
   texto_t.close()##
