
# función para realizar el cifrado del mensaje
# parametros de entrada:    tasa - es la tasa que se usara en la encriptación
#                           mensaje_lista - el mensaje a encriptar en modo de lista
<<<<<<< Updated upstream
def cifrado_cesar(tasa, mensaje_lista):  # funcion 4
    return # retornar el mensaje cifrado en string
=======

def cifrado_cesar(tasa, mensaje_lista):  # funcion 4

  for i in range(len(mensaje_lista)) :
      
      temp = ord(mensaje_lista[i])
      
      if (temp <= 90) :
          temp += tasa
          mensaje_lista[i] = chr((temp%65)+65)
        
      elif (temp <= 122) :
          temp += tasa
          mensaje_lista[i] = chr((temp%97)+97)


  return mensaje_lista # retornar el mensaje cifrado en string

>>>>>>> Stashed changes
