from machine import Pin
from neopixel import NeoPixel
from utime import sleep
pin = Pin(16, Pin.OUT)   # set GPI=16 to output to drive NeoPixels
np = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO16 for 1 pixel
#
''' **********************************
MODULE NEOPIXEL
24/4/2022, by Mauro Vannini, info@mondogeo.it

Salvare il modulo neo_pixel.py nella cartella :/lib/neo_pixel.py

Il modulo proposta sfrutta il modulo builtin in Micropython neopixel.
All'inizio del Vs. modulo per usarlo richiamatelo con 'from neo_pixel import neo_pixel'

La funzione accetta come argomenti:
    neo_pixel(1)
I valori 0 o 1 come interi per accendere alla massima luminosità come bianco o spengere il led.
    neo_pixel(0.25)
Valori frac compresi fra 0 e 1 per accendere il led con colore bianco
fra la minima potenza (0) e le massima (1)
    neo_pixel(200,0.5)
Una tupla o lista di 2 valori con i primo compreso fra 0 e 255 rappresenta l'intensità del led bianco
ed il secondo in secondi compreso fra 0 e 60 il tempo di accensione del led.
Il ritardo è realizzato con 'sleep()', blocca l'esecuzione del codice per il tempo impostato.
    neo_pixel((100,225,40))
Una tupla o lista di 3 valori interi compresi fra 0 e 255 per accenderlo del colore e potenza voluti.

La funzione restituisce:
1 se il comando è andato a buon fine ed eseguito senza errori
0 se il comando è fallito. Verificare la confruità degli argomenti
    **********************************
''' 
def neo_pixel (valore):
    try:
        # se valore è una tupla/lista di 3 termini:
        if len(valore)==3:
            if 0<=valore[0]<=255 and 0<=valore[1]<=255 and 0<=valore[2]<=255:
                np[0] = (int(valore[0]),int(valore[1]),int(valore[2]))
                np.write()
                return 1
            else:
                return 0
        # se valore è una tupla/lista di 2 termini:
        elif len(valore)==2:
            if 0<=valore[0]<=255 and 0<=valore[1]<=60:
                np[0] = (int(valore[0]),int(valore[0]),int(valore[0]))
                np.write()
                sleep(valore[1])
                np[0] = (0,0,0)
                np.write()
                return 1
            else:
                return 0
    except:
        try:
            # Se valore è un solo valore
            if 0<=valore<=1:
                np[0] = (int(255*valore),int(255*valore),int(255*valore))
                np.write()
                return 1
        except:
            return 0
# ************************************
