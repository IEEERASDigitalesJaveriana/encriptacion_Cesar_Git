#función para realizar el cifrado del mensaje
# parametros de entrada:    tasa - es la tasa que se usara en la encriptación
#                           mensaje_lista - el mensaje a encriptar en modo de lista
def cifrado_cesar(tasa, mensaje_lista):  # funcion 4
    carc = ""
    for i in mensaje_lista:
        if i.isalpha():
            codigo=ord(i)+tasa  #ord(char)--> pasa a código ascii
            if i.islower():  #islower-->¿Es minúscula?   isupper-->¿Es mayúscula?
                if codigo > 122:
                    codigo = 96 + (codigo - 122)
            if i.isupper():
                if codigo > 90:
                    codigo = 64 + (codigo - 90)
            carc += chr(codigo)
        else:
            carc += i
        #¿Qué pasa si... pasa el circulo? Si supera la Z o z --> A o a
    return carc  # retornar el mensaje cifrado en string
#print(cifrado_cesar(25,list("Algo")))

