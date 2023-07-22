# Ceasar Cipher

def rot13(message):
    encoded_message = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
            encoded_message += char(rotated)
        else:
            encoded_message += char
    return encoded_message

