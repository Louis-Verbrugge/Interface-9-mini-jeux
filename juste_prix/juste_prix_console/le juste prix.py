import random



    
def regle(choix_ordi):
    print(f'Chacun, de gauche à droite (vue du téléspectateur), \nen commençant par le plus à gauche (première estimation) \nou le dernier appelé (estimations suivantes), donne une seule estimation de ({choix_ordi}) par exemple ;). \nLe plus proche du juste prix (sans le dépasser) \nremporte le cadeau et rejoint l\'animateur.')

def indice_pour_humain(choix_humain, choix_ordi):
    if choix_humain > choix_ordi:
        print('Le chiffre est plus petit !')
    else:
        print('Le nombre est plus grand !')

def choix_humain():
    choix_de_l_humain = int(input('\ndit un chiffre :'))
    while verif_choix_humain(choix_de_l_humain) == False:
        choix_de_l_humain = int(input('\ndit un autre chiffre :'))
    return choix_de_l_humain

def verif_choix_humain(choix_de_l_humain):
    if choix_de_l_humain < 1000:
        print('votre chiffre est trop petit !')
        point = calcul_de_point(nombre_de_points)
        print(f'il vous reste plus encore {point} essai')        
        return False
    if choix_de_l_humain > 10000:
        print('votre chiffre est trop grand !')
        point = calcul_de_point(nombre_de_points)
        print(f'il vous reste plus encore {point} essai')
        return False
    return True
    
def calcul_de_point(nombre_de_points):
    nombre_de_points -= 1
    return nombre_de_points

def verif_niveau(niveau):
    if niveau == 'facile':
        return True 
    if niveau == 'moyen':
        return True 
    if niveau == 'difficile' or 'hard':
        return True 

def victoire(choix_humain, choix_ordi, nombre_de_points):
    if choix_humain == choix_ordi:
        return True
    if nombre_de_points == 1:        
        return True
    if nombre_de_points == 2:
        print('\nvous avez plus que 1 cout a jouer !\n')

    return False

def main(nombre_de_points):
    choix_ordi = random.randint(1000,10000)
    regle(choix_ordi)
    choix_de_l_humain = choix_humain()
    while victoire(choix_de_l_humain, choix_ordi, nombre_de_points) == False:
        nombre_de_points = calcul_de_point(nombre_de_points)
        print(f'il vous reste plus encore {nombre_de_points} essai')
        indice_pour_humain(choix_de_l_humain, choix_ordi)
        choix_de_l_humain=choix_humain()

    nombre_de_points = calcul_de_point(nombre_de_points)
    if nombre_de_points == 0:
        print(f'\nDommage tu t\'es trompé trop de fois...\nLe chiffre de l\ordinateur été {choix_ordi} et il te reste endore {nombre_de_points} donc encore {nombre_de_points} d\'essai')
    else:
        print(f'\nBIEN JOUE, tu as gagné le chiffre ete {choix_ordi} et tu as fini avec {nombre_de_points}')

encore_une_partie = 'oui'
while encore_une_partie == 'oui' or encore_une_partie == 'Oui' or encore_une_partie == 'OUI' or encore_une_partie == 'avec plaisir':
    print('\033[00m')
    niveau = str(input('quelle niveau choisissez vous ? \n -facile \n -moyen \n -difficile\nAlors que choisissez vous :'))
    while verif_niveau(niveau) == False:
        niveau = str(input('quelle niveau choisissez vous ? \n -facile \n -moyen \n -difficile '))
    if niveau == 'facile':
        print('\033[92m')
        nombre_de_points = 20

    elif niveau == 'moyen':
        print('\033[93m')
        nombre_de_points = 10

    elif niveau == 'difficile' or 'hard':
        print('\033[91m')
        nombre_de_points = 5

    main(nombre_de_points)
    encore_une_partie = str(input('Voulez-vous refaire une partie ?'))
print('Merci d\avoir joué !!! ')


print('\033[92m')
print('\033[00m')
