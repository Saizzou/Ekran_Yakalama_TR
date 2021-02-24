from PIL import ImageGrab
import time

def yakalavegoster():
    #ss = ImageGrab.grab()
    #kayit = ss.save() # bura islem yapmio cünkü alan belli degil bi önceki satirda

    kirp = ImageGrab.grab(bbox=(0,0,300,300)) # x1=0 y1=0 x=300 y2=300 koordinatlarini yakala
    kirp.show() # kirptigimiz bölgeyi gosteriyor
    time.sleep(2) # 2 sn ara veriyor