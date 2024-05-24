from ASCCI_a_byte import convert_to_ascii 
from byte_a_palabra import convert_to_byte

print("Menú de opciones:")
print("1. Generar representación en byte de un carácter")
print("2. Generar representación en byte de una palabra")
print("3. Generar representación ASCII de un byte")

option = int(input("Selecciona una opción (1/2/3): "))

if option == 1:
        char = input("Ingresa un carácter: ")
        print("Representación en byte:", convert_to_byte(char))
elif option == 2:
        word = input("Ingresa una palabra: ")
        print("Representación en byte:", convert_to_byte(word))
elif option == 3:
        byte = input("Ingresa un byte en formato binario (8 dígitos): ")
        print("Representación ASCII:", convert_to_ascii(byte))
else:
        print("Opción inválida")