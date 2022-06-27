import multiprocessing

#La synchronisation des processus: les verrous et les semaphores
#de resoudre la concurrence sur des ressources critiques

def double(nbr, lock):
    print("p1 starts")

    #Mettre un verrou
    lock.acquire()
    nbr.value = nbr.value * 2

    #Liberer le verrou pour le processous suivant 
    lock.release()
    print("p1 stops")


def carre (nbr, lock):
    print("p2 starts")
    
    #Mettre un verrou
    lock.acquire()
    nbr.value = nbr.value * nbr.value
  
    #Liberer le verrou pour le processous suivant
    lock.release()
    print("p2 stops")


def main ():
    #initialisation du nombre dans la memoire partagee
    nombre = multiprocessing.Value('i', 2)

    #creation du verrou
    lock = multiprocessing.Lock()


    #Creation des nouveaux processus
    p1 = multiprocessing.Process(target=double, args=(nombre,lock))
    p2 = multiprocessing.Process(target=carre, args=(nombre,lock))

    #execution des processus
    p1.start()
    p2.start()

    #Attendre jusqu'a la fin des executions
    p1.join()
    p2.join()

    #Print nombre
    print("Nombre final{}".format(nombre.value))
    
if __name__ == "__main__":

    main()
 


    
