# función para seleccionar el numero que se usara para la tasa de encriptación
# Ingresar un nmero entre 1 y 25, que no se permitan los demas
def seleccionar_numero():  # funcion 3
    while True:
        num = int(input("Ingrese un numero: "))
        if(num >= 1 and num<=25):
            return num # retornar el numero seleccionado
        else:
            print("EL numero debe estar entre 1 y 25")
#print(seleccionar_numero())