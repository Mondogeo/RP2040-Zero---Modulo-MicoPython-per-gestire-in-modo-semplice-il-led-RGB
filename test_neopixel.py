'''
Programma di test per il modulo neo_led.

2022/06/20 By Mondogeo, mauro.vannini@virgilio.it
'''
from neo_led import neopixel #importo la nostra funzione
from utime import sleep
from random import randint

#
print(neopixel (1)) #accende il led e stampa il valore di ritorno
sleep(1)
#
print(neopixel (0)) #spenge il led e stampa il valore di ritorno
sleep(1)
#
neopixel ((255, 0, 0)) #accende il led rosso alla massima potenza
sleep(1)
#
neopixel ((0, 255, 0)) #accende il led verde alla massima potenza
sleep(1)
#
neopixel ((0, 0, 255)) #accende il led blu alla massima potenza
sleep(1)
#
neopixel (0) #spenge il led
sleep(1)
#
# Accendiamo il led con funzioni casuali in un ciclo infinito
#
def ridu(n):
    '''
    Funzione per ridurre i valori fra 0 e 255
    0 --> 255 invariati
    256 --> 511 discendenti fra 255 e zero
    e così via in avanti
    '''
    num=n-(n//512)*512 # riporto il valore fra 0 e 511
    
    if num<256:
        return int(num)
    else:
        return int(512-num)
#
while True:
    index=0
    step=5
    r=0
    rr=randint(0,6) #gamma di escursione rosso
    v=0
    rv=randint(0,6) #gamma di escursione verde
    b=0
    rb=randint(0,6) #gamma di escursione blu
    max_cicli=randint(0,6) #numero massimo di cicli
    
    print(rr,rv, rb, max_cicli) #

    while index<255*max_cicli:
        
        r=(r+step*rr)
        v=(v+step*rv)
        b=(b+step*rb)
        
        neopixel ((ridu(r), ridu(v), ridu(b)))
        
        index+=step
        
        sleep(0.03)
    #
    neopixel (0)
    sleep(0.2)
