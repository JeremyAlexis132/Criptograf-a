print("Algoritmo del cifrado César en Python")
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def cifrado_cesar(texto, desplazamiento):
  # la variable desplazamiento es n, la llave
  # texto es el mensaje a cifrar
  # Arreglo del alfabeto donde A tiene índice 0 y Z tiene índice 26

  textoCifrado = ""

  for caracter in texto:
    posicionActual = alfabeto.index(caracter)
    # Calcular la nueva posición con el desplazamiento
    nuevaPosicion = (posicionActual + desplazamiento) % 26
    # Obtener el carácter cifrado del arreglo
    textoCifrado += alfabeto[nuevaPosicion]

  return textoCifrado
  
def descifrado_cesar(texto, desplazamiento):

  #Proceso inverso al anterior, solo se cambia el signo a - en el modulo
  textoDescifrado = ""
  for caracter in texto:
    posicionActual = alfabeto.index(caracter)
    # Calcular la nueva posición con el desplazamiento
    nuevaPosicion = (posicionActual - desplazamiento) % 26
    # Obtener el carácter cifrado del arreglo
    textoDescifrado += alfabeto[nuevaPosicion]

  return textoDescifrado

def main():
  opcion = input("¿Desea cifrar o descifrar un texto? (cifrar/descifrar): ").strip().lower()
  desplazamiento = int(input("Ingrese el desplazamiento (n): "))
  texto = input("Ingrese el texto a transformar: ").upper()  # Conversion a mayúsculas

  if opcion == "cifrar":
    textoCifrado = cifrado_cesar(texto, desplazamiento)
    print("Texto cifrado:", textoCifrado)
  elif opcion == "descifrar":
    textoCifrado = descifrado_cesar(texto, desplazamiento)
    print("Texto descifrado:", textoCifrado)
  else:
    print("Opción no válida.")
    return

main()