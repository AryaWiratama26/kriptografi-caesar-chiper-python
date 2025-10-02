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

# while True:
    
#     data_input = input("Masukan kata : ")
#     jumlah_key = int(input("Masukan Key : "))
#     opsi = int(input("1.Encrypt\n2.Decrypt\nPilihan Kamu : "))

#     if opsi == 1:
#         hasil_encrypt = caesar_encrypt(data_input, jumlah_key)
#         print(hasil_encrypt)
#         is_decrypt = input("Apakah ingin di decrypt (y/n) : ")
#         if is_decrypt == 'y' or is_decrypt == 'Y':
#             print(caesar_decrypt(hasil_encrypt, jumlah_key))
#         else:
#             print("Input Tidak Valid")
        
#     elif opsi == 2:
#         print(caesar_decrypt(data_input, jumlah_key))
#     else :
#         print("Input tidak valid (Masukan antara 1 dan 2)")
        
#     print("\n--------------------------------------------------\n")

#     is_done = input("Apakah mau jalankan ulang program (y/n) : ")
#     if is_done == 'n' or is_done == 'N':
#         break
    
    
# print("\nProgram Berakhir")


    



    