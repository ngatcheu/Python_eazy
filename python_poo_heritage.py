class Animal:
    def __init__(self,nom,couleur,categorie) :
        print("**animal")
        self.nom = nom
        self.couleur = couleur
        self.categorie = categorie
        
    def display(self):
        print("\n je suis un animal,\n Nom : ",self.nom,"\n couleur:",self.couleur, "\n Categorie :",self.categorie)
   
    def manger(self):
        print("\n je mange un peu de tout ")
        

#classe 2
class Carnivore(Animal):
    def __init__(self, nom, couleur, categorie):
        print("**Carnivore")
        super().__init__(nom, couleur, categorie)
    
    def manger (self):
        print("\n****je mange la viande")
        
#classe 3
class Carnisauvage(Carnivore):
    '''
    Classe d'animaux  sauvages qui sont carnivores
    
    '''
    def __init__(self):
        pass
    def parler(self):
        print("je vis dans la foret !")



#main code : 
can = Carnivore("Bobo","Rouge","Chien")
can.display()
can.manger()
print("-----------------------------------------")
cs = Carnisauvage()
cs.parler()
print(cs.__doc__)



        

        
    
