'''
FUNZIONE neopixel() per board Whaveshare RP2040-Zero

Può ricevere:
- 1 --> accende il led bianco
- 0 --> spenge il led
- lista/tupla di 3 valori --> accende il led del colore indicato (0-255).
La funzione restituisce:
- 1 se il comando è andato a buon fine.
- 0 se qualcosa è andato storno oppure il parametro era incongruente.

2022/06/20 By Mondogeo, mauro.vannini@virgilio.it
'''
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
pin = Pin(16, Pin.OUT)   # set GPI=16 to output to drive NeoPixels
np = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO16 for 1 pixel
#
# ************************************
def neopixel (valore):
    try:
        # se valore è una tupla/lista di 3 termini:
        if len(valore)==3:
            if 0<=valore[0]<=255 and 0<=valore[1]<=255 and 0<=valore[2]<=255:
                np[0] = valore
                np.write()
                return 1
            else:
                return 0
    except:
        try:
            if valore==0:
                np[0] = (0,0,0)
                np.write()
                return 1
            elif valore==1:
                np[0] = (255,255,255)
                np.write()
                return 1
        except:
            return 0
# ************************************
if __name__=="__main__":
    print("Libreria non eseguibile come modulo principale")
