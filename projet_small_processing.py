import multiprocessing


#Afficher la liste totale
def print_records(records):
       for record in records :
           print("Name: {0}\nscore : {1}\n".format(record[0],record[1]))

#Insert un nouvel element
def insert_record(record,records):
        records.append(record)
        print("New record added!\n")

#Supprime un nouvel element
def remove_record(records):
    for record in records:
        if record[0] == 'citron' and record[1] == 'vert':
            records.remove(record)
            print("New record removed:\n")

if __name__ == "__main__":

    with multiprocessing.Manager() as manager:
        #Creation de la liste en memoire du processus serveur
        records = manager.list([('banane' , 'jaune'),('citron', 'vert'),('orange','orange')])

        #Record a ajouter
        new_record = ('goyave','vert')
        
        #Creation des processus
        p1 = multiprocessing.Process(target=remove_record, args=(records,))
        p2 = multiprocessing.Process(target=insert_record, args=(new_record,records))
        p3 = multiprocessing.Process(target=print_records, args=(records,))


     # execution du processus p1 pour supprimer ('citron','vert')
        p1.start()
        p1.join()
  
    #execution du processus p2 pour inserer ('goyave','vert')
        p2.start()
        p2.join()
       
    #Execution de p3 pour afficher la liste
        p3.start()
        p3.join()






