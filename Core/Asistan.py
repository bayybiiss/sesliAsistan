import speech_recognition as sr
from Core.UI import UI

class Asistan(sr.Recognizer):
    def __int__(self):
        super().__init__()

        ## UI
        self.window = UI()
        self.speak_button = self.window.buton_ekle_ui(command=self.sesi_algila)

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


    @property
    def sesi_algila(self):
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = self.listen(source)

                try:
                    new_input = self.recognize_google(audio_data=audio, language="tr_TR")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results fromm Google Speech Recognition service; {0}".format(e))
                else:
                    print("Google Speech Recognition thinks you said" + new_input),
                    return new_input
        except:
            print("Cannot access to a mic.")


    def awake_asistan(self):
        input = self.sesi_algila()

        if input:
            print(input)


