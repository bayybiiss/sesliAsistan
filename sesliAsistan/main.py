from Core.Asistan import Asistan
import json

FILENAME = "configuration.json"
DEFAULT_CONFIG = {
    "lang": "tr",
    "tld": "com.tr"
}


def make_configuration():
    try:
        ## configuration dosyası aç
        with open(FILENAME, "r") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        with open(FILENAME, "w") as new_config_file:
            json.dump(DEFAULT_CONFIG, new_config_file, indent=4)
            make_configuration()
    else:
        lang = config_data.get("lang")
        tld = config_data.get("tld")

        asistan = Asistan(lang=lang, tld=tld)
        asistan.print_devices()
        asistan.start_ui()


make_configuration()
