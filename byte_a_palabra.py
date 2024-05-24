def convert_to_byte(char):
    return ' '.join(format(ord(c), '08b') for c in char)


print("Menú de opciones:")
print("1. Generar representación en byte de un carácter")
print("2. Generar representación en byte de una palabra")
option = int(input("Selecciona una opción (1/2/3): "))

if option == 1:
        char = input("Ingresa un carácter: ")
        print("Representación en byte:", convert_to_byte(char))
elif option == 2:
        word = input("Ingresa una palabra: ")
        print("Representación en byte:", convert_to_byte(word))
else:
        print("Opción inválida")
