import threading, time

#https://docs.python.org/fr/3.10/library/threading.html?highlight=lock#threading.Lock
#global variable x  

x = 0

def increment ():
    global x
    x += 1

def thread_tache(lock):
    time.sleep
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()

def main_tache():
    global x
    # initialisateur la variable globale x a 9
    x = 0
    lock = threading.Lock()
    #Creation des threads
    t1 = threading.Thread(target=thread_tache, args=(lock,))
    t2 = threading.Thread(target=thread_tache, args=(lock,))

    #start les threads
    t1.start()
    t2.start()

    #Attente jusqu a la fin des executions
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_tache()
        print("iteration {0}: x = {1}".format(i,x))
