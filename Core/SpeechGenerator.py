from gtts import gTTS
import os
from playsound import playsound

FILENAMAE = "temp.mp3"


class SpeechGenerator:
    def __int__(self, lang, tld):
        self.lang = lang
        self.tld = tld

    def say(self, text):
        try:
            tts = gTTS(text=text, lang=self.lang, tld=self.tld, slow=False)
            tts.save(FILENAMAE)
        except UnicodeDecodeError as err:
            print(err)
        else:
            playsound(FILENAMAE)
        finally:
            os.remove(FILENAMAE)
