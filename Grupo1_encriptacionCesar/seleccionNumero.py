# función para seleccionar el numero que se usara para la tasa de encriptación
# Ingresar un nmero entre 1 y 25, que no se permitan los demas
def seleccionar_numero():  # funcion 3
    Num=input("Ingrese el número que desea usar de encripatción\n")
    Num=int(Num)
    
    while Num > 25 or Num < 1:
        print("Ingrese un número entre 1 y 25")
        Num=input("Ingrese el número que desea usar de encripatción:\n")
        Num=int(Num)
        
    return Num
