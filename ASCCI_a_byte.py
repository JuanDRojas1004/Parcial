def convert_to_ascii(byte):
    ascii_char = chr(int(byte, 2))
    ascii_code = ord(ascii_char)
    return f"{ascii_char}-{ascii_code}"

print("Menú de opciones:")
option = int(input("Selecciona una opción (1): "))
if option == 1:
        byte = input("Ingresa un byte en formato binario (8 dígitos): ")
        print("Representación ASCII:", convert_to_ascii(byte))
else:
    print("Opción inválida")