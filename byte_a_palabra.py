def convert_to_byte(char):
    return ' '.join(format(ord(c), '08b') for c in char)


