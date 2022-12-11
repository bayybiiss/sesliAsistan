import speech_recognition as sr
from Core.UI import UI

class Asistan(sr.Recognizer):
    def __int__(self):
        super().__init__()

        ## UI
        self.window = UI()
        self.speak_button = self.window.buton_ekle_ui(command=self.sesi_algila())

    def start_ui(self):
        self.window.mainloop()
    """
    mikrofon gibi cihazların ismini döndürdüğümüz fonksiyon
    """

    def listele_cihazlar(self):
        from prettytable import PrettyTable

        table = PrettyTable()
        table.title = "AVAILABLE MICRPPHONES"
        table.field_names = ["Index", "Device Name"]
        table.add_rows(enumerate(sr.Microphone.list_microphone_names()))
        table.align = "l"
        print(table)


    def sesi_algila(self):
        pass

