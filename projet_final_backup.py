#! /usr/bin/env python

import  glob, datetime ,multiprocessing
import time , signal , sys
from zipfile import ZipFile


def scan_compteur(path,q):
    #initialisation des nombres de fichiers 
    nbrDir = nbrTxt = autre = 0
    print("Processus 1 starts:")
    time.sleep(1)

    nbrDir = len(glob.glob(path+'**/*/', recursive = True))
    nbrTxt = len(glob.glob(path+'**/*.txt', recursive = True))
    autre  = len(glob.glob(path+'**/*.*', recursive = True)) - nbrTxt

    #conversion des nbres en chaines  de caractere et ajout a la chaine
    q.put("Nombre  totale de sous repertoire : "+str(nbrDir))
    q.put("Nombre de fichier .txt: " + str(nbrTxt))
    q.put("Autres fichiers :"+str(autre))

def scan_archive(path,q):
    now = datetime.datetime.now()
    print("Processus 2 starts: ")
    time.sleep(1)
    
    #Conversion du temp en chaine de charactere
    today = now.strftime("%m_%d_%Y_%H_%M_%S")
    nom_zipfile = 'backup_ '+today+'.zip'
    q.put("dernier backup : "+today)
    
    #Ajouter un fichier dans notre backup
    files = glob.glob(path+'**/*.txt', recursive = True)
    for data in files :
        with Zipfile (nom_zipfile,'w') as zp:
            zp.write(data)

def print_infos(path , q):
    print("Processus 3 starts :")
    time.sleep(1)
    print("*"*50,"\nInfos sur le dossier:", path)
    #recuperer les infos dans notre queue
    while not q.empty():
        print(q.get())

if __name__ == "__main__":
    #creating multiprocessing Queue
    q = multiprocessing.Queue()
    path = "/home/inverse"

 #Creation des processus
    p1 = multiprocessing.Process(target=scan_compteur, args=(path, q))
    p2 = multiprocessing.Process(target=scan_archive, args=(path,q))
    p3 = multiprocessing.Process(target=print_infos, args=(path,q))

    
    # execution du processus p1 pour supprimer ('citron','vert')
    p1.start()
    p1.join()
  
    #execution du processus p2 pour inserer ('goyave','vert')
    p2.start()
    p2.join()
       
    #Execution de p3 pour afficher la liste
    p3.start()
    p3.join()






        

        
    
    
