def convert_to_byte(char):
    return ' '.join(format(ord(c), '08b') for c in char)

if __name__ == '__main__':
    print("Menú de opciones:")
    print("1. Generar representación en byte de un carácter")

option = int(input("Selecciona una opción (1/2/3): "))

if option == 1:
        char = input("Ingresa un carácter: ")
        print("Representación en byte:", convert_to_byte(char))