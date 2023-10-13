import random


carte = {
    0 : {'as_de_trefle':1,'trefle_2':2,'trefle_3':3,'trefle_4':4,'trefle_5':5,'trefle_6':6,'trefle_7':7,'trefle_8':8,'trefle_9':9,'trefle_10':10},
    1 : {'as_de_pique':1,'pique_2':2,'pique_3':3,'pique_4':4,'pique_5':5,'pique_6':6,'pique_7':7,'pique_8':8,'pique_9':9,'pique_10':10},
    2 : {'as_de_coeur':1,'coeur_2':2,'coeur_3':3,'coeur_4':4,'coeur_5':5,'coeur_6':6,'coeur_7':7,'coeur_8':8,'coeur_9':9,'coeur_10':10},
    3 : {'as_de_carreau':1,'carreau_2':2,'carreau_3':3,'carreau_4':4,'carreau_5':5,'carreau_6':6,'carreau_7':7,'carreau_8':8,'carreau_9':9,'carreau_10':10},
    4 : {'valet_trefle':10,'damme_trefle':10,'roi_trefle':10,'valet_carreau':10,'damme_carreau':10,'roi_carreau':10,'valet_coeur':10, 'damme_coeur':10,'roi_coeur':10,'valet_pique':10,'damme_pique':10,'roi_pique':10,}
    }

repetition_0 = []
repetition_1 = []
repetition_2 = []
repetition_3 = []
repetition_4 = []
nombre_de_repetition_carte_0 = []
nombre_de_repetition_carte_1 = []
nombre_de_repetition_carte_2 = []
nombre_de_repetition_carte_3 = []
nombre_de_repetition_carte_4 = []
humain = {}
ordinateur = {}



def regle():
    print('\nIl consiste à battre la Banque, représentée par le Croupier, \nsans dépasser 21 sinon vous perdez votre mise. \nSi vous atteignez le Blackjack (soit une carte valant 10 + un As) \nvotre mise est payée 3 pour 2, si vous gagnez contre le Croupier, \nmais sans atteindre 21 points, vous remportez 1 fois votre mise.\n')

def nombre_de_carte_dans_le_jeu():
    nombre_de_carte = 0
    for i in range (len(carte)):
        for _ in range (len(carte[i])):
            nombre_de_carte+=1
    return nombre_de_carte

def pioche_humain_ordinateur(nombre_de_tour):
    #nombre_de_carte = nombre_de_carte_dans_le_jeu()

    for _ in range (nombre_de_tour):  # 4 car l'humain prend 2 carte et l'ordinateur aussi, donc 2 + 2 = 4
        pioche = random.randint(0, len(carte)-1)
        while pour_contre_les_les_repetitions(pioche, nombre_de_repetition_carte_0, nombre_de_repetition_carte_1, nombre_de_repetition_carte_2, nombre_de_repetition_carte_3, nombre_de_repetition_carte_4) == False:
            pioche = random.randint(0, len(carte)-1)

        if pioche == 0:
            nombre_de_repetition_carte_0.append(pioche)

        if pioche == 1:
            nombre_de_repetition_carte_1.append(pioche)

        if pioche == 2:
            nombre_de_repetition_carte_2.append(pioche)

        if pioche == 3:
            nombre_de_repetition_carte_3.append(pioche)

        if pioche == 4:
            nombre_de_repetition_carte_4.append(pioche)
        

        detaille = transforme_nombre_en_la_carte(pioche, nombre_de_tour)
    return detaille

def pour_contre_les_les_repetitions(pioche, nombre_de_repetition_carte_0, nombre_de_repetition_carte_1, nombre_de_repetition_carte_2, nombre_de_repetition_carte_3, nombre_de_repetition_carte_4):
    if pioche == 0:
        if len(nombre_de_repetition_carte_0) == 9:
            return False
    if pioche == 1:
        if len(nombre_de_repetition_carte_1) == 9:
            return False
    if pioche == 2:
        if len(nombre_de_repetition_carte_2) == 9:
            return False
    if pioche == 3:
        if len(nombre_de_repetition_carte_3) == 9:
            return False
    if pioche == 4:
        if len(nombre_de_repetition_carte_4) == 9:
            return False
    return True

def transforme_nombre_en_la_carte(nombre_a_transforme, nombre_de_tour):

    if nombre_a_transforme == 0:
        pioche = random.randint(0, len(carte[0]))
        while pioche in repetition_0:
            pioche = random.randint(0, len(carte[0]))
        
        ListeOfKeys = carte[0].keys()
        ListeOfKeys = list(ListeOfKeys)

        ListeOfValues = carte[0].values()
        ListeOfValues = list(ListeOfValues)   
        repetition_0.append(pioche)   

    if nombre_a_transforme == 1:
        pioche = random.randint(0, len(carte[1]))
        while pioche in repetition_1:
            pioche = random.randint(0, len(carte[1]))
        ListeOfKeys = carte[1].keys()
        ListeOfKeys = list(ListeOfKeys)

        ListeOfValues = carte[1].values()
        ListeOfValues = list(ListeOfValues)    
        repetition_1.append(pioche)

    if nombre_a_transforme == 2:
        pioche = random.randint(0, len(carte[2]))
        while pioche in repetition_2:
            pioche = random.randint(0, len(carte[2]))
        ListeOfKeys = carte[2].keys()
        ListeOfKeys = list(ListeOfKeys)

        ListeOfValues = carte[2].values()
        ListeOfValues = list(ListeOfValues) 
        repetition_2.append(pioche) 

    if nombre_a_transforme == 3:
        pioche = random.randint(0, len(carte[3]))
        while pioche in repetition_3:
            pioche = random.randint(0, len(carte[3]))
        ListeOfKeys = carte[3].keys()
        ListeOfKeys = list(ListeOfKeys)

        ListeOfValues = carte[3].values()
        ListeOfValues = list(ListeOfValues)
        repetition_3.append(pioche)    

    if  nombre_a_transforme == 4:
        pioche = random.randint(0, len(carte[4]))
        while pioche in repetition_4:
            pioche = random.randint(0, len(carte[4]))
        ListeOfKeys = carte[4].keys()
        ListeOfKeys = list(ListeOfKeys)

        ListeOfValues = carte[4].values()
        ListeOfValues = list(ListeOfValues)   
        repetition_4.append(pioche)

    if nombre_de_tour == 4:
        if len(humain) != 2:
            humain.update({ListeOfKeys[pioche-1]:ListeOfValues[pioche-1]})
        else:
            ordinateur.update({ListeOfKeys[pioche-1]:ListeOfValues[pioche-1]})
    else:
        carte_a_ajoute={ListeOfKeys[pioche-1]:ListeOfValues[pioche-1]}
        return carte_a_ajoute

def choix_de_l_humain():
    choix_humain = str(input('que voulez vous faire ?\n\n   -pioche\n\n   ou\n\n   ne rien faire ?'))
    while verif_choix(choix_humain, humain) == False:
        choix_humain = str(input('Merci de choisir un choix entre\n\n   -pioche\n\n   ou\n\n   ne rien faire ?'))
    return choix_humain

def choix_de_l_ordinateur():
    nombre_de_point = 0
    listeCalcule = ordinateur.values()
    listeCalcule = list(listeCalcule)
    print(listeCalcule)
    for i in range (len(listeCalcule)):
        nombre_de_point= nombre_de_point+listeCalcule[i]

    if nombre_de_point <= 15:
        choix_ordi = 'pioche'
        
    else:
        choix_ordi = 'ne rien faire'
    
    verif_choix(choix_ordi, ordinateur)
    return choix_ordi

def verif_choix(choix_a_verif, qui_pioche):
    if choix_a_verif == 'ne rien faire' or choix_a_verif == 'r':
        return True

    if choix_a_verif == 'pioche' or choix_a_verif == 'p':
        
        detaille = pioche_humain_ordinateur(1)
        detailleOfKeys = detaille.keys()
        detailleOfKeys = list(detailleOfKeys)

        while detailleOfKeys[len(detaille)-1] in humain or detailleOfKeys[len(detaille)-1] in ordinateur:
            detaille = pioche_humain_ordinateur(1)  # il faut que mette un npuveau nombre aleatoire !!! 
            detailleOfKeys = detaille.keys()
            detailleOfKeys = list(detailleOfKeys)

        qui_pioche.update(detaille)
        return True
    
    return False

def affiche_carte_humain():
    '''
    dans cette fonction je devrai affichier toutes les carte de l'humain
    et 1 carte aléatoire de l'oridinateur,
    biensur je devrai toujours afficher la meme carte de l'ordinateur.'''
    point_humain = calcul_point(humain)
    carte_humain = humain.keys()
    carte_humain = list(carte_humain)
    print('\033[92m')
    print('voici voc carte :')
    print(carte_humain)
    print(f'vous avez un total de {point_humain} points')
    print('\033[00m')

def calcul_point(calcul_les_points_de_qui):
    nombre_de_point = 0
    listeCalcule = calcul_les_points_de_qui.values()
    listeCalcule = list(listeCalcule)
    print(listeCalcule)
    for i in range (len(listeCalcule)):
        nombre_de_point+=listeCalcule[i]
    return nombre_de_point

def victoire(choix_humain, choix_ordi):
    point_humain = calcul_point(humain)
    point_ordinateur = calcul_point(ordinateur)
    
    print(choix_ordi)
    if point_humain > 21:
        print('\033[91m')
        print(f'L\'ordinateur a gagné cette partie avec un total de {point_ordinateur} point, \ncomparé a l\'humain avec un total de {point_humain} points')
        print('\033[00m')
        return True

    if point_ordinateur > 21:
        print('\033[96m')
        print(f'L\'humain a gagné cette partie avec un total de {point_humain} point, \ncomparé a l\'ordinateur avec un total de {point_ordinateur} points')
        print('\033[00m')
        return True

    if choix_humain == 'ne rien faire' or choix_humain == 'r':   # ce test verif que si les deux joueur (ordinateur et humain) pioche le jeux s'arrete, car sinon il vas etre infinie 
        if choix_ordi == 'ne rien faire' or choix_ordi == 'r':
            if point_humain > point_ordinateur:
                print('\033[96m')
                print(f'l\humain à gagné avec un total de {point_humain} comparé a l\ordinateur qui a {point_ordinateur}')
                print('\033[00m')
            else:
                print('\033[91m')
                print(f'l\ordinateur à gagné avec un total de {point_ordinateur} comparé a l\humain qui a {point_humain}')
                print('\033[00m')
            return True
        else:
            print('l\ordinateur joue encore !!! ')
    return False

def main():
    joueur_qui_commence = random.randint(0, 1)   
    regle()
    pioche_humain_ordinateur(4)   # je suis oblige de mettre 'ttt' car de toute facon a ce moment personne a encore joue donc personne n'a encore pioche donc il y a auccun soucis 

    if joueur_qui_commence == 1:
        choix_ordi = choix_de_l_ordinateur()
        joueur_qui_commence = 0

    if joueur_qui_commence == 0:
        affiche_carte_humain()
        choix_humain = choix_de_l_humain()
        joueur_qui_commence = 1

    while victoire(choix_humain, choix_ordi) == False:
        if joueur_qui_commence == 0: 
            affiche_carte_humain()
            choix_humain = choix_de_l_humain()
            joueur_qui_commence = 1
        else:
            choix_ordi = choix_de_l_ordinateur()
            joueur_qui_commence = 0

main()

print('\033[92m')
print('\033[00m')
