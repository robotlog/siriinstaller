MESAJ="Siri İOS Otomatik Deploy Kuruluma Hoş Geldiniz"
MESAJ+="\nTelegram: @SiriUserBot"
echo y | apk update
clear
echo -e $MESAJ
echo "Python Yükleniyor"
echo y | apk add python3
clear
echo -e $MESAJ
echo "Git Yükleniyor"
echo y | apk add git
clear
echo -e $MESAJ
echo "TeleThon Yükleniyor"
python3 -m pip install telethon
echo "Repo klonlanıyor..."
git clone https://github.com/ErdemBey1/Siriinstaller
clear
echo -e $MESAJ
clear
echo -e $MESAJ
echo "Gereksinimler Yükleniyor"
cd Siriİnstaller
python3 -m pip install wheel
python3 -m pip install -r requirements.txt
clear
python3 -m siri_installer
