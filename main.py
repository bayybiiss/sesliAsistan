from Core.Asistan import Asistan
from configurator import get_config

##PROPS
assistance = Asistan()

##DEBUG
if get_config("debug_mode"):
    assistance.listele_cihazlar()

##INIT
assistance.start_ui()



