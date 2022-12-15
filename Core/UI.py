from tkinter import *
from tkinter import messagebox

TITLE_Font = ("Avenir", 25, "bold")
BTN_Font = ("Avenir", 18, "bold")


class UI(Tk):
    def __int__(self):
        super().__init__()
        self.title("Sesli Asistan")
        self.config(padx=50, pady=50)

    def buton_ekle_ui(self, command):
        ##Başlık
        title_lbl = Label(text="Sesli Asistan")
        title_lbl.config(pady=20, font=TITLE_Font)
        title_lbl.pack()

        ## konuşma butonu
        speak_btn = Button(text="Konuşmak İçin Bas", command=command)
        speak_btn.config(width=40, pady=40, font=BTN_Font)
        speak_btn.pack()
        return speak_btn

    def show_mic_errror(self):
        messagebox.showinfo(title="Hata", message="Bir mikrofona erişim sağlanamadı")