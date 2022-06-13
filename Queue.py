import multiprocessing

def add_list(mylist, q):
   #Ajouter les elemets dans la liste
   for n in mylist:
       print("ajout: ",n)
       q.put(n)

def print_queue(q):
    print("les elemets presents dans votre queue:")
    while not q.empty():
        print(q.get())
    print("Notre Queue est vide!")

if __name__ == "__main__":
    #notre liste
    mylist = ["fabrice","toto","titi","tata"]

    #creation de notre queue
    q =  multiprocessing.Queue()

    #Creation de notre processus
    p1 = multiprocessing.Process(target=add_list,args=(mylist,q))
    p2 = multiprocessing.Process(target=print_queue,args=(q,))

   #Execution du processus p1 
    p1.start()
    p1.join()

    #Affichage de la liste
    print("******** Apres insertion ****************")
    #Execution du processus p2 
    p2.start()
    p2.join()
