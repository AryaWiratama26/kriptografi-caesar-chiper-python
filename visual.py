import tkinter as tk
from tkinter import ttk
from proccess import caesar_encrypt
from tkinter.messagebox import showinfo



app_caesar_chiper = tk.Tk()
app_caesar_chiper.geometry("600x600")
app_caesar_chiper.title("Encrypt dan Ecrypt")
app_caesar_chiper.resizable(False, False)
app_caesar_chiper.configure(bg="black")



label_plain = tk.Label(app_caesar_chiper, text="Masukkan Teks:", fg="white", bg="black", )
label_plain.pack(pady=10)


entry_plain = tk.Entry(app_caesar_chiper, width=40)
entry_plain.pack(pady=5)


label_shift = tk.Label(app_caesar_chiper, text="Masukkan Keys :", fg="white", bg="black")
label_shift.pack(pady=10)

entry_shift = tk.Entry(app_caesar_chiper, width=10)
entry_shift.pack(pady=5)


def encrypt_text():
    text = entry_plain.get()
    try:
        shift = int(entry_shift.get())
        hasil = caesar_encrypt(text, shift)
        showinfo("Hasil Enkripsi", f"Data terenkripsi: {hasil}")
    except ValueError:
        showinfo("Error", "Keys harus berupa angka!")

btn_encrypt = tk.Button(app_caesar_chiper, text="Encrypt", command=encrypt_text)
btn_encrypt.pack(pady=20)

app_caesar_chiper.mainloop()