import speech_recognition as sr
from Core.UI import UI
from Core.SpeechGenerator import SpeechGenerator


class Asistan(sr.Recognizer):
    def __int__(self, **kw):
        super().__init__()

        ## UI
        self.window = UI()
        self.speak_button = self.window.buton_ekle_ui(command=self.awake_asistan)

        ## Speech
        lang = kw.get("lang") if kw.get("lang") else "tr"
        tld = kw.get("tld") if kw.get("tld") else "tld"
        self.generator = SpeechGenerator(lang=lang, tld=tld)

    def start_ui(self):
        self.window.mainloop()

    """
    mikrofon gibi cihazların ismini döndürdüğümüz fonksiyon
    """

    def listele_cihazlar(self):
        from prettytable import PrettyTable

        table = PrettyTable()
        table.title = "AVAILABLE MICROPHONES"
        table.field_names = ["Index", "Device Name"]
        table.add_rows(enumerate(sr.Microphone.list_microphone_names()))
        table.align = "l"
        print(table)

    def __update_btn_lbl(self, is_listening):
        new_text = "Dinliyorum..." if is_listening else "Konuşmak için bas"
        self.speak_button.config(text=new_text)
        self.speak_button.update()

    def __sesi_algila(self):
        try:
            with sr.Microphone() as source:
                self.__update_btn_lbl(True)

                audio = self.listen(source)

                try:
                    new_input = self.recognize_google(audio_data=audio, language="tr_TR")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results fromm Google Speech Recognition service; {0}".format(e))
                else:
                    return new_input
        except:
            self.window.show_mic_errror()
        finally:
            self.__update_btn_lbl(False)

    def awake_asistan(self):
        input = self.__sesi_algila()

        if input and input.casefold() == "Merhaba".casefold():
            self.generator.say(text="Merhaba, nasıl yardımcı olabilrim?")
        else:
            print(input)
