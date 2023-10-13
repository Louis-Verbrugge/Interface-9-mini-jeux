import pygame
import sys
import random






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










BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SABLE = (218, 229, 179)

GREEN_CLAIR = (57, 255, 4)
GREEN_FONCE = (0, 113, 14)

WIDTH, HEIGHT = 1400, 1100   ### WIDTH, HEIGHT = 1000, 800

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Démineur")



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



def emplacement_case(maps): # (x x' y y')
    emplacement_casee = []
    for ligne in range (len(maps)):
        emplacement_casee.append([])
        for col in range (len(maps[0])):
            emplacement_casee[ligne].append([300+((WIDTH-600)/len(maps[0]))*col, 300+((WIDTH-600)/len(maps[0]))*col + ((WIDTH-600)/len(maps[0])), 150+((HEIGHT-300)/len((maps)))*ligne, 150+((HEIGHT-300)/len((maps)))*ligne + ((HEIGHT-300)/len((maps)))])
            
    return emplacement_casee 





def affiche_maps_debut_game(maps):
    
    for ligne in range (len(maps)):
        for col in range (len(maps[0])):
            
    
            affiche_choix_chiffre(maps, col, ligne)
    
    



def affiche_choix_chiffre(maps, coordonne_x, coordonne_y):
    chiffre = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    if maps[coordonne_y][coordonne_x] in chiffre:#l'utilisateur a clique sur un chiffre !
        pygame.draw.rect(SCREEN, SABLE, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
            
            
        nombre_trouve = pygame.font.SysFont("bahnschrift", 30).render(str(maps[coordonne_y][coordonne_x]), True, "white")
        affiche_nombre_trouve = nombre_trouve.get_rect(center=((300+((WIDTH-600)/len(maps[0]))*coordonne_x)+ ((WIDTH-600)/len(maps[0]))/2, (150+((HEIGHT-300)/len(maps))*coordonne_y)+((HEIGHT-300)/len(maps))/2))
        SCREEN.blit(nombre_trouve, affiche_nombre_trouve)
        
            
    else: #l'utilisateur a cliqué sur une bombe..
        pygame.draw.rect(SCREEN, RED, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps))))) 
        print('TTTT')












maps = creation_grille(4, 4)  #(longueur x; longueur y)
emplacement = emplacement_case(maps)
affiche_maps_debut_game(maps)


pygame.display.update()


for elem in emplacement:
    print(elem)

print(len(emplacement))
run = True
while run:  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT: # clique a gauche
                print('gauche')
                mouvement = "q"
                for i in range (len(maps)):
                    fonction_cherche_ligne_modif(maps, i, mouvement)
                affiche_maps_debut_game(maps)
                pygame.display.update()

            elif event.key == pygame.K_RIGHT: # clique a gauche
                print('droite')
                mouvement = "d"
                for i in range (len(maps)):
                    fonction_cherche_ligne_modif(maps, i, mouvement)
                affiche_maps_debut_game(maps)
                pygame.display.update()



            elif event.key == pygame.K_DOWN: # clique a gauche
                print('bas')
                mouvement = "s"
                for i in range (len(maps)):
                    fonction_cherche_ligne_modif(maps, i, mouvement)
                affiche_maps_debut_game(maps)
                pygame.display.update()



            elif event.key == pygame.K_UP: # clique a gauche
                print('haut')
                mouvement = "z"
                for i in range (len(maps)):
                    fonction_cherche_ligne_modif(maps, i, mouvement)
                affiche_maps_debut_game(maps)
                pygame.display.update()



