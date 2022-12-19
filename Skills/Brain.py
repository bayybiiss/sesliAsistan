from Core.SpeechGenerator import SpeechGenerator
from Skills.Calendar import Calendar
class Brain:
    def __init__(self):
        self.speak = SpeechGenerator().say

    def __chech(self, input, keywords):
        return bool(any(key in input for key in keywords))

    def make_sense(self,input):
        if not input:
            return
        i = input.casefold()

        if self.__chech(i,Calendar.time_keywords):
            self.speak(Calendar().get_time())
        elif self.__chech(i,Calendar.date_keywords):
            self.speak(Calendar().get_date()[0])
        else:
            #todo log to csv
            self.speak("ne söylediğini anlayamadım")

print(Brain().make_sense("hangi gündeyiz"))