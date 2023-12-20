import random
import string

def presentacion():
  nombre = input("Ingrese su nombre: ")
  print(f"¡Bienvenido {nombre} ¡Comencemos el juego")

def palabra_oculta():
  palabras = ["jugo", "manzana", "lobo", "bosque", "tiburon", "celeste", "botella", "servilleta","araña", "naranja", "frambuesa"]
  return random.choice(palabras)

def mostrar_linea(palabra):
    lineas = "_ " * len(palabra)
    return lineas

def es_letra(caracter):
    return caracter in string.ascii_lowercase

def juego():
  presentacion()
  palabra_oculta_seleccionada = palabra_oculta()
  lineas = mostrar_linea(palabra_oculta_seleccionada)
  intentos = 6

  print(f"El juego consiste en adivinar la palabra la palabra oculta, cuentas con {intentos} intentos. Superados los intentos, pierdes.")
  print(lineas)

  while intentos > 0:
        caracter = input("Ingresa una letra o la palabra completa: ").lower()

        if len(caracter) == 1 and es_letra(caracter):  ## Si se ingresa una letra
            if caracter in palabra_oculta_seleccionada: 
                ### Reemplazo las líneas con la letra en la posición que corresponde
                reemplazo_lineas = ""
                for i in range(len(palabra_oculta_seleccionada)):
                    if palabra_oculta_seleccionada[i] == caracter:
                        reemplazo_lineas += caracter
                    else:
                        reemplazo_lineas += lineas[i]
                lineas = reemplazo_lineas
                print(f"¡Correcto! {lineas}")
            else:
                intentos -= 1
                print(f"Fallaste. Te quedan {intentos} intentos.")
        else:  ## Si ingresamos la palabra completa o no es una letra
            if caracter == palabra_oculta_seleccionada:
                print("¡Felicidades! Has encontrado la palabra oculta.")
                break
            else:
                if es_letra(caracter)== False: 
                    print("Por favor, ingresa solo letras del abecedario.")
                else:
                    intentos -= 1
                    print(f"El caracter ingresado no es válido. Te quedan {intentos} intentos.")

        if lineas.replace(" ", "") == palabra_oculta_seleccionada:
            print("¡Felicidades! Has encontrado la palabra oculta.")
            break

        if intentos == 0:

          print(f"Lo siento, has agotado todos tus intentos. La palabra era: {palabra_oculta_seleccionada}")

# Iniciamos el juego
juego()