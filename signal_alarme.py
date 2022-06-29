#https://docs.python.org/3/library/signal.html?highlight=signal#module-signal

import signal
import time

def gest_alarme(signum,stack):
    print("\n Intercepeteur : \n")
    print('Alarme :' , time.ctime())

#Assigner le gest_alarme a SIGALRM
signal.signal(signal.SIGALRM, gest_alarme)

#Declencher l'alarme apres 4 secondes
signal.alarm(4)
    
print('Heure actuel :', time.ctime())


#Retard suffisant pour que l'alarme apparaisse
time.sleep(6)
