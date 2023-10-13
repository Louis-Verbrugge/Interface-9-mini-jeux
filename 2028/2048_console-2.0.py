
import random





def creation_grille(long_x, long_y):
    maps = []
    for _ in range (long_y):
        maps.append([0*x for x in range(long_x)])


    for _ in range (2):
        pos_x = random.randint(0, len(maps)-1)
        pos_y = random.randint(0, len(maps)-1)
        while maps[pos_y][pos_x] != 0:
            pos_x = random.randint(0, len(maps)-1)
            pos_y = random.randint(0, len(maps)-1)           

        maps[pos_y][pos_x] = 2

    return maps





def fonction_cherche_ligne_modif(maps, cood_x, mouvement):
    if mouvement == "z" or mouvement == "s":
        ligne = [maps[col][cood_x] for col in range (len(maps))]

    else:
        ligne = maps[cood_x]

    
    if mouvement == "s" or mouvement == "d":
        
        nv_ligne = [x for x in ligne if x!=0]
        nvvv_ligne = [0 for _ in range (len(maps[0]) - len(nv_ligne))]
        nv_ligne = nvvv_ligne + nv_ligne
        

        ligne = fonction_test_si_addition_vers_le_bas(nv_ligne, mouvement)

        
        
        
    elif mouvement == "z" or mouvement == "q":

        nv_ligne = [x for x in ligne if x!=0]
        nvvv_ligne = [0 for _ in range (len(maps[0]) - len(nv_ligne))]
        nv_ligne = nv_ligne + nvvv_ligne
        ligne = fonction_test_si_addition_vers_le_haut(nv_ligne, mouvement)
    
    modification_maps_apres_mouvement(ligne, cood_x, mouvement)

    return maps












def fonction_test_si_addition_vers_le_haut(ligne, mouvement):
    for coordonne_y in range(len(ligne)-1):
        if ligne[coordonne_y] == ligne[coordonne_y+1]:
            fonction_addition(ligne, coordonne_y, mouvement)
            # créee fonction addition et pour monter les chiffre de droite vers la gauche.
    
    return ligne



def fonction_test_si_addition_vers_le_bas(ligne, mouvement):
    for coordonne_y in range(len(ligne)-1):
        if ligne[len(ligne)-1 - coordonne_y] == ligne[len(ligne)-1 - coordonne_y-1]:
            fonction_addition(ligne, coordonne_y, mouvement)
            # créee fonction addition et pour monter les chiffre de droite vers la gauche.
    return ligne





def fonction_addition(ligne, coordonne_y, mouvement):
    print(ligne)
    print(coordonne_y)
    if mouvement == "z" or mouvement == "q":
        ligne[coordonne_y] += ligne[coordonne_y+1]
        ligne.pop(coordonne_y+1)
        ligne.append(0)
        
        
    else:
        ligne[len(ligne)-1 - coordonne_y] += ligne[len(ligne)-1 - coordonne_y-1]
        ligne.pop(len(ligne)-1 - coordonne_y-1)
        ligne.insert(0, 0) 
        
            

def modification_maps_apres_mouvement(ligne, cood_x, mouvement):
    if mouvement == "s" or mouvement == "z":
        for i in range (len(ligne)):
            maps[i][cood_x] = ligne[i] 
            
    else:
        maps[cood_x] = ligne
     
        
        
"""maps = [[0, 2, 2, 5],
        [5, 2, 2, 0], 
        [0, 4, 0, 0], 
        [2, 4, 0, 5]]"""


maps = creation_grille(4, 4)
print(maps)

mouvement = str(input("mouvement ? \"z\"/ \"q\"/ \"s\"/ \"d\" "))
run = True
while run:
    if mouvement == "quitte":
        run = False
        
    else:
        

        for i in range (len(maps)): # car il y a 4 rangées
            print(f'\n {i}')

            aa = fonction_cherche_ligne_modif(maps, i, mouvement)
            print(aa)


        print('MAINTENANT : \n')
        for elem in maps:
            print(elem)
            
        mouvement = str(input("mouvement ? \"z\"/ \"q\"/ \"s\"/ \"d\" "))





