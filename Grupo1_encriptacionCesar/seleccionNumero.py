
# función para seleccionar el numero que se usara para la tasa de encriptación
# Ingresar un número entre 1 y 25, que no se permitan los demas

def seleccionar_numero():  # funcion 3
<<<<<<< Updated upstream
    return # retornar el numero seleccionado
=======

  tasa = int(0)

  while tasa < 1 or tasa > 25 :

    tasa = int(input("Tasa (número) de encriptación: "))
  

  return tasa # retornar el numero seleccionado

>>>>>>> Stashed changes
