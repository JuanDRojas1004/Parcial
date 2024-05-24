def convert_to_ascii(byte):
    ascii_char = chr(int(byte, 2))
    ascii_code = ord(ascii_char)
    return f"{ascii_char}-{ascii_code}"

