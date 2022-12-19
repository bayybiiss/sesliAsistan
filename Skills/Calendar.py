from datetime import datetime
import random

class Calendar:
    time_keywords =[
        "saat","saat kaç","saat ne", "hangi saat",
        "hangi saatteyiz", "saat kaç oldu",
        "saatin var mı","saat kaçı gösteriyor"
    ]
    date_keywords = [
        "tarih", "bugünün tarihi ne", "ayın kaçı", "bugün ayın kaçı",
        "hangi gündeyiz", "bugün hangi gün","ayın kaçındayız",
        "hangi gün", "tarihi söyler misin","hangi aydayız",
        "hangi yıldayız"
    ]
    def __init__(self):
        # Todo: config
        pass
    def get_time(self):
        hour = datetime.now().hour
        min = str(datetime.now().minute)

        if hour in [1, 11, 21, 5, 15, 8, 18]:
            hour = str(hour) + " i"
        elif hour in [2, 12, 22, 7, 17, 28]:
            hour = str(hour) + " yi"
        elif hour in [6, 16]:
            hour = str(hour) + " yi"
        elif hour in [9, 19, 10]:
            hour = str(hour) + " u"
        elif hour in [4, 14, 3, 13, 23, 24]:
            hour = str(hour) + " ü"
        elif hour in [0, 00]:
            hour = str(hour) + " ı"
        else:
            hour = str(hour)

        sentences =[
            f"Saat, {hour} {min} geçiyor",
            f"Şu anda saat {hour} {min} geçiyor.",
            f"{hour} {min} geçiyor.",
            f"Şu anda {hour}{min} geçiyor."
        ]
        return random.choice(sentences)

    def get_date(self):
        month_names =[
            "Ocak","Şubat","Mart","Nisan","Mayıs","Haziran",
            "Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"
        ]
        day_names =[
            "Pazartesi","Salı","Çarşamba","Perşembe","Cuma",
            "Cumartesi","Pazar"
        ]

        date_num = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        is_important = self.is_an_important_date(date_num,month)

        day = day_names[datetime.now().weekday()]
        month =month_names[datetime.now().month-1]
        sentences =[
            f"Bugün {date_num} {month}, {day}",
            f"{date_num} {month} {year}, {day}",
            f"{date_num} {month}, bugün günlerden {day}"
        ]

        return (random.choice(sentences), is_important)

    def is_an_important_date(self,day,month):
        #todo: read from a csv
        # return sentence & func or none
        return None

time = Calendar().get_date()
print(time)