#!/usr/bin/env python

import signal
import sys

#Definition du gestionnaire de signal
def signal_handler(sig , frame):
     print(' vous avez appuyer ctrl+c')
     sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Appuyer ctrl+c')

#Mettre le processus en veille 
signal.pause()
