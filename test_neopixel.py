''' **********************************
NEOPIXEL TEST
24/4/2022, by Mauro Vannini, info@mondogeo.it
Modulo di test di neo_pixel.py

    **********************************
''' 
from neo_pixel import neo_pixel # importa il modulo neo_pixel 
from utime import sleep
# Accende e spenge il led 1 volta per 0,2 s e stampa il valore di ritorno
print(neo_pixel(1))
sleep(0.2)
print(neo_pixel(0))
sleep(1)
# Accende il led 3 volte per tempi differenti
valore=(200,0.3)
neo_pixel(valore)
sleep(0.5)
valore=(200,0.6)
neo_pixel(valore)
sleep(0.5)
valore=(200,1)
neo_pixel(valore)
sleep(1)
# accende e spenge il led bianco con rampa
for step in range (0,100,1):
    valore=step/100
    neo_pixel(valore)
    sleep(0.01)
sleep(1)  
for step in range (100,0,-1):
    valore=step/100
    neo_pixel(valore)
    sleep(0.01)
    neo_pixel(0)
# accende e spenge il led rosso con rampa
for step in range (0,100,1):
    valore=(int(step/100*255),0,0)
    neo_pixel(valore)
    sleep(0.01)
sleep(1)  
for step in range (100,0,-1):
    valore=(int(step/100*255),0,0)
    neo_pixel(valore)
    sleep(0.01)
    neo_pixel(0)
# accende e spenge il led verde con rampa
for step in range (0,100,1):
    valore=(0,int(step/100*255),0)
    neo_pixel(valore)
    sleep(0.01)
sleep(1)  
for step in range (100,0,-1):
    valore=(0,int(step/100*255),0)
    neo_pixel(valore)
    sleep(0.01)
    neo_pixel(0)
# accende e spenge il led blu con rampa
for step in range (0,100,1):
    valore=(0,0,int(step/100*255))
    neo_pixel(valore)
    sleep(0.01)
sleep(1)  
for step in range (100,0,-1):
    valore=(0,0,int(step/100*255))
    neo_pixel(valore)
    sleep(0.01)
    neo_pixel(0)