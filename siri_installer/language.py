from . import logo, console, bilgi, hata, soru
from rich.panel import Panel
from time import sleep
from json import loads

def importlang ():
    COUNTRY = "Turkey"
    LANGUAGE = "TR"
    TZ = "Europe/Istanbul"
    while True:
        console.clear()
        logo()
        bilgi("[blue]\n\n[1] Türkçe\n[2] Azərbaycanca\n[3] English[/]")
        try:   
            Dil = int(soru("[bold yellow]Bir dil seçin / Please select a language[/]"))
        except ValueError:
            hata('🔢 Just Enter Number! / Sadece Sayı! / Yalnız nömrə!')
            sleep(2)

        if Dil == "1":
            COUNTRY = "Turkey"
            LANGUAGE = "TR"
            TZ = "Europe/Istanbul"
            break
        elif Dil == "2":
            COUNTRY = "Azerbaijan"
            LANGUAGE = "AZ"
            TZ = "Asia/Baku"
            break
        elif Dil == "3":
            COUNTRY = "United Kingdom"
            LANGUAGE = "EN"
            TZ = "Europe/London"
            break
        else:
            console.clear()
            hata('🏴 Wrong choice! / Yanlış seçim! / Səhv seçim!')
            sleep(2)

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./siri_installer/language/{LANGUAGE}.sirijson", "r").read())["STRINGS"]
