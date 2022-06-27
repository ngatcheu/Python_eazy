import threading
import os


# https://docs.python.org/fr/3.10/library/threading.html?highlight=threading#module-threading

def tache1():
    print(" --> Tache1 attribue au thread: {}".format(threading.current_thread().name))
    print("ID du processus associe a la tache1: {}".format(os.getpid()))
    
def tache2():
    print(" --> Tache2 attribue au thread: {}".format(threading.current_thread().name))
    print("ID du processus associe a la tache2: {}".format(os.getpid()))

if __name__ == "__main__":

    #ID Processus courant
    print("ID du processus associe au main : {}".format(os.getpid()))

    #nom main thread
    print("nom Main thread : {}".format(threading.main_thread().name))
 
    #Creation des threads
    t1 = threading.Thread(target=tache1 ,name='t1')
    t2 = threading.Thread(target=tache2 ,name='t2')
    
    
    #execution des processus
    t1.start()
    t2.start()

    #Attendre jusqu'a la fin des executions
    t1.join()
    t2.join()
