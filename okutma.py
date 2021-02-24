from PIL import ImageGrab
from PIL import Image
import datetime
now = datetime.datetime.now()

def kayit():
    yeni = ImageGrab.grab(bbox=(0,0,300,300))
    isim = "Resim" + str(now) +".png"
    kayit = yeni.save(isim)

def goster(resim):
    ac = "./" + resim
    gosterim = Image.open(ac)
    gosterim.show()

kayit() #Kayit fonksiyonu
goster("test.png") # Resmi gösterme fonksiyonu