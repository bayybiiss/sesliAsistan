import json

FILENAME = "configuration.json"
DEFAULT_CONFIG = {
    "personalization":{
        "user": {
            "name": "Yusuf"
        }
    },
    "speechRecognation":{
        "language": "tr_TR"
    },
    "speechGeneration":{
        "language": "tr",
        "tld": "com.tr",
        "slow_talk":"false"
    },
    "debug_mode":"true",
    "services":{

    }
}

def __create_config_file():
    with open(FILENAME, "w") as new_config_file:
        json.dump(DEFAULT_CONFIG, new_config_file, indent=4)
    print("*** New config file has been created. ***")

def __return_default(param: str, *args):
    def_config = DEFAULT_CONFIG.get(param)
    for arg in args:
        new_value = def_config.get(arg)
        if new_value:
            if new_value == "true" or new_value == "false":
                def_config = bool(new_value == "true")
            else:
                def_config = new_value
    return def_config

def get_config(param: str, *args):
    try:
        with open(FILENAME, "r") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        __create_config_file()
        return __return_default(param, args)
    else:
        found_config = config_data.get(param)

        for arg in args[0]:
            new_value = found_config.get(arg)
            if new_value:
                if new_value == "true" or new_value == "false":
                    found_config = bool(new_value == "true")
                else:
                    found_config = new_value

        return found_config if not (found_config is None) else __return_default(param, args)

print(get_config("speechRecognation","language"))


# def make_configuration():
#     try:
#         ## configuration dosyası aç
#
#     except FileNotFoundError:
#         with open(FILENAME, "w") as new_config_file:
#             json.dump(DEFAULT_CONFIG, new_config_file, indent=4)
#             make_configuration()
#     else:
#         lang = config_data.get("lang")
#         tld = config_data.get("tld")
