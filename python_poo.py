#https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants
#Classe et objet 
#Definition de la classe 


class Homme:
    '''
    Description de ma classe homme
    '''
    #constructeur 
    def __init__(self,nom,age):
        #attributs
        self.nom = nom
        self.age = age
    #methode
    def show (self):
        print("je suis ",self.nom,", j'ai ",self.age) 
        
#Programme principal 
if __name__ == "__main__":
    #creer un objet
    h1 = Homme("Toto",12)
    #Afficher l'objet
    h1.show()
    print(h1.__doc__) # description de la classe
    print(h1.__dict__) # convert les attribut en dict
    print(h1.__module__) 
    del h1 # Supprimer l'objet 
    h1.show() # va retourner une erreur
    
