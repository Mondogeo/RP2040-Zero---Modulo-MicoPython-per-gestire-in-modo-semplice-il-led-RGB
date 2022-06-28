# RP2040-Zero---Modulo-MicoPython-per-gestire-in-modo-semplice-il-led-RGB
Il modulo mette a disposizione un unica funzione per utilizzare il led RGB del RP2040 Zero come un semplice led on/off, come led temporizzato oppure gestirne i singoli colori. 
Sulla scheda RP2040 Zero è presente un led rgb del tipo WS2812 NeoPixel.
Per gestirlo in MicroPython è presente la librteria builtin descritta in
https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html

![image](https://user-images.githubusercontent.com/79664812/164966373-7f1f14d5-aa6c-4b71-953c-df89e9ab7fd1.png)

Il modulo di gestione neo_pixel.py va salvato nella cartella lib dello Zero.

![files](https://user-images.githubusercontent.com/79664812/164966242-fa23206d-bd49-44ff-930c-4d892522259c.jpg)

Nel nostro programma dobbiamo richiamare
from neo_pixel import neo_pixel
A questo punto avremo a disposizione la funzione neo_pixel(valore).

La funzione accetta come argomenti:

    neo_pixel(1)
    
Il valore 1 per accendere alla massima luminosità come led bianco.

    neo_pixel(0)
    
Il valore 0 per soengere il led.

    neo_pixel((100,225,40))
    
Una tupla o lista di 3 valori interi compresi fra 0 e 255 per accenderlo del colore e potenza voluti.

La funzione restituisce:

1 se il comando è andato a buon fine ed eseguito senza errori

0 se il comando è fallito. Verificare la confruità degli argomenti

Il modulo test_neopixel.py permette di testare queste prestazioni.
