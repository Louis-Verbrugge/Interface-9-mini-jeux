import pygame
import sys
import random
import operator as op
import time




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
    
    modification_maps_apres_mouvement(maps, ligne, cood_x, mouvement)

    return maps








def fonction_copy(maps):
    copie = []
    for i in range (len(maps)):
        copie.append([elem for elem in maps[i]])
    return copie


def fonction_test_si_addition_vers_le_haut(ligne, mouvement):
    for coordonne_y in range(len(ligne)-1):
        if ligne[coordonne_y] == ligne[coordonne_y+1]:
            fonction_addition(ligne, coordonne_y, mouvement)
    
    return ligne



def fonction_test_si_addition_vers_le_bas(ligne, mouvement):
    for coordonne_y in range(len(ligne)-1):
        if ligne[len(ligne)-1 - coordonne_y] == ligne[len(ligne)-1 - coordonne_y-1]:
            fonction_addition(ligne, coordonne_y, mouvement)
            
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
        
            

def modification_maps_apres_mouvement(maps, ligne, cood_x, mouvement):
    if mouvement == "s" or mouvement == "z":
        for i in range (len(ligne)):
            maps[i][cood_x] = ligne[i] 
            
    else:
        maps[cood_x] = ligne







def function_add_chiffre_random(maps):
    
    choix_nombre = random.randint(0, 5)  # j ai 1 chance sur 5 que un cube "4" apparait sinon c'est "2"
    if choix_nombre >= 2:
        choix_nombre = 2
    else:
        choix_nombre = 4
    
    
    # je cherche maintenant des coordonnes alea d'une case vide pour mettre le chiffre aleatoire
    
    coordonne_y = random.randint(0, len(maps)-1)
    coordonne_x = random.randint(0, len(maps[0])-1)
    while maps[coordonne_y][coordonne_x] != 0:
        coordonne_y = random.randint(0, len(maps)-1)
        coordonne_x = random.randint(0, len(maps[0])-1)        
 
    maps[coordonne_y][coordonne_x] = choix_nombre
    
    return maps


def est_dans_la_grille(maps, coord_y, coord_x):
    if 0 <= coord_y <= len(maps)-1 and 0<= coord_x <= len(maps[0])-1:
        return True
    return False


def fin_game_defaite(maps):
    accu = 0
    
    for i in range (len(maps)):
        accu += op.countOf(maps[i], 2048)
        
    if accu != 0:
        return False, "VICTOIRE"
        
        
        
        
    for coordonne_y in range (len(maps)):
        for coordonne_x in range (len(maps[0])):
            
           
            if maps[coordonne_y][coordonne_x] == 0:
                return True, "continue"
            
            else:
                ht = [0, 1, -1, 0]
                lg = [-1, 0, 0, 1]
                for i in range (4):
                    if est_dans_la_grille(maps, coordonne_y + ht[i], coordonne_x + lg[i]):
                        if maps[coordonne_y + ht[i]][coordonne_x + lg[i]] == maps[coordonne_y][coordonne_x]:
                            return True, "continue"
    
           
    return False, "PERDU.."






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





def affiche_maps_debut_game(SCREEN, maps):
    
    # affiche les cases:
    for ligne in range (len(maps)):
        for col in range (len(maps[0])):
            affiche_choix_chiffre(SCREEN, maps, col, ligne)
        
    # affiche les lignes:
    print(150+((HEIGHT-300)/len(maps)))
    print(300+((WIDTH-600)/len(maps[0])))
    
    #VERTICALE:
    for i in range (len(maps)):
        
        pygame.draw.line(SCREEN, BLACK, (300+(WIDTH-600)/len(maps[0])+(WIDTH-600)/len(maps[0])*i, 150), (300+(WIDTH-600)/len(maps[0])+(WIDTH-600)/len(maps[0])*i, HEIGHT-152), 3)
        
    
    
    #HORIZONTALE:
    for i in range (len(maps)):
        pygame.draw.line(SCREEN, BLACK, (300, 150+((HEIGHT-300)/len(maps))+((HEIGHT-300)/len(maps))*i), (WIDTH-300, 150+((HEIGHT-300)/len(maps))+((HEIGHT-300)/len(maps))*i), 3)
        




def affiche_choix_chiffre(SCREEN, maps, coordonne_x, coordonne_y):
    
    
    if test_si_chiffre(str(maps[coordonne_y][coordonne_x])) and maps[coordonne_y][coordonne_x] != 0:
    #if maps[coordonne_y][coordonne_x] in chiffre:#l'utilisateur a clique sur un chiffre !
        pygame.draw.rect(SCREEN, dictionnaire_couleur_valeur[maps[coordonne_y][coordonne_x]], (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps)))))
            
            
        nombre_trouve = pygame.font.SysFont("bahnschrift", 30).render(str(maps[coordonne_y][coordonne_x]), True, 'black')
        affiche_nombre_trouve = nombre_trouve.get_rect(center=((300+((WIDTH-600)/len(maps[0]))*coordonne_x)+ ((WIDTH-600)/len(maps[0]))/2, (150+((HEIGHT-300)/len(maps))*coordonne_y)+((HEIGHT-300)/len(maps))/2))
        SCREEN.blit(nombre_trouve, affiche_nombre_trouve)
        
            
    else: #l'utilisateur a cliqué sur une bombe..
        pygame.draw.rect(SCREEN, GREY, (300+((WIDTH-600)/len(maps[0]))*coordonne_x, 150+((HEIGHT-300)/len(maps))*coordonne_y, ((WIDTH-600)/len(maps[0])), ((HEIGHT-300)/len((maps))))) 
        






def test_si_chiffre(text_a_verif):
    chiffre = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for elem in text_a_verif:
        if elem not in chiffre:
            return False
        
    return True













def choix_du_niveau(SCREEN):
    
    fond_acceil = pygame.image.load('./image/main.jpg')
    fond_acceil = fond_acceil.convert()
    
    
    
    
    
    choix_du_niveau = pygame.font.SysFont("bahnschrift", 50).render("Choisissez un niveau :", True, "white")
    affiche_niveau = choix_du_niveau.get_rect(center=(WIDTH/2, HEIGHT/3))

    facilee = pygame.font.SysFont("bahnschrift", 50).render("4x4", True, "white")
    nieau_facilee = facilee.get_rect(center=(WIDTH/4, HEIGHT/1.5))

    moyenn = pygame.font.SysFont("bahnschrift", 50).render("6x6", True, "white")
    niveau_moyenn = moyenn.get_rect(center=(WIDTH/2, HEIGHT/1.5))

    hardd = pygame.font.SysFont("bahnschrift", 50).render("8x8", True, "white")
    niveau_hardd = hardd.get_rect(center=(WIDTH/1.4, HEIGHT/1.5))        
    
    
    # affiche les commentaires pour le choix du niveau
    facile = pygame.font.SysFont("bahnschrift", 30).render("petit", True, "white")
    nieau_facile = facile.get_rect(center=(WIDTH/4, HEIGHT/1.5+50))   
    
    moyen = pygame.font.SysFont("bahnschrift", 30).render("moyen", True, "white")
    niveau_moyen = moyen.get_rect(center=(WIDTH/2, HEIGHT/1.5+50))    
    
    hard = pygame.font.SysFont("bahnschrift", 30).render("GRAND !", True, "white")
    niveau_hard = hard.get_rect(center=(WIDTH/1.4, HEIGHT/1.5+50))    
    
    
    affiche_choix_niveau = True
    while affiche_choix_niveau:


        mouse = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #affiche_choix_niveau = False
                return "quitte"

        if (WIDTH/4)-80 <= mouse[0] <= (WIDTH/4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
                 
            SCREEN.blit(facile, nieau_facile)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [4, 4]

            
        # je test si l'utilisateur clique dans la case MOYEN !
        elif (WIDTH/2)-80 <= mouse[0] <= (WIDTH/2)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
            
            SCREEN.blit(moyen, niveau_moyen)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [6, 6]
                
        # je test si l'utilisateur clique dans la case HARD !
        elif (WIDTH/1.4)-80 <= mouse[0] <= (WIDTH/1.4)+90 and (HEIGHT/1.5)-50 <= mouse[1] <= (HEIGHT/1.5)+30:
            
            SCREEN.blit(hard, niveau_hard)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                return [8, 8]

       
        else:
            SCREEN.blit(fond_acceil, (0,0))
            SCREEN.blit(choix_du_niveau, affiche_niveau)

            SCREEN.blit(facilee, nieau_facilee)
            SCREEN.blit(moyenn, niveau_moyenn)
            SCREEN.blit(hardd, niveau_hardd)   
            
            
            pygame.draw.rect(SCREEN, WHITE, ((WIDTH/4)-85, (HEIGHT/1.5)-40, 175, 70), 2) #  facile 
            pygame.draw.rect(SCREEN, WHITE, ((WIDTH/2)-85, (HEIGHT/1.5)-40, 175, 70), 2) # moyen
            pygame.draw.rect(SCREEN, WHITE, ((WIDTH/1.4)-70, (HEIGHT/1.5)-40, 150, 70), 2) # hard  
    
        pygame.display.update()


















def affiche_fin_partie(SCREEN, resultat_fin_partie):
    if resultat_fin_partie == "VICTOIRE":
        fond = pygame.image.load('./image/victoire_carss.jpg') 
        couleur= "black"  

    else:
        fond = pygame.image.load('./image/lapin_pendu_defaite.jpg')
        couleur= "white"

    run_affice_fin = True
    while run_affice_fin:

    

        test_affiche_win = pygame.font.SysFont("bahnschrift", 100).render(resultat_fin_partie, True, couleur)  # affiche le gagnant !
        win = test_affiche_win.get_rect(center=(WIDTH/4, HEIGHT/3))  # c'est la position ou j 'affiche le gagnant
        
                        
        recommencer_une_partie = pygame.font.SysFont("bahnschrift", 30).render("cliquer pour RECOMMENCER !", True, "white") # affiche si le joueur veut refaire une partie !
        restart = recommencer_une_partie.get_rect(center=(WIDTH-200, HEIGHT-100))  # affiche la position du boutton !


        fond = fond.convert()
        SCREEN.blit(fond, (0,0))        
        fond = fond.convert()
        SCREEN.blit(fond, (0,0))
        SCREEN.blit(test_affiche_win, win)  
        SCREEN.blit(recommencer_une_partie, restart)

        mouse = pygame.mouse.get_pos()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
            if event.type == pygame.MOUSEBUTTONDOWN: #je test si il y a un clique sur le boutton pour recommence une partie 
                if WIDTH-420 <= mouse[0] <= WIDTH and HEIGHT-120 <= mouse[1] <= HEIGHT: 
                    main_2048()
                    run_affice_fin = False
    print('LE programme est fini !') 
    
    







BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SABLE = (218, 229, 179)
GREY = (125, 125, 125)

"""
# couleur des cases:
GRIS_2 = (228, 230, 223)
HEX_4 = (202, 205, 167)
ORANGE_8 = (255, 194, 54)
ORANGE_16 = (247, 141, 53)
ROUGE_32 = (244, 30, 30)
ROUGE_64 = (255, 0, 0)
JAUNE_128 = (252, 248, 94)
JAUNE_256 = (238, 232, 35)
JAUNE_512 = (235, 228, 15)
JAUNE_1024 = (211, 205, 0)
JAUNE_2048 = (236, 229, 0)"""

# dictionnaire qui contient les couleurs associé au valeur
dictionnaire_couleur_valeur = {
    2 : (228, 230, 223),
    4 : (202, 205, 167), 
    8 : (255, 194, 54), 
    16 : (247, 141, 53), 
    32 : (243, 102, 88), 
    64 : (255, 0, 0), 
    128 : (252, 248, 94),
    256 : (238, 232, 35),
    512 : (235, 228, 15),
    1024 : (211, 205, 0), 
    2048 : (236, 229, 0)
}


GREEN_CLAIR = (57, 255, 4)
GREEN_FONCE = (0, 113, 14)



WIDTH, HEIGHT = 1560, 1200   ### WIDTH, HEIGHT = 1000, 800





def main_2048():
    
    
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"2048")

    
    
    niveau = choix_du_niveau(SCREEN)
    if niveau != "quitte":
        SCREEN.fill(BLACK)
        maps = creation_grille(niveau[0], niveau[1])  #(longueur x; longueur y)
        emplacement = emplacement_case(maps)
        affiche_maps_debut_game(SCREEN,maps)


        pygame.display.update()


        for elem in emplacement:
            print(elem)

        print(len(emplacement))

        run = True
        while run:  


            if fin_game_defaite(maps)[0] == False: 
                fin_game = fin_game_defaite(maps)[1]             
                run = False            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin_game="quitte"
                    run = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: # clique a gauche
                        print('gauche')
                        mouvement = "q"
                        maps_2 = fonction_copy(maps)
                        
                        for i in range (len(maps)):
                            fonction_cherche_ligne_modif(maps, i, mouvement)
                            
                        if maps != maps_2:  # si il y a eu aucun modif il ne r'ajoute pas de chiffre
                            maps = function_add_chiffre_random(maps)
                            affiche_maps_debut_game(SCREEN,maps)
                            pygame.display.update()



                    elif event.key == pygame.K_RIGHT: # clique a gauche
                        print('droite')
                        mouvement = "d"
                        maps_2 = fonction_copy(maps)
                        
                        for i in range (len(maps)):
                            fonction_cherche_ligne_modif(maps, i, mouvement)
                        
                        if maps != maps_2:  # si il y a eu aucun modif il ne r'ajoute pas de chiffre
                            maps = function_add_chiffre_random(maps)
                            affiche_maps_debut_game(SCREEN,maps)
                            pygame.display.update()



                    elif event.key == pygame.K_DOWN: # clique a gauche
                        print('bas')
                        mouvement = "s"
                        maps_2 = fonction_copy(maps)
                        
                        for i in range (len(maps)):
                            fonction_cherche_ligne_modif(maps, i, mouvement)
                            
                        if maps != maps_2:  # si il y a eu aucun modif il ne r'ajoute pas de chiffre
                            maps = function_add_chiffre_random(maps)
                            affiche_maps_debut_game(SCREEN, maps)
                            pygame.display.update()
                    

                    elif event.key == pygame.K_UP: # clique a gauche
                        print('haut')
                        mouvement = "z"
                        maps_2 = fonction_copy(maps)
                        
                        for i in range (len(maps)):
                            fonction_cherche_ligne_modif(maps, i, mouvement)
                            
                        if maps != maps_2:  # si il y a eu aucun modif il ne r'ajoute pas de chiffre
                            maps = function_add_chiffre_random(maps)
                            affiche_maps_debut_game(SCREEN, maps)
                            pygame.display.update()
                            
                            

        
        if fin_game != "quitte":
            print('sqddsqdsqd')
            time.sleep(1)
            
            affiche_fin_partie(SCREEN, fin_game)
        
