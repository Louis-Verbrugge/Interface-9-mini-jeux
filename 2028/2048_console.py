


def fonction_cherche_ligne_modif(maps, cood_x):
    ligne = [maps[col][cood_x] for col in range (len(maps))]

    #je decale toute les valeurs dans la bonne directrion  ( pour le test je fais vers la gauche donc vers le haut )
    nv_ligne = [x for x in ligne if x!=0]
    nvvv_ligne = [0 for _ in range (len(maps[0]) - len(nv_ligne))]
    nv_ligne = nv_ligne + nvvv_ligne


    print(nv_ligne)

    print('TTTTTTGGGGGGGGGGGGGGGGGGGGGGGG')


    map = fonction_test_si_addition(maps, nv_ligne, cood_x)

    for elem in map:
        print(elem)

    print('C est maintenant : ')

    return ligne, nv_ligne, nvvv_ligne


def fonction_test_si_addition(maps, ligne, cood_x):
    for coordonne_x in range(len(ligne)-1):
        if ligne[coordonne_x] == ligne[coordonne_x+1]:
            lignee = fonction_addition(ligne, coordonne_x)
            # créee fonction addition et pour monter les chiffre de droite vers la gauche.
    
    # test si il faut mettre en reverse ou non...

    print(lignee)
    
    ### mapss = [maps[x][cood_x] for x in range (len(maps))]

    print(maps)
    print(ligne)
    #x=int(input('FSD'))

    maps[cood_x] = ligne


    print(maps)
    print(ligne)
    #x=int(input('FSD'))
    
    return lignee

def fonction_addition(ligne, coordonne_y):
    print(ligne)
    print(coordonne_y)
    ligne[coordonne_y] += ligne[coordonne_y+1]
    ligne.pop(coordonne_y+1)
    ligne.append(0)
    return ligne
            


maps = [[0, 2, 2, 5],
        [2, 2, 2, 0], 
        [0, 4, 0, 0], 
        [2, 4, 0, 5]]



carte = []
for i in range (4):
    print(f'\n {i}')

    aa = fonction_cherche_ligne_modif(maps, i)
    print(aa)
    carte.append(aa)


print('MAINTENANT : \n')
for elem in carte:
    print(elem)



