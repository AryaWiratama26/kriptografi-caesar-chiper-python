def caesar_encrypt(kata, keys):
    hasil_encrypt = ""

    for i in kata:
        if i.isupper():
            hasil_encrypt += chr((ord(i) - ord('A') + keys) % 26 + ord('A'))

        elif i.islower():
            hasil_encrypt += chr((ord(i) - ord('a') + keys) % 26 + ord('a'))

        else:
            hasil_encrypt += i

    return hasil_encrypt

def caesar_decrypt(kata, keys):
    return caesar_encrypt(kata, 26 - keys)

