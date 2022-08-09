from abc import ABC, abstractmethod

class EtreVivant(ABC):
    @abstractmethod
    def manger(self):
        pass
    def deplacer(self):
        pass

class Homme(EtreVivant):
    #redefinition abstract method 
    def manger(self):
        print("Je mange tout")
    def deplacer(self):
        print("Je me deplace avec mes pieds !")

class Lapin(EtreVivant):
    def manger(self):
        print("Je suis un rongeur")
    def deplacer(self):
        print("Je me deplace avec mes petites pattes !")
        
# Driver code
P = EtreVivant()
R = Homme()
R.manger()
R.deplacer
print("***********************************************************")

L = Lapin()
L.manger()
L.deplacer()


#Impossibe instancier une classse abstraire a partir d'une methode Abstraite    
