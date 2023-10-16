import tkinter as tk
import tkinter.messagebox

def harf_degistir(kelime):
    kelime = kelime.replace("ı", "(i|ı|I|İ)").replace("i", "(i|ı|I|İ)").replace("o", "(ö|o|Ö|O)").replace("ö", "(ö|o|Ö|O)").replace("c", "(ç|c|C|Ç)").replace("ç", "(ç|c|C|Ç)").replace("u", "(ü|u|Ü|U)").replace("ü", "(ü|u|Ü|U)").replace("s", "(s|ş|S|Ş)").replace("ş", "(s|ş|S|Ş)").replace("g", "(g|ğ|G|Ğ)").replace("ğ", "(ğ|g|G|Ğ)").replace(" ", r"\s")
    return kelime

def goster():
    kelime = kelime_giris.get("1.0", "end-1c")  # Get text from the input Text widget
    yenikelime = harf_degistir(kelime)
    sonuc_text.delete("1.0", tk.END)  # Clear the existing content in the result Text widget
    sonuc_text.insert(tk.END, yenikelime)  # Insert the new result
    panoya_kopyala_button.config(state="normal")

def panoya_kopyala():
    kelime = sonuc_text.get("1.0", "end-1c")  # Get text from the result Text widget
    root.clipboard_clear()
    root.clipboard_append(kelime)
    root.update()
    tkinter.messagebox.showinfo("Bilgi", "Sonuç panoya kopyalandı.")

root = tk.Tk()
root.title("Regex Oluşturucu")

baslik_etiketi = tk.Label(root, text="Regex Oluşturucu", font=("Helvetica", 16))
baslik_etiketi.pack(pady=10)

kelime_etiketi = tk.Label(root, text="Kelime:")
kelime_etiketi.pack()
kelime_giris = tk.Text(root, height=4, width=40)
kelime_giris.pack(pady=5)

olustur_dugme = tk.Button(root, text="Oluştur Regex", command=goster)
olustur_dugme.pack(pady=10)
panoya_kopyala_button = tk.Button(root, text="Kopyala", state="disabled", command=panoya_kopyala)
panoya_kopyala_button.pack()

sonuc_text = tk.Text(root, height=4, width=40)
sonuc_text.pack()

metin = "Created By Cevher GEŞGİN"
metin_etiketi = tk.Label(root, text=metin, font=("Arial", 10), fg="gray")
metin_etiketi.place(relx=1, rely=1, anchor="se")

# Add a label with the text "masterch" at the top
text1 = r"""

  __  __           _         _______        _      
 |  \/  |         | |       |__   __|      | |     
 | \  / | __ _ ___| |_ ___ _ __| | ___  ___| |__   
 | |\/| |/ _` / __| __/ _ \ '__| |/ _ \/ __| '_ \  
 | |  | | (_| \__ \ ||  __/ |  | |  __/ (__| | | | 
 |_|  |_|\__,_|___/\__\___|_|  |_|\___|\___|_| |_| 
                                                   
                                                   


"""
masterch_label = tk.Label(root, text=text1, font=("Courier", 10))
masterch_label.pack(side="top", pady=20)

root.geometry("500x450")

root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))

root.mainloop()
