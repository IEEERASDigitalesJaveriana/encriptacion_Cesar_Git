from leerMensaje import leer_mensaje
from mensajeLista import mensaje_a_lista
from seleccionNumero import seleccionar_numero
from cifradoCesar import cifrado_cesar
from mensajetxt import mensaje_a_txt
from mensajeUser import mensaje_usuario
from txtmensaje import txt_a_mensaje
from decifradoCesar import decifrado_cesar
from mosrarMensaje import mostrar_mensaje
from mensajeDecifradotxt import mensaje_decifrado_a_txt
from os import strerror

print("Bienvenido al SW para cifrar y decifrar de RAS usando el metodo de Cesar")
selector = 0
while(selector != 3):
    print("En este programa tienes dos funciones: \n \t1. Cifrar archivo\n \
\t 2. DeCifrar archivo\n \t 3. Salir")
    selector = int(input("¿Qué quieres realizar? "))
    if(selector == 1):
        mensaje_secreto = mensaje_a_lista(leer_mensaje())
        tasa_cesar = seleccionar_numero()
        mensaje_cifrado = cifrado_cesar(tasa_cesar,mensaje_secreto)
        mensaje_a_txt(mensaje_cifrado)
        mensaje_usuario(tasa_cesar, mensaje_cifrado)
    elif(selector == 2):
        try:
            s = open('mensaje_cifrado_grupo1.txt', "rt")
            s.close()
            tasa_cesar = seleccionar_numero()
            mensaje_decifrado = decifrado_cesar(tasa_cesar,  mensaje_a_lista(txt_a_mensaje()))
            mostrar_mensaje(tasa_cesar, mensaje_decifrado)
            mensaje_decifrado_a_txt(mensaje_decifrado)
        except IOError as e:
            print("Aún no has cifrado nigún mensaje")