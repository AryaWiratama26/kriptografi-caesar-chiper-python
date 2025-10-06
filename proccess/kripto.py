from main import caesar_decrypt, caesar_encrypt

while True:
    
    data_input = input("Masukan kata : ")
    jumlah_key = int(input("Masukan Key : "))
    opsi = int(input("1.Encrypt\n2.Decrypt\nPilihan Kamu : "))

    if opsi == 1:
        hasil_encrypt = caesar_encrypt(data_input, jumlah_key)
        print(hasil_encrypt)
        
    elif opsi == 2:
        print(caesar_decrypt(data_input, jumlah_key))
    else :
        print("Input tidak valid (Masukan antara 1 dan 2)")
        
    print("\n--------------------------------------------------\n")

    is_done = input("Apakah mau jalankan ulang program (y/n) : ")
    if is_done == 'n' or is_done == 'N':
        break
    
    
print("\nProgram Berakhir")


    



    