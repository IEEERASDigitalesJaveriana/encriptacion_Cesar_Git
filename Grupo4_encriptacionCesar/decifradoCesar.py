#función para realizar el decifrado del mensaje
# parametros de entrada:    tasa - es la tasa que se usara en la encriptación
#                           mensaje_lista - el mensaje a desencriptar en modo de lista
def decifrado_cesar(tasa, mensaje_cifrado):  # funcion 8
    carc = ""
    for i in mensaje_cifrado:
        if i.isalpha():
            codigo=ord(i)-tasa  #ord(char)--> pasa a código ascii
            if i.islower():  #islower-->¿Es minúscula?   isupper-->¿Es mayúscula?
                if codigo < 97:
                    codigo = 123 - (codigo - 97)
            if i.isupper():
                if codigo < 65:
                    codigo = 91 - (codigo - 65)
            carc += chr(codigo)
        else:
            carc += i
        #¿Qué pasa si... pasa el circulo? Si supera la Z o z --> A o a
    return carc  # retorne el mensaje decifrado