# Pequeño proyecto de prueba que lanza un dado de N caras, donde N es introducido por el usuario

from random import choice
import re # módulo para control de expresiones regulares

dado = 0
validacion = r"[0-9]+" # expresión regular que vamos a estar comprobando en la entrada de datos del usuario

while True:
  dado = input("Número de caras del dado (0 para salir): ")
  if re.match(validacion,dado):
    dado = int(dado)
    if dado == 0:
      break
    else:
      print("El resultado de la tirada fue: " + str(choice(range(1,dado+1)))+"\n--------------------------")
  else:
    print("¡El valor introducido DEBE ser un número!\n--------------------------")

# Esto es un comentario final para probar la integración con el control de versiones de GitHub